# Take the dispatch desk

Give yourself one point for each decision and one for the clue that supports it. Six points closes the shift.

**1. Wrong hour.** Inventory should run at 09:15 on weekdays. The user’s schedule reads `9 15 * * 1-5`. At 09:20 the file is still old. What time does the rule actually select, and what change fits the ticket?

<details><summary>Check ticket 1</summary>

15:09. The first field is the minute. Change the rule to `15 9 * * 1-5` in the exercise.

</details>

**2. Missed maintenance.** A laptop is often powered off overnight. A daily housekeeping job should catch up after startup. Which tool fits, and which part of the requirement matters?

<details><summary>Check ticket 2</summary>

Anacron fits periodic work that comes due while a machine is off. The requirement is completing an overdue daily job. A fixed wall-clock minute is unnecessary.

</details>

**3. Green timer, stale report.** At 09:16 the timer lists LAST 09:15. The service journal at 09:15 reports a missing input. The inventory file contains yesterday’s date. What do you check before rescheduling?

<details><summary>Check ticket 3</summary>

Check the input path used by the service. The journal puts the failure after activation. Restore the input in the practice lab, run the command, and verify a fresh output record.

</details>

[Try ticket 3 in a terminal](../labs/report-run.md) · [All games](README.md)
