#  set up your client SSH configuration file so that you can
# connect to a server without typing a password.

file {  '/etc/ssh/ssh_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => "Host 54.84.66.149\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no"
}
