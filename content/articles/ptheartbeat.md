Title: Pt-heartbeat can't use an undefined value as an ARRAY reference
lang: en
Category: Linux
Tags: mysql,HA, planet-inuits
Slug: pt-heartbeat-array-error

Today I got a strange issue with [`pt-heartbeat`](http://www.percona.com/doc/percona-toolkit/2.2/pt-heartbeat.html).

When I launched `pt-heartbeat`:

    :::bash
    pt-heartbeat --pid /var/opt/inu/pt-heartbeat.pid --update --database \
      pth --create-table --socket /var/opt/inu/mysql/mysql.sock --user=pth \
      --password=str0ng

I got the following error message:

    :::text
    Can't use an undefined value as an ARRAY reference at
      /usr/bin/pt-heartbeat line 4297.



It was because I did not have access to the `/tmp/percona-version-check` file.
The file was created under an other user and the current user could not access
it. I have found it out by using `strace -e trace=file`.

Just removing the file solved the problem (of course the first `pt-heartbeat`
daemon was not running anymore).

    :::bash
    rm /tmp/percona-version-check
