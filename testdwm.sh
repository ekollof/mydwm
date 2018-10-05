#!/bin/sh

Xephyr :1 -ac -screen 1280x1024 -br -reset -terminate&
DISPLAY=:1 ~/bin/startdwm
