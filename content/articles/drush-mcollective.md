Title: Drush mcollective agent
Category: Linux
Tags: sysadmin, drupal
Slug: drush-mcollective

I have written a [mcollective](https://puppetlabs.com/mcollective/) agent to run [drush](http://drush.ws) commands. It will help you to automate the deployments of your drupal websites.

I have implemented two drush commands so far:
* `cache-clear`
* `updatedb`

The full configuration is available on the [github project](https://github.com/roidelapluie/mcollective-drush).

### Examples

    ::bash
    $ sudo mco rpc drush updatedb root=/var/vhost/frontend-demo yes=true -C /webfrontend/

    ::bash
    $ sudo mco rpc drush cache-clear root=/var/vhost/frontend-demo uri=http://demo.example.net type=all -C /webfrontend/

Please note: `-C /webfrontend/` is just a [mcollective filter](http://docs.puppetlabs.com/mcollective/reference/basic/basic_cli_usage.html).

### Links

* [mcollective](https://puppetlabs.com/mcollective/)
* [drush](http://drush.ws)
* [the agent on gihub](https://github.com/roidelapluie/mcollective-drush)

