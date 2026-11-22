# Play a storage shift

A host reports “No space left on device,” but its disk still has room. Earn one point for each finding: the host, the mount point, and the device. Each prompt allows two tries. Open two terminals in the same Linux environment. The game uses Python 3 and creates small text reports in a temporary directory.

From the repository root in terminal one:

```bash
python3 games/storage-shift.py
```

If you haven't cloned the repo, open [the game file](storage-shift.py), use GitHub's download raw file button, and run `python3 storage-shift.py` from the download directory. In terminal two, run the two inspection commands printed by the game. Each file is a simulated host report. Compare the available inodes and block usage before answering.

To replay a fixed case, add `--seed 7` to the launch command. Leave it off for a fresh draw. The score appears after the third question. Quitting closes the temporary workspace. On a phone or with only one terminal, use the [paper version](../review/inode-ticket.md).

[What an inode measures](../labs/inode-budget.md) · [Table of contents](../README.md)
