# Find the device behind a directory

In a [free Ubuntu practice terminal](https://killercoda.com/playgrounds/scenario/ubuntu), run these display commands. Leave all devices attached.

```bash
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
findmnt -T / -o TARGET,SOURCE,FSTYPE
df -h /
```

Read TYPE before SIZE. A row marked disk is a whole block device. A row marked part is a partition. Look for the mount point `/`, then compare its source with the second command. The third command reports filesystem capacity. A disk and its partitions overlap, so adding every SIZE in the tree would double-count storage.

**If your sandbox shows overlay:** Record the source and filesystem type exactly as displayed. A container can show a mounted root filesystem without exposing a matching physical device. Use this illustrative VM capture for the device-matching exercise:

| Name | Type | Size | Filesystem | Mount point |
| --- | --- | --- | --- | --- |
| vda | disk | 32G | | |
| vda1 | part | 1G | vfat | /boot/efi |
| vda2 | part | 31G | ext4 | / |

Which device would you investigate for a full root filesystem? The capture points to vda2. Use `df -h /` for used and available space. The 31G in the tree describes partition size. It cannot tell you how many files are stored there.

[lsblk manual](https://man7.org/linux/man-pages/man8/lsblk.8.html) · [Read a mirror status](mirror-status.md)
