#!/usr/bin/pup
# Install a specific version off flask 2.1.0
package { 'flask':
	ensure    => '2.1.0',
	provider  => 'pip3',
}
