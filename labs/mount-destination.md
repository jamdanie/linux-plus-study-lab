# Which filesystem receives this file?

A backup runbook says to write under /srv. Before writing, check which filesystem actually serves the path. In an Ubuntu terminal, use the path of a directory that already exists.

```bash
dir=$(mktemp -d)
findmnt --target "$dir" --output TARGET,SOURCE,FSTYPE
df -h "$dir"
```

TARGET is the mount point covering the directory. SOURCE identifies the backing source as Linux sees it. A container may show overlay, and /tmp can have its own tmpfs. Compare TARGET with the Mounted on column from df. The name of a directory by itself gives you no guarantee that a separate disk is mounted there.

**Try another path.** Run `findmnt --target / --output TARGET,SOURCE,FSTYPE`. Do the two paths resolve to the same mount on your system? Record the output either way. For a job that requires a specific volume, compare the observed result with the expected mount before writing.

[Read the example storage map](../visual/storage-map.md)

## Compare the host path with the container path

A host can see a volume in the engine's storage area while the application sees /reports. Inspect the mount from the perspective named in the ticket. In the [two replacement captures](container-inspect.md), write the volume identity and the application-visible destination on separate lines. Which line changes for the green candidate?
