Title: Pcs support merged into puppetlabs-corosync
Category: Puppet
Tags: centos,automation,ha
Slug: puppetlabs-corosync-pcs

This is a good news from people using an el-based distribution and the [puppetlabs-corosync](https://github.com/puppetlabs/puppetlabs-corosync)
puppet module: [pcs support has been merged yesterday](https://github.com/puppetlabs/puppetlabs-corosync/pull/64).

This change is important because it means that no additional rpm is required to use that puppet module.

Starting from CentOS 6.4, the `crm` shell was not provided by Red Hat anymore, but the puppet module was using that package in its only provider for custom types.

My work is based on previous work done by [Joshua Hoblitt](https://github.com/jhoblitt). It keeps `crmsh` compatibility, useful for CentOS < 6.4 users, which means there is now two providers in the module.

Please test & feedback that merge.
