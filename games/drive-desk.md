# Drive desk

Score one point for a decision and one for naming the clue you used. Open each answer after choosing. All three tickets can be played on GitHub.

**Ticket 1.** A user opens the report. The storage capture reads `raid1 [2/1] [U_]`. Close the alert, escalate a degraded mirror, or restore yesterday’s report?

<details><summary>Score ticket 1</summary>

Escalate the degraded mirror. Only one of two expected members is active. A successful file read answers the user’s availability question while the missing redundancy still needs attention.

</details>

**Ticket 2.** A four-drive RAID 10 uses pairs 1+2 and 3+4. Drive 1 is down. Which second failure would remove a whole pair: drive 2 or drive 3?

<details><summary>Score ticket 2</summary>

Drive 2. Drives 1 and 2 held the two copies in that pair. Confirm it by covering columns in the [four-bay layout](../visual/four-bays.md).

</details>

**Ticket 3.** Both members of a mirror are healthy. Yesterday’s correct inventory was overwritten this morning. Pick a source for recovery and a way to verify it.

<details><summary>Score ticket 3</summary>

Choose a retained version from before the overwrite. Restore it to a separate location and compare its contents with a known-good record. Reading the second mirror member gives the current mirrored data.

</details>

For a second round, swap tickets with a classmate. Ask them to explain which single observation would change their answer to ticket 1. [Try the terminal captures](../labs/mirror-status.md).
