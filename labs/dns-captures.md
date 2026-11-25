# Compare four resolver captures

Work from the repository root in Bash. These are simplified text records for inspection, not packet captures. Preview the kinds of queries first.

```bash
grep -H '^Query:' fixtures/dns-shift/*.txt
grep -H '^Status:' fixtures/dns-shift/*.txt
grep -H '^Client message:' fixtures/dns-shift/*.txt
```

The first command prints four filenames; the second prints three. Before running the third command, predict which filename will be missing from the second output. The timeout case has no Status line because the client received no DNS reply. Read all of rack-b.txt before classifying its empty answer.

**Live command counterpart.** On your Ubuntu lab host, `getent ahostsv4 localhost` asks the system's configured name-service sources for IPv4 results. A local hosts entry can satisfy it. `dig example.org A` asks DNS using the configured resolver. Read the header status, question, answer and SERVER fields. Try the second command in a network-enabled playground with dig installed. Both commands can return an address while answering different diagnostic questions.

[Linux getent manual](https://man7.org/linux/man-pages/man1/getent.1.html) · [BIND dig reference](https://bind9.readthedocs.io/en/stable/manpages.html)
