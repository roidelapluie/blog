#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Julien Pivotto'
SITENAME = u'roidelapluie'
SITEURL = u'http://roidelapluie.be'
EXHERBO_SITEURL = u'http://exherbo.roidelapluie.be'
TAGLINE="Julien Pivotto is a passionate Linux Systems Administrator, currently working at <a href=\"http://www.inuits.eu/\">Inuits</a>."

TIMEZONE = 'Europe/Paris'

import sys
sys.path.append('./')

from plugins import git_dates

PLUGINS = [git_dates]
CACHE_CONTENT = False


DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_RSS='rss.xml'
FEED_ALL_ATOM='atom.xml'

# Blogroll
LINKS =  (
        ('Inuits', 'https://www.inuits.eu/'),
        ('RMLL', 'https://rmll.info/'),
        ('Loadays', 'https://loadays.org/'),
        ('Fosdem', 'https://fosdem.org/'),
        ('Gajim', 'https://gajim.org/'),
         )
# Social widget
SOCIAL = (
        ('github', 'https://github.com/roidelapluie'),
        ('twitter', 'https://twitter.com/roidelapluie'),
        ('linkedin', 'https://linkedin.com/in/julienpivotto'),
        ('slideshare', 'http://www.slideshare.net/roidelapluie')
        )

DEFAULT_PAGINATION = 2
DEFAULT_ORPHANS = 1
USER_LOGO_URL = SITEURL + '/logo.png'

#CSS_FILE='main-2107.css'

THEME='./pelican-svbhack'
PAGE_URL='wiki/{slug}.html'
PAGE_SAVE_AS='wiki/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/hai.png',
    'extra/humans.txt',
    'extra/logo.png',
]
EXTRA_PATH_METADATA = {
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/hai.png': {'path': 'hai.png'},
    'extra/logo.png': {'path': 'logo.png'},
}

MD_EXTENSIONS = ['codehilite','extra']
