# !!!RAW DRAFT!!!




## Windows 11 (Pro)


### Basic info

- [Official download link](https://www.microsoft.com/software-download/windows11)
  - Go to _Download Windows 11 Disk Image (ISO) for x64 devices_ section for _iso_ file
  - _Select edition: Windows 11 (multi-edition ISO for x64 devices)_
  - _Select the product language: English (United States)_
- Metadata:
```
   iso: Win11_23H2_English_x64v2.iso
 label: CCCOMA_X64FRE_EN-US_DV9
  size: 6812706816 (6.34 GB)
   md5: b036c5867361d3ca52db74b16bacd586
  sha1: cd5e995387669b2ff2c58c23894900f1d238a103
sha256: 36de5ecb7a0daa58dce68c03b9465a543ed0f5498aa8ae60ab45fb7c8c4ae402
```


### HOWTOs

TBA




## Windows 10 (Pro)


**Basic info**

- [Official download link](https://www.microsoft.com/en-us/software-download/windows10ISO)
  - _Select edition: Windows 10 (multi-edition ISO)_
  - _Select the product language: English (United States)_
- Metadata:
```
   iso: Win10_22H2_English_x64v1.iso
 label: CCCOMA_X64FRE_EN-US_DV9
  size: 6140975104 (5.71 GB)
   md5: c2b19762870226ca467d6cbd87cd8fab
  sha1: bbb1b234ea7f5397a1906ee59187087c78374f35
sha256: a6f470ca6d331eb353b815c043e327a347f594f37ff525f17764738fe812852e
```


### Preparations

- dowload official ISO
- burn ISO on DL DVD-R(W) disc using compatible ROM drive
- connect DVD-ROM to PC
- insert Windows DVD into DVD-ROM
- turn on PC
- go to BIOS settings
- enable UEFI/SB/TPM
- reboot


### Installation

- wait for `Press any key to boot from CD or DVD...` and press any key
- wait for booting
- `Windows Setup` window: keep/set Language, Time & Keyboard as EN_US, `Next`
- `Install now` button: _click_
- `Activate Windows` window: type product key, `Next`
- `License agreement` text: `I accept` checkbox, `Next`
- `Custom` installation option
- partition disk: `New` button, type _megabytes_ (`1024`-based) using formula:  
`N = xG * 1024 (GiB) + 100 (UEFI) + 16 (MSR) + 522 (MSRECOVERY) + 2 (align)`  
where X is desired amount of `C:\` drive in _GiB_, i.e. to make _64 GiB_:  
`64 * 1024 + 100 + 16 + 522 + 2(?) = 66176`, `Apply`, `OK`
- select `Drive 0 Partition 3`, `Next`
- `Installing Windows` window: _wait_
- wait for reboot
- wait for reboot again
- `Just a moment...` screen: _wait_
- `Let's start with region` window: `US`, `Yes`
- `Keyboard layout` window: `US`, `Yes`
- `Second keyboard layout` window: `Skip`
- `I don't have internet` button: _click_
- `Continue with limited setup` button: _click_
- type your new login, `Next`
- type your password, `Next`
- re-type your password to confirm, `Next`
- set 3 pairs of question/answer, `Next`
- `Privacy settings` window: all to `No`, `Accept`
- `Cortana` window: `Not now`
- on desktop `Microsoft Edge` request: `Maybe later`


### Configuration

#### Filesystem

- reboot to _GNULinux_
- check partitions' alignment by running `$ sudo gdisk -l /dev/sdXN`
- if C:\ partition is misaligned, then:
  - boot to _Windows_
  - shrink `C:\` by _1MB_ using `disk manager`
  - boot to _GNULinux_
  - extend `C:\` with _alignment by cylinder_ in `gparted`
  - boot to _Windows_
  - check `C:\` through reboot
  - run in _Windows_ `cmd.exe` with _administrative rights_: `sfc  /scannow`
  - reboot
- install all updates usinng `Settings`
- side notes:
  - `capacity - size = _4K_` (for metablock?)
  - _Windows 10_ **Update Error(0x80070643)** is fully **OK**
- size notes:
  - _after install_: `~14.7 GB`
  - _after updates_: `~24.9 GB`


#### Disable online requests

- right click on the _Search Box_ and under _Search_ uncheck _Show Search Highlights_
- right click on the taskbar and under _News and Interests_ check _Turn off_


#### Activation

- get a legal licence key from a machine:
  - in GNULinux: `$ sudo  strings  /sys/firmware/acpi/tables/MSDM`
  - in Windows: `> wmic  path  SoftwareLicensingService  get  OA3xOriginalProductKey`


If your legal work machine key doesn't work but your organization is a legal corporate client, run `cmd.exe` as _admin_ and then:

get & set default windows 10 pro legal activation key:
C:\Windows\system32>slmgr /ipk AAAAA-BBBBB-CCCCC-DDDDD-EEEEE

get & set your organization legal activation key domain:
C:\Windows\system32>slmgr /skms  ----.--------.---

set activation process:
C:\Windows\system32>slmgr /ato

get activation status:
C:\Windows\system32>slmgr /xpr


