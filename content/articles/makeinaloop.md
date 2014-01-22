Title: Make stucked in a loop
Category: Linux
Tags: exherbo
Slug: make-in-a-loop

I got an unexpected result when I was trying to compile a small lib: it seems to never finished (I stopped it after 3 hours).

The problem was that I had in `/usr/lib64` files timestamped in the future.

The following command fixed it and I have eventually compiled my library in 30 seconds.

    :::bash
    touch now
    find /usr/lib64 -newer now -exec touch ´{}´ ´;´

