Title: Couldn't recognize the image file format for file 'foo.png'

Solution 1
----

    gdk-pixbuf-query-loaders > /usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders.cache

Solution 2
----

    update-mime-database /usr/share/mime
