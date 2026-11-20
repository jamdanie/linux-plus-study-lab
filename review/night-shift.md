# Close a night-shift ticket

A simulated shift has three facts. Two servers share a 100 Mb/s uplink. Together they send 100 MB over ten seconds. The log tags, in order, are link, disk, link. A teammate wants the uplink replaced immediately.

1. Calculate the combined average and state the units.
2. Show a command that counts each tag, even when the same tag appears on nonconsecutive lines.
3. Write a handoff sentence naming one piece of evidence you still need before replacing the uplink.

<details><summary>Compare your findings</summary>

The average is 80 Mb/s. For the event counts, try `printf '%s\n' link disk link | sort | uniq -c`. Expect one disk tag and two link tags. A useful handoff would ask for timestamped interface error or drop counters during the affected interval. An average below capacity and two matching labels are insufficient to identify faulty hardware.

</details>

For a portfolio entry, attach your command output, label the dataset as simulated, and explain which measurement would change your recommendation.

[Table of contents](../README.md)
