Title: Git status and submodules
lang: en
Category: Linux
Tags: git, planet-inuits
Slug: git-status-submodules

Here is an awesome trick for people using git submodules:

In your `~/.gitconfig`, add the following snippet:

    :::ini
    [status]
        submodulesummary = true


You should now get more information when running git status (`>` new commits, `<` 'removed' commits):

    :::text
    On branch master
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            modified:   submodule1
            modified:   submodule2

    Submodule changes to be committed:

    * submodule1 5c675a2...569574e (1):
      > One new feature

    * submodule2 5c03abb...ffe9f66 (1):
      < One super commit that would disappear :(

