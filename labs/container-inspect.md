# Inspect a replacement before rerunning the job

The collector reads and writes a shift report under /reports. Both replacement candidates are running. Which one has the expected storage at the expected path? Work from the repository root. These small JSON captures are fictional training data in the shape of selected Docker inspect fields.

```bash
python3 labs/inspect-mounts.py fixtures/container-shift/before.json
python3 labs/inspect-mounts.py fixtures/container-shift/after.json
```

Read each mapping from left to right. Name identifies the volume. Destination is the directory visible to the process inside the container. RW means the mount permits writes; ordinary file permissions can still restrict the process. Both captures are also readable on GitHub: [before](../fixtures/container-shift/before.json) and [after](../fixtures/container-shift/after.json).

**Try it.** Cover the volume names and pick a replacement using the destination alone. Then uncover the names. Blue has the expected path but a different volume. Green has the expected volume at a different path. Neither matches the original configuration. A volume named “empty” still needs a content check before anyone claims it contains nothing.

[Play the scored ticket](../games/container-shift.md)
