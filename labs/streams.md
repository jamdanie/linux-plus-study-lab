# Capture an error separately

Linux+ XK0-006 objective 1.5 · [Table of contents](../README.md)

A command found one requested file and missed another. How do you save the error without mixing it into the result?

Standard output carries ordinary results. Standard error carries diagnostics. Bash can send them to different files during the same command.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
touch found.txt
ls -d found.txt missing.txt > results.txt 2> errors.txt
printf 'Command status: %s\n' "$?"
cat results.txt
cat errors.txt
```

## Read the result

The status is nonzero. results.txt contains found.txt and errors.txt names missing.txt. A command can produce useful output and still report failure.

**Check yourself.** Why capture the status before running cat?

<details><summary>Show answer</summary>

Each command updates $?. After cat, the value describes the read of the report.

</details>
