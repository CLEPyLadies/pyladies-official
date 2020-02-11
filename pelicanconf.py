#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'pelican-themes/Flex'

AUTHOR = 'Cleveland PyLadies'
SITENAME = 'Cleveland PyLadies'
SITETITLE = 'Cleveland PyLadies'
SITEURL = 'https://clepyladies.github.io/pyladies-official'
SITESUBTITLE = 'A community for PyLadies, PyNonbinaries, \n and the PyCurious'
SITELOGO = SITEURL + '/images/pylady_geek_girl_standard.png'
SITEDESCRIPTION = 'Cleveland, Ohio chapter of PyLadies - a Python professional organization' # For <meta> tag in header
FAVICON = SITEURL + '/images/favicon.ico'
# BROWSER_COLOR = '#810016'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['representative_image', 'pin_to_top', 'post_stats']

# USE_LESS = True

# MAIN_MENU = True

PATH = 'content'
ARTICLE_PATHS = ['articles', 'blog', 'past-events']

TIMEZONE = 'America/New_York'
OG_LOCALE = 'en_US'
LOCALE = 'en_US.UTF-8'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Upcoming Events', 'https://www.meetup.com/cle-pyladies'),
         ('Past Events', 'https://clepyladies.github.io/pyladies-official/past-events'),
         ('Cleveland Python news', 'https://tinyletter.com/clepy'),
         ('Blog for us!', 'https://medium.com/cleveland-pyladies'),
         ('PyLadies Global', 'https://www.pyladies.com'),)

# Social widget
SOCIAL = (('twitter', 'https://www.twitter.com/clepyladies'),
          ('facebook', 'https://www.facebook.com/clepyladies'),
          ('meetup', 'https://www.meetup.com/cle-pyladies'),
          ('instagram', 'https://www.instagram.com/clepyladies'),
          ('slack', 'https://cleveland-tech.slack.com'),
          ('slack', 'https://slackin.pyladies.com'),
          ('github', 'https://www.github.com/clepyladies'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# LINKS_WIDGET_NAME = 'Contribute to Open-Source'
# SOCIAL_WIDGET_NAME = 'Connect'

DISPLAY_PAGES_ON_MENU = True
