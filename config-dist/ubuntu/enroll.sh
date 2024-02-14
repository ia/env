#!/usr/bin/env bash
#set -x
set -e

echo "====>>>> Disabling recommends and suggests for apt..."
cp  etc_apt_apt.conf.d_00bloatware  /etc/apt/apt.conf.d/

echo "====>>>> Setting repos for apt..."
cp  etc_apt_sources.list  /etc/apt/sources.list
apt  update

echo "====>>>> Setting debug repos for apt..."
cp  etc_apt_sources.list.d.debug.list  /etc/apt/sources.list.d/debug.list
apt  update

echo "====>>>> Update grub config..."
cp  etc_default_grub  /etc/default/grub
update-grub

# TBA

echo "====>>>> Update packages..."
apt  -y  dist-upgrade
apt  -y  autoremove

