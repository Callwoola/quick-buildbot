#!/usr/bin/env bash


if ! type apache2 > /dev/null; then
  # install foobar here
  sudo apt-get install -y apache2
fi

sudo apt-get install -y php5
sudo apt-get install -y mysql-server
sudo apt-get install -y php5-mysql
sudo apt-get install -y unzip
sudo apt-get install -y curl
sudo apt-get install -y openssl
sudo apt-get install -y php5-mcrypt
sudo a2enmod rewrite
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
