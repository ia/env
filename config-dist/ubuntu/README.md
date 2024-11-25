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




TBA

