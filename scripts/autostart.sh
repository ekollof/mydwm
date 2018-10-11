#!/bin/sh

(pasystray) &
(nm-applet) &
(pamac-tray) &
(kleopatra --daemon) &
(run_keybase) &
