#!/usr/bin/env python

from pelican import signals
from git import Repo
import difflib
from pelican.utils import strftime
from datetime import datetime
from pelican import rstdirectives, contents  # NOQA
from markdown import Markdown
MD_EXTENSIONS = ['codehilite','extra']


ARTICLES = []

_md = Markdown(extensions=MD_EXTENSIONS)

def workoncontent(git,repo,content):
    gitcommits = git.log("--format=%H",content.source_path).split("\n")
    commits = []
    prevcommit = None
    prevcommitcontent = None
    for commithash in reversed(gitcommits):
        commit = repo.commit(commithash)
        tree = commit.tree
        passedcontent = False
        path = []
        for doc in content.source_path.split("/"):
            if doc == "content":
                passedcontent = True
            if passedcontent:
                path.append(doc)
                tree = tree[doc]
        commit_content = git.cat_file("-p",tree)
        if prevcommit == None or prevcommitcontent == None:
            diff = ["    :::markdown"]
            for i in commit_content.split("\n"):
                diff.append("     "+ i.decode('utf-8'))
            print_commit_content = "\n".join(diff)
        else:
            fromfile = ["a"] + path
            tofile = ["b"] + path
            diff = ["    :::diff"]
            for i in difflib.unified_diff(prevcommitcontent.split('\n'),commit_content.decode('utf-8').split('\n'),fromfile="/".join(fromfile),tofile="/".join(tofile)):
                diff.append("    " + i.strip("\n"))
            print_commit_content = "\n".join(diff)

        commits.append({
                'hash': commithash,
                'date': strftime(datetime.fromtimestamp(commit.authored_date), content.date_format),
                'message': commit.message,
                'content': _md.convert(print_commit_content)
            })
        prevcommit = commithash
        prevcommitcontent = commit_content.decode('utf-8')
    return commits

def genarticlegitdiffs(article_generator, writer):
    repo = Repo(".")
    git = repo.git
    for content in article_generator.articles:
        commits = workoncontent(git,repo,content)

        writer.write_file("/".join(content.save_as.split('/')[:-1])+"/source.html" , article_generator.get_template('source'),
              article_generator.context, article=content, source="".join(open(content.source_path,'r').readlines()).decode('utf-8'), back_link="index.html",
              override_output=hasattr(content, 'override_save_as'))
        writer.write_file("/".join(content.save_as.split('/')[:-1])+"/changelog.html" , article_generator.get_template('history'),
              article_generator.context, article=content, gitcommits=commits, back_link="index.html",
              override_output=hasattr(content, 'override_save_as'))

def genpagegitdiffs(page_generator, writer):
    repo = Repo(".")
    git = repo.git
    for content in page_generator.pages:
        commits = workoncontent(git,repo,content)

        writer.write_file(".".join(content.save_as.split('.')[:-1])+"-source.html" , page_generator.get_template('source'),
              page_generator.context, article=content, source="".join(open(content.source_path,'r').readlines()).decode('utf-8'),
              override_output=hasattr(content, 'override_save_as'), back_link=content.save_as.split('/')[-1])
        writer.write_file(".".join(content.save_as.split('.')[:-1])+"-changelog.html" , page_generator.get_template('history'),
              page_generator.context, article=content, gitcommits=commits,
              override_output=hasattr(content, 'override_save_as'), back_link=content.save_as.split('/')[-1])

def add_links(content):
    repo = Repo(".")
    git = repo.git
    try:
        if isinstance(content, contents.Static):
            return
        elif isinstance(content, contents.Article):
            content.commits = workoncontent(git,repo,content)
            content.source_link = "source.html"
            content.change_link = "changelog.html"
        elif isinstance(content, contents.Page):
            content.commits = workoncontent(git,repo,content)
            content.source_link = ".".join(content.save_as.split('/')[-1].split('.')[:-1])+"-source.html"
            content.change_link = ".".join(content.save_as.split('/')[-1].split('.')[:-1])+"-changelog.html"
    except:
        print content


def register():
    signals.content_object_init.connect(add_links)
    signals.article_writer_finalized.connect(genarticlegitdiffs)
    signals.page_writer_finalized.connect(genpagegitdiffs)
