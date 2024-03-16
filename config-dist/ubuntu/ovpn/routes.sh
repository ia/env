#!/usr/bin/env bash
set -x
set -e

CLIENT="10.8.0.11"
IFACE="tun0"
TABLE=vpnclient

# one time command:
# $ echo  "200 vpnclient"  |  sudo  tee  -a  /etc/iproute2/rt_tables

ip  route  add  10.8.0.0/24               dev  ${IFACE}  src  10.8.0.1  table  vpnclient
ip  route  add  default  via  10.8.0.254  dev  ${IFACE}                 table  vpnclient
ip  rule   add  from  ${CLIENT}/32                                      table  vpnclient
ip  rule   add  to    ${CLIENT}/32                                      table  vpnclient

ip  route  flush  cache

