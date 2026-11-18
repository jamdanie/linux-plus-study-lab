# Practice ticket: verify a restored handoff

A teammate hands over a compressed archive and a separate, trusted checksum file. Recover the shift note into an empty directory and show that the recovered file matches the baseline. Work in a fresh Bash terminal.

## Prepare the sample

```bash
cd "$(mktemp -d)"
mkdir original recovered
printf 'Switch port 7 inspected\n' > original/handoff
(cd original && sha256sum handoff) > trusted.sha256
tar -czf shift.tar.gz -C original handoff
```

**Your task:** List the archive, restore it under recovered, and verify the restored copy. Then change the port number in the restored copy and rerun the same check. Record the filename, result, and exit status for each check.

<details><summary>Compare your commands and findings</summary>

```bash
tar -tzf shift.tar.gz
tar -xzf shift.tar.gz -C recovered
(cd recovered && sha256sum -c ../trusted.sha256)
echo "$?"
printf 'Switch port 8 inspected\n' > recovered/handoff
(cd recovered && sha256sum -c ../trusted.sha256)
echo "$?"
```

Expect OK and 0 before the edit, then FAILED and 1 afterward. Running the check inside recovered matters because the baseline names the relative path handoff. For a portfolio note, explain how you know you checked the recovered copy rather than the original.

</details>

[Review archive recovery](../labs/archive.md) · [Review checksums](../labs/checksum.md) · [Contents](../README.md)
