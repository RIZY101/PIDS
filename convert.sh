#!/bin/bash
sudo ffmpeg -framerate 30 -i /var/www/html/video.h264 /var/www/html/video.mp4 -y -loglevel quiet
