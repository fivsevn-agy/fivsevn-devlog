"""Validate uploads and normalize saved photographs to WebP.

The policy follows the existing Flux and Savour archives: keep existing WebP bytes, encode photographs at quality
85, and encode PNG/GIF graphics losslessly while retaining animation timing.
"""
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

try:
    from pillow_heif import register_heif_opener
except ImportError:
    register_heif_opener = None
else:
    register_heif_opener(thumbnails=False)

SUPPORTED_FORMATS = {"JPEG", "MPO", "PNG", "WEBP", "GIF", "HEIF"}


def validate_image(data: bytes, filename: str) -> None:
    """Decode every real animation frame; auxiliary phone frames are stills."""
    if not data:
        raise ValueError(f"Empty image upload: {filename}")
    try:
        with Image.open(BytesIO(data)) as image:
            if image.format not in SUPPORTED_FORMATS:
                raise ValueError(f"Unsupported image format: {filename}")
            image.verify()
        with Image.open(BytesIO(data)) as image:
            animated = image.format in {"GIF", "PNG", "WEBP"} and getattr(image, "is_animated", False)
            for frame in range(image.n_frames if animated else 1):
                image.seek(frame)
                image.load()
    except (OSError, SyntaxError, EOFError, Image.DecompressionBombError) as error:
        hint = " (HEIC/HEIF uploads require pillow-heif)" if Path(filename).suffix.lower() in {".heic", ".heif"} and register_heif_opener is None else ""
        raise ValueError(f"Invalid or damaged image upload: {filename}{hint}") from error


def convert_image(data: bytes, filename: str) -> bytes:
    """Return a fully decoded, oriented WebP without resizing the photograph."""
    validate_image(data, filename)
    try:
        with Image.open(BytesIO(data)) as image:
            fmt = image.format
            if fmt == "WEBP":
                return data  # Avoid quality loss from recompressing an existing WebP.
            animated = fmt in {"GIF", "PNG"} and getattr(image, "is_animated", False)
            lossless = fmt in {"PNG", "GIF"}
            options = {"method": 4 if lossless else 6, "lossless": lossless,
                       "quality": 75 if lossless else 85}
            if lossless:
                options["exact"] = True
            if image.info.get("icc_profile"):
                options["icc_profile"] = image.info["icc_profile"]
            if animated:
                frames, durations = [], []
                loop = image.info.get("loop")
                # GIF loop is a repeat count; WebP loop is a total-play count.
                options["loop"] = (0 if loop == 0 else (loop + 1 if loop is not None else 1)) if fmt == "GIF" else (loop or 0)
                start = 1 if image.info.get("default_image") else 0
                for number in range(start, image.n_frames):
                    image.seek(number)
                    frames.append(image.convert("RGBA"))
                    durations.append(image.info.get("duration", 100) or 100)
                options.update(save_all=True, append_images=frames[1:], duration=durations,
                               minimize_size=False)
                primary = frames[0]
            else:
                primary = ImageOps.exif_transpose(image)
                exif = primary.getexif()
                if exif:
                    options["exif"] = exif.tobytes()
                has_alpha = "A" in primary.getbands() or "transparency" in primary.info
                primary = primary.convert("RGBA" if has_alpha else "RGB")
            output = BytesIO()
            primary.save(output, format="WEBP", **options)
            result = output.getvalue()
        validate_image(result, filename + ".webp")
        return result
    except (OSError, SyntaxError, EOFError, Image.DecompressionBombError) as error:
        raise ValueError(f"Invalid or damaged image upload: {filename}") from error

