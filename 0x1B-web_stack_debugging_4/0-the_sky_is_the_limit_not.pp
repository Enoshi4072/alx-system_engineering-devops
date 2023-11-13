# Address high request volume issue

exec {'adjust_ulimit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart_nginx'],
}

exec {'restart_nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
