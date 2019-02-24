#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jens Bergmann'
SITENAME = u'Logbuch @ 1cu.de'
SITEURL = 'https://1cu.de'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/jnsbrgmnn'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_SAVE_AS = '{date:%Y-%m}/{slug}.html'
ARTICLE_URL = '{date:%Y-%m}/{slug}.html'
