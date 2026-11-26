# The report exists. Did this run produce it?

Use Bash in the [free Ubuntu playground](https://killercoda.com/playgrounds/scenario/ubuntu). Run the blocks in order in one terminal. This exercise runs the reporting command by hand so you can isolate what happens after a scheduler launches it.

```bash
lab=$(mktemp -d)
cd "$lab" || exit
mkdir input
printf '%s\n' rack-07 > input/rack
cat > report.sh <<'EOF'
#!/bin/sh
rack=$(cat input/rack) || exit 1
printf '%s %s\n' "$(date -u +%FT%TZ)" "$rack" >> inventory.log
EOF
sh report.sh
cat inventory.log
```

Expect one UTC timestamp followed by rack-07. Now simulate an input file being renamed.

```bash
mv input/rack input/rack.old
sh report.sh
echo "$?"
wc -l < inventory.log
```

The error names the missing input. The exit status is 1. The line count stays at one. An operator who only checks that the report exists could mistake yesterday’s inventory for today’s.

```bash
mv input/rack.old input/rack
sh report.sh
echo "$?"
cat -n inventory.log
```

Expect status 0 and a second record. For a portfolio note, save the failed status, the before-and-after counts, and the change that restored output. This run tests the report command. To investigate its scheduled launch, continue to the [timer inspection lab](timer-inspection.md).
