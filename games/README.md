# Play a storage shift

A host reports “No space left on device,” but its disk still has room. Earn one point for each finding: the host, the mount point, and the device. Each prompt allows two tries. Open two terminals in the same Linux environment. The game uses Python 3 and creates small text reports in a temporary directory.

From the repository root in terminal one:

```bash
python3 games/storage-shift.py
```

If you haven't cloned the repo, open [the game file](storage-shift.py), use GitHub's download raw file button, and run `python3 storage-shift.py` from the download directory. In terminal two, run the two inspection commands printed by the game. Each file is a simulated host report. Compare the available inodes and block usage before answering.

To replay a fixed case, add `--seed 7` to the launch command. Leave it off for a fresh draw. The score appears after the third question. Quitting closes the temporary workspace. On a phone or with only one terminal, use the [paper version](../review/inode-ticket.md).

[What an inode measures](../labs/inode-budget.md) · [Table of contents](../README.md)

## Switch to the service desk

For a second game with no download, take the [three-ticket service shift](service-desk.md). Storage Shift tests whether you can identify a constrained resource. Service Desk Shift tests which observation can justify closing a ticket. For a mixed round, diagnose a storage shortage first, then decide how to verify that the reporting service has recovered.

## Play a container replacement shift

[Container Shift](container-shift.md) gives you two running replacement candidates and a missing report. Score yourself on the mount evidence and recovery check. Choose this round when you want to practice reading configuration captures in a browser without downloading an image.

## Take a DNS shift

[Play four resolver tickets](dns-shift.md) in one terminal with Python 3, or open each evidence file directly on GitHub. Each round asks you to classify a different outcome. Replay with a fixed seed if you want a classmate to see the same questions in the same order.

## Work the dispatch desk

[Play three scheduling tickets](dispatch.md). Earn points for predicting a run time, choosing a catch-up tool, and tracing a stale report back to its input.

## Which drive failed?

[Play Drive desk](drive-desk.md) when you want to decide whether a storage ticket can close. Three rounds cover a degraded mirror, two failures in a four-bay layout, and a report overwrite.
