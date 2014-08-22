Title: Mcollective agent to use drush
Category: Linux
Tags: sysadmin, drupal, planet-inuits
Slug: drush-mcollective

I have written a [mcollective](https://puppetlabs.com/mcollective/) agent to run [drush](http://drush.ws) commands. It will help you to automate the deployments of your drupal websites.

I have implemented two drush commands so far:

* `cache-clear`
* `updatedb`

The full configuration is available on the [github project](https://github.com/roidelapluie/mcollective-drush).

### Examples

#### Updatedb

    ::text
    mco rpc drush updatedb root=/var/vhost/frontend-demo yes=true

#### Cache-clear

    ::text
    mco rpc drush cache-clear root=/var/vhost/frontend-demo uri=http://demo.example.net type=all

### Links

* [mcollective](https://puppetlabs.com/mcollective/)
* [drush](http://drush.ws)
* [the agent on github](https://github.com/roidelapluie/mcollective-drush)

