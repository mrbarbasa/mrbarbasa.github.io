#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marifel Barbasa'
SITENAME = 'Marifel Barbasa'
SITEDESCRIPTION = 'musings of a lifelong learner'
SITEURL = ''
THEME = 'themes/pelicanyan'
PATH = 'content'
TIMEZONE = 'Pacific/Honolulu'
DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images', 'favicon.ico']
PAGE_PATHS = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None # 'feeds/all.atom.xml'
FEED_ALL_RSS = None # 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None # 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/mrbarbasa'),
    ('Kaggle', 'https://www.kaggle.com/mrbarbasa'),
    ('LinkedIn', 'https://www.linkedin.com/in/mrbarbasa'),)

# Uncomment following line if you want document-relative URLs
# when developing
# RELATIVE_URLS = True

# pelicanyan theme settings
# GA_ACCOUNT # GA account id such as 'UA-12344321-1' (see base.html)
TWITTER_ACCOUNT = 'mrbarbasa'
DIRECT_TEMPLATES = (
    'index', 'categories', 'authors', 'archives', 'sitemap', 
    'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DATE_FORMATS = { 'en': '%B %d, %Y', }
TYPOGRIFY = True # Optional: Need to install it with pip
