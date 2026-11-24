# Check whether a file changed

Linux+ XK0-006 objective 3.5 · [Table of contents](../README.md)

Two files can have the same name and size. How can you tell if their contents still match a saved baseline?

A SHA-256 digest is calculated from file contents. Keep a trusted copy of the reference digest when using it to verify integrity.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
printf 'rack A\n' > inventory
sha256sum inventory > baseline.sha256
sha256sum -c baseline.sha256
printf 'rack B\n' > inventory
sha256sum -c baseline.sha256
```

## Read the result

The first check says OK. The second reports FAILED even though only one letter changed. That final nonzero status is expected.

**Check yourself.** Does a mismatch tell you who edited the file?

<details><summary>Show answer</summary>

It shows the current contents differ from the baseline. Attribution needs separate evidence.

</details>

## Compare two files of equal size

In a fresh practice directory, create two inventory records and predict which column will change.

```bash
cd "$(mktemp -d)"
printf 'A7\n' > old
printf 'A8\n' > new
wc -c old new
sha256sum old new
```

Each file is three bytes, including its newline. Compare the digests before reading the labels at the right. File size alone would miss this edit.

## Verify a group of recovered files

In a fresh directory, save two named files and generate one manifest with `sha256sum first second > manifest` after creating both with `touch first second`. Append one line to second, then run `sha256sum -c manifest`. The per-file results identify which file changed. Even one failure makes the overall check fail. Compare that evidence with the capacity findings in the [storage ticket](../review/inode-ticket.md).

## Separate content verification from mount verification

Two disposable volumes both contain identical copies of yesterday's handoff. Their SHA-256 values match. Does that identify which volume is attached to the running writer? Inspect the mount mapping for that question. Use the checksum to verify the recovered contents and the [mount reader](container-inspect.md) to verify identity and destination.
