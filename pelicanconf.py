#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import json

AUTHOR = u'Julien Pivotto'
SITENAME = u'roidelapluie'
SITEURL = u'file:///home/roidelapluie/blog/blog/output'
EXHERBO_SITEURL = u'https://roidelapluie.be/exherbo'
TAGLINE="Julien Pivotto is a passionate Linux Systems Administrator, currently working at <a href=\"https://www.inuits.eu/\">Inuits</a>."

TIMEZONE = 'Europe/Paris'

import sys
sys.path.append('./')

from plugins import git_dates, git_history, copyarticle, feed, gitdiff, colorize, i18n_subsites

PLUGINS = [git_dates, git_history, copyarticle, feed, gitdiff, i18n_subsites]
CACHE_CONTENT = False
LICENSE='Written by <a href="https://roidelapluie.be/">Julien Pivotto</a>. Licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.'


DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
JINJA_FILTERS = {'tojson': json.dumps, 'colorize': colorize.colorize}

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

FEED_RSS='rss.xml'
FEED_ALL_ATOM='atom.xml'

INDEX_SAVE_AS='blog/index.html'
# Blogroll
MENUITEMS =  (
        ('Blog', '%s/blog/index.html' % SITEURL),
        ('Notes', '%s/wiki/index.html' % SITEURL),
        ('About me', '%s/index.html' % SITEURL),
         )
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
SOCIAL=()

DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 1
USER_LOGO_URL = SITEURL + '/logo.png'

#CSS_FILE='main-2107.css'

THEME='./primertheme'
PAGE_URL='wiki/{slug}.html'
PAGE_SAVE_AS='wiki/{slug}.html'
DIRECT_TEMPLATES = ('index', 'categories', 'archives')
PAGINATED_DIRECT_TEMPLATES=('index',)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = [
    'images',
    'uploads',
    'extra/hai.png',
    'extra/humans.txt',
    'extra/logo.png',
    'extra/htaccess',
    'extra/hai100.png',
    'extra/33AE92DA.pub',
]
EXTRA_PATH_METADATA = {
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/hai.png': {'path': 'hai.png'},
    'extra/hai100.png': {'path': 'hackergotchi.png'},
    'extra/logo.png': {'path': 'logo.png'},
    'extra/33AE92DA.pub': {'path': 'gpg/33AE92DA.pub'},
}
SIDEBAR_IMAGE = "logo.png"

MD_EXTENSIONS = ['codehilite','extra']
EXTRA_TEMPLATES_PATHS=['templates']
I18N_SUBSITES = {
        'fr': {
            }
        }


languages_lookup = {
            'en': 'English',
            'fr': 'Français',
        }


def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

#TOP_TEXT='<strong>Happy New Year!</strong> Best wishes for 2015!'
