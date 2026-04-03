#! /usr/bin/env python

import sys
from scapy.all import IP, ICMP, AsyncSniffer, send

# sniffing packets from interface asynchronously, filtering only ICMP packets 
captured_packets = AsyncSniffer(count=10, iface='VirtualBox Host-Only Ethernet Adapter', filter='icmp')
captured_packets.start()

# testing network traffic by sending a ping request to iface
ping_request = send(IP(dst='192.168.56.101')/ICMP())

# stopping the sniffer and showing the captured packets
captured_packets.stop()
captured_packets.results[1].show()

