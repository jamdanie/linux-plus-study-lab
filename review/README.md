# Chapter review cards

On GitHub, choose a chapter and open each answer after making your choice. In Anki Desktop, download [the tab-separated deck](linux-plus.tsv) using the raw download button, then choose **File → Import**. Use the Basic note type and a deck named `Linux+ XK0-006`. In the preview, check that columns 1, 2, and 3 map to Front, Back, and Tags. Filter by `chapter_01`, `chapter_02`, `chapter_03`, `chapter_04`, or `chapter_05` to study one lesson. [Anki text import guide](https://docs.ankiweb.net/importing/text-files.html)

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

## Chapter 4

**Two timers named sleep are running. What identifies one of those running processes?**

- A. Its command name
- B. Its PID
- C. The terminal title

🧠 Think: Which value distinguishes two instances of one program?

<details><summary>Show answer</summary>

**B. Its PID**

- A. Its command name: Both commands have the same name.
- B. Its PID: Linux gives each live process a distinct process ID.
- C. The terminal title: The same terminal can start both timers.

📦 Key Idea: Record the PID while the process is running.

</details>

**Which Bash command waits for your background timer and gives you its exit status?**

- A. jobs -l
- B. ps -p "$timer_pid"
- C. wait "$timer_pid"

🧠 Think: Do you need a snapshot or the completion result?

<details><summary>Show answer</summary>

**C. wait "$timer_pid"**

- A. jobs -l: Lists jobs tracked by this shell.
- B. ps -p "$timer_pid": Reports whether the process is present at that moment.
- C. wait "$timer_pid": Waits for this child process and returns its status.

📦 Key Idea: Read $? immediately after wait to capture its result.

</details>

**Which value should you save immediately after starting sleep 120 & to identify that child?**

- A. $!
- B. $?
- C. $$

🧠 Think: Which shell value changes when a background job starts?

<details><summary>Show answer</summary>

**A. $!**

- A. $!: Expands to the most recent background PID.
- B. $?: Holds the preceding command’s exit status.
- C. $$: Identifies the shell itself.

📦 Key Idea: Capture $! before starting another background job.

</details>


## Chapter 5

**You want to see which IPv4 gateway the host uses by default. Which check fits?**

- A. ip -brief link
- B. ip route show default
- C. ps -p 1

🧠 Think: Which output describes the next hop?

<details><summary>Show answer</summary>

**B. ip route show default**

- A. ip -brief link: Shows interfaces and link information.
- B. ip route show default: Displays the default IPv4 route if one exists. Look for via and dev.
- C. ps -p 1: Shows process information for PID 1.

📦 Key Idea: Read the route to identify the next hop.

</details>

**A wired adapter stays UP but changes from LOWER_UP to NO-CARRIER. What should you inspect first?**

- A. The DNS search suffix
- B. The backup directory
- C. The cable and peer switch port

🧠 Think: At what layer was a change observed?

<details><summary>Show answer</summary>

**C. The cable and peer switch port**

- A. The DNS search suffix: Name resolution cannot explain a lost carrier signal.
- B. The backup directory: Storage usage does not establish Ethernet link state.
- C. The cable and peer switch port: The local link lost carrier. Check both cable ends and the peer port.

📦 Key Idea: Administrative state and carrier answer different questions.

</details>

**Which interface lets software address this same Linux host through loopback?**

- A. lo
- B. A physical switch port
- C. The default gateway

🧠 Think: Which path stays within the host?

<details><summary>Show answer</summary>

**A. lo**

- A. lo: lo is the Linux loopback interface.
- B. A physical switch port: This is a connection point on a switch.
- C. The default gateway: This is a next hop used by a default route.

📦 Key Idea: Loopback traffic stays on the host.

</details>

[Back to the book](../README.md)
