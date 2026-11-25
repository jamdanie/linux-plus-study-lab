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

## Watch output while saving a copy

From the practice directory above, run `cat results.txt | tee handoff.txt`, then `cmp results.txt handoff.txt && echo 'Same contents'`. The filename appears on screen and in the saved copy. A plain redirect would write the output without displaying it. The earlier error remains in errors.txt because it was captured separately.

## Preserve a lookup tool's status

A capture can contain a meaningful diagnostic even when a command returns an unsuccessful status. Conversely, dig can exit successfully after receiving an NXDOMAIN reply. Record both the program's exit status and the DNS header code when available. For a timeout, quote the client's diagnostic. [See the contrasting cases](dns-captures.md).
