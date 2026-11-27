# Compare two mirror status captures

These are simplified training captures for a two-member Linux software mirror. Run the block in Bash. It creates two text files in a fresh temporary directory. No disk configuration or administrator access is needed.

```bash
work=$(mktemp -d)
cd "$work" || exit
printf '%s\n' 'md0 : active raid1 vdb1[0] vdc1[1]' '      1048576 blocks [2/2] [UU]' > healthy.txt
printf '%s\n' 'md0 : active raid1 vdb1[0]' '      1048576 blocks [2/1] [U_]' > degraded.txt
diff -u healthy.txt degraded.txt
echo "$?"
```

Expect exit status 1 from diff. It means the two files differ. Read the minus and plus lines. The second member name disappears and the active count drops from two to one. In this example each U represents a working slot and the underscore marks a missing one. The word active can appear in both captures.

Try `grep -F '[U_]' degraded.txt` to select the status line literally. Square brackets have special meaning in regular expressions, so the fixed-string option matters here.

On a Linux host that exposes software arrays, `cat /proc/mdstat` displays the kernel’s current summary. A playground without a configured software mirror may have no array rows. For the ticket, cite the training capture and explain which evidence would justify calling the mirror healthy again: two active members, both slots up, and any recovery operation complete.

[Play the ticket game](../games/drive-desk.md) · [Kernel documentation](https://docs.kernel.org/admin-guide/md.html)
