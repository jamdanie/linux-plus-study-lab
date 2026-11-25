# Play DNS Shift

A rack monitor reports a name lookup problem. Before touching a switch, read what the client asked and what the resolver actually returned. All evidence below is simulated. One point per correct diagnosis, four points available.

**Play in a terminal.** From a downloaded or cloned copy of this repository, run `python3 games/dns-shift.py`. The game reads four local captures, shuffles the cases and choices, and explains each answer. Add `--seed 9` to repeat a session. No connection to a lab server is needed.

**Play on GitHub.** Open one capture at a time: [A](../fixtures/dns-shift/rack-a.txt), [B](../fixtures/dns-shift/rack-b.txt), [C](../fixtures/dns-shift/rack-c.txt), [D](../fixtures/dns-shift/rack-d.txt). For each, choose: IPv4 address returned, requested type absent, name reported nonexistent, or no reply observed. Cite a line before revealing the key.

<details><summary>Check the four tickets</summary>

A returns 192.0.2.10 for an A query. B has an existing name with no AAAA record in the supplied evidence. C has an NXDOMAIN response for the name. D has a timeout and no response header. D alone cannot tell you whether the name exists.

</details>

**For a portfolio note**, choose one failed lookup. Include the queried name, record type, resolver, exact outcome, and the next check that outcome justifies. [Example decision diagram](../visual/dns-response.md)
