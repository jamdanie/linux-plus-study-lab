# 2. Find the error inside a log

A teammate asks for the errors from a backup run. You remember the files end in `.log`, but a filename alone won't tell you what failed. Use `find` to identify files by properties such as their names. Use `grep` to select lines by their contents. Both commands can print filenames, which is one reason they're easy to mix up.

## Lab: build a two-line incident report

Create a small set of sample logs. Each quoted argument to `printf` becomes one line because the format ends in `\n`.

```bash
lab=$(mktemp -d)
cd "$lab"
mkdir logs
printf '%s\n' 'INFO started' 'ERROR destination missing' 'ERROR copy skipped' > logs/backup.log
printf '%s\n' 'INFO connected' > logs/network.log
find logs -type f -name '*.log'
```

Expect two paths, in either order. `-type f` selects regular files. Quoting `'*.log'` passes the pattern to `find` so the shell doesn't expand it first.

```bash
grep -n '^ERROR ' logs/backup.log
grep '^ERROR ' logs/backup.log > incident.txt
cat incident.txt
wc -l < incident.txt
```

The first command should show matches on lines 2 and 3. The caret anchors the match to the start of the line. The second command leaves line numbers out of the report so the reader gets the original messages. The last command reads the file through standard input and prints the number of lines: 2.

**What if you only need a count?** A pipe (`|`) sends the output of one command to the next command. Try `grep '^ERROR ' logs/backup.log | wc -l`. A redirect (`>`) sends output to a file. Choose the pipe for a quick count and the redirect when a teammate needs a report to read later.

**Try it without the steps.** Append a success message to the backup log. Verify that the file grew to four lines while the error count stayed at two.

<details><summary>Check your answer</summary>

```bash
printf '%s\n' 'INFO retry complete' >> logs/backup.log
wc -l < logs/backup.log
grep -c '^ERROR ' logs/backup.log
```

The results should be 4 and 2. The double arrow appends. A single arrow would replace the earlier evidence.

</details>

[Previous: terminal basics](01-terminal.md) · [Review cards](../review/README.md) · [Next: investigate storage](03-storage.md)

## Find the most frequent event label

If the same error appears twice with an unrelated event in between, a straight count of adjacent lines misses the repeat. Preserve the original log for its timeline and sort a copy of the labels for counting. Work through the [three-row pipeline puzzle](../visual/pipeline-puzzle.md) to see exactly where the output changes.
