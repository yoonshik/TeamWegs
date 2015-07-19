#!/bin/bash
echo "Starting the food tracker of doom!"
#Launch motion tracker
screen -SL MotionTracker -d -m ./MotionTracker/motion_tracker.py
echo "Motion tracker started"
systemctl start mariadb.service
systemctl status mariadb.service
echo "SQL Server activated"
cd webDisplay
screen -SL pyramidWebDisplay -d -m pserve development.ini
cd -
echo "Wegs is love, Wegs is life."
