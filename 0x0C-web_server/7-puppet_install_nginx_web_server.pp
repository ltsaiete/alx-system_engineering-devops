# configure an Nginx server using Puppet

class { 'nginx':
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => '<html>\
<head>\
  <title>Document</title>\
</head>\
<body>Hello World!</body>
</html>',
}

nginx::resource { 'redirection':
  location => '/redirect_me',
  www_root => '/var/www/html/',
  index    => 'index.html',
  rewrite  => '^/redirect_me https://youtu.be/F1RrJ7DfDMg permanent',
}


