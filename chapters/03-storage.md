# 3. Investigate a storage ticket

**Practice ticket:** A teammate found a large file in the backups folder and thinks the filesystem is full. Check both parts of that report. How much space is available on the filesystem, and which practice directory accounts for most of the data?

A **filesystem** organizes files and tracks space. Its **mount point** is the directory where you can enter it. Several directories can share the same filesystem. Giving a directory to `df` selects the filesystem containing it. Giving that directory to `du` selects the files underneath it to measure.

## Lab: follow the numbers

```bash
lab=$(mktemp -d)
cd "$lab"
mkdir backups reports
dd if=/dev/zero of=backups/sample.bin bs=1M count=4 status=none
printf '%s\n' 'Daily totals' > reports/today.txt
df -h .
du -h --max-depth=1 .
```

The `dd` command writes four 1 MiB blocks to a new practice file. In `df`, read **Avail**, **Use%**, and **Mounted on**. These describe the filesystem shared by the practice directories. In `du`, look for the lines ending in `./backups` and `./reports`. The line ending in a single dot is their parent total. Exact sizes depend on the filesystem, but on a typical Ubuntu filesystem the backups directory uses roughly 4 MiB and the text report uses much less. Transparent compression can change the allocated size.

**Check the scope of your evidence.** Run the following before deciding what to tell your teammate.

```bash
df -h backups reports
du -sh backups reports
```

The two paths refer to the same filesystem and have the same filesystem-wide availability here. Their directory totals can differ. A large file in one directory is evidence about that directory. To decide whether space is running low, use the actual available space and the workload's needs.

**Try it without the steps.** Which command would you use to answer “How much space does the backups directory use?” Which output would you attach if someone asked whether there was space for another 100 MiB backup?

<details><summary>Check your answer</summary>

Use `du -sh backups` for the directory. Use `df -h backups` and compare **Avail** with the requested space for the capacity question. The large practice file stays in place, so you can repeat both checks.

</details>

**For your portfolio:** Capture your two command outputs in one screenshot or text block. Under it, name the filesystem, report its available space, identify the larger practice directory, and explain whether the evidence supports the ticket. Label it a simulated ticket and use the numbers from your own run.

[Previous: search a log](02-logs.md) · [Review cards](../review/README.md) · [Next: watch a process](04-processes.md)
