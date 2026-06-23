# fivsevn System Map

This document is the operational map for the fivsevn system.

Its purpose is to give any AI collaborator enough context to understand the whole structure of fivsevn: public entry surface, content categories, repository responsibilities, publishing surfaces, storage rules, and routing decisions.

It is an AI-optimized operational brief written to make the system easier for assistants, agents, scheduled tasks, and future automation workflows to parse and use.

Core principles:

  * keep the system lightweight;
  * keep content portable;
  * separate display from source storage;
  * avoid unnecessary hierarchy;
  * preserve long-term maintainability;
  * route new material by function, medium, and public/private status.

* * *

## 1. Quick orientation

fivsevn is a lightweight personal publishing, archive, and creative system.

It is composed of several layers:

  * `fivsevn.com` — the public website and visual entrance.
  * `devlog.fivsevn.com` — the public text archive and GitHub Pages reading layer.
  * GitHub repositories — the long-term storage layer for text, sources, scripts, specs, assets, and system records.
  * WordPress — the visual presentation and page design layer.
  * YouTube — the video hosting layer.
  * assets repositories / CDN links — the preferred home for reusable images and static files.
  * private/internal repositories — the staging layer for private, unfinished, or not-yet-public material.

The system should be understood as a separation between:

    public display surface
    ↓
    portable source files
    ↓
    repository-level storage and maintenance rules

Pages are for presentation. Repositories are for source-of-truth storage.

* * *

## 2. Public surfaces

### 2.1 `fivsevn.com`

    https://fivsevn.com/

`fivsevn.com` is the public-facing entrance. It should be treated as the external link when presenting fivsevn to other people.

It is based on WordPress and is responsible for:

  * visual layout;
  * page organization;
  * public-facing navigation;
  * curated presentation;
  * image, video, and visual storytelling;
  * flexible page design.

WordPress is good for expressive pages and visual browsing, but it should not be treated as the only source of truth for important long-term content.

### 2.2 `devlog.fivsevn.com`

    https://devlog.fivsevn.com/

`devlog.fivsevn.com` is the public text archive and source-facing reading layer.

It is published from the `fivsevn-devlog` repository through GitHub Pages. It is used for:

  * long-form writing;
  * structured notes;
  * topic archives;
  * source lists;
  * reading logs;
  * backend maintenance logs;
  * repository text that should be publicly browsable.

Section pages on `fivsevn.com` may link to corresponding devlog articles when longer text, structured notes, source material, or archive records are needed.

When there is a conflict between the rendered devlog site and the repository source, prefer the repository source.

* * *

## 3. Page and content structure

The system can be understood through this content map:

    fivsevn.com
    │
    ├─ Knowledge and notes
    │  ├─ posts
    │  ├─ natsci
    │  └─ netcom
    │
    ├─ High-frequency life pages
    │  └─ foodie
    │
    ├─ Images and visual expression
    │  ├─ stills
    │  │  └─ bygone
    │  └─ motion
    │
    ├─ Sources and reading intake
    │  └─ intake
    │
    ├─ Narrative experiment
    │  └─ 57store
    │
    └─ Backend and publishing logs
       └─ blogops / system notes

    devlog.fivsevn.com
    └─ public text archive and source-facing reading layer

`fivsevn.com` provides the section-level public navigation. `devlog.fivsevn.com` provides long-form text, structured notes, source lists, archive records, and backend logs that can be linked from the relevant section pages.

The major categories are:

  * `posts` — default notes, essays, observations, miscellaneous writing.
  * `natsci` — natural science notes and observations.
  * `netcom` — networks, communications, technical systems, infrastructure, and engineering notes.
  * `foodie` — food, restaurants, drinks, and daily eating records.
  * `stills` — photography, still images, static visual work.
  * `bygone` — old photos, family images, memory-oriented visual archive.
  * `motion` — video, motion design, AI-generated motion, moving-image work.
  * `intake` — sources, feeds, reading inputs, daily news, external signals.
  * `57store` — narrative experiment, fictional archive, worldbuilding.
  * `blogops` — backend logs, publishing process, maintenance notes, system operations.

* * *

## 4. Visual and interface style

The fivsevn visual language is dark, low-saturation, and interface-oriented.

Common visual references:

  * monospace / code-font feeling;
  * terminal-like UI;
  * log and archive interfaces;
  * subdued color palette;
  * status-line and directory-tree aesthetics;
  * green link or status accents, often close to `#6becae`;
  * visual density controlled through text, symbols, comments, labels, and interface grammar rather than heavy images.

The site should feel like a browsable personal system rather than a conventional portfolio.

Each section has its own presentation metaphor:

  * `posts` behaves like a stream;
  * `foodie` behaves like a phone-chat or mobile-message interface;
  * `natsci` behaves like a species observation window;
  * `stills` behaves like a roll archive;
  * `motion` behaves like a livestream or video interface;
  * `devlog` behaves like a text directory and repository archive.

Do not flatten all pages into the same visual template unless the task explicitly requires it. Presentation form is part of the content.

* * *

## 5. Knowledge and note categories

### 5.1 `posts`

    https://fivsevn.com/posts/
    https://devlog.fivsevn.com/posts/

`posts` is the default note area.

Use `posts` for:

  * ordinary notes;
  * personal observations;
  * short essays;
  * daily thoughts;
  * miscellaneous writing;
  * material that does not yet justify a more specific category.

There are two related surfaces:

  * `fivsevn.com/posts/` — more stream-like, casual, short, and visually integrated into the WordPress site.
  * `devlog.fivsevn.com/posts/` — more archive-like, suitable for longer writing, formal notes, and Markdown files with frontmatter.

If a WordPress post needs to reference a longer text, it can link to the corresponding devlog article.

### 5.2 `natsci`

    https://fivsevn.com/natsci/
    https://devlog.fivsevn.com/natsci/

`natsci` means natural science.

Use `natsci` for:

  * natural science knowledge;
  * biology;
  * species observations;
  * natural objects;
  * scientific concepts;
  * natural phenomena;
  * structured notes about the natural world.

`fivsevn.com/natsci/` is more visual and observational. `devlog.fivsevn.com/natsci/` is more suitable for source material, articles, and structured notes.

### 5.3 `netcom`

    https://fivsevn.com/netcom/
    https://devlog.fivsevn.com/netcom/

`netcom` means networks, communications, and technical systems.

Use `netcom` for:

  * networking;
  * communication systems;
  * protocols;
  * radio / RF;
  * computing systems;
  * embedded systems;
  * technical infrastructure;
  * engineering notes.

`fivsevn.com/netcom/` provides the section-level surface when a public page is needed. `devlog.fivsevn.com/netcom/` is suitable for longer writing, technical notes, source material, and Markdown files with frontmatter.

* * *

## 6. High-frequency life pages

### 6.1 `foodie`

    https://fivsevn.com/foodie/

`foodie` is the food and drink page.

It is a high-frequency life page, not a sibling of the knowledge categories `posts / natsci / netcom`.

Use `foodie` for:

  * food;
  * drinks;
  * restaurants;
  * daily eating records;
  * food photos;
  * lightweight food-related notes.

The page currently uses a phone-message-like interface. WordPress is appropriate here because this section depends heavily on visual presentation and frequent small updates.

Future lifestyle pages can be added at a similar level only when enough content exists and the new page has its own recognizable presentation logic.

* * *

## 7. Images and visual expression

Images, photography, graphic work, and display methods are part of fivsevn’s expressive system.

General rule:

    image/source asset → fivsevn-assets
    visual page display → WordPress

Images should usually live in `fivsevn-assets`. WordPress should reference them rather than becoming the only storage location.

### 7.1 `stills`

    https://fivsevn.com/stills/

`stills` is the static image area.

Use `stills` for:

  * photography;
  * still images;
  * graphic visuals;
  * curated image sets;
  * visual work where the still image is the main object.

The current style emphasizes black-and-white photography, visual sequencing, and curated display.

### 7.2 `bygone`

    https://fivsevn.com/stills/bygone/

`bygone` is a sub-area of `stills` for old photos and memory-oriented images.

Use `bygone` for:

  * family old photos;
  * historical images;
  * memory archives;
  * time-marked visual material.

The current design treats each image as an individual post for easier browsing and commenting.

### 7.3 `motion`

    https://fivsevn.com/motion/

`motion` is the moving-image area.

Use `motion` for:

  * videos;
  * motion design;
  * moving-image experiments;
  * AI-generated motion;
  * visual work where time, movement, or sequence is central.

Videos should usually be hosted on YouTube and embedded into WordPress pages. Large video files should not be stored directly in GitHub or WordPress unless there is a specific reason.

* * *

## 8. Sources and reading intake

### 8.1 `intake`

    https://fivsevn.com/intake/
    https://devlog.fivsevn.com/intake/
    https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/intake

`intake` is the source and reading-input area.

Use `intake` for:

  * RSS sources;
  * reading lists;
  * external signals;
  * daily news feeds;
  * institutions, projects, observatories;
  * journals and publications;
  * datasets;
  * newsletters;
  * report series;
  * tools and databases.

`intake` is not the same as formal notes. It mainly supports reading, browsing, source collection, and revisitability.

`fivsevn.com/intake/` can provide the public-facing browsing surface. `devlog.fivsevn.com/intake/` and the repository source provide the structured source archive.

A source belongs in `intake`. It becomes a formal note only when it is summarized, commented on, compared, quoted, or turned into an independent idea.

Conversion rules:

    source / feed / institution → intake
    source reading summary → posts
    natural science summary → natsci
    network / communications / technical-system summary → netcom
    publishing process / script / maintenance experience → blogops

* * *

## 9. Narrative experiment

### 9.1 `57store`

    https://fivsevn.com/57store/

`57store` is the narrative experiment area.

Use `57store` for:

  * fictional archive material;
  * worldbuilding;
  * story fragments;
  * settings;
  * characters;
  * scenes;
  * objects;
  * text that lives between notes and fiction.

`57store` must stay separate from real-world content because it represents a self-contained fictional world.

Routing rule:

    real-world content → posts / natsci / netcom / foodie / intake
    fictional world / narrative atmosphere → 57store

If the content is only for public page display, WordPress may be enough. If it involves worldbuilding source files, settings, interactive pages, scripts, or reusable resources, use `fivsevn-57store`.

Do not mix `57store` content into `posts`, `blogops`, or the ordinary archive unless the task explicitly concerns cross-referencing or system documentation.

* * *

## 10. Backend and publishing logs

### 10.1 `blogops`

    https://devlog.fivsevn.com/blogops/

`blogops` is the backend maintenance and publishing-method area.

Use `blogops` for:

  * blog maintenance records;
  * publishing workflows;
  * automation scripts;
  * WordPress / GitHub / assets coordination;
  * CDN usage notes;
  * system organization methods;
  * maintenance notes written for the owner’s future self;
  * operational documentation.

When a task is about how the system is maintained, published, migrated, structured, or automated, `blogops` is usually the right destination.

* * *

## 11. Repository structure

Pages and repositories should be understood separately:

  * pages are for display, navigation, and visual organization;
  * repositories are for preservation, management, migration, and specifications.

GitHub namespace convention:

  * `fivsevn-agy` — workflows, text, specifications, collaboration-related repositories.
  * `fivsevn` — public brand assets, visual resources, and independent subsystems.

Repository map:

    GitHub / repositories
    │
    ├─ fivsevn-agy/fivsevn-devlog
    ├─ fivsevn/fivsevn-assets
    ├─ fivsevn-agy/fivsevn-spec
    ├─ fivsevn/fivsevn-57store
    └─ fivsevn/fivsevn-internal

### 11.1 `fivsevn-devlog`

    https://github.com/fivsevn-agy/fivsevn-devlog

`fivsevn-devlog` is the main text repository.

Use it for:

  * `posts`;
  * `natsci`;
  * `netcom`;
  * `intake`;
  * `blogops`;
  * important Markdown files;
  * long-form text;
  * source lists;
  * automation scripts;
  * portable body text.

Important text and portable writing should usually be saved here first.

### 11.2 `fivsevn-assets`

    https://github.com/fivsevn/fivsevn-assets

`fivsevn-assets` is the static asset repository.

Use it for:

  * images;
  * photography;
  * icons;
  * graphic materials;
  * page reference assets;
  * static files that can be served through CDN or direct links.

Images should usually enter `fivsevn-assets` first and then be referenced by WordPress pages.

### 11.3 `fivsevn-spec`

    https://github.com/fivsevn-agy/fivsevn-spec

`fivsevn-spec` is the specification and convention repository.

Use it for:

  * naming rules;
  * metadata rules;
  * document formats;
  * classification principles;
  * workflow conventions;
  * habits and maintenance rules that need structure.

It is not limited to the blog. It can also support structured daily-life systems.

### 11.4 `fivsevn-57store`

    https://github.com/fivsevn/fivsevn-57store

`fivsevn-57store` is the dedicated repository or subsystem for the 57store fictional world.

Use it for:

  * narrative experiment source files;
  * worldbuilding material;
  * 57store page resources;
  * interactive pages;
  * future `57store.fivsevn.com` work;
  * reusable resources related to the fictional system.

### 11.5 `fivsevn-internal`

    https://github.com/fivsevn/fivsevn-internal

`fivsevn-internal` is the private repository.

Use it for:

  * private drafts;
  * temporary material;
  * internal plans;
  * records not suitable for publication;
  * content whose public/private status is still unclear.

If public status is uncertain, put the material in `internal` first. Move it to a public repository or page only after it is clearly safe and useful to publish.

* * *

## 12. Responsibility of WordPress, GitHub, assets, and YouTube

### 12.1 WordPress

WordPress is responsible for `fivsevn.com` page editing and visual display.

Use WordPress for:

  * entrance pages;
  * visual layouts;
  * flexible page design;
  * reader-facing browsing experience;
  * curated organization of images and videos.

Do not use WordPress as the only long-term storage layer for important source text or reusable assets.

### 12.2 GitHub

GitHub is responsible for long-term preservation and portability.

Use GitHub for:

  * Markdown body text;
  * image resources;
  * specification files;
  * system records;
  * source registries;
  * automation scripts;
  * materials that should be portable and versioned.

`devlog.fivsevn.com` is published from the `fivsevn-devlog` repository through GitHub Pages.

### 12.3 Assets

`fivsevn-assets` stores images and static resources.

Basic rule:

    image file → assets
    page display → WordPress

WordPress pages may reference assets through CDN or direct links.

### 12.4 YouTube

    https://www.youtube.com/@fivsevn

YouTube is used for video hosting.

Use YouTube for:

  * videos;
  * large moving-image files;
  * embeddable video material;
  * 57store / CCTV-related video work when it belongs to that narrative system.

Avoid storing large video files directly in GitHub or WordPress.

### 12.5 Responsibility table

| Layer | Responsible for | Not responsible for |
|---|---|---|
| WordPress | Display, pages, visual layout, entrance organization | Sole long-term storage |
| GitHub | Preservation, migration, specifications, scripts, body text | Complex visual page layout |
| `fivsevn-devlog` | Text, long-form writing, sources, automation scripts, backend logs | Large images and videos |
| `fivsevn-assets` | Images, photography, icons, static resources | Body text |
| YouTube | Video hosting | Text archive |
| `fivsevn-spec` | Naming, metadata, formatting, classification, workflow rules | Daily body content |
| `fivsevn-internal` | Private material, uncertain-public-status content | Public display |

### 12.6 License principle

Different repositories may use different licenses depending on content type.

General rule:

  * code and tools can use open-source licenses;
  * public documents can use Creative Commons licenses;
  * personal photos, visual archives, family materials, and fictional-world resources follow the license or usage statement in their own repository.

Always prefer the local `LICENSE`, repository notice, or file-level instruction when available.

* * *

## 13. New content routing rules

When adding new content, classify it by public status and expression form first.

Default routing:

  * uncertain public/private status → `fivsevn-internal`
  * ordinary notes, thoughts, miscellaneous observations → `posts`
  * natural science, biology, nature observations → `natsci`
  * networks, communications, technical systems → `netcom`
  * food and daily eating records → `foodie`
  * static images, photography, graphic visuals → `stills`
  * old photos and family memory images → `bygone`
  * video, motion, moving images → `motion`
  * sources, RSS, news, reading inputs → `intake`
  * story, worldbuilding, narrative experiment → `57store`
  * blog maintenance, system organization, publishing methods → `blogops`

### 13.1 Decision order

When classifying new material, follow this order:

  1. Is it uncertain whether it should be public? → `internal`
  2. Is it a source, feed, or reading list? → `intake`
  3. Is it backend maintenance or publishing workflow? → `blogops`
  4. Does it belong to the 57store fictional world? → `57store`
  5. Is the main object a static image? → `stills` or `bygone`
  6. Is the main object video or motion? → `motion`
  7. Is it food or daily eating content? → `foodie`
  8. Is it natural science? → `natsci`
  9. Is it networks, communications, or technical systems? → `netcom`
  10. Otherwise → `posts`

### 13.2 Content location table

| Content type | Default storage | Display surface | Notes |
|---|---|---|---|
| Ordinary essays and miscellaneous observations | `fivsevn-devlog/posts` | `fivsevn.com/posts` or `devlog/posts` | Default destination |
| Long-form formal notes | `fivsevn-devlog/posts` | `devlog/posts` | Can be linked from WordPress |
| Natural science | `fivsevn-devlog/natsci` | `fivsevn.com/natsci` or `devlog/natsci` | Species, observation, science concepts |
| Networks / communications / technical systems | `fivsevn-devlog/netcom` | `fivsevn.com/netcom` or `devlog/netcom` | Technical notes and infrastructure writing |
| Sources / RSS / reading sources | `fivsevn-devlog/intake` | `fivsevn.com/intake` or `devlog/intake` | Not equivalent to formal notes |
| Backend maintenance | `fivsevn-devlog/blogops` | `devlog/blogops` | Publishing process, system maintenance |
| Images / static visual resources | `fivsevn-assets` | WordPress pages | Image files should not primarily live in WordPress |
| Video | YouTube | WordPress embeds | Large files should not enter GitHub |
| 57store worldbuilding | `fivsevn-57store` or WordPress 57store | `fivsevn.com/57store` | Keep separate from real-world content |
| Private or uncertain-public-status material | `fivsevn-internal` | Not public | Migrate only after review |

### 13.3 When to create a new top-level page or repository

Only create a new top-level page or repository if all of the following are true:

  1. the existing content volume clearly exceeds what ordinary categories can hold;
  2. the new area has its own display form or maintenance workflow;
  3. it does not naturally fit inside `posts / natsci / netcom / intake / blogops / stills / motion / 57store`;
  4. the new area will not create duplicate entrances or unnecessary hierarchy.

Do not add structure merely for completeness.

* * *

## 14. AI collaboration rules

AI collaborators should follow these rules when working with fivsevn content.

### 14.1 First distinguish pages from repositories

Before editing, classifying, or proposing changes, identify whether the task concerns:

  * a public-facing page;
  * a source text file;
  * an asset;
  * a script;
  * a repository rule;
  * a private/internal draft.

Do not assume that the public page is the only source of truth.

### 14.2 Prefer source files over rendered pages

For important content and system logic, prefer repository files over rendered HTML.

Use rendered pages to understand presentation and browsing behavior. Use repository files to understand canonical content and structure.

### 14.3 Preserve lightweight structure

Do not introduce complex hierarchy unless there is a clear maintenance reason.

When uncertain:

  * use `posts` for public ordinary notes;
  * use `internal` for uncertain public/private material;
  * avoid creating new repositories or categories prematurely.

### 14.4 Respect the 57store boundary

`57store` is a fictional/narrative system. Do not blend it into real-world notes, backend logs, or general site documentation unless explicitly discussing its system design.

### 14.5 Treat `intake` as source intake, not finished writing

`intake` is for sources and reading input. Do not convert sources into formal notes unless the task includes summarizing, commenting, comparing, citing, or developing them into an independent piece.

### 14.6 Preserve the visual grammar

When proposing page designs, keep the existing interface logic in mind:

  * dark, low-saturation, code/interface feeling;
  * section-specific metaphors;
  * restrained image density;
  * text, labels, comments, and structural marks as design elements.

Do not convert the system into a generic portfolio or blog layout unless explicitly asked.

### 14.7 Use the `ai/` folder as the AI-facing coordination layer

The `ai/` folder in `fivsevn-devlog` is reserved for AI collaboration support files.

It may contain:

  * machine-readable data bundles;
  * AI-readable summaries;
  * scheduling inputs;
  * monitoring files;
  * source registries;
  * assistant instructions;
  * future automation support files.

Files in `ai/` should be stable, easy to parse, and useful for assistants. They are not primarily visual pages. The root `system-map.md` is the system-level map.

* * *

## 15. Minimal summary

fivsevn is a lightweight personal creative system with `fivsevn.com` as the public entrance, GitHub as the long-term source and archive layer, WordPress as the display layer, YouTube as the video layer, and several content zones: knowledge notes, lifestyle pages, visual expression, source intake, narrative experiment, and backend logs.

When in doubt:

    important text → fivsevn-devlog
    images → fivsevn-assets
    videos → YouTube
    private or uncertain material → fivsevn-internal
    ordinary public notes → posts
    sources → intake
    system maintenance → blogops
    fictional world material → 57store
