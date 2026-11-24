# Replace a collector and read its handoff

Use a disposable Linux environment with a running Docker Engine and access to the alpine:3.22 image. Keep one Bash session open. If you only have GitHub or Python, the [capture lab](container-inspect.md) practices the same decision without an engine.

```bash
volume=$(docker volume create)
docker run --rm --mount "type=volume,src=$volume,dst=/reports" alpine:3.22 sh -ec 'echo rack-07 > /reports/handoff; echo scratch > /tmp/local-note'
docker run --rm --mount "type=volume,src=$volume,dst=/reports,readonly" alpine:3.22 sh -ec 'cat /reports/handoff; test ! -e /tmp/local-note && echo "Local note absent"'
```

Predict the second container's output before running it. Expect rack-07 and Local note absent. Each run creates a different container. The engine-generated volume name is held in the shell variable and explicitly reattached at the same path. The second mount is read-only because verification only needs a read.

**Change the destination.** Reuse the volume and read the report at its new path.

```bash
docker run --rm --mount "type=volume,src=$volume,dst=/archive,readonly" alpine:3.22 cat /archive/handoff
```

After confirming the report, remove only the disposable volume created above with `docker volume rm "$volume"`. The lab containers were removed at exit. This final step discards the practice report.

[Visual explanation](../visual/container-layers.md)
