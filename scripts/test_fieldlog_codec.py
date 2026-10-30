"""Check image properties that must survive source-format normalization."""
from io import BytesIO
import unittest
from PIL import Image
from fieldlog_image_codec import convert_image, register_heif_opener


def encoded(image, format, **options):
    output = BytesIO()
    image.save(output, format=format, **options)
    return output.getvalue()


class CodecTests(unittest.TestCase):
    def test_existing_webp_is_preserved_byte_for_byte(self):
        source = encoded(Image.new("RGB", (17, 11), "red"), "WEBP", quality=91)
        self.assertEqual(convert_image(source, "photo.webp"), source)

    def test_photo_orientation_dimensions_and_metadata(self):
        image = Image.new("RGB", (17, 11), "red")
        exif = image.getexif()
        exif[274] = 6
        exif[315] = "Savour"
        source = encoded(image, "JPEG", exif=exif, icc_profile=b"saved ICC profile")
        with Image.open(BytesIO(convert_image(source, "photo.jpg"))) as saved:
            self.assertEqual(saved.format, "WEBP")
            self.assertEqual(saved.size, (11, 17))
            self.assertIsNone(saved.getexif().get(274))
            self.assertEqual(saved.getexif().get(315), "Savour")
            self.assertEqual(saved.info["icc_profile"], b"saved ICC profile")

    def test_png_transparency_and_pixels_remain_lossless(self):
        image = Image.new("RGBA", (3, 1))
        image.putdata([(255, 0, 0, 255), (11, 22, 33, 127), (90, 80, 70, 0)])
        source = encoded(image, "PNG")
        with Image.open(BytesIO(convert_image(source, "graphic.png"))) as saved:
            self.assertEqual(saved.size, image.size)
            self.assertEqual(saved.convert("RGBA").tobytes(), image.tobytes())

    def test_multiframe_phone_photo_is_not_an_animation(self):
        source = encoded(Image.new("RGB", (20, 10), "red"), "MPO", save_all=True,
                         append_images=[Image.new("RGB", (20, 10), "blue")])
        with Image.open(BytesIO(source)) as original:
            self.assertEqual(original.n_frames, 2)
        with Image.open(BytesIO(convert_image(source, "phone.jpeg"))) as saved:
            self.assertEqual(saved.n_frames, 1)
            self.assertEqual(saved.size, (20, 10))

    def test_gif_frames_durations_and_finite_repeat_count(self):
        source = encoded(Image.new("RGB", (4, 3), "red"), "GIF", save_all=True,
                         append_images=[Image.new("RGB", (4, 3), "blue")],
                         duration=[100, 240], loop=2)
        with Image.open(BytesIO(convert_image(source, "animation.gif"))) as saved:
            self.assertEqual(saved.n_frames, 2)
            self.assertEqual(saved.info["loop"], 3)
            for number, (duration, color) in enumerate([(100, (255, 0, 0)), (240, (0, 0, 255))]):
                saved.seek(number); saved.load()
                self.assertEqual(saved.info["duration"], duration)
                self.assertEqual(saved.convert("RGB").getpixel((0, 0)), color)

    def test_gif_without_loop_metadata_plays_once(self):
        source = encoded(Image.new("RGB", (4, 3), "red"), "GIF", save_all=True,
                         append_images=[Image.new("RGB", (4, 3), "blue")], duration=100)
        with Image.open(BytesIO(convert_image(source, "once.gif"))) as saved:
            self.assertEqual(saved.info["loop"], 1)

    def test_apng_default_poster_is_not_an_extra_animation_frame(self):
        source = encoded(Image.new("RGBA", (4, 3), "green"), "PNG", save_all=True,
                         append_images=[Image.new("RGBA", (4, 3), "red"), Image.new("RGBA", (4, 3), "blue")],
                         default_image=True, duration=[120, 240], loop=2)
        with Image.open(BytesIO(convert_image(source, "animation.png"))) as saved:
            self.assertEqual(saved.n_frames, 2)
            self.assertEqual(saved.info["loop"], 2)
            for number, duration in enumerate([120, 240]):
                saved.seek(number); saved.load()
                self.assertEqual(saved.info["duration"], duration)

    @unittest.skipUnless(register_heif_opener is not None, "HEIF support requires pillow-heif")
    def test_heif_photo_keeps_full_dimensions(self):
        source = encoded(Image.new("RGB", (18, 12), "green"), "HEIF")
        with Image.open(BytesIO(convert_image(source, "phone.heic"))) as saved:
            self.assertEqual(saved.format, "WEBP")
            self.assertEqual(saved.size, (18, 12))
            self.assertEqual(saved.n_frames, 1)

    def test_damaged_empty_and_unsupported_uploads_fail(self):
        for data, filename in [(b"", "empty.jpg"), (b"bad bytes", "broken.jpg"),
                               (encoded(Image.new("RGB", (3, 2)), "BMP"), "unsupported.jpg")]:
            with self.subTest(filename=filename), self.assertRaises(ValueError):
                convert_image(data, filename)


if __name__ == "__main__":
    unittest.main()
