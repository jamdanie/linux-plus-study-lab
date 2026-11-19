# Compare working and staged changes

Linux+ XK0-006 objective 4.4 · [Table of contents](../README.md)

You staged a shift note, then fixed a line. Which version would the next commit contain?

The working tree is where you edit. The index holds the snapshot prepared for the next commit. This local practice repo needs no remote or account.

## Try it in Bash

Start in a fresh temporary directory in an Ubuntu terminal. Run the lines in order.

```bash
cd "$(mktemp -d)"
git init -q
printf 'port 7\n' > handoff
git add handoff
printf 'port 8\n' > handoff
git diff -- handoff
git diff --cached -- handoff
```

## Read the result

The first diff shows the edit from 7 to 8. The cached diff shows the staged new file containing port 7. Read the added line beginning with +.

**Check yourself.** How do you stage the correction?

<details><summary>Show answer</summary>

Run git add handoff again. The ordinary diff should then be empty and the cached diff should show port 8.

</details>

## Read the two status columns

After editing the staged file in this lab, run `git status --short`. Expect `AM handoff`. The left column shows the new file staged for addition. The right column shows a further working-tree modification. Stage the correction and run the same check again: the M disappears. Now [follow the commit on a branch graph](../visual/branch-map.md).
