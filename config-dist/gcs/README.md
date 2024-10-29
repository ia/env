# Google Cloud Shell


## Instance information

### Basic environment

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

user@cloudshell:~$ tmux -V
tmux 2.1

user@cloudshell:~$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 79
model name      : Intel(R) Xeon(R) CPU @ 2.20GHz
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 2199.998
cache size      : 56320 KB
physical id     : 0
siblings        : 2
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt arat md_clear arch_capabilities
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs taa mmio_stale_data retbleed bhi
bogomips        : 4399.99
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:

processor       : 1
vendor_id       : GenuineIntel
cpu family      : 6
model           : 79
model name      : Intel(R) Xeon(R) CPU @ 2.20GHz
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 2199.998
cache size      : 56320 KB
physical id     : 0
siblings        : 2
core id         : 0
cpu cores       : 1
apicid          : 1
initial apicid  : 1
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt arat md_clear arch_capabilities
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs taa mmio_stale_data retbleed bhi
bogomips        : 4399.99
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:
```


### Additional details

 - to get external IP address: `$ curl  -s  ifconfig.me`
 - to connect using _ssh_ client: `$ ssh  -p 6000  USERNAME@IP`




## Limitations

 - 50hrs/week
 - unreliable access
 - after ~20 mins of inactivity after closing shell
 - reboot every 12hrs
 - modification of `rootfs`
 - modification of _some_ configs in `~`

Related links:
 - https://cloud.google.com/shell/docs/quotas-limits
 - &cloudshellsafemode=true
 - https://stackoverflow.com/questions/64231409/google-cloud-shell-appears-to-be-hanging-on-provisioning




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




## CLI setup


### Installation
This section based on [the official documentation with installation instructions](https://cloud.google.com/sdk/docs/install#deb).


- upgrade all available packages:
```
$ sudo  apt  update  &&  sudo  apt  dist-upgrade  -y  &&  sudo  apt  autoremove
```
- install required packages:
```
$ sudo  apt  install  apt-transport-https  ca-certificates  gnupg  curl
```
- download and import gpg key:
```
$ curl  https://packages.cloud.google.com/apt/doc/apt-key.gpg  |  sudo gpg  --dearmor  -o /usr/share/keyrings/cloud.google.gpg
```
- add repo:
```
$ echo  "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main"  |  sudo  tee  -a  /etc/apt/sources.list.d/google-cloud-sdk.list
```
- update packaging database:
```
$ sudo  apt  update
```
- install main cloud CLI tool:
```
$ sudo  apt  install  google-cloud-cli
```


### Configuration
This section based on the official documentation about:
- [initializing](https://cloud.google.com/sdk/docs/initializing);
- [authorizing](https://cloud.google.com/sdk/docs/authorizing);
- [managing configurations](https://cloud.google.com/sdk/docs/configurations).


- add login credentials for your account:
```
$ gcloud  auth  login
```
- make initial start of instance for your account to test the setup and to get the shell:
```
$ gcloud  --account=USERNAME@gmail.com  cloud-shell  ssh
```
- location of directory with related configuration files & credentials:
```
~/.config/gcloud
```

