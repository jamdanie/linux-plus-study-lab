# Which host needs an inode investigation?

Three simulated backup agents run on separate hosts. Only one reports a file-creation failure despite having free data blocks. Match the symptom to the host and choose the first Linux command you would run there.

| Host | Mount | Block space used | Free inodes |
| --- | --- | ---: | ---: |
| cedar | /srv | 42% | 0 |
| maple | /var | 100% | 4,800 |
| alder | /data | 58% | 6,000 |

<details><summary>Check your diagnosis</summary>

Cedar matches both clues. Run `df -i /srv` to confirm the inode count and `df -h /srv` to check the separate block measurement. Maple has its own block-space problem. For a portfolio handoff, record both readings, the affected mount, and which host generated the original error. Before removing anything, investigate which application creates the files and what its retention policy allows.

</details>

[Replay with different host labels](../games/README.md) · [Table of contents](../README.md)
