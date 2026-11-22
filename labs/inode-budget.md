# Why can an empty file use an inode?

An inode records a file's metadata. A filesystem can run out of available inodes while it still has data blocks available. Predict which count will change when you create four empty files in a new directory.

```bash
cd "$(mktemp -d)"
touch a b c d
wc -c a b c d
ls -i a b c d
df -i .
df -h .
```

Each file has zero bytes of content, but the four names have four distinct inode numbers. Compare IFree in the inode report with Avail in the block report. On a shared filesystem, other tasks can change the filesystem totals while you work. Use the four file records as your direct evidence. Some filesystems report no fixed inode limit.

**Second round.** Run `ln a a-second-name` followed by `ls -li a a-second-name`. Both names point to the same inode. Explain why counting directory entries alone would overstate the number of distinct files in this example.

[Play the storage shift](../games/README.md)
