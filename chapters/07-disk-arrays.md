# Chapter 7. The report opens, but one drive is missing

A practice ticket says a two-drive mirror lost a member. The inventory report still opens. Can you close the ticket? You have evidence that a read worked. To find out how many working copies remain, you need the array status.

RAID stands for *redundant array of independent disks*. A member is one device participating in the array. Linux software RAID can combine those devices into a logical block device such as `/dev/md0`. A filesystem can live on that device. The mount point is the directory where you access its files.

| Layout | Where the data goes | If a drive fails |
| --- | --- | --- |
| RAID 0, striping | Pieces of the data go to different drives. | A single lost member breaks the array. |
| RAID 1, mirroring | In a two-drive mirror each member holds a copy. | One healthy member can continue serving reads. |
| RAID 5 | Data and one drive’s worth of parity are spread across at least three drives. Parity lets the array reconstruct missing data. | Tolerates one failed drive. |
| RAID 6 | Two independent sets of parity are spread across at least four drives. | Tolerates two failed drives. |
| RAID 10 | In a conventional four-drive layout, two mirrored pairs are striped together. | One failure is tolerated. A second failure depends on which pair loses a member. |

A mirror also mirrors changes. If someone overwrites the report, both working members can contain the same wrong version. To recover yesterday’s contents, look for a retained backup or snapshot from before the change.

Start with the [four-bay exercise](../visual/four-bays.md). Then [inspect the Linux device tree](../labs/disk-tree.md) and [read a mirror status capture](../labs/mirror-status.md). Finish with the [drive desk game](../games/drive-desk.md).

[Linux kernel software RAID documentation](https://docs.kernel.org/admin-guide/md.html) · [Table of contents](../README.md)
