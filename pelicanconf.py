#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Andy"
SITENAME = "God Object"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ["diary"]
STATIC_PATHS = ["css", "images"]

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/godobject"

MARKDOWN = {
    "extension_configs": {
        "mdx_wikilink_plus": {
            "base_url": "/pages",
        },
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}