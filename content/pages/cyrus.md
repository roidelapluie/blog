Title: Playing with cyrus-imapd replication
lang: en

* Run everything as the Cyrus user
* sync_client must run on the master
* sync_server must run on the slave

Synchronize a user (mail + metadata)
----

    /usr/lib/cyrus-imapd/sync_client -u username
