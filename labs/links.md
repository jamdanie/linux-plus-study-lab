# Hard links and symbolic links

Linux+ XK0-006 objective 2.1 · [Table of contents](../README.md)

A report has two shortcuts. What happens to each when someone renames the original?

A hard link is another name for the same inode (the filesystem's record for a file). A symbolic link stores a path. That difference matters when files move.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
printf 'ready\n' > report
ln report hard-copy
ln -s report shortcut
ls -li
mv report renamed
cat hard-copy
readlink shortcut
test -L shortcut && test ! -e shortcut && echo 'Target missing'
```

## Read the result

The inode numbers for the original and hard-copy match. After the rename, hard-copy still prints ready. readlink prints report because that is the path stored in the shortcut.

**Check yourself.** How could you repair the shortcut without changing either link?

<details><summary>Show answer</summary>

Move renamed back to report. The stored path resolves again.

</details>

## Predict the inode numbers

In the directory from this lab, run `ls -li renamed hard-copy shortcut`. Match the first column for the two names that still open the same data. Next run `printf 'second line\n' >> hard-copy` and read `cat renamed`. The new line appears through either hard link. The broken symbolic link still points to the old name.
