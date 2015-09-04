#!/usr/bin/env python
from pelican import signals
def gensymlinks(article_generator, writer):
    NEXT_DATE = None
    for content in article_generator.articles:
        if content.source_path == '/home/roidelapluie/blog/blog/content/articles/android-calendar.md':
            NEXT_DATE = content.date
    for content in article_generator.articles:
        if NEXT_DATE and content.date <= NEXT_DATE:
            writer.write_file(content.save_as.split('/')[-2]+".html" , article_generator.get_template(content.template),
                  article_generator.context, article=content, category=content.category,
                  override_output=hasattr(content, 'override_save_as'))
def register():
    signals.article_writer_finalized.connect(gensymlinks)
