#!/usr/bin/env python3.6

import os
import sys
import time
import datetime
import socket
import psutil
import ssl
import urllib.request

from Xlib.display import Display

def main():

    display = Display()
    root = display.screen().root

    # Static stuff
    hostname = socket.gethostname()
    localip = socket.gethostbyname(hostname)
    pubip = urllib.request.urlopen('https://enabledns.com/ip',context=ssl._create_unverified_context()).read().decode("utf-8")

    while(True):
        cpuload = psutil.cpu_percent()
        now = datetime.datetime.now()
        curtime = now.strftime("%d-%m-%Y %H:%M:%S")

        status = f"CPU: {cpuload: >5}% - {curtime};" + \
            f"Host: {hostname: <20} Local IP: {localip: <18} Public IP: {pubip: <18}"
        root.set_wm_name(status)
        display.sync()
        time.sleep(1)

if __name__ == "__main__":
    main()
