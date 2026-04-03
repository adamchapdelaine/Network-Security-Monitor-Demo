#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

# IP envelope with ping request
p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()


