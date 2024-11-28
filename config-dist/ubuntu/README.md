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

TBA

