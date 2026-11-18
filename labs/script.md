# Write a Bash file check

Linux+ XK0-006 objective 4.2 · [Table of contents](../README.md)

A backup job needs a quick check that a report exists and has some content.

A positional parameter passes a path into a script. A conditional chooses the outcome. An exit status lets the next program act on that outcome.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
cat > check-report.sh <<'BASH'
if [[ -f "$1" && -s "$1" ]]; then
    echo 'Report has content'
    exit 0
fi
echo 'Report missing or empty' >&2
exit 1
BASH
touch 'daily report'
bash check-report.sh 'daily report'
printf 'Empty report status: %s\n' "$?"
printf 'Complete\n' > 'daily report'
bash check-report.sh 'daily report'
printf 'Filled report status: %s\n' "$?"
```

## Read the result

The empty file returns 1. The filled file returns 0. Quoting the path keeps daily report together as one argument.

**Check yourself.** Would checking only that the file exists have caught the first failure?

<details><summary>Show answer</summary>

No. An empty report exists. The size check catches that case.

</details>
