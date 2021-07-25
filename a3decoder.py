#!/bin/python3
from scapy.all import *
import base64
import argparse

parser=argparse.ArgumentParser(description='Pass args to Assignment 1')
parser.add_argument('sourceIP', metavar="sourceIP", type=str, help="Source IP")
parser.add_argument('destinationIP', metavar="destinationIP", type=str, help="Destination IP")
parser.add_argument('--dport', metavar="destinationPort", type=int, default=4443, help="Destination port (default 4443")


def main():
    args = parser.parse_args()
    print( args )

    pkts = sniff(filter="src " + args.sourceIP + \
                " && dst " + args.destinationIP + \
                " && tcp dst port " + str(args.dport), \
                prn=lambda x: base64.b64decode(x[DNS].qd.qname.split(".", 1)[0]).decode())


if __name__ == "__main__":
    main()
