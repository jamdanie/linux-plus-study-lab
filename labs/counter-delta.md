# Measure traffic between two readings

Linux interface byte counters accumulate over time. A total such as 9,000,000 bytes tells you little about the current rate until you compare it with an earlier reading of the same counter.

Use this fictional capture of transmitted bytes from one interface. The first column is elapsed seconds. The second is the cumulative byte count.

```bash
printf '%s\n' '0 1000000' '4 9000000' |
awk 'NR == 1 { start = $1; bytes = $2; next }
     { printf "%.1f Mb/s\n", ($2 - bytes) * 8 / (($1 - start) * 1000000) }'
```

Expect 16.0 Mb/s. Dividing the second reading alone by four would count bytes sent before the observation began. For a live comparison, use `ip -s link show dev lo` twice on Ubuntu and read the TX bytes field each time. An idle loopback device can give you a zero difference. Use a fresh baseline if the counter resets between samples.

[Table of contents](../README.md)
