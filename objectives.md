# XK0-006 objective tracker

The domain weights below come from the [CompTIA Linux+ V8 exam objectives, version 5.0](https://lecbyo.files.cmp.optimizely.com/download/90b9ac985c0e11f0b004a2a93c999a21). Use the PDF for the full list of commands and concepts. The links below identify the part of each objective you can practice here.

| Exam domain | Weight | Practice available |
| --- | ---: | --- |
| 1. System management | 23% | 1.3: [filesystem and directory space](chapters/03-storage.md). 1.4: [interface and route inspection](chapters/05-interfaces.md). 1.5: [shell output, pipes, and text filtering](chapters/02-logs.md), [error redirection](labs/streams.md). 1.6: [restore an archive](labs/archive.md). |
| 2. Services and user management | 20% | 2.1: [paths and directories](chapters/01-terminal.md) and [finding files](chapters/02-logs.md). 2.1: [hard and symbolic links](labs/links.md). 2.2: [inspect account and group identity](labs/identity.md). 2.3: [process IDs, jobs, and exit status](chapters/04-processes.md). |
| 3. Security | 18% | 3.3: [file mode changes](labs/permissions.md). 3.5: [SHA-256 integrity checks](labs/checksum.md). |
| 4. Automation, orchestration, and scripting | 17% | 4.2: [script conditions and exit status](labs/script.md). 4.4: [staging and comparing changes](labs/git.md). |
| 5. Troubleshooting | 22% | 5.2: [initial storage diagnosis](chapters/03-storage.md). 5.3: [link state versus routing](chapters/05-interfaces.md). |

These are introductory exercises within broader objectives. For example, using `df` and `du` covers two tools in 1.3. Partitioning, mounts, RAID, and logical volumes still need separate practice. When reviewing a skill, try the chapter challenge in a fresh terminal and explain which output supports your answer.

### Visual practice by objective

Use the [same-subnet packet walk](visual/packet-walk.md) to practice reading neighbor evidence for 1.4, the [branch graph](visual/branch-map.md) to trace a commit for 4.4, and the [rack ticket](visual/rack-ticket.md) to distinguish link recovery from application recovery for 5.3. Review those skills in the [visual lab checkpoint](review/README.md#visual-lab-checkpoint).

[Back to the book](README.md)

## Night-shift practice by objective

| Objective | What you can demonstrate |
| --- | --- |
| 1.5 · Shell operations | [Group and count repeating labels](visual/pipeline-puzzle.md). |
| 2.4 · Software management | [Look up a package's installation status and file ownership](labs/package-owner.md). |
| 4.3 · Python basics | [Filter a list of rack asset records](labs/python-inventory.md). |
| 5.1 · Monitoring | [Calculate an interval rate from cumulative counters](labs/counter-delta.md). |

Use the [night-shift ticket](review/night-shift.md) to practice deciding which conclusion the measurements support.

## Storage shift practice

| XK0-006 objective | Task | Evidence |
| --- | --- | --- |
| 1.3 · Storage | [Identify the destination filesystem](labs/mount-destination.md) | Match the path to TARGET and SOURCE. |
| 5.2 · Storage troubleshooting | [Diagnose a file-creation failure](review/inode-ticket.md) | Compare block and inode readings on the affected mount. |

[Replay the ticket with a new dataset](games/README.md).

## Practice systemd unit management

For objective **2.5**, [build and remove an enablement link](labs/offline-enable.md) and [inspect a unit's recent journal](labs/unit-journal.md). Check your judgment in the [service desk shift](games/service-desk.md). A complete answer distinguishes activation at boot, current state, and evidence that the application produced the expected result.
