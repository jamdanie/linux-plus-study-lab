# Round 3 · The quiet monitor

**Ticket.** Alder's long-running rack monitor restarted at 11:05. At 11:12 its unit is active. Its output file still has a modification time of 10:58. The runbook expects a new sample every minute.

A: close the ticket based on active. B: check the configured output destination, logs since restart, and whether a new valid sample arrives. C: enable the unit and wait for a reboot.

<details><summary>Score the decision</summary>

B earns the first point. The existing file predates the restart. For the second point, say how you would verify recovery: observe a new, correctly formatted sample at the intended destination during the next reporting interval. A running process can keep running while writing to the wrong location. Preserve the old report until you understand the gap.

</details>

**Write your handoff.** Include the last known good sample time and the first verified new sample. If you haven't observed a new sample, say which check remains open.

[Return to the shift menu](service-desk.md) · [Read a service state diagram](../visual/service-state.md)

## Trace stale output after container replacement

Suppose the reporter's PID changed during a container replacement. Before testing another restart, check whether its configured report path is backed by the intended volume. Compare the old and new mappings, then verify a fresh sample. [Use the two capture files](../labs/container-inspect.md).

## Check the reporter's destination name

The service now produces a local sample, but sending it to the collector fails during name lookup. Capture the full hostname and the resolver outcome at the time of failure. A fresh local file verifies production; a successful delivery requires separate evidence. [Practice choosing the next name-service check](dns-shift.md).
