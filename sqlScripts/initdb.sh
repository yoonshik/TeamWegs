#!/bin/bash
echo "Logging into local MySQL/MariaDB root account. For hackathon we assume no password."
mysql -u root < ./makeDB.sql
echo "Database created"
mysql -u root < ./makeUsers.sql
echo "User table created"
