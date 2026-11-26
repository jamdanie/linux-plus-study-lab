# Hand off a rack check to the next technician

Use the [free rack ticket](rack-ticket.md) or open a cabling scenario in the paid Steam game [Data Center Simulator](https://store.steampowered.com/app/4535710/). Pick one server connection and trace it to the switch. Write down the two endpoint labels you can actually see. If one label is hidden, record that gap.

Then open a separate [free Ubuntu terminal](https://killercoda.com/playgrounds/scenario/ubuntu) and run:

```bash
ip -br link
ip route show default
```

Look for the interface name after `dev` on the default route. Find that same name in the link listing. If there is no default route, say so. The browser VM and the simulated rack are separate environments. Record the VM’s interface name under its own heading so the handoff never implies a physical connection between them.

For a recruiter-facing sample, pair an annotated rack screenshot or drawing with the two command outputs. Explain what you traced, which interface the VM would use for its default IPv4 route, and which physical switch port the Linux output leaves unidentified. If you also want to show a changing record, complete the [inventory report lab](../labs/report-run.md) and include the two observed line counts.
