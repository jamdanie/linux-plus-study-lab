# Read and change file permissions

Linux+ XK0-006 objective 3.3 · [Table of contents](../README.md)

A handoff should be writable by its owner and readable by its group. How do you check the result?

A file mode has separate read, write, and execute bits for its owner, group, and everyone else. In numeric notation read is 4, write is 2, and execute is 1.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
touch handoff
chmod 600 handoff
stat -c '%A %a %n' handoff
chmod g+r handoff
stat -c '%A %a %n' handoff
```

## Read the result

The modes change from 600 to 640. The middle digit gains 4. The owner and group names stay the same because chmod changes permissions.

**Check yourself.** How would you remove only the permission you just added?

<details><summary>Show answer</summary>

Use chmod g-r handoff, then check for 600. Changing ownership would address a different problem.

</details>

## Read a mode one group at a time

For a regular file showing `-rw-r-----`, cover the first character and split the rest into three groups.

| Owner | Group | Others |
| --- | --- | --- |
| rw- = 4 + 2 | r-- = 4 | --- = 0 |

Predict the result of `chmod u-w handoff` after the 640 step above. Check with `stat -c '%A %a' handoff`. You should get 440. Restore the owner's write bit with `chmod u+w handoff`.

## Distinguish two file-creation failures

A process reports “Permission denied” creating a file. The next ticket says “No space left on device.” Before changing any permission, record the exact error. For the first, check the process identity and write/search permissions on the parent directory. For the second, compare block and inode availability on that directory's filesystem. [Try the storage case](../review/inode-ticket.md).
