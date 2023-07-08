#  set up your client SSH configuration file so that you can
# connect to a server without typing a password.
file {  '~/.ssh/config':
  ensure  => 'present',
  path    => '~/.ssh/config',
  content => "Host 54.84.66.149\n
                \tIdentityFile ~/.ssh/school
                \tPasswordAuthentication no"
}
