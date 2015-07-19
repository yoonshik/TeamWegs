#!/bin/bash
dnf -y install git python python-pip opencv* usbutils vim python-pyramid npm
pip install requests pymysql
npm install -g bower
dnf -y install mariadb mariadb-server
echo "About to run the SQL secure installer. Please do not set a password for root. Accept all other defaults"
mysql_secure_installation
cd sqlScripts && ./initdb.sh && cd -
cd webDisplay && python setup.py develop && cd -
echo "Done"
