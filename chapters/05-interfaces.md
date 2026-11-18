# 5. Follow a cable to a Linux interface

Picture a server with an Ethernet cable running from its network adapter to port 7 on a switch. On the server, Linux might call the adapter's interface `enp1s0`. On the switch, the jack might be labeled “7.” Those labels belong to opposite ends of the cable. To document the connection, record both.

| Term | Where you encounter it | What it tells you |
| --- | --- | --- |
| Network interface controller (NIC) | A server's Ethernet adapter | The hardware that connects the server to a network. A VM can also have a virtual NIC. |
| Interface | A name in Linux such as `enp1s0` | The network connection the OS can inspect. `lo` is loopback and stays within the host. |
| Switch port | A numbered jack on a switch | Where the cable terminates at the switch. A port's link light can help you trace a connection. |
| Carrier | The link signal an Ethernet interface detects | A reported carrier is evidence of a link. You still need to check addressing and routing. |
| Default gateway | The next hop on a default route | Where traffic goes when no more specific route matches. |

## Lab: read a host's view of the connection

Use an Ubuntu VM or the [Ubuntu playground](../practice.md). These commands display the configuration. Keep the same terminal open. In a hosted playground or WSL, the interface you see is typically virtual.

```bash
ip -brief link
ip -brief address
ip route show default
```

1. In the first output, look for an interface besides `lo`. Write down its exact name and reported state. A loopback state of UNKNOWN is common.
2. Find the same name in the address output. Record its IPv4 address and prefix length, if one is assigned. The number after the slash is the prefix length.
3. In the default route, read the name after `dev` and the gateway after `via`, if present. If the command prints nothing, record “no IPv4 default route shown.” That alone doesn't tell you whether a cable is plugged in.

**Try it with two possible outcomes.** The following is sample output from a fictional lab. Read it if your sandbox restricts the network commands, or use it after checking your own output.

| Observation | Before | After |
| --- | --- | --- |
| Adapter flags from `ip link` | `<BROADCAST,MULTICAST,UP,LOWER_UP>` | `<NO-CARRIER,BROADCAST,MULTICAST,UP>` |
| Cable check | Both ends seated | Server end unplugged |

**What changed?** The adapter stayed administratively enabled (`UP`). The disappearance of `LOWER_UP` and appearance of `NO-CARRIER` fit the observed loss of the physical link. If the flags stayed the same but the host lost its default route, the route table would be the next place to investigate.

**Optional physical exercise.** On a spare Linux computer with a wired adapter, use its local keyboard and screen. Connect a spare Ethernet cable to your own powered switch. Run `ip monitor link`, unplug only that practice cable, reconnect it, then press Ctrl+C. Watch for the interface name in both events. Compare its flags before and after. On a shared network, a remote session, or a computer with Wi-Fi only, use the sample above.

**Portfolio note.** Draw the two cable endpoints and label them. Underneath, include one observation from your own terminal and one thing the output can't establish, such as the physical switch port number. Mark a VM diagram as virtual.

[Previous: processes](04-processes.md) · [Chapter 5 cards](../review/README.md#chapter-5) · [Practice resources](../practice.md)
