Title: Puppet 3.6.1 depreciation warning
Category: Puppet
Tags: centos,automation
Slug: puppet-361-depreciation

Dear puppet users using a yum-based distribution, once you will upgrade to [puppet 3.6.1](http://docs.puppetlabs.com/puppet/3.6/reference/release_notes.html),
you will notice the following warning message each time you use a package type:

    :::text
    Warning: The package type's allow_virtual parameter will be changing its
    default value from false to true in a future release. If you do not want to
    allow virtual packages, please explicitly set allow_virtual to false.
    (at /usr/lib/ruby/site_ruby/1.8/puppet/type.rb:816:in `set_default')

There is nothing you can do with that except setting a global parameter in your puppet tree:

    :::puppet
    Package {
      allow_virtual => true,
    }

This disturbing behaviour is discussed in [issue PUP-2650](https://tickets.puppetlabs.com/browse/PUP-2650) and in the [mailing list](https://groups.google.com/d/msg/puppet-users/QadW3Px9GEU/tmNNgBG1uPQJ).
