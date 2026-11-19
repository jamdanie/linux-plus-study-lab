# Where to practice

**For a first session, open the free Ubuntu playground.** Your commands run on a temporary Linux machine in the browser. Its free session lasts up to one hour and is then deleted. Copy any notes you want to keep before it expires. [Launch Killercoda Ubuntu](https://killercoda.com/playgrounds/scenario/ubuntu) · [Session rules](https://killercoda.com/faq/)

Try this in that terminal. The first listing should be empty. The second should show the words you wrote. Run the first line again whenever you want a fresh practice directory.

```bash
cd "$(mktemp -d)"
ls
printf '%s\n' 'Cable A goes to switch port 7' > cable-note.txt
cat cable-note.txt
```

**Another free browser option:** On JSLinux, choose an Alpine Linux **Console** and click its startup link. Try the four commands above. Alpine's utilities can support different options from Ubuntu's, so use Ubuntu for chapters that specify GNU utilities or Bash. [Launch JSLinux](https://bellard.org/jslinux/)

## Watch a command, then run it

| Free lesson | One thing to try while watching |
| --- | --- |
| [Learn Linux TV: The ps Command](https://www.learnlinux.tv/linux-essentials-the-ps-command/) | Pause when the process list appears. Start the timer in [Chapter 4](chapters/04-processes.md) and find its PID in your own terminal. |
| [Learn Linux TV: How to Use the ip Command in Linux](https://www.learnlinux.tv/how-to-use-the-ip-command-in-linux-a-beginners-guide/) | Pause at the interface listing. Run the display commands in [Chapter 5](chapters/05-interfaces.md) and identify loopback and the interface used by your default route. |

## If you like learning through games

Two paid Steam games have similar names. Pick by what you want to practice. The free browser labs are enough to do the command exercises in this guide.

| Steam game | What the developer describes | Pair it with Linux |
| --- | --- | --- |
| [Data Center](https://store.steampowered.com/app/4170200/) | Place servers and switches in racks, connect Ethernet cables, and watch colored traffic move through the layout. | Follow one cable and name both endpoints. Then inspect the server side of a virtual connection in Chapter 5. |
| [Data Center Simulator](https://store.steampowered.com/app/4535710/) | Work through technician scenarios with cable connections, component replacements, VLAN setup, and terminal commands with simulated output. | Try a network scenario, then reproduce the interface and route checks in Ubuntu. The store describes a simulated terminal and doesn't document full Bash support. |

For a short session, do one of these pairings. A screenshot of the layout explains where you connected the cable. A terminal capture explains what Linux could see from one end.

## Pick one activity for this session

| If you want to see… | Start here | Evidence to keep |
| --- | --- | --- |
| A physical fault | [Rack ticket, with a free diagram or optional Steam game](visual/rack-ticket.md) | Both cable endpoints and the layer you verified after the fix |
| A packet exchange | [Same-subnet ping in Packet Tracer](visual/packet-walk.md) | ARP request and ICMP reply from one simulated network |
| A branch move | [Free browser game and local Git graph](visual/branch-map.md) | Two branch labels and the file content at each one |
| A process disappear | [Live timer and process viewer](chapters/04-processes.md#watch-one-timer-in-a-process-viewer) | The PID and the observation after the timer exits |

[Back to the chapters](README.md)
