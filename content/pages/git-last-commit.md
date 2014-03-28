Title: Removing the last commit in git

A one shot command to remove the last commit in git.. useful when you want to re-apply a patch.

    EDITOR="echo noop >" git rebase -i HEAD~1
