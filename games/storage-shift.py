"""Generate a simulated storage ticket and check three findings. Python 3 only."""
import argparse
import random
from pathlib import Path
from tempfile import TemporaryDirectory


def ask(prompt, expected, hint):
    for attempt in range(2):
        answer = input(prompt + " > ").strip().casefold()
        if answer == expected.casefold():
            print("Correct.")
            return 1
        if attempt == 0:
            print("Hint:", hint)
    print("Expected:", expected)
    return 0


def play(seed):
    rng = random.Random(seed)
    hosts = ["web-a", "db-b", "backup-c"]
    rng.shuffle(hosts)
    mounts = ["/srv", "/var", "/data"]
    devices = ["vdb1", "vdc2", "vdd1"]
    rng.shuffle(mounts)
    rng.shuffle(devices)
    with TemporaryDirectory(prefix="linux-plus-shift-") as directory:
        root = Path(directory)
        conditions = ["inodes", "blocks", "healthy"]
        for host, mount, device, condition in zip(hosts, mounts, devices, conditions):
            used = 100 if condition == "blocks" else 42
            free_inodes = 0 if condition == "inodes" else 5100
            (root / (host + ".txt")).write_text(
                f"host={host}\nmount={mount}\ndevice=/dev/{device}\n"
                f"blocks_used_percent={used}\nfree_inodes={free_inodes}\n",
                encoding="utf-8",
            )
        print("Ticket: one host cannot create a file although blocks are available.")
        print("In a second terminal, inspect the simulated reports:")
        print("  cd", directory)
        print("  cat *.txt")
        print("Keep this session open. The temporary reports disappear at exit.")
        score = ask("Which host has the inode shortage?", hosts[0],
                    "Find the report with free_inodes=0.")
        score += ask("Which mount is affected?", mounts[0], "Read its mount field.")
        score += ask("Which device supplies that mount?", "/dev/" + devices[0],
                     "Copy the device field including /dev/.")
        print(f"Score: {score}/3")
        print("Debrief: df -i checks inode availability. df -h checks block space.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, help="Replay the same ticket.")
    args = parser.parse_args()
    try:
        play(args.seed)
    except (EOFError, KeyboardInterrupt):
        print("\nShift ended.")
