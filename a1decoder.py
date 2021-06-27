from scapy.all import *

#!/bin/python3
from scapy.all import *
import argparse

parser=argparse.ArgumentParser(description='Pass args to Assignment 1')
parser.add_argument('sourceIP', metavar="sourceIP", type=str, help="Source IP")
parser.add_argument('destinationIP', metavar="destinationIP", type=str, help="Destination IP")
parser.add_argument('--dport', metavar="destinationPort", type=int, default=4443, help="Destination port (default 4443")


def main():
    args = parser.parse_args()
    print( args )

    pkts = sniff(filter="src " + args.sourceIp + " && tcp dst port " + args.destinationPort, \
                prn=lambda x:int(x[TCP].seq/16777216))


if __name__ == "__main__":
    main()
