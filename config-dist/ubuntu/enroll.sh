#!/usr/bin/env bash
#set -x
set -e

echo "====>>>> Disabling recommends and suggests for apt..."
cp  etc_apt_apt.conf.d_00bloatware  /etc/apt/apt.conf.d/

# TBA
