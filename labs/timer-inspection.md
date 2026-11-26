# Follow a timer to its service

On a Linux VM running systemd, run `systemctl list-timers --all --no-pager`. Pick a row with a previous trigger. Read LAST, UNIT and ACTIVATES across that row. LAST records the timer trigger. ACTIVATES names the unit to inspect for execution details.

```bash
read -r -p "Service name from ACTIVATES: " unit
systemctl show "$unit" -p Result -p ExecMainStatus -p ActiveState
journalctl -u "$unit" -b -n 15 --no-pager
```

Compare the journal time with LAST. A one-shot service can finish successfully and return to inactive. If journal access is limited or the last run was before this boot, the current-boot view may have no matching entry.

**Browser fallback.** Practice with this illustrative capture. LAST is 09:15, UNIT is rack.timer, and ACTIVATES is rack.service. The service journal reports “missing input/rack” at 09:15 and an exit status of 1. Which piece establishes launch? Which explains the failed report? The timer timestamp and matching service entry show activation. The application's missing-input message explains where to look next.

[systemd timer manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html) · [Reproduce the missing input](report-run.md)
