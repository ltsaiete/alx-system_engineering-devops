# install flask from pip3

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  refreshonly => true,
}
