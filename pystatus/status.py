#!/usr/bin/env python3.6

import os
import sys
import time
import datetime

from Xlib.display import Display

def main():

    display = Display()
    root = display.screen().root

    while(True):

        now = datetime.datetime.now()
        curtime = now.strftime("%d-%m-%Y %H:%M:%S")

        status = f"{curtime}"
        root.set_wm_name(status)
        display.sync()
        time.sleep(1)

if __name__ == "__main__":
    main()
