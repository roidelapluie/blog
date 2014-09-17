#!/usr/bin/env python

from pelican import signals
from git import Repo
import difflib
from pelican.utils import strftime
from datetime import datetime
from pelican import rstdirectives  # NOQA
from markdown import Markdown
MD_EXTENSIONS = ['codehilite','extra']


ARTICLES = []

_md = Markdown(extensions=MD_EXTENSIONS)

def gengitdiffs(article_generator, writer):
    repo = Repo(".")
    git = repo.git
    for content in article_generator.articles:
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
                for i in commit_content.decode('utf-8').split("\n"):
                    diff.append("     "+ i)
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

        writer.write_file("/".join(content.save_as.split('/')[:-1])+"/source.html" , article_generator.get_template('source'),
              article_generator.context, article=content, source="".join(open(content.source_path,'r').readlines()).decode('utf-8'),
              override_output=hasattr(content, 'override_save_as'))
        writer.write_file("/".join(content.save_as.split('/')[:-1])+"/changelog.html" , article_generator.get_template('history'),
              article_generator.context, article=content, gitcommits=commits,
              override_output=hasattr(content, 'override_save_as'))

def register():
    signals.article_writer_finalized.connect(gengitdiffs)
