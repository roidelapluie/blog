Title: Puppet 4 create_resource killer
lang: en
Category: Automation
Tags: automation, planet-inuits, puppet
Slug: puppet-4-create-resources

Puppet 4 brings very nice features that will definitely kill the `create_resources`
function.

### Parameters as a hash

```Puppet
$parameters = {
  mode    => '0755',
  content => 'foo',
}

file {
  '/tmp/test_base':
    * => $parameters
}
```

It is the same as:

```Puppet
file {
  '/tmp/test_base':
    mode    => '0755',
    content => 'foo',
}
```

### Resource defaults

```Puppet
file {
  default:
    mode    => '0755',
    content => 'foo';
  '/tmp/test_base':;
  '/tmp/test_base':
    mode => '0644',
}
```

Is the same as:


```Puppet
file {
  '/tmp/test_base':
    mode    => '0755',
    content => 'foo';
  '/tmp/test_base':
    mode    => '0644',
    content => 'foo';
}
```

Or (but the scope is different):

```Puppet
File {
  mode    => '0755',
  content => 'foo';
}
file {
  '/tmp/test_base':;
  '/tmp/test_base':
    mode => '0644',
}
```


### Combining both of them

```Puppet
$parameters = {
  content => 'foo',
  ensure  => present,
}

$default = {
  noop => true,
  mode => '0644',
}

file {
  default:
    * => $default;
  '/tmp/test':
    * => $parameters
}
```

In a loop:

```Puppet
$parameters = {
  content => 'foo',
  ensure => present,
}

$default = {
  noop   => true,
  mode   => '0644',
}

$files = ['/tmp/foo', '/tmp/bar']

$files.each | String $file_path | {
  file {
    default:
      * => $default;
    $file_path:
      * => $parameters
  }
}
```
