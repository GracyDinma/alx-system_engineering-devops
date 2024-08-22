# Increase the amount of service an nginx can handle

# Increase the ULIMIT of the default file
exec { 'fix--for nginx':
  # modify the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # specify the path for the sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  # specify the path for the limit script
  path    => '/etc/init.d/',
} 
