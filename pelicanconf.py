#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'simple'

AUTHOR = 'Cleveland PyLadies'
SITENAME = 'Cleveland PyLadies'
SITEURL = 'https://clepyladies.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Source for this project on GitHub', 'https://www.github.com/clepyladies/clepyladies.github.io'),)

# Social widget
SOCIAL = (('Find us on Meetup', 'https://www.meetup.com/CLE-PyLadies'),
          ('Connect with us on Twitter', 'https://www.twitter.com/clepyladies'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/favicon.ico']

LINKS_WIDGET_NAME = 'Resources'
SOCIAL_WIDGET_NAME = 'Connect with us'

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
