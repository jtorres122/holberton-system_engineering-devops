# Manifest installs puppet-lint using puppet

package { 'puppet-lint':
  ensure          => '2.5.0',
  provider        => 'gem',
  source          => 'https://rubygems.org/',
}

