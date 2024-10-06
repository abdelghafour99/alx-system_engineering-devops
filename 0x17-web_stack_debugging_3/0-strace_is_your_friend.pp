#Fixes bad 'phpp' Extensions to 'php' in the WordPress File 'wp-settings.php'

exec { 'fix-wordpress':
 i command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
