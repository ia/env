# GNU/Linux Ubuntu post-installation todo

# UNDER DEVELOPMENT

**Unless specified otherwise, originally these files have been configured for Ubuntu 24.04**
**They may or may not work in other environments/distros**


## Package management

### apt

#### configuration

- disable suggested and recommended packages to reduce download/storage size on installation:
```
$ sudo  vim  /etc/apt/apt.conf.d/00bloatware
$ cat /etc/apt/apt.conf.d/00bloatware
APT::Install-Recommends "0";
APT::Install-Suggests "0";
```

#### sources.list

- get codename for the distro: `$ lsb_release  -c`
- get hostname with _https_ support [here](https://launchpad.net/ubuntu/+archivemirrors)
- edit and put this file instead of original `/etc/apt/sources.list` accordingly:
```
deb     HOSTNAME/  CODENAME            main restricted universe multiverse
deb-src HOSTNAME/  CODENAME            main restricted universe multiverse

deb     HOSTNAME/  CODENAME-updates    main restricted universe multiverse
deb-src HOSTNAME/  CODENAME-updates    main restricted universe multiverse

deb     HOSTNAME/  CODENAME-backports  main restricted universe multiverse
deb-src HOSTNAME/  CODENAME-backports  main restricted universe multiverse

deb     HOSTNAME/  CODENAME-security   main restricted universe multiverse
deb-src HOSTNAME/  CODENAME-security   main restricted universe multiverse

deb     HOSTNAME/  CODENAME-proposed   main restricted universe multiverse
deb-src HOSTNAME/  CODENAME-proposed   main restricted universe multiverse

deb     http://archive.canonical.com/ubuntu CODENAME partner
deb-src http://archive.canonical.com/ubuntu CODENAME partner
```


#### debug symbols

- edit and put this file as `/etc/apt/sources.list.d/dbgsyms.list`:
```
deb     http://ddebs.ubuntu.com  CODENAME           main restricted universe multiverse
deb-src http://ddebs.ubuntu.com  CODENAME           main restricted universe multiverse

deb     http://ddebs.ubuntu.com  CODENAME-updates   main restricted universe multiverse
deb-src http://ddebs.ubuntu.com  CODENAME-updates   main restricted universe multiverse

deb     http://ddebs.ubuntu.com  CODENAME-proposed  main restricted universe multiverse
deb-src http://ddebs.ubuntu.com  CODENAME-proposed  main restricted universe multiverse
```


#### packages

TBA




## System configuration

### grub

- edit and put this content as `/etc/default/grub`:
```
# default entry
GRUB_DEFAULT=0

# autoboot timeout
GRUB_TIMEOUT=4

# distro name generator
GRUB_DISTRIBUTOR=`echo GNU/Linux Ubuntu`

# default cmd line
GRUB_CMDLINE_LINUX=""

# no quite autoboot timeout
GRUB_HIDDEN_TIMEOUT_QUIET=false

# verbose boot
# based on https://wiki.archlinux.org/index.php/Boot_debugging#Insane_Debug
GRUB_CMDLINE_LINUX_DEFAULT="ignore_loglevel no_console_suspend verbose=1 udev.log_priority=8 loglevel=9 earlyprintk=vga,keep log_buf_len=10M print_fatal_signals=1 pause_on_oops=2 panic=5 sysrq_always_enabled"

# disable submenus
GRUB_DISABLE_SUBMENU="y"

# enable luks support for rootfs partition
GRUB_ENABLE_CRYPTODISK="y"
GRUB_CRYPTODISK_ENABLE="y"

# boot the previous boot item
GRUB_DEFAULT=saved
GRUB_SAVEDEFAULT=true
```


TBA

