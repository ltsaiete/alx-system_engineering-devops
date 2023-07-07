# kills a process named killmenow
exec { 'kill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin:/usr/bin:/bin',
}
