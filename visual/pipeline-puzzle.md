# Follow a ticket through a pipeline

Three alerts arrived in order: disk, link, disk. Which alert repeats? Try each line separately. Before pressing Enter, predict how many output rows you will get.

```bash
cd "$(mktemp -d)"
printf '%s\n' disk link disk > alerts
uniq -c alerts
sort alerts
sort alerts | uniq -c
```

| Stage | What you should see |
| --- | --- |
| Count in arrival order | Three rows, each with count 1 |
| Sort labels | disk, disk, link on separate lines |
| Count adjacent labels after sorting | Two rows: 2 disk and 1 link |

Change the input to disk, link, disk, link. Predict the two counts and rerun. For another round, try a browser shell puzzle on [CMD Challenge](https://cmdchallenge.com/). To inspect a command before running it, paste `sort alerts | uniq -c` into [explainshell](https://explainshell.com/). The diagram explains arguments. Use your terminal to see what your actual data produces.

[Table of contents](../README.md)
