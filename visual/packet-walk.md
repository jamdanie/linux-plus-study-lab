# Watch a same-subnet ping

Use two PCs and one 2960 switch in [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer). Connect each PC's Ethernet interface to its own switch port with a copper straight-through cable. Give PC-A 192.0.2.10 and PC-B 192.0.2.20, both with mask 255.255.255.0. Leave the gateways blank. Both hosts are on the same subnet.

1. Wait for the links to come up. Switch to Simulation mode and use the event filters to show ARP and ICMP.
2. From PC-A's Desktop → Command Prompt, enter `ping 192.0.2.20`. Use Capture/Forward to step through events. With a fresh topology, look for the broadcast asking who owns .20 and the reply from PC-B.
3. Run the ping again while the address mapping is cached. Compare the event types. If the first run also omitted ARP, inspect the existing mapping with `arp -a` on PC-A.
4. On a separate Ubuntu terminal, run `ip neigh show`. This displays the Linux host's own neighbor table. An empty table is a possible result. The simulated .20 host belongs to the Packet Tracer network.

**Pass check.** Explain why PC-A needed a destination MAC address and why the exchange could succeed with an empty gateway field. Save one screenshot of the ARP request and one of the ICMP reply. Label each with the question it answers.

[Trace a cable](rack-ticket.md) · [Linux interface walkthrough](../chapters/05-interfaces.md)

## Predict which device answers ARP

Keep the original two-PC topology. On paper, move PC-B to 198.51.100.20/24 and give PC-A a reachable gateway on its own subnet. For an off-subnet destination, PC-A needs the gateway's MAC address for the first hop. The final IP destination remains PC-B. Compare that prediction with your original same-subnet capture, where PC-B answered directly. A functioning routed topology would also need a router and return path.
