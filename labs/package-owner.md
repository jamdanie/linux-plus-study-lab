# Find which Ubuntu package installed a command

A ticket mentions a problem with the system copy of `ls`. Before suggesting a reinstall, identify its package. Run these read-only queries in Debian or Ubuntu.

```bash
command -v ls
dpkg-query -L coreutils | grep -E '/(bin|sbin)/ls$'
dpkg-query -W -f='${Package} ${Status}\n' coreutils
```

The listing shows the path recorded by the package. Use that exact path with `dpkg-query -S` to perform the reverse lookup. A system with merged /usr may launch /usr/bin/ls while the package database records /bin/ls. An interactive alias can also change what command -v prints. The expected package status ends in “install ok installed.”

If the package query says “no packages found,” run `dpkg-query -W | head`. An empty listing can occur in a stripped-down container even when the executable is present. Use a standard Ubuntu installation for the ownership check and record the missing database as a limitation of the container.

**Check yourself.** Does this status prove every file is intact? It records the package's installation state. File integrity is a different check.

[Table of contents](../README.md)
