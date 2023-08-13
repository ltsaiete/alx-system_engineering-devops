# configure an Nginx server using Puppet
# Configure your Nginx server to have a custom response header

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

exec {'redirect_me':
  command  => 'sed  "/listen [::]:80 default_server;/    add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
