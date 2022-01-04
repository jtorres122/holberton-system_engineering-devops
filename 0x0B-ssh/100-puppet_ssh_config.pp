# Manifest makes change to config file
include stdlib

file_line { 'BatchMode':
  line => 'BatchMode yes',
  path => '/etc/ssh/ssh_config',
}

file_line { 'IdentifyFile':
  line => 'IdentityFile ~/.ssh/school',
  path => '/etc/ssh/ssh_config',
}
