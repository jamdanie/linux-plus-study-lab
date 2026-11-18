# Review the first three chapters

On GitHub, choose a chapter and open each answer after making your choice. In Anki Desktop, download [the tab-separated deck](linux-plus.tsv) using the raw download button, then choose **File → Import**. Use the Basic note type and a deck named `Linux+ XK0-006`. In the preview, check that columns 1, 2, and 3 map to Front, Back, and Tags. Filter by `chapter_01`, `chapter_02`, or `chapter_03` to study one lesson. [Anki text import guide](https://docs.ankiweb.net/importing/text-files.html)

## Chapter 1

**You changed directories and want the absolute path of your current location. Which command do you run?**

- A. ls
- B. pwd
- C. cd ..

🧠 Think: Do you need a listing, a location, or a move?

<details><summary>Show answer</summary>

**B. pwd**

- A. ls: Lists entries in the current directory.
- B. pwd: Prints the current working directory.
- C. cd ..: Moves to the parent directory.

📦 Key Idea: Check your location before diagnosing a missing file.

</details>

**You are inside notes, and ls shows handoff.txt. Which command reads it from here?**

- A. cat handoff.txt
- B. cat notes/handoff.txt
- C. ls handoff.txt

🧠 Think: Resolve each path from the directory you're in.

<details><summary>Show answer</summary>

**A. cat handoff.txt**

- A. cat handoff.txt: Reads the file in the current directory.
- B. cat notes/handoff.txt: Looks for another notes directory below the current one.
- C. ls handoff.txt: Lists the entry without reading its text.

📦 Key Idea: A relative path begins at the current directory.

</details>

**You are in the notes directory. Which command moves up exactly one directory?**

- A. cd /
- B. cd .
- C. cd ..

🧠 Think: Where does each path lead?

<details><summary>Show answer</summary>

**C. cd ..**

- A. cd /: Moves to the filesystem root.
- B. cd .: Stays in the current directory.
- C. cd ..: Moves to the parent directory.

📦 Key Idea: A single dot means here. Two dots mean the parent.

</details>

## Chapter 2

**You know the filename ends in .log but don't know its directory under logs. Which command finds matching regular files?**

- A. grep ERROR logs/backup.log
- B. find logs -type f -name '*.log'
- C. ls logs

🧠 Think: Are you searching names or contents, and should the search include subdirectories?

<details><summary>Show answer</summary>

**B. find logs -type f -name '*.log'**

- A. grep ERROR logs/backup.log: Reads matching lines in one named file.
- B. find logs -type f -name '*.log': Searches the directory tree for regular files matching the quoted name pattern.
- C. ls logs: Lists the immediate entries without filtering by name or descending into each directory.

📦 Key Idea: Use find for a search by file properties.

</details>

**Which command displays matching error lines with their original line numbers?**

- A. grep -c '^ERROR ' logs/backup.log
- B. wc -l logs/backup.log
- C. grep -n '^ERROR ' logs/backup.log

🧠 Think: What information needs to remain attached to each matching line?

<details><summary>Show answer</summary>

**C. grep -n '^ERROR ' logs/backup.log**

- A. grep -c '^ERROR ' logs/backup.log: Prints the number of matching lines.
- B. wc -l logs/backup.log: Counts every newline in the file.
- C. grep -n '^ERROR ' logs/backup.log: Prints each matching line with its source line number.

📦 Key Idea: Use -n to locate a match and -c to count matching lines.

</details>

**Your log already has three entries. Which operator adds a fourth entry at the end?**

- A. &gt;&gt;
- B. &gt;
- C. |

🧠 Think: What should happen to the first three entries?

<details><summary>Show answer</summary>

**A. &gt;&gt;**

- A. &gt;&gt;: Appends new output to the existing file.
- B. &gt;: Replaces the file contents with new output.
- C. |: Sends output to another command.

📦 Key Idea: Use append redirection to preserve existing entries.

</details>

## Chapter 3

**A teammate asks how much room is available on the filesystem holding backups. Which command answers that?**

- A. du -sh backups
- B. ls backups
- C. df -h backups

🧠 Think: Does the question concern one directory or the filesystem holding it?

<details><summary>Show answer</summary>

**C. df -h backups**

- A. du -sh backups: Summarizes space used under the directory.
- B. ls backups: Lists its entries.
- C. df -h backups: Reports filesystem capacity and available space.

📦 Key Idea: Read Avail in df when planning another write.

</details>

**Which command compares allocated space under backups and reports separately?**

- A. du -sh backups reports
- B. df -h backups reports
- C. pwd

🧠 Think: Both directories are on the same mount.

<details><summary>Show answer</summary>

**A. du -sh backups reports**

- A. du -sh backups reports: Reports a total for each named directory.
- B. df -h backups reports: Reports space at filesystem scope.
- C. pwd: Prints the working directory path.

📦 Key Idea: Two directories on one filesystem can have very different totals.

</details>

**The backups directory uses 4 MiB. What else do you need to assess whether a 100 MiB backup will fit?**

- A. The number of lines in the backup log
- B. Available space on the destination filesystem
- C. The name of your current shell

🧠 Think: Which measurement can be compared with the requested capacity?

<details><summary>Show answer</summary>

**B. Available space on the destination filesystem**

- A. The number of lines in the backup log: Describes log length, not available storage.
- B. Available space on the destination filesystem: Lets you compare available capacity with the size of the planned write.
- C. The name of your current shell: Identifies the command interpreter.

📦 Key Idea: A directory's current size alone cannot establish free capacity.

</details>

[Back to the book](../README.md)
