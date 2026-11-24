# Play Container Shift

A replacement collector starts successfully, but yesterday's rack handoff has disappeared from its expected path. Take one point for each correct prediction and one for each piece of evidence you can name. Play entirely on GitHub or use the [offline Python reader](../labs/container-inspect.md).

| Round | Evidence | Your decision |
| --- | --- | --- |
| 1. Establish the baseline | [Original host capture](../fixtures/container-shift/before.json) | Which volume and destination must you preserve? |
| 2. Choose the repair | [Replacement captures](../fixtures/container-shift/after.json) | For each candidate, identify the one mapping field that must change. |
| 3. Close the ticket | The repaired service is running and yesterday's handoff is readable. The job promises a fresh sample every minute. | What would you verify before closing the ticket? |

<details><summary>Score your shift out of six</summary>

1. One point for rack-history, one for /reports. Keep the volume identity and its destination together in the handoff.
2. One point for each correction. Blue needs rack-history in place of rack-history-empty. Green needs /reports in place of /archive. The captures show both mounts permit writes.
3. One point for observing a fresh valid sample at the intended path during the next interval. One for recording its timestamp or contents alongside the verified volume mapping. A running process and an old readable file establish only part of recovery.

</details>

**Portfolio challenge.** Save the two mappings and write a three-sentence ticket closure. If you only inspected the captures, state which live verification remains open.

[See how an image, layer, and volume fit together](../visual/container-layers.md)
