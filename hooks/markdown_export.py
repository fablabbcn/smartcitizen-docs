"""
Export every page in the nav as a markdown file for LLMs, next to its HTML:

    /hardware/kit/  ->  /hardware/kit.md

plus an /llms.txt index (https://llmstxt.org) grouped by nav section.

The markdown is taken after the macros plugin has rendered the Jinja
templating, so variables and snippets are already resolved. On top of that:
- The HTML card grids (custom_theme/templates/*-item.html) become markdown lists
- Links are made absolute, and links to other pages point to their .md export
"""
import html
import os
import posixpath
import re
from urllib.parse import urljoin, urlsplit

from mkdocs.plugins import event_priority
from mkdocs.structure.pages import Page

_markdown = {}  # src_uri -> rendered markdown
_nav = None
_files = None


def md_url(url):
    url = url.strip('/')
    return f'{url}.md' if url else 'index.md'


@event_priority(-100)  # run after the macros plugin
def on_page_markdown(markdown, page, config, files):
    _markdown[page.file.src_uri] = markdown
    return markdown


def on_nav(nav, config, files):
    global _nav, _files
    _nav, _files = nav, files
    return nav


# Card grids -------------------------------------------------------------------

def _div_end(text, start):
    """Index after the </div> closing the <div> that opens at start"""
    depth = 0
    for m in re.compile(r'<div\b|</div>').finditer(text, start):
        depth += 1 if m.group() != '</div>' else -1
        if depth == 0:
            return m.end()
    return len(text)


def _strip_tags(fragment):
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def _card(fragment):
    href = re.search(r'href="([^"]+)"', fragment)
    name = re.search(r'<h1>(.*?)</h1>', fragment, re.S)
    excerpt = re.search(r'class="sensor-excerpt">(.*?)</p>', fragment, re.S)
    tags = [' '.join(_strip_tags(t).split())
            for t in re.findall(r'<p[^>]*>([^<|]*\|\s*<b.*?</b>)</p>', fragment, re.S)]
    line = f"- [{_strip_tags(name.group(1)) if name else href.group(1)}]({href.group(1) if href else ''})"
    if tags:
        line += f" ({'; '.join(tags)})"
    if excerpt and _strip_tags(excerpt.group(1)):
        line += f": {_strip_tags(excerpt.group(1))}"
    return line


def _cards_to_lists(markdown):
    while (start := markdown.find('<div class="sensor-block-multi')) != -1:
        end = _div_end(markdown, start)
        grid = markdown[start:end]
        cards, pos = [], 0
        while (s := grid.find('<div class="sensor-banner', pos)) != -1:
            e = _div_end(grid, s)
            cards.append(_card(grid[s:e]))
            pos = e
        markdown = markdown[:start] + '\n'.join(cards) + '\n' + markdown[end:]
    return markdown


# Links ------------------------------------------------------------------------

_LINK = re.compile(r'(\]\(|href="|src=")([^)"\s]+)')


def _rewrite_links(markdown, page, files, site_url, page_urls):
    base = urljoin(site_url, page.url)

    def fix(m):
        target = m.group(2)
        if re.match(r'^([a-z][a-z0-9+.-]*:|#)', target, re.I):
            return m.group(0)
        path, _, fragment = target.partition('#')
        if path.endswith('.md'):  # link to a source file
            src = posixpath.normpath(posixpath.join(posixpath.dirname(page.file.src_uri), path))
            f = files.get_file_from_path(src)
            if f is not None:
                path = '/' + f.url
        url = urljoin(base, path)
        page_path = urlsplit(url).path.lstrip('/')
        if page_path and not page_path.endswith('/') and page_path + '/' in page_urls:
            page_path += '/'
        if m.group(1) != 'src="' and page_path in page_urls:
            url = site_url + md_url(page_path)
        return m.group(1) + url + (f'#{fragment}' if fragment else '')

    return _LINK.sub(fix, markdown)


# Output -----------------------------------------------------------------------

def _index(items, site_url, depth=2):
    lines = []
    for item in items:
        if isinstance(item, Page):
            lines.append(f"- [{item.title}]({site_url}{md_url(item.url)})")
        elif item.is_section:
            lines += ['', f"{'#' * depth} {item.title}", '']
            lines += _index(item.children, site_url, min(depth + 1, 6))
    return lines


def on_post_build(config):
    site_url = config['site_url'].rstrip('/') + '/'
    pages = [p for p in _nav.pages if p.file.src_uri in _markdown]
    page_urls = {p.url for p in pages}
    for page in pages:
        markdown = _cards_to_lists(_markdown[page.file.src_uri])
        markdown = _rewrite_links(markdown, page, _files, site_url, page_urls)
        out = os.path.join(config['site_dir'], md_url(page.url))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w') as f:
            f.write(f"<!-- Source: {site_url}{page.url} -->\n\n{markdown}")

    lines = [f"# {config['site_name']}", '']
    if config.get('site_description'):
        lines += [f"> {config['site_description']}", '']
    lines += _index(_nav.items, site_url)
    with open(os.path.join(config['site_dir'], 'llms.txt'), 'w') as f:
        f.write('\n'.join(lines) + '\n')

