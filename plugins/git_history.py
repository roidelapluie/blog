#!/usr/bin/env python

from pelican import signals

import os



def get_source(content):
    content.git_filename = os.path.basename(content.source_path)

def register():
    signals.content_object_init.connect(get_source)
