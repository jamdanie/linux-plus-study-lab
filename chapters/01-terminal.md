# 1. Find your way around the terminal

A **terminal** is the window where you type. The **shell** is the program that reads what you enter. In these labs the shell is Bash. When you type `ls -a .`, the command is `ls`, the option `-a` includes hidden names, and the argument `.` tells it which directory to list.

Your **working directory** is where the shell starts looking when you give it a relative path. A path beginning with `/` is **absolute** and starts at the root of the filesystem. A path like `notes/handoff.txt` is **relative** and starts wherever you are. That difference matters when a file existed a minute ago and now the shell says it can't find it.

## Lab: recover a missing handoff note

Create a fresh practice directory. `mktemp -d` creates a directory with a unique name. The first line saves its path in a shell variable called `lab`. The quotes keep its value together as one argument.

```bash
lab=$(mktemp -d)
cd "$lab"
mkdir notes
printf '%s\n' 'Handoff: check the backup log.' > notes/handoff.txt
pwd
ls notes
```

You should see your practice path followed by `handoff.txt`. The `>` sent the text into that file. It creates the file or replaces its contents, so use it only on the practice file here.

Move one level deeper and try the original relative path again.

```bash
cd notes
pwd
cat notes/handoff.txt
```

Expect “No such file or directory.” From here, that command looks for a second directory named `notes` inside the first. Check what is actually here, then read the file two ways.

```bash
ls
cat handoff.txt
cat "$lab/notes/handoff.txt"
```

Both reads should print the same handoff. The first uses the current directory. The second uses the full path saved earlier. In a support ticket, the output of `pwd` would explain why the original command failed.

**Try it without the steps.** Move to the parent directory and read the handoff using a relative path. Which part of the path did you have to add back?

<details><summary>Check your answer</summary>

Use `cd ..`, then `cat notes/handoff.txt`. Two dots mean the parent directory. Use `pwd` to check where you landed. For help with a Bash built-in such as `cd`, try `help cd`. For a GNU utility such as `ls`, try `ls --help`.

</details>

[Review cards](../review/README.md) · [Next: search a log](02-logs.md)
