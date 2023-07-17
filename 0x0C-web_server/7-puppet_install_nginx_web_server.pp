# configure an Nginx server using Puppet

exec { 'install_puppet_nginx_module':
  command     => 'puppet module install puppet-nginx',
  path        => '/usr/local/bin:/usr/bin:/bin',
  unless      => 'puppet module list --modulepath /etc/puppetlabs/code/modules\
   | grep puppet-nginx',
  require     => Class['puppet_agent'],
  refreshonly => true,
}

class { 'nginx':
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => '<html>
<head>
  <title>Document</title>
</head>
<body>Hello World!</body>
</html>',
}

nginx::resource { 'default':
  port => 80
}

nginx::resource { 'redirection':
  location => '/redirect_me',
  www_root => '/var/www/html/',
  index    => 'index.html',
  rewrite  => '^/redirect_me https://youtu.be/F1RrJ7DfDMg permanent',
}
