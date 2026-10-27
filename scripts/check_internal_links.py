"""
Check internal links and anchors in the built site (mkdocs build).

External links are not checked: they are slow and flaky (one request per URL).
Only links on pages in the nav are checked (drafts and snippets are also built,
but not published); use --all to check every built page.

Footnote back-references (#fnref:N) are ignored: they only break when a
footnote is defined but never cited, which is harmless.

Usage:
    mkdocs build
    python scripts/check_internal_links.py [--all] [site_dir]

Exits with 1 if any broken link is found.
"""
import argparse
import os
import sys
from collections import defaultdict
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit

SITE_URL = 'https://docs.smartcitizen.me/'
LINK_ATTRS = {'a': 'href', 'img': 'src', 'source': 'src', 'iframe': 'src'}
SKIP_SCHEMES = ('mailto:', 'tel:', 'javascript:', 'data:')


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('id', 'name'):
            if attrs.get(key):
                self.ids.add(attrs[key])
        attr = LINK_ATTRS.get(tag)
        if attr and attrs.get(attr):
            self.links.append(attrs[attr].strip())


def page_url(site_dir, path):
    """URL of a built file, relative to the site root (hardware/kit/index.html -> /hardware/kit/)"""
    rel = os.path.relpath(path, site_dir).replace(os.sep, '/')
    if rel.endswith('index.html'):
        rel = rel[:-len('index.html')]
    return '/' + rel


def resolve(site_dir, url_path):
    """Built file for a URL path, or None if it doesn't exist"""
    target = os.path.join(site_dir, unquote(url_path).lstrip('/'))
    if os.path.isdir(target):
        target = os.path.join(target, 'index.html')
    return target if os.path.isfile(target) else None


def nav_urls(config_file='mkdocs.yml'):
    from mkdocs.config import load_config
    from mkdocs.structure.files import get_files
    from mkdocs.structure.nav import get_navigation

    config = load_config(config_file)
    nav = get_navigation(get_files(config), config)
    return {unquote('/' + page.url) for page in nav.pages}


def main(site_dir='site', check_all=False):
    pages = {}
    for root, _, files in os.walk(site_dir):
        for name in files:
            if name.endswith('.html'):
                path = os.path.join(root, name)
                parser = PageParser()
                with open(path, encoding='utf-8') as f:
                    parser.feed(f.read())
                pages[path] = parser

    published = None if check_all else nav_urls()
    broken = defaultdict(list)
    checked = 0
    for path, parser in pages.items():
        base = page_url(site_dir, path)
        if published is not None and unquote(base) not in published:
            continue
        checked += 1
        for link in parser.links:
            if link.startswith(SITE_URL):
                link = '/' + link[len(SITE_URL):]
            if link.startswith(SKIP_SCHEMES) or urlsplit(link).scheme or link.startswith('//') \
                    or link.startswith('#fnref:'):
                continue
            url = urlsplit(urljoin(base, link))
            target = resolve(site_dir, url.path)
            if target is None:
                broken[base].append(link)
            elif url.fragment and target.endswith('.html'):
                if unquote(url.fragment) not in pages[target].ids:
                    broken[base].append(link)

    for page in sorted(broken):
        print(page)
        for link in sorted(set(broken[page])):
            print(f'    {link}')
    count = sum(len(set(links)) for links in broken.values())
    print(f'\n{count} broken internal links in {len(broken)} pages ({checked} pages checked)')
    return 1 if count else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0].strip())
    parser.add_argument('site_dir', nargs='?', default='site')
    parser.add_argument('--all', action='store_true', help='check every built page, not only the nav')
    args = parser.parse_args()
    sys.exit(main(args.site_dir, args.all))
