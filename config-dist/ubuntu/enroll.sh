#!/usr/bin/env bash
#set -x
set -e

echo "====>>>> Disabling recommends and suggests for apt..."
cp  etc_apt_apt.conf.d_00bloatware  /etc/apt/apt.conf.d/

echo "====>>>> Setting repos for apt..."
cp  etc_apt_sources.list  /etc/apt/sources.list

echo "====>>>> Update grub config..."
cp  etc_default_grub  /etc/default/grub

# TBA
