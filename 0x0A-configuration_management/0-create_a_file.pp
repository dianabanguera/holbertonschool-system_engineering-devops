# Creates a file in /tmp with specific requirements

file { '/tmp/school':
  ensure  => 'file',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
