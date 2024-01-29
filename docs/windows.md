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

`Press any key to boot from CD or DVD...`: <press>
Wait for booting
`Windows Setup window`: keep/set Language, Time & Keyboard as EN_US, `Next`
`Install now` button: click
`Activate Windows` window: type product key, `Next`
`License agreement` text: `I accept` checkbox, `Next`
`Custom` installation option
Partition disk: `New` button, type _megabytes_ (`1024`-based) using formula: N = xG * 1024 (GiB) + 100 (UEFI) + 16 (MSR) + 522 (MSRECOVERY) + 2 (align), where X is desired amount of C:\ drive in GiB, i.e. to make 64GiB: 64 * 1024 + 100 + 16 + 522 + 2(?) = 66176, `Apply`, `OK`
Select `Drive 0 Partition 3`, `Next`
`Installing Windows`: wait
Wait for reboot
Wait for reboot again
`Just a moment...` screen
`Let's start with region.`: US, `Yes`
`Keyboard layout`: US, `Yes`
`Second keyboard layout`: `Skip`
`I don't have internet`
`Continue with limited setup`
Type your new login, `Next`
Type your password, `Next`
Re-type your password to confirm, `Next`
Set 3 pairs of question/answer, `Next`
`Privacy settings`: all to `No`, `Accept`
`Cortana`: `Not now`
`Microsoft Edge`: `Maybe later`

after install: 14.7 GB
after updates: 24.9 GB


### Configuration

#### File system

Reboot to GNULinux
if C:\ partition is misaligned, then:
boot to windows
shrink C:\ by 1MB
boot to GNULinux
extend C:\ with alignment by cylinder in gparted

sfc /scannow

4K (for metablock?)

install all updates
Windows 10 Update Error(0x80070643) is ok

after updates: 24.9 GB

#### Disable online requests

right click on the Search Box. Under Search uncheck Show Search Highlights
right click on the taskbar. Under News and Interests, check Turn off

#### Activation

sudo strings /sys/firmware/acpi/tables/MSDM

wmic path SoftwareLicensingService get OA3xOriginalProductKey

if your legal work machine key doesn't work but your organization is a legal corporate client, run cmd.exe as admin:

get & set default windows 10 pro legal activation key:
C:\Windows\system32>slmgr /ipk AAAAA-BBBBB-CCCCC-DDDDD-EEEEE

get & set your organization legal activation key domain:
C:\Windows\system32>slmgr /skms  ----.--------.---

set activation process:
C:\Windows\system32>slmgr /ato

get activation status:
C:\Windows\system32>slmgr /xpr

