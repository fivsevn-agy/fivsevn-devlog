---
id: natsci-fieldlog-readme
title: Fieldlog publishing and maintenance
module: natsci
submodule: fieldlog
topic: guide
type: note
status: active
canonical: true
summary: Content packages, publishing, validation, and maintenance for the natural observation archive.
parents: [natsci-readme]
related: []
tags: [natsci, fieldlog]
audience: [self, internal]
languages: [en]
maturity: evolving
confidence: null
visibility: public
source_of_truth: devlog
filename_policy: entrypoint
created: '2026-10-30'
updated: '2026-10-30'
metadata_updated: '2026-10-30'
---
# Fieldlog

Fieldlog is the natural observation photo archive at [devlog.fivsevn.com/natsci/fieldlog](https://devlog.fivsevn.com/natsci/fieldlog/). This directory contains its editable source packages, shared interface assets, and publication state. The wider [natsci study archive](https://devlog.fivsevn.com/natsci/) contains the accompanying notes.

Upload photos to [`trigger_imgs/`](trigger_imgs/). Each image becomes one independent post with an optional Markdown caption. The [image inbox guide](trigger_imgs/README.md) provides concise everyday instructions in Chinese; this README describes the content and publishing system in English.

## Repository layout

```text
natsci/fieldlog/
  YYYY/MM/{id}/
    index.md                       Canonical metadata and editable Markdown caption
    assets/                        This post's archived image
  trigger_imgs/                    Temporary image-upload inbox
    README.md                      Chinese upload guide
  ui/                              Shared image, fonts, CSS, and navigation behavior
  site-data/
    history.json                   Stable order for posts sharing an exact timestamp
  .publishing/
    state.json                     Upload cursor and immutable image-event records
    deployed.json                  File hashes from the last verified public build
scripts/
  site_post_metadata.py            Shared metadata normalization and validation
  fieldlog_image_codec.py          Shared image validation and WebP conversion
  normalize_fieldlog_images.py     Normalize saved package images without changing post IDs
  import_fieldlog_triggers.py      Import committed inbox snapshots into post packages
  build_fieldlog.py                Build listings, details, assets, and a build receipt
  verify_fieldlog_live.py          Verify the public build before clearing originals
  fieldlog_image_inbox.py          Clear only matching, publicly verified inbox files
  fieldlog_templates/              Page and opening-window templates
  requirements-fieldlog.txt        Pinned dependencies
schemas/                           Local shared core and site-post schema copies
_site/natsci/fieldlog/              Generated deployment artifact
```

Edit source packages and templates. Generated HTML belongs only to `_site/` and is rebuilt from source. Fieldlog serves its own photographs, fonts, and interface assets.

## Publish images

1. Pull the latest `main` before uploading from Working Copy or a phone shortcut. Browser uploads can use the [image upload page](https://github.com/fivsevn-agy/fivsevn-devlog/upload/main/natsci/fieldlog/trigger_imgs).
2. Save one or more photos into `natsci/fieldlog/trigger_imgs/`, keeping their original filenames.
3. Use the commit summary for an operation label. Put an optional public Markdown caption in the **extended description** below the summary. Leave it empty for an image-only post.
4. Commit and push to `main`, wait for the repository's [publishing workflow](https://github.com/fivsevn-agy/fivsevn-devlog/actions) to succeed, then check the [archive](https://devlog.fivsevn.com/natsci/fieldlog/) and the individual post.

Configure Working Copy and phone shortcuts to use **fivsevn-agy/fivsevn-devlog**, the inbox path above, and the `main` branch. The publishing bot saves packages, publication state, and verified inbox cleanup in new commits. Pull those commits before the next upload.

Each image creates a separate post. Images in one commit share the caption from its extended description. Uploads need only a photo and optional caption; the importer completes the shared metadata automatically.

### Dates, names, and retries

- Publication time comes from the upload commit's **committer timestamp**, converted to `Asia/Shanghai` and saved with its timezone offset.
- A package ID combines that timestamp with a digest of the upload commit and path. The saved directory is `YYYY/MM/{id}/`.
- Uploaded paths are sorted to assign stable batch numbers. Saved media is named `YYYYMMDD-HHMMSS-NN.webp`.
- A commit and path are processed once. Retrying a run preserves the package and any later caption edits.
- Uploading the same filename or identical bytes in a **new commit** creates a new post. Edit the saved package to revise an existing post.
- Deleting an inbox file does not withdraw an earlier committed upload event. Hide or remove its saved post instead.

The precise timestamp and the visible 12-digit observation code are separate from the stable package ID. If an observation date needs correction, edit `extra.published_at` and `extra.observation_id` while preserving the ID and directory. The post URL stays unchanged.

## Images

New uploads accept JPG/JPEG, PNG, WebP, GIF, HEIC, and HEIF, including uppercase extensions, Unicode filenames, and nested inbox folders.

| Input | Archived behavior |
| --- | --- |
| JPEG and HEIC/HEIF photos | WebP at quality 85, original display dimensions, corrected orientation, retained ICC profile and applicable EXIF metadata |
| PNG graphics | Lossless WebP retaining transparency and animation timing |
| GIF animations | Lossless animated WebP retaining frames, timing, transparency, and loop behavior |
| Existing WebP | Validated and retained byte-for-byte |

MPO and HEIF inputs use the primary display photograph; auxiliary phone frames do not become animation frames. Every saved package image is WebP. Existing valid WebP files retain their bytes and filename spelling; builds copy them into the deployment artifact without another encode.

`normalize_fieldlog_images.py` also handles photos saved directly into package assets, including hidden and draft posts and images no longer selected by the post. It validates the complete batch, stages the WebP files, updates `extra.image` references and applicable upload records, and replaces old-format files as one transaction. A failed batch restores the previous files and metadata. Repeating normalization changes no files when the archive is already WebP.

The current content tree stores the WebP archive without separate JPEG, PNG, HEIC, or GIF originals. Inbox originals are temporary and remain until public verification succeeds; earlier source formats remain recoverable from Git history. Post IDs, post URLs, observation dates, and captions stay unchanged through conversion.

The on-screen `OBS-…_raw.tif` text is a virtual specimen filename used by the interface. The actual displayed file comes from `extra.image` and is WebP.

## Captions and saved posts

A package contains an `index.md` and its own `assets/` directory:

```yaml
---
id: 2026-10-30-174000-example
title: 30 Oct, 2026 17:40
module: natsci
submodule: fieldlog
topic: null
type: log
status: published
canonical: true
summary: null
parents: []
related: []
tags: []
audience: [public]
languages: [zh]
maturity: evolving
confidence: null
visibility: public
source_of_truth: devlog
filename_policy: entrypoint
created: '2026-10-30'
updated: '2026-10-30'
metadata_updated: '2026-10-30'
extra:
  profile: site-post-v1
  published_at: '2026-10-30T17:40:00+08:00'
  author: 五月七日
  image: assets/20261030-174000-01.webp
  alt: A specimen observed in the field
  observation_id: '261030174000'
  display_status: Archived
---

Write the accompanying observation here. **Markdown** and [named links](https://example.com/) are supported.
```

Saved posts follow the same [shared core metadata contract](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/content-metadata.schema.json) and [site-post profile](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/site-post.schema.json) as Flux and Savour. The shared helper and schemas are committed locally, so normalization, validation, and building work without a network connection. Update the helper and schema copies together when adopting a new contract version.

| Field | Meaning |
| --- | --- |
| `id` | Unique stable identity, matching the existing directory name |
| `title` | Label beside Annotation Log; separate from the publication timestamp |
| `module`, `submodule`, `type` | `natsci`, `fieldlog`, and `log` |
| `status`, `visibility` | Listed only when visibility is `public` and status is `active`, `publish`, or `published` |
| `created`, `updated` | Content dates, separate from publication time |
| `metadata_updated` | Metadata maintenance date; unchanged normalization does not refresh it |
| `extra.profile` | `site-post-v1` |
| `extra.published_at` | Precise observation/publication timestamp with a timezone offset; controls ordering |
| `extra.image`, `extra.alt` | Package-relative image under `assets/` and its alternative text |
| `extra.observation_id` | Visible 12-digit OBS time code; may be shared by more than one post |
| `extra.display_status` | Window display label, usually `Archived`; independent of publication status |

Put the accompanying text after the closing `---`. Captions appear on the individual post; the listing shows the photograph and metadata. Missing fields in manually saved packages are completed before validation. Explicit statuses and visibility settings are preserved, and unrecognized older metadata is retained under `legacy.metadata`.

Edit a saved `index.md` to revise its caption, label, or visibility. Set `status` to `hidden` or `draft`, or `visibility` to `private` or `internal`, to exclude it from the generated website. These fields do not hide files in the public Git repository. Delete the entire package directory to remove a post; earlier versions remain in Git history.

## Interface and URLs

Each listing page contains up to **11 published posts**. The opening workspace window and closing Root Directory link are separate from the post count. A partial final page contains the remaining posts.

Individual post URLs remain `/natsci/fieldlog/YYYY/MM/{id}/`; subsequent listing pages use `/natsci/fieldlog/page/N/`. OBS anchors are mapped to the current listing page, so older pagination bookmarks continue to reach the correct post after the page count changes. The green `X` returns to the source listing and post position. Direct visits use the current listing anchor. A detail window scrolls internally when its content exceeds the viewport.

The opening image, centered windows, typography, and colors are controlled by `ui/fieldlog.css` and `scripts/fieldlog_templates/`. Root Directory links lead to [fivsevn.com](https://fivsevn.com/).

## Build and publish

The repository uses one Pages deployment for the complete devlog site. Its workflow normalizes metadata and saved photos, tests publishing behavior, imports committed inbox images, validates source packages, builds the main site, and overlays the Fieldlog artifact. It saves source packages and the upload cursor together before deployment.

After deployment, `verify_fieldlog_live.py` compares the public receipt and required page/media bytes with the local artifact. Changed files, the first and last listing pages, and pending inbox packages are checked. An unchanged archive does not require downloading every retained photo again. Cleanup checks the uploaded source digest and the saved image digest separately, then removes only matching originals from the inbox. Failed runs, newer uploads, private/draft posts, and changed saved images retain their originals.

The workflow checks that the remote branch still matches the run before committing cleanup. A failed run can be rerun; a new upload commit creates a new post. Do not clear publication cursors or event records during routine maintenance.

### Local development

```sh
python3 -m pip install -r scripts/requirements-fieldlog.txt
python3 scripts/site_post_metadata.py normalize --site fieldlog --root natsci/fieldlog --schema-dir schemas
python3 scripts/normalize_fieldlog_images.py
python3 scripts/site_post_metadata.py check --site fieldlog --root natsci/fieldlog --schema-dir schemas
python3 -m unittest discover -s scripts -p 'test_fieldlog_*.py'
python3 -m unittest discover -s tests -p 'test_fieldlog.py'
python3 scripts/build_fieldlog.py
python3 scripts/build_fieldlog.py --check
python3 -m http.server 8000 --directory _site
```

Open `http://localhost:8000/natsci/fieldlog/`. `build_fieldlog.py` defaults to `_site/natsci/fieldlog`; `--output /absolute/path` selects another module artifact directory, and `--root` selects a repository checkout. `--check` validates metadata, generated links, and artifact freshness without writing output.

For deployed verification and inbox cleanup, use the exact artifact that was published:

```sh
python3 scripts/verify_fieldlog_live.py
python3 scripts/fieldlog_image_inbox.py
```

Both accept `--root` and `--output`; public verification also accepts `--url`. Cleanup requires matching public verification and deployment records. A normal local build does not authorize inbox removal.

### Maintenance and recovery

- `.publishing/state.json` records immutable upload events, source and saved image digests, and package paths. Preserve it when changing captions or templates.
- `.publishing/deployed.json` records the last verified artifact hashes. The artifact's `build-receipt.json` identifies the current build, and `.verified.json` is a local verification marker.
- `site-data/history.json` stabilizes ordering for identical timestamps. To replace a saved photograph, update the image in its package assets folder and commit it. If its filename changes, update `extra.image` too. The workflow normalizes it to WebP, then records and verifies the current bytes; no fixed historical checksum blocks an intentional replacement.
- If an image upload is damaged or unsupported, replace or remove the offending inbox file and push. A later repair supersedes the invalid event; a current invalid upload blocks its batch without partially installing sibling posts.
- If a newer commit arrives or public bytes differ, let the latest queued workflow continue or rerun against the latest `main`. Pull bot commits before the next phone upload.
- If a cursor is missing or no longer belongs to the branch's first-parent history, review or restore Git history before repairing state. Resetting it can replay already processed uploads.
