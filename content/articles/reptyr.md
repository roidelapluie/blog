Title: Rattaching a running process to a screen
lang: en
Category: Linux
Tags: sysadmin, screen, planet-inuits
Slug: reptyr

[Reptyr](https://github.com/nelhage/reptyr) is a small project written in C that enable you to "re-pty" your process. It means you can, for example, attach a running process inside a screen.

For example, you launched irssi outside your screen, and you do not want to relaunch it.

Install reptyr, then, in a screen, run the following commands:

    :::bash
    $ pidof irssi
    27518
    $ reptyr 27518

That's it. The process will be rattached to Init but you will be able to use it directly from your screen, without notifying the difference.

Tested and approved to rattach a 6-hour process launched outside a screen.

* [Reptyr](https://github.com/nelhage/reptyr): Tested and approved
* [Retty](http://pasky.or.cz//dev/retty/): Alternative, more limitations and only for x86
