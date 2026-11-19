# Linux+ study lab

Start with one question: if a command says a file is missing, how do you tell whether the file is gone or you're looking in the wrong directory? Chapter 1 walks through that problem in a real Linux shell. The chapters work in Ubuntu with Bash using a regular account.

## Table of contents

[Beginner chapters](#read-the-book) · [Exam objective tracker](objectives.md) · [Chapter flashcards](review/README.md) · [Restore challenge](review/restore-ticket.md)

| XK0-006 domain | Jump directly to a topic |
| --- | --- |
| 1. System management | [Filesystem space](chapters/03-storage.md) · [Interfaces and routes](chapters/05-interfaces.md) · [Search log text](chapters/02-logs.md) · [Separate output and errors](labs/streams.md) · [Restore a backup](labs/archive.md) |
| 2. Services and user management | [Paths and directories](chapters/01-terminal.md) · [Hard and symbolic links](labs/links.md) · [Owner and group](labs/identity.md) · [Processes and jobs](chapters/04-processes.md) |
| 3. Security | [File permissions](labs/permissions.md) · [Verify a checksum](labs/checksum.md) |
| 4. Automation, orchestration, and scripting | [Bash conditions and exit status](labs/script.md) · [Git staging and diffs](labs/git.md) |
| 5. Troubleshooting | [Investigate a storage ticket](chapters/03-storage.md) · [Trace a cable to an interface](chapters/05-interfaces.md) |

## Visual labs

[Trace a rack cable](visual/rack-ticket.md) · [Step through a packet exchange](visual/packet-walk.md) · [Move a Git branch](visual/branch-map.md) · [Test yourself](review/README.md#visual-lab-checkpoint)

Start with the rack diagram if you're on a phone or don't have lab software installed. The packet exercise adds a simulator, and the Git exercise pairs a browser game with a real terminal.

## Read the book

| Chapter | What you'll do at the keyboard |
| --- | --- |
| [1. Find your way around the terminal](chapters/01-terminal.md) | Create a handoff note, reproduce a path error, and read the note from a different directory. |
| [2. Find the error inside a log](chapters/02-logs.md) | Locate a log, extract the lines a teammate needs, and verify the report. |
| [3. Investigate a storage ticket](chapters/03-storage.md) | Read a filesystem report, compare two directories, and decide what the evidence supports. |
| [4. Watch a process start and finish](chapters/04-processes.md) | Start a timer and follow its PID until it exits. |
| [5. Follow a cable to a Linux interface](chapters/05-interfaces.md) | Read interface and route output, then compare it with a cable observation. |

[Free browser terminals, videos, and optional Steam games](practice.md)

Begin with [lab setup](setup.md) if you need a Linux terminal. Each chapter has a short lab and a question you can try without the walkthrough. After one chapter, review just its [flashcards](review/README.md).

Preparing for CompTIA Linux+ V8 (XK0-006)? Use the [objective tracker](objectives.md) to see exactly which skills these labs practice and which topics still need study. For a portfolio sample, the [storage ticket](chapters/03-storage.md) ends with directions for writing up your own findings.
