#!/bin/bash
dnf -y install git python python-pip opencv* usbutils vim
pip install requests
dnf -y install mariadb mariadb-server
cd sqlScripts && ./initdb.sh && cd -
echo "Done"
