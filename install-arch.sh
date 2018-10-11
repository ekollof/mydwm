#!/bin/sh

echo "Installing dependancies..."
sudo pacman -S --noconfirm gcc pacaur light network-manager-applet pasystray pulseaudio alsa-oss alsa-plugins alsa-utils pamac dmenu feh gajim slock touchpad-toggle wmname spectacle compton
pacaur -S --noconfirm keybase-bin passdmenu xinit-xsession ttf-twemoji-color ttf-fira-code
TOP=`pwd`
echo "Building window manager and utilities"
make  
sudo make install
cd console
make -s
sudo make install
cd ../slstatus
make -s
sudo make install
cd $TOP

echo "Installing startup scripts"
cp scripts/xinitrc ~/.xinitrc
chmod 755 ~/.xinitrc

mkdir -p ~/.dwm
cp scripts/autostart.sh ~/.dwm
chmod 755 ~/.dwm/autostart.sh

mkdir -p ~/bin
cp scripts/startdwm ~/bin
chmod 755 ~/bin/startdwm

