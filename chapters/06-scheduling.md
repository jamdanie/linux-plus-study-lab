# Chapter 6. When should the rack report run?

It’s Monday at 09:20. You expected a new rack inventory at 09:15. Before changing the script, check two things. What time did the schedule call for? What did the job actually write?

| Term | When it fits | What to check |
| --- | --- | --- |
| cron | Run a command on a repeating clock schedule. | Check the five time fields in the user’s crontab and the scheduler’s time zone. |
| crontab | Store recurring jobs for one user. | Use `crontab -l` to list your own entries when cron is installed. A system crontab has an extra user field. |
| at | Queue a one-time job, such as a report after tonight’s maintenance. | Use `atq` to see pending jobs when the utility is installed. |
| anacron | Run periodic work on a machine that may be off when a daily job comes due. | Think in days and startup delays when planning the run. |
| systemd timer | Activate a unit on a calendar schedule or after an interval. | Read the timer’s trigger time, then check the service it activates. |

## Read one line

In a user crontab, `15 9 * * 1-5 /opt/lab/report` asks cron to run the command at 09:15 Monday through Friday. Read the fields from left to right as minute, hour, day of month, month, and day of week. The stars leave the day of month and month unrestricted. Swapping the first two fields gives 15:09 on those same days. Both expressions are valid, which makes this an easy error to miss.

## Try it

1. [Move the run time](../visual/cron-clock.md) and predict the next match.
2. [Run a report in a temporary directory](../labs/report-run.md) and see how a failed run can leave old output behind.
3. [Work the dispatch tickets](../games/dispatch.md) before opening the answers.

For XK0-006, connect scheduling tools with objective 2.3 and systemd timers with 2.5. [Objective tracker](../objectives.md) · [Chapter list](../README.md)
