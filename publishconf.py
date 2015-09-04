#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://roidelapluie.be'
RELATIVE_URLS = False

TAG_FEED_RSS = 'feeds/%s.tag.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.cat.rss.xml'
FEED_ALL_ATOM = 'atom.xml'
TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.cat.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
MENUITEMS =  (
        ('Blog', '%s/blog/index.html' % SITEURL),
        ('Notes', '%s/wiki/index.html' % SITEURL),
        ('About me', '%s/index.html' % SITEURL),
         )

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
