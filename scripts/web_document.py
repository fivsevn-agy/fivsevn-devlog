"""Language and search/share metadata for the three Devlog HTML generators.

Only the document language, known UI language attributes and managed head tags
change. Body text, scripts, styles and images belong to their owning builder.
This module uses the standard library so the Intake job can use it as well.
"""
from html import escape, unescape
from html.parser import HTMLParser
import re
from urllib.parse import urljoin, urlparse


ORIGIN = 'https://devlog.fivsevn.com'
SITE_NAME = 'fivsevn-devlog'
MANAGED_NAMES = {'description', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image'}
MANAGED_PROPERTIES = {'og:title', 'og:description', 'og:type', 'og:url', 'og:site_name', 'og:locale', 'og:image'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
LANGUAGE = re.compile(r'[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*\Z')
BLOCK = re.compile(r'<!-- devlog-document-metadata:start -->.*?<!-- devlog-document-metadata:end -->', re.S)


class Document(HTMLParser):
    """Read visible prose and exact head tag ranges without serializing HTML."""
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.text = text
        self.lines = [0] + [match.end() for match in re.finditer('\n', text)]
        self.in_head = False
        self.in_body = False
        self.head_end = None
        self.html_tag = None
        self.tags = []
        self.title = []
        self.prose = []
        self.images = []
        self.ui_tags = []
        self.stack = []
        self.feed(text)

    def position(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        raw = self.get_starttag_text()
        if tag == 'html':
            self.html_tag = (self.position(), self.position() + len(raw), values)
        if tag == 'head':
            self.in_head = True
        if self.in_head and tag in {'meta', 'link'}:
            self.tags.append((self.position(), self.position() + len(raw), tag, values))
        if tag == 'body':
            self.in_body = True
        if self.in_body and tag == 'img' and values.get('src'):
            self.images.append(values['src'])
        if self.in_body and 'lang' not in values:
            classes = set(values.get('class', '').split())
            language = None
            if classes & {'title-zh', 'section-title-zh', 'section-description-zh'}:
                language = 'zh-CN'
            elif tag == 'div' and {'footer', 'border-top'} <= classes:
                language = 'en'  # The existing Primer open-source footer.
            if language:
                self.ui_tags.append((self.position(), self.position() + len(raw), raw, language))
        if tag not in VOID:
            classes = set(values.get('class', '').split())
            hidden = (tag in {'script', 'style', 'pre', 'code', 'noscript', 'template', 'nav', 'footer'}
                      or {'footer', 'border-top'} <= classes
                      or 'hidden' in values or values.get('aria-hidden') == 'true'
                      or bool(self.stack and self.stack[-1][1]))
            self.stack.append((tag, hidden))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == 'head':
            self.head_end = self.position()
            self.in_head = False
        if tag == 'body':
            self.in_body = False
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, value):
        if self.in_head and self.stack and self.stack[-1][0] == 'title':
            self.title.append(value)
        if self.in_body and not (self.stack and self.stack[-1][1]):
            self.prose.append(value)

    def existing(self, *, name=None, property=None):
        for _, _, tag, attrs in self.tags:
            if tag == 'meta' and ((name and attrs.get('name', '').lower() == name)
                                  or (property and attrs.get('property', '').lower() == property)):
                return attrs.get('content', '')
        return ''

    def canonical(self):
        for _, _, tag, attrs in self.tags:
            if tag == 'link' and 'canonical' in attrs.get('rel', '').lower().split():
                return attrs.get('href', '')
        return ''


def clean_text(value, limit=None):
    text = re.sub(r'\s+', ' ', unescape(str(value or ''))).strip()
    text = ''.join(char for char in text if ord(char) >= 32)
    if limit and len(text) > limit:
        text = text[:limit - 1].rstrip() + '…'
    return text


def visible_text(html):
    """Extract prose without counting scripts, styles, fenced code or hidden UI."""
    if '<body' not in html.lower():
        html = '<html><head></head><body>' + html + '</body></html>'
    return clean_text(' '.join(Document(html).prose))


def language_tag(value):
    if not isinstance(value, str) or not LANGUAGE.fullmatch(value):
        return None
    if value.lower() == 'zh':
        return 'zh-CN'
    return value.split('-')[0].lower() + ''.join('-' + (part.upper() if len(part) == 2 else part.title()) for part in value.split('-')[1:])


def primary_language(metadata=None, prose=''):
    metadata = metadata or {}
    explicit = language_tag(metadata.get('lang'))
    if explicit:
        return explicit
    languages = metadata.get('languages') or []
    if isinstance(languages, str):
        languages = [languages]
    languages = list(dict.fromkeys(tag for value in languages if (tag := language_tag(value))))
    if len(languages) == 1:
        return languages[0]
    # Compare Chinese characters with Latin words, rather than their letters.
    # Source-code and script/style text is excluded by Document before this call.
    chinese = len(re.findall(r'[\u3400-\u9fff]', prose))
    japanese = len(re.findall(r'[\u3040-\u30ff]', prose))
    latin = len(re.findall(r'[A-Za-z]+(?:[\'-][A-Za-z]+)*', prose))
    if japanese >= 4 and japanese * 2 >= chinese:
        detected = 'ja'
    elif chinese and chinese >= latin:
        detected = 'zh-CN'
    elif latin:
        detected = next((tag for tag in languages if tag.startswith('en')), languages[0] if languages else 'en')
    elif chinese:
        detected = 'zh-CN'
    else:
        detected = languages[0] if languages else 'en'
    return detected


def http_url(value, base):
    if not isinstance(value, str) or not value.strip():
        return ''
    resolved = urljoin(base, value.strip())
    parsed = urlparse(resolved)
    if parsed.scheme not in {'https', 'http'} or not parsed.netloc or parsed.username or parsed.password:
        return ''
    return resolved


def document_metadata(html, *, url, metadata=None, description=None, image=None, page_type=None, noindex=False):
    """Return HTML with head metadata and language attributes, preserving text."""
    metadata = metadata or {}
    document = Document(html)
    if document.head_end is None or document.html_tag is None:
        raise ValueError('Expected a complete HTML document with a head')
    block = BLOCK.search(html, 0, document.head_end)
    prose = clean_text(' '.join(document.prose))
    lang = primary_language(metadata, prose)
    title = clean_text(''.join(document.title)) or clean_text(metadata.get('title')) or SITE_NAME
    summary = next((clean_text(value, 160) for value in
                    (metadata.get('description'), metadata.get('summary'), description,
                     document.existing(name='description'), prose, metadata.get('title'), title)
                    if clean_text(value)), title)
    canonical = (http_url(metadata.get('canonical_url'), url) or http_url(document.canonical(), url)
                 or http_url(url, ORIGIN + '/'))
    if not canonical:
        raise ValueError('A public HTTP(S) canonical URL is required')
    chosen_image = next((found for value in (image, document.existing(property='og:image'),
                                             document.existing(name='twitter:image'), *document.images)
                         if (found := http_url(value, canonical))), '')
    if page_type is None:
        page_type = 'website' if metadata.get('type') in {None, 'index'} else 'article'
    locale = lang.replace('-', '_')
    if '-' not in lang:
        locale = {'en': 'en_US', 'ja': 'ja_JP'}.get(lang, lang)
    attributes = [
        ('name', 'description', summary), ('property', 'og:title', title),
        ('property', 'og:description', summary), ('property', 'og:type', page_type),
        ('property', 'og:url', canonical), ('property', 'og:site_name', SITE_NAME),
        ('property', 'og:locale', locale),
        ('name', 'twitter:card', 'summary_large_image' if chosen_image else 'summary'),
        ('name', 'twitter:title', title), ('name', 'twitter:description', summary),
    ]
    if chosen_image:
        attributes.extend([('property', 'og:image', chosen_image), ('name', 'twitter:image', chosen_image)])
    tags = ['<link rel="canonical" href="' + escape(canonical, quote=True) + '">']
    tags.extend('<meta ' + kind + '="' + name + '" content="' + escape(value, quote=True) + '">' for kind, name, value in attributes)
    # Keep any authored robots/googlebot instruction, including an explicit index.
    authored_robots = any(tag == 'meta' and attrs.get('name', '').lower() in {'robots', 'googlebot'}
                          and not (block and block.start() <= start < block.end())
                          for start, _, tag, attrs in document.tags)
    if noindex and not authored_robots:
        tags.append('<meta name="robots" content="noindex, follow">')
    managed = []
    for start, end, tag, attrs in document.tags:
        if block and block.start() <= start < block.end():
            continue
        if ((tag == 'meta' and (attrs.get('name', '').lower() in MANAGED_NAMES
                              or attrs.get('property', '').lower() in MANAGED_PROPERTIES))
                or (tag == 'link' and 'canonical' in attrs.get('rel', '').lower().split())):
            managed.append((start, end))
    replacement = '<!-- devlog-document-metadata:start -->\n  ' + '\n  '.join(tags) + '\n  <!-- devlog-document-metadata:end -->'
    edits = [(start, end, '') for start, end in managed]
    if block:
        edits.append((block.start(), block.end(), replacement))
    else:
        edits.append((document.head_end, document.head_end, '  ' + replacement + '\n'))
    start, end, _ = document.html_tag
    opening = html[start:end]
    pattern = r'\s+lang\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)'
    if re.search(pattern, opening, re.I):
        opening = re.sub(pattern, ' lang="' + escape(lang, quote=True) + '"', opening, count=1, flags=re.I)
    else:
        opening = opening[:-1] + ' lang="' + escape(lang, quote=True) + '">'
    edits.append((start, end, opening))
    for start, end, raw, language in document.ui_tags:
        edits.append((start, end, raw[:-1] + ' lang="' + language + '">'))
    for start, end, text in sorted(edits, reverse=True):
        html = html[:start] + text + html[end:]
    return html
