# Google Cloud Shell


## Basic info

 - [direct link to the service](https://shell.cloud.google.com/?show=terminal)
 - VM specifications:
   - GNU/Linux Debian 11 bullseye
   - 8GB RAM
   - x86_64 vCPU
 - full list of installed packages
 - shell output:
```
user@cloudshell:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 11 (bullseye)
Release:        11
Codename:       bullseye

user@cloudshell:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       986Mi       5.2Gi       0.0Ki       1.6Gi       6.5Gi
Swap:             0B          0B          0B

user@cloudshell:~$ uname -a
Linux cs-default 6.1.58+ #1 SMP PREEMPT_DYNAMIC Mon Jan 29 15:19:25 UTC 2024 x86_64 GNU/Linux

user@cloudshell:~$ gcc --version
gcc (Debian 10.2.1-6) 10.2.1 20210110
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

user@cloudshell:~$ bash --version
GNU bash, version 5.1.4(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

user@cloudshell:~$ tmux version

user@cloudshell:~$ cat /proc/cpuinfo
```


## Deploying

DRAFT
 - VM
test -f /READY
upload ssh keys & set permissions
restart ssh
setup ssh tunnel
setup ssh socks
get ip
show banner
touch /READY
tmux  set  -g  status  on
tmux  split-window  -h
keep awake
 - server
the most minimal SSH jail-like chroot
setup ssh keys
 - client
config


