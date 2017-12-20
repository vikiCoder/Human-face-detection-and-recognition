#!/bin/bash

killall python

time=$(date)
cd /home/pi/Desktop/Project

python /home/pi/Desktop/Project/photoCapture.py 1>"$time"