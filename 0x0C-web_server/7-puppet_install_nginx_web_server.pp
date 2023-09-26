# Installs a Nginx server
# Puppet manifest to install and configure Nginx

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
      try_files \$uri \$uri/ =404;
      add_header X-Hello-World 'Hello World!';
    }

    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;

    location = /404.html {
      internal;
    }
  }",
}

# Create "Hello World!" HTML file
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Create custom 404 page
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
}
