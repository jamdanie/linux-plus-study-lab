# Predict which branch moves

Open [Learn Git Branching](https://learngitbranching.js.org/) and try the introductory branching level. Before the next commit, point to the branch you think will move. A branch name follows the newest commit on that branch. HEAD tells you which branch is checked out in this exercise.

Recreate the idea in a temporary local Git repository. The name and email settings apply only to this disposable repo. Nothing is pushed.

```bash
cd "$(mktemp -d)"
git init -q -b main
git config user.name 'Lab Learner'
git config user.email 'learner@example.invalid'
printf 'port 7\n' > rack-note
git add rack-note
git commit -qm 'Record initial port'
git switch -qc cable-check
printf 'port 8\n' > rack-note
git commit -qam 'Correct the port label'
git log --oneline --decorate --graph --all
git show main:rack-note
git show cable-check:rack-note
```

**Read the labels.** HEAD and cable-check should point to the correction. Main should still point to the first commit. The two file reads return different ports. Both commits sit on one line of history so far. For a fork in the drawing, switch back to main, add a different note there, commit it, and rerun the graph.

[Review staging first](../labs/git.md) · [Contents](../README.md)
