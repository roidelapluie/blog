Title: pcsd limitations in EL7
lang: en
Category: Linux
Tags: centos,automation,HA, planet-inuits
Slug: pcs-resource-debug

The High Availability stack shipped with CentOS/RHEL 7.1 comes with a daemon
called `pcsd` that provides a web UI to manage a clusters. You can reach
it at `https://hostname:2224/`.

I gave it a try and here is the lis of limitations I have found so far:

* It does not show colocation sets at all.
* It does not show the "kind" of resource ordering preferences (optional, mandatory, serialize).
* It does not show failcounts.
* It refreshes every 20 seconds but you do not see the timestamp of the last refresh. It would be great to have a refresh button as well.
* It does not support pending operations (starting is displayed as started).
* In the resource list, failed, inactive and disabled are displayed in red (I would prefer to see red, orange and grey).
* You can not manage/unmanage resources easily (you can do it by adding a meta attribute).

For now I will stick with the `pcs` command and `crm_*` commands that work very well.

That said, the pacemaker stack got a lot of love in EL7 (thanks OpenStack I guess), and remains a key tool to
provide High Availability in Linux.
