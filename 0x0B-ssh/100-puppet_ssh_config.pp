# Manifest makes change to config file
include stdlib

file_line { 'ssh_config_line':
  line => 'BatchMode yes
IdentityFile ~/.ssh/school',
  path => '/etc/ssh/ssh_config',
}
