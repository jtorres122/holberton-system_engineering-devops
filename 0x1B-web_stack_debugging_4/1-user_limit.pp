# Manifest makes it possible to login with holberton user without error

exec { 'maxsoft' :
  command => 'sed -i s/4/50000/ /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
exec { 'maxhard' :
  command => 'sed -i s/5/50000/ /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
