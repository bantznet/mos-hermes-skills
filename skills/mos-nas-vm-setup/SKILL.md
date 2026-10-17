---
name: mos-nas-vm-setup
description: Use when running MOS NAS OS in a VM or building its images.
---

# MOS (mos-nas) in a VM

MOS = Devuan-based NAS OS. Boots UEFI from a FAT32 volume labeled `MOS` with the release ZIP extracted at its root (no ISO; an ISO is read-only and MOS stores config/updates on the boot device). Releases: github.com/mos-nas/mos-releases (assets `mos_<tag>_amd64.zip`, `.md5`, `mos_amd64.img.xz`; API gives sha256 `digest`). Docs: docs.mos-official.net.

## Always-on rules
- Images/VMs built for this are for trying MOS only. Anything user-facing (README, release notes) must say they are unofficial and that long-term use follows MOS's official install docs.
- Mark any hypervisor/platform or import path not actually booted as UNTESTED in docs, and never flip a recommendation toward an untested path: write docs only from what was seen to boot.
- Validate settings by hand before automating: don't build helper scripts for a platform until the manual steps are confirmed.

## Proxmox recipe (worked)
- Build the boot image as a plain 16 GiB image file (never a real disk): one bootable MBR partition formatted FAT32 with label `MOS`, with the release ZIP extracted flat at its root (EFI, grub, rootfs, image, drivers...). Work through a loop device on the file and unmount it afterwards.
- VM: q35, `--bios ovmf`, efidisk `pre-enrolled-keys=0` (Secure Boot off), cpu host, 4c/8G, virtio net, scsi0=imported img (boot), scsi1=blank disk for "Install to Disk"/pools.
- Glob pitfall: ZIP name uses underscores (`mos_*_amd64.zip`), not hyphens.
- Non-LVM storage (e.g. Ceph RBD): a raw-device USB-passthrough fallback using /dev/pve paths does not apply.

## Pitfalls
- Proxmox noVNC console shows a garbled framebuffer early in boot; boot is fine (the login banner with the IPv4 appears once boot completes). If the console stays unusable, find the IP via MAC: ping-sweep the /24 then `ip neigh | grep <mac>`, open http://<ip>/.
- IP can change after restart/install-to-disk (new DHCP lease; old IP dead). Reserve a lease on your DHCP server or set a static IP in MOS.
- Two IPs may show the same MAC in the neighbor table (stale + new); curl each.
- Pool types: single, multi (btrfs raid0/raid1), mergerfs (+optional SnapRAID parity disk, XFS data disks), nonraid (unRAID-style; install the "NonRAID Driver" plugin in MOS Hub and restart; one nonraid pool max). ZFS = plugin, no UI.
- SnapRAID is not a separate install: it is the optional parity disk on a `mergerfs` pool (see the mos-nas-api skill for the API calls).
- Mirror choice: btrfs raid1 (only mirror with UI) over ZFS (plugin, CLI only, kernel-coupled); bcachefs is new/experimental. On virtual disks backed by shared storage, parity/mirrors only exercise the MOS workflow, not real redundancy.
- QEMU smoke test on a no-KVM host works but is slow (~130-180s to WebUI over TCG); needs `qemu-system-x86` + `ovmf` (firmware in /usr/share/OVMF/OVMF_CODE_4M.fd). Attach the image with `snapshot=on` so the test doesn't modify it.
- In shell scripts under `set -o pipefail`, never `ls a b 2>/dev/null | head -1` to pick the first existing file: a missing path makes ls fail and aborts the script silently; loop with `[ -f ]` instead.

## Portable images (ESXi/Hyper-V/KVM/desktop)
`qemu-img convert -f raw -O vmdk -o subformat=streamOptimized` (+ OVF wrapper -> OVA), `qcow2`. VM needs UEFI, Secure Boot off, SATA/NVMe disk, e1000e NIC. TESTED: Proxmox, VirtualBox (OVA), VMware Workstation (OVA). UNTESTED: Fusion, ESXi. NOT SUPPORTED: Hyper-V (below).
- ESXi: upload streamOptimized VMDK then `vmkfstools -i in.vmdk -d thin out.vmdk` (ESXi won't attach a sparse VMDK directly), or import the OVA. Guest OS "Other Linux 64", UEFI, Secure Boot off, SATA/NVMe, e1000e first (VMware paravirtual drivers in the MOS kernel unverified).
- VirtualBox (TESTED with the OVA): File > Import Appliance, then BEFORE first boot tick Settings > System > Motherboard > Enable EFI: the OVA's UEFI flag is a `vmw:` tag VirtualBox ignores, so it imports as legacy BIOS and won't boot. Import Appliance accepts only OVA/OVF; a bare VMDK must be attached to a Machine > New VM (SATA, EFI on) and that path is UNTESTED. Bridged adapter on wired NIC (Wi-Fi bridging often gets no lease; NAT needs a port-forward host 8080 -> guest :80, also untested), Intel PRO/1000. Cannot run x86 guests on Apple Silicon (suggest UTM).
- VMware Workstation (TESTED): open/import the OVA, no setting changes needed (UEFI, SATA, e1000e come from the OVF); bridged adapter; IP appears on the console banner.
- Hyper-V is NOT supported by the MOS kernel as shipped (cause inferred from `# CONFIG_HYPERV is not set` in mos-kernel kernel-config/config; upstream unconfirmed): a Gen 2 guest reaches the initramfs and stops with `ERROR: MOS boot device with label: MOS not found` because VMBus/storvsc is absent (Gen 1 is BIOS-only; MOS needs UEFI). The boot-label scan runs before the `drivers` modules can load, so a fix needs `CONFIG_HYPERV=y` + `CONFIG_HYPERV_STORAGE=y` built in (netvsc/utils/keyboard can be modules). The `PCI: Fatal: No config space access function found` line on Gen 2 is harmless. Don't publish VHDX or write Hyper-V steps until upstream ships support; point Windows users to VirtualBox/Workstation.
- First boot shows a blank/frozen/garbled console for 1-3 min: wait. When boot finishes the console login banner prints `IPv4: <addr>`, so no DHCP lookup is needed; `smartd failed` in the log is normal in a VM.

## MOS REST API
Swagger UI at `http://<mos-ip>/api-docs/`; endpoint reference and verified calls are in the `mos-nas-api` skill in this repo.
