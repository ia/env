# OpenVPN server / Ubuntu 18.04


## CA host

mkdir  -p  tools
cd  tools

easyrsa="EasyRSA-3.1.7"
wget  https://github.com/OpenVPN/easy-rsa/releases/download/v3.1.7/${easyrsa}.tgz
tar  -xvf  ${easyrsa}.tgz

cp  -afr  ${easyrsa}  ${easyrsa}-ca
cp  -afr  ${easyrsa}  ${easyrsa}-ov

# set CA config
cd  ${easyrsa}-ca
cp  vars.example  vars

echo "
set_var EASYRSA_REQ_COUNTRY   \"US\"
set_var EASYRSA_REQ_PROVINCE  \"California\"
set_var EASYRSA_REQ_CITY      \"San Francisco\"
set_var EASYRSA_REQ_ORG       \"HomeLab\"
set_var EASYRSA_REQ_EMAIL     \"root@example.com\"
set_var EASYRSA_REQ_OU        \"RND dept\"
" >> vars

# generate PKI
./easyrsa  init-pki
./easyrsa  build-ca

# type password, type CN,
ckfdfjvybccbbQQ!123

tpx

ca.crt - public cert
ca.key - private key


#### OV host

cd ..
cd ${easyrsa}-ov

./easyrsa  init-pki
./easyrsa  gen-req  server  nopass
sudo  cp  pki/private/server.key  /etc/openvpn/

(s)cp  pki/private/server.req  /tmp/ @ CA


# switch to CA

./easyrsa  import-req  /tmp/server.req  server
./easyrsa  sign-req  server  server

(s)cp  pki/issued/server.crt  /tmp/ @ OV
(s)cp  pki/ca.crt  /tmp/ @ OV


# switch to OV

mkdir  -p  client-configs/keys
chmod  -R  700  client-configs

sudo  cp  /tmp/{server.crt,ca.crt}  /etc/openvpn/
./easyrsa  gen-dh

openvpn  --genkey  --secret  ta.key
sudo  cp  {ta.key,pki/dh.pem}  /etc/openvpn/

- per client configuration:

./easyrsa  gen-req  client1  nopass
cp  pki/private/client1.key  client-configs/keys/
(s)cp  pki/reqs/client1.req  /tmp/ @ CA


# switch to CA

./easyrsa  import-req  /tmp/client1.req  client1
./easyrsa  sign-req  client  client1

(s)cp  pki/issued/client1.crt  /tmp/ @ OV


# switch to OV

cp  /tmp/client1.crt  client-configs/keys/

cp  easyrsa-ov/ta.key  client-configs/keys/
sudo  cp  /etc/openvpn/ca.crt  client-configs/keys/


# TODO: TBA: rearrange




### openvpn server config

sudo  cp  /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz  /etc/openvpn/
sudo  gzip  -d  /etc/openvpn/server.conf.gz

/etc/openvpn/server.conf
firewall
sudo systemctl start openvpn@server

tun 10.8.0.1


# client config files

mkdir  -p  client-configs/files

cp  /usr/share/doc/openvpn/examples/sample-config-files/client.conf  client-configs/base.conf

make mkovpn script

client:
sudo apt install openvpn-systemd-resolved


# Server configuration

## Packet forwarding for IPv4

- temporally (until next boot):
```
$ echo  1  |  sudo  tee  /proc/sys/net/ipv4/ip_forward
```
- permanently:
  - manually:
    - edit and add/uncomment line `net.ipv4.ip_forward=1` in file `/etc/sysctl.conf`
    - apply new setting: `sudo  sysctl  -p`
  - automatically with one-liner:
```
$ echo  "net.ipv4.ip_forward=1"  |  sudo  tee  -a  /etc/sysctl.conf  &&  sudo  sysctl  -p
```


### 
TBA:
ufw/iptables
sysctl/ipv4
sudo service openvpn@server restart
revoke
revoke one sample @ creation to move db


# Client configuration

TBA:
ovpn file


# Gateway configuration

TBA:
ufw/iptables
sysctl/ipv4
routes/route.sh


# LINKS

## main
https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-18-04

## gw
https://forums.openvpn.net/viewtopic.php?t=27421
https://astojanov.github.io/blog/2013/03/31/openvpn-routes.html

