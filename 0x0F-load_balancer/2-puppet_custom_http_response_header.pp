# Like The file 0-custom_http_response_header
# Automate the task of creating a custom HTTP header response, but with Puppet

# Update ubuntu server
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->

# Install nginx web server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->

# Set The name of custom HTTP header ( X-Served-By)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->

# Start services
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
