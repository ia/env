#!/usr/bin/env bash
#set -x
set -e

tmux  set-option  status  on
tmux  split-window  -h

mkdir       ~/.ssh
chmod  0700 ~/.ssh

cd  ~/.ssh
touch        known_hosts  authorized_keys  id_ed25519  id_ed25519.pub
chmod  0600  known_hosts  authorized_keys  id_ed25519  id_ed25519.pub

echo  "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEjZTxFq0g56ltExFgEGpc6vBvzVibAwA4T5pIu7CcTx cloudshell"  >>  authorized_keys
cat  authorized_keys  >>  id_ed25519.pub

echo "|1|16jSnNgPkHhqC49iRpRS21Z2alI=|AesgdhBe4jQTjwugUOKOVxvSTpY= ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIiyFQuTwegicQ+8w7dLA7A+4JMZkCk8TLWrKPklWcRt
|1|gfYq8go/NdexMO1CWBJUjGCSPb8=|bz9O0y2lyCOtgTcIqQsR+rrBQb4= ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCf7bgcKf2oDCpMdHjIqUkMihxpiVZ3j0zrRUeKhgn4FXx1FXerCe7cojAVuGcFsTH4JzIiK6SInKMRt8UANUBggae2llCHFsjV7L6NcLPgaByhWi4gOZba+FT1A0PSX7T8BFNPOmcu696PNILFru98BRf2Vd43E9mBAintLH5Ya6XnOQf9D44XNWToebokcEv48ju0dWDiRwt5IhQPj+cVZstWWJaqGueoR9GWcgSiPT6bISp0lSJfSq/ird7EEKJrU3f2g7Zi20DiDNJS7lfuWDKZeAphoZTXhciIlVRDWQHR8ssgiWVkcjWWi0LgDZ7hhhh+pcfvf71qpnOR0m2b
|1|gXM3qKw6WQO+7tppU7z8pCDKa6A=|IaTxD91MQhH7Glq9iuELVltcd/o= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPXSkWZ8MqLVM68cMjm+YR4geDGfqKPEcIeC9aKVyUW32brmgUrFX2b0I+z4g6rHYRwGeqrnAqLmJ6JJY0Ufm80=
|1|4g/IsNi0wTaVr2MeDpmb6ED33BA=|j7J8pg3PNSY25tpNC1vFhNk31Nw= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPXSkWZ8MqLVM68cMjm+YR4geDGfqKPEcIeC9aKVyUW32brmgUrFX2b0I+z4g6rHYRwGeqrnAqLmJ6JJY0Ufm80=
|1|wpZhVMBSd7F/o8DLfQEC9naYrmY=|/D1s49q6CghLMhPbNjMCF4rbOmk= ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCf7bgcKf2oDCpMdHjIqUkMihxpiVZ3j0zrRUeKhgn4FXx1FXerCe7cojAVuGcFsTH4JzIiK6SInKMRt8UANUBggae2llCHFsjV7L6NcLPgaByhWi4gOZba+FT1A0PSX7T8BFNPOmcu696PNILFru98BRf2Vd43E9mBAintLH5Ya6XnOQf9D44XNWToebokcEv48ju0dWDiRwt5IhQPj+cVZstWWJaqGueoR9GWcgSiPT6bISp0lSJfSq/ird7EEKJrU3f2g7Zi20DiDNJS7lfuWDKZeAphoZTXhciIlVRDWQHR8ssgiWVkcjWWi0LgDZ7hhhh+pcfvf71qpnOR0m2b
|1|kWs1Eh8PrTcOg0SgLdlJQxpjK+E=|jtBjaq85eTjPpRMTfh3TFNxcc6w= ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIiyFQuTwegicQ+8w7dLA7A+4JMZkCk8TLWrKPklWcRt
|1|bpKIuKCo00V7RyAb3cnke6IP6Xo=|uotPZxm4vrIxVtn3SsNprmpiCGA= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDnTZ9abAoQ9FkJAF6RAfvSwjfYvLkqYy/ggjIqolfwX3e5pYFUhuiyWMX0PnCLS8gWZRqIWwgkD0gDBLMo7EqE=
|1|Oz1xKGgzOYd6OCtMHlWNkVS/WiQ=|iw8tuWWW6nNx/hHDCe5odENdpSQ= ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9UYySvgzB6/psZ8J3K8V7cEZ8S8XeAaOx0E1OaDO4mJWv+PfnzLB24RvJOSqBNNpAo7LN1g7aULTms0M2u2qe634+RJMi9hgZwXSdkIC51nXiwBRQe69pg19WUG/rS4FJDaZS75XbRAhHIawmajlzg+cCPfoTXI/0yZKCz9VjtVUhtsm4h8M02u4X8v7BtBst+rDlTH6pqDh9YV/DsBMxyH6vPJbQsLoFF/FxRChCZgEI6DPtYs3U1sQNov24nnokqwmfAEOCkt6YTRtMbjNmRe5UOh58fqNiiIacbXlk1Zaz1Cd/ZSjCMmkMggaUk08wZEOaKS7S/E5vKK0/udIh
|1|Ziq1wgOMT3X14NMJuw5EhdKlHaw=|22d3VS2NzEndNsUDASZalB2RJlI= ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINQjNrMZYuXlqucuv/39JnrUuza7VingFzMy6NtFjb6+
|1|sLWFx/xPVnLMN2wCXvRphEvUSm8=|+6iJyhKFoU7pjH14rpRgv5Ey0Xs= ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9UYySvgzB6/psZ8J3K8V7cEZ8S8XeAaOx0E1OaDO4mJWv+PfnzLB24RvJOSqBNNpAo7LN1g7aULTms0M2u2qe634+RJMi9hgZwXSdkIC51nXiwBRQe69pg19WUG/rS4FJDaZS75XbRAhHIawmajlzg+cCPfoTXI/0yZKCz9VjtVUhtsm4h8M02u4X8v7BtBst+rDlTH6pqDh9YV/DsBMxyH6vPJbQsLoFF/FxRChCZgEI6DPtYs3U1sQNov24nnokqwmfAEOCkt6YTRtMbjNmRe5UOh58fqNiiIacbXlk1Zaz1Cd/ZSjCMmkMggaUk08wZEOaKS7S/E5vKK0/udIh
|1|V4urZv8I9CemusqtjkU0LgnOjRo=|AVsPZg+bKXSS71eOYUpFT4GQEfs= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDnTZ9abAoQ9FkJAF6RAfvSwjfYvLkqYy/ggjIqolfwX3e5pYFUhuiyWMX0PnCLS8gWZRqIWwgkD0gDBLMo7EqE=
|1|JY7qzYQ7bEOIoju0YPyUzGLvKwQ=|cO4EDH1tYK66gsJChh4YH0C0S4Q= ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINQjNrMZYuXlqucuv/39JnrUuza7VingFzMy6NtFjb6+" >> known_hosts

sudo  service  ssh  restart

echo "

- reverse ssh tunnel directly:

HOST: $ ssh  -o ServerAliveInterval=20  -R  8080:localhost:22  USER@HOST
RMTE: $ ssh  -o ServerAliveInterval=20  CLOUD_USERNAME@localhost  -p  8080


"

exit 0
