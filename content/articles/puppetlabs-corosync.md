Title: Puppet-corosync and pcs provider
Category: Linux, Puppet
Tags: high availability
Slug: puppet-corosync-pcs

Since the release 6.4, el-based distributions are not shipped with the `crm` command
by default. [`pcs`](http://github.com/feist/pcs) is the new [recommended way](http://blog.clusterlabs.org/blog/2013/pacemaker-on-rhel6-dot-4/) to [setup the clusters](http://blog.clusterlabs.org/blog/2012/pacemaker-and-cluster-filesystems/) on CentOS/RHEL >= 6.4.

A lot of the people using the [puppetlabs-corosync](http://github.com/puppetlabs/puppetlabs-corosync) module
have been surprised and they just installed a RPM found somewhere accross the web.

I adapted the puppetlabs-corosync to end that dependency. My puppetlabs-corosync
module is [available here](http://github.com/roidelapluie/puppetlabs-corosync).

It is not perfect, but I still plan on working on it in the following months (and
I accept pull requests of course). Any feedback is welcome.

