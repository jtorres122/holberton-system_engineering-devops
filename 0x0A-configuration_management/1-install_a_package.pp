# Manifest installs puppet-lint using puppet

package { 'puppet-lint':
  ensure   => 'latest',
  provider => 'gem',
}

