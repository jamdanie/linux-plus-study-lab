# Round 1 · The reboot

**Ticket.** A technician manually started rack-report.service on Cedar. Its report is fresh. The runbook requires the service to start through multi-user.target at the next boot. This unit has an [Install] section with WantedBy=multi-user.target.

| Check | Simulated result |
| --- | --- |
| systemctl is-active rack-report.service | active |
| systemctl is-enabled rack-report.service | disabled |

Pick a response. A: restart the running service. B: check the boot enablement requirement and enable the unit. C: replace the server's Ethernet cable.

<details><summary>Score the decision</summary>

B earns the first point. The current run is healthy, but the expected boot link is missing. For the second point, explain why restarting only tests the present run. In this scenario the targeted change is `systemctl enable rack-report.service`, followed by `systemctl is-enabled rack-report.service`. Confirm actual startup after the next planned boot. Other dependencies or manual starts can still activate a disabled unit.

</details>

[Next ticket](service-failure.md) · [Shift menu](service-desk.md)
