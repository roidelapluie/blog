#!/usr/bin/env python

from pelican import signals

import six
if not six.PY3:
    from codecs import open



def rss_generated(path,context,feed):
    encoding = 'utf-8' if six.PY3 else None
    npath=path.split('/')
    npath[-1] = 'pic.' + npath[-1]
    npath = '/'.join(npath)
    for item in feed.items:
        item['description'] += '<small style="margin-top:2em;"><a href="%s">This article</a> has been written by <a href="http://roidelapluie.be/">Julien Pivotto</a> and is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.</small>' % item['link']
    with open(path, 'w', encoding=encoding) as fp:
        feed.write(fp, 'utf-8')
    for item in feed.items:
        item['description'] = '<img src="http://roidelapluie.be/hackergotchi.png" width="100" height="100" alt="" align="right" style="float: right;" />' + item['description']
    with open(npath, 'w', encoding=encoding) as fp:
        feed.write(fp, 'utf-8')

def register():
    signals.feed_written.connect(rss_generated)
