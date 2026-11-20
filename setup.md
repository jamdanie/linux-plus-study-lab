# Open a Linux terminal

Want to try one lab without installing software? [Open a free browser terminal](practice.md).

**Already using Ubuntu?** Open Terminal and type `bash`. You can start Chapter 1. These first labs use ordinary Linux commands and temporary practice files. Keep the same terminal open for the whole chapter so its variables stay available.

**On Windows 11 or Windows 10 version 2004 (build 19041) or later?** Open PowerShell and enter `wsl -l -v`. If Ubuntu is listed, open Ubuntu from the Start menu. For a first installation, open PowerShell as administrator, enter `wsl --install`, and restart Windows when prompted. Open Ubuntu and choose a Linux username and password when asked. The password prompt stays blank as you type. [Microsoft's WSL setup guide](https://learn.microsoft.com/en-us/windows/wsl/install)

Run these next two commands **inside Ubuntu**:

```bash
whoami
pwd
```

The first line of output should be your Linux username. The second shows your working directory. If your prompt starts with `PS C:\`, open Ubuntu before running the lab. You won't need administrator access inside Linux for these chapters.

A terminal window is enough for these labs. Packet Tracer can help you draw a network later. For now, seeing paths, matching lines, and disk usage change as you type is the point of the exercise.

[Start Chapter 1](chapters/01-terminal.md)

## Check what this terminal can run

For the new exercises, run `command -v awk sort uniq python3 dpkg-query` inside Linux. Each line names an available program. The pipeline puzzle uses sort and uniq, and the rack calculation uses awk. If dpkg-query is absent on a different distribution, use the Ubuntu playground for the package exercise. [Choose a practice space](practice.md)
