#!/bin/python3
from scapy.all import *
import argparse

parser=argparse.ArgumentParser(description='Pass args to Assignment 1')
parser.add_argument('sourceIP', metavar="sourceIP", type=str, help="Source IP")
parser.add_argument('destinationIP', metavar="destinationIP", type=str, help="Destination IP")
parser.add_argument('plaintext', metavar="plaintext", type=str, help="Covert message")
parser.add_argument('--dport', metavar="destinationPort", type=int, default=4443, help="Destination port (default 4443")

def encodeText(plaintext):
    return ord(plaintext) * 16777216


def main():
    
    args = parser.parse_args()
    print( args )

    for element in args.plaintext:
        send(Ether()/IP(src=args.sourceIP, dst=args.destinationIP)/TCP(seq=encodeText(element),dport=args.dport))

if __name__ == "__main__":
    main()