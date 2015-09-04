Title: Sysdig
lang: en

[Sysdig](http://www.sysdig.org/) is an open-source app that "straces" all the system.



can be downloaded here http://pkgs.org/download/sysdig

does not need epel

usage:

listing helpers script

    :::text
    sysdig -cl


writing to a file

    :::text
    sysdig -w sysdig.tr # writing to a file


filtring by pid

    :::text
    sysdig -r sysdig.tr pid = 5000


filtering my filename

    :::text
    sysdig fd.dilename=puppet.conf


## Extra

Mattias has written a [blog post](http://mattiasgeniar.be/2014/10/03/sysdig-cli-examples/) with more examples (october 2014).
