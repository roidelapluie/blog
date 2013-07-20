#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Julien Pivotto'
SITENAME = u'sysadmin {\'roidelapluie\':}'
SITEURL = u'http://roidelapluie.be'

TIMEZONE = 'Europe/Paris'

import sys
sys.path.append('./')

from plugins import git_dates

PLUGINS = [git_dates]


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

DEFAULT_PAGINATION = 10

CSS_FILE='main-2107.css'

THEME='./notmyidea'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
