# Find the owner and group

Linux+ XK0-006 objective 2.2 · [Table of contents](../README.md)

Before changing access on a ticket, whose account and file are you actually looking at?

Linux tracks users and groups with numeric IDs. id shows the identity of the running account, while stat identifies the owner and group attached to a file.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
touch shift-note
id -un
id -Gn
stat -c 'owner=%U group=%G mode=%a' shift-note
```

## Read the result

Compare the reported owner with your username. Group membership helps explain which permission bits can apply to someone other than the owner.

**Check yourself.** Does seeing a group name on a file mean every member can edit it?

<details><summary>Show answer</summary>

Check the mode. A group can own a file with no group write permission.

</details>
