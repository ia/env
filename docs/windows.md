# !!!RAW DRAFT!!!

## Windows 10 (Pro)

Dowload official ISO
Burn ISO on DL DVD-R(W) disc using compatible ROM
Connect DVD-ROM to PC
Insert Windows DVD
Turn on PC
Go to BIOS settings
Enable UEFI
Reboot
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

14.7 GiB

Reboot to GNULinux
if C:\ partition is misaligned, then:
boot to windows
shrink C:\ by 1MB
boot to GNULinux
extend C:\ with alignment by cylinder in gparted

sfc /scannow

install all updates
Windows 10 Update Error(0x80070643) is ok

right click on the Search Box. Under Search uncheck Show Search Highlights
right click on the taskbar. Under News and Interests, check Turn off

sudo strings /sys/firmware/acpi/tables/MSDM

wmic path SoftwareLicensingService get OA3xOriginalProductKey

