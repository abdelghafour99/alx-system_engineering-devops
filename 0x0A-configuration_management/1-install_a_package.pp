#!/usr/bin/pup
# Install a specific version of flask 2.1.0

exec { 'flask':
  command => '/usr/bin/apt-get pip install flask',
}
