Title: GlusterFS quorums
lang: en
Category: Linux
Tags: GlusterFS, planet-inuits
Slug: glusterfs-quorum

[GlusterFS](http://gluster.org) quorums should prevent brain-split by deactivating the nodes when less that 50% of the servers are connected (you can change that number).

To enable the feature, it is simple:

    :::bash
    srv01$ sudo gluster volume set gv0 cluster.server-quorum-type server
    volume set: success

Then I isolated one VM on the network. I could not access the files on that node:

    :::bash
    srv03$ ls /mnt
    ls: cannot access /mnt: No such file or directory

But it worked on the other nodes:

    :::bash
    srv02$ ls /mnt|wc -l
    41

    srv01$ ls /mnt|wc -l
    41

So I got the expected results.

Then I created a file on one of the connected servers.

    :::bash
    srv02$ echo test > /mnt/test2

I re-enabled the network on the third server and the node went back online and the replica was done.

    :::bash
    srv03$ ls /mnt/|wc -l
    42
    srv03$ ls /export/brick1/sdb1/|wc -l
    42

### Links

* [GlusterFS](http://gluster.org)
* [GlusterFS quorums](http://www.gluster.org/community/documentation/index.php/Features/Server-quorum) documentation
