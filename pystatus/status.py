#!/usr/bin/env python3

import os
import os.path
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

        if os.path.isfile('/tmp/statquit'):
            sys.exit()

        cpuload = psutil.cpu_percent()
        memused = int(dict(psutil.virtual_memory()._asdict())['used'] / 1024 / 1024)
        memtotal = int(dict(psutil.virtual_memory()._asdict())['total'] / 1024 / 1024)
        swapused =  int(dict(psutil.swap_memory()._asdict())['used'] / 1024 / 1024)
        swaptotal =  int(dict(psutil.swap_memory()._asdict())['total'] / 1024 / 1024)
        now = datetime.datetime.now()
        curtime = now.strftime("%d-%m-%Y %H:%M:%S")

        status = f"MEM: {memused: >6}/{memtotal: >6} MB : SWAP {swapused: >6}/{swaptotal: >6} : CPU: \x03{cpuload: >5}%\x01 - {curtime};" + \
            f"Host: {hostname: <20} Local IP: {localip: <18} Public IP: {pubip: <18}"
        root.set_wm_name(status)
        display.sync()
        time.sleep(1)

if __name__ == "__main__":
    main()
