# Round 2 · The failed collector

**Ticket.** On Maple, the collector is enabled but has failed. You receive this fictional timeline from the current boot:

| Time | Source | Event |
| --- | --- | --- |
| 09:10:00 | collector | Opening /srv/rack/ports.csv |
| 09:10:00 | collector | File not found: /srv/rack/ports.csv |
| 09:10:01 | systemd | Main process exited, status=1/FAILURE |
| 09:11:15 | unrelated timer | Completed successfully |

Which check comes first? A: inspect the configured input path and the mount serving its parent directory. B: enable the collector again. C: treat the timer's success as recovery.

<details><summary>Score the decision</summary>

A earns the first point. Earn the second by citing the missing path as the first specific failure. Status 1 reports an unsuccessful exit but gives less detail. Check the expected filename and whether /srv/rack is on the expected filesystem before creating or restoring anything. An empty replacement file could hide the original problem.

</details>

[Next ticket](service-output.md) · [Practice filtering the journal](../labs/unit-journal.md)
