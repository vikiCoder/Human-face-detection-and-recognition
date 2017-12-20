#!/bin/sh
echo $1
gsutil cp -r /home/pi/Desktop/Project/image.jpg  gs://el213-project.appspot.com/$1
