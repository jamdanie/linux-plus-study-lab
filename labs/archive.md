# Restore a file from a backup

Linux+ XK0-006 objective 1.6 · [Table of contents](../README.md)

You have a backup archive. Can you show that it contains a usable copy of the handoff?

An archive collects files into one file. Compression reduces its size. A restore check answers a different question: can you recover the expected contents?

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
mkdir notes restored
printf 'Rack 7 inspected\n' > notes/handoff
tar -czf notes.tar.gz notes
tar -tzf notes.tar.gz
tar -xzf notes.tar.gz -C restored
diff -s notes/handoff restored/notes/handoff
```

## Read the result

The listing includes notes/handoff. The comparison reports identical files. The restore went into its own directory, so you can compare both copies.

**Check yourself.** Which command could succeed even if the archive contained yesterday's handoff?

<details><summary>Show answer</summary>

Listing the archive only shows the stored names. Compare the restored contents with the expected version.

</details>

## Recover just one item

In the same lab directory, run `mkdir one-file` followed by `tar -xzf notes.tar.gz -C one-file notes/handoff`. Check `find one-file -type f`. You should see just the requested file. Use the member name exactly as it appeared in the archive listing. An absolute path on the live machine can refer to a different location.
