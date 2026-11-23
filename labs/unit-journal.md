# Narrow the journal to the failed run

On a disposable systemd VM, run `systemctl list-units --type=service --all` and choose a service visible on that machine. Read its exact unit name into a variable with `read -r unit` and type the name at the prompt. Then run:

```bash
systemctl status "$unit" --no-pager
journalctl -u "$unit" -b -n 20 --no-pager
```

The first command gives a state snapshot. The second limits journal entries to that unit and the current boot, and prints up to 20 recent entries. A failed or inactive status can produce a nonzero exit code. An empty journal view can mean no matching entries or limited access. Record those limitations before deciding that nothing happened.

**No live journal?** Read the four supplied events in [the failed collector](../games/service-failure.md). Separate the application's specific diagnostic from systemd's summary of its exit. Put the event times beside each other before choosing a fix.

[journalctl manual](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
