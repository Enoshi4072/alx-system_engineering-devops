#using Puppet to make changes to our configuration file
#!/usr/bin/env bash
file_line { 'Turn off passwd auth':
ensure  => present,
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?IdentityFile',
  require => File['/etc/ssh/sshd_config'],
}
