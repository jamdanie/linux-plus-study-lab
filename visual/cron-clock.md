# Move the run time

Open [crontab guru](https://crontab.guru/). Paste the five schedule fields from each row. The editor explains the expression without installing a job. Imagine the scheduler’s local clock reads Monday 09:07. Cover the last column and predict its next match.

| Schedule | What changed? | Next matching local time |
| --- | --- | --- |
| `15 9 * * 1-5` | Weekday inventory | Monday 09:15 |
| `9 15 * * 1-5` | Minute and hour swapped | Monday 15:09 |
| `*/15 9 * * 1-5` | Every quarter hour during the 09 hour | Monday 09:15, then 09:30 |
| `0 */6 * * *` | Minute zero of every sixth clock hour | Monday 12:00 |

Change the imaginary time to Friday 09:46. When does the third row next match? The minute field matches 00, 15, 30 and 45. The hour field rules out Friday 10:00. The weekday field moves the next match to Monday 09:00.

Try writing a rule for 17:05 on weekdays. Check your answer in the editor and explain what the first field controls. [Back to Chapter 6](../chapters/06-scheduling.md)
