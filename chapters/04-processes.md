# 4. Watch a process start and finish

When you type a command and the prompt comes back, how do you tell whether the program finished or is still working? A **process** is a running instance of a program. The shell can run it in the **background**, which leaves your prompt available. A **PID** is the number Linux assigns to the process. A **job number** is how this particular shell keeps track of the work it started.

## Lab: follow one timer

Open Bash in the [free Ubuntu playground](../practice.md). Keep the same terminal open throughout. Start a timer and record its PID on the very next line. The ampersand asks Bash to run the timer in the background. The special variable `$!` holds the PID of the most recent background job.

```bash
sleep 120 &
timer_pid=$!
jobs -l
ps -p "$timer_pid" -o pid,stat,comm
```

Find the same PID in both outputs. In an interactive shell, `jobs -l` also shows a job number in brackets. In the `ps` output, look for `sleep` under COMMAND. An S in STAT means sleeping. A timer waiting for its time to expire is doing exactly what you asked it to do.

**Watch the change.** Press Enter after each command below. The first command waits for a new three-second timer. The final `ps` checks whether that short timer still exists.

```bash
sleep 3 &
short_pid=$!
wait "$short_pid"
printf 'Timer exit status: %s\n' "$?"
ps -p "$short_pid" -o pid,comm
```

Expect exit status 0 and no process row for the short timer. The header may still appear. `wait` applies to a child of this shell, so use the original terminal. The first timer will finish on its own.

**Try it.** Before the two minutes expire, use the first PID with `ps` again. Why can two commands named `sleep` finish at different times? Each invocation started a separate process with its own PID and duration. For a support note, capture the command name and PID while the longer timer is still running. The name alone can't tell the two timers apart.

[Previous: storage](03-storage.md) · [Next: cables and interfaces](05-interfaces.md) · [Chapter 4 cards](../review/README.md#chapter-4)

## Watch one timer in a process viewer

Start a fresh `sleep 90 &` in interactive Bash and run `echo $!` to capture its PID. Open `top -p "$!"` immediately in the same shell. Watch the command and state columns. If the timer finishes, its row disappears on refresh. Press q to exit. On a system with [htop](https://htop.dev/) installed, you can repeat the exercise with `htop -p "$!"` immediately after launching a new timer. Record the PID so another sleep process cannot be mistaken for yours.
