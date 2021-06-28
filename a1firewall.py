#!/bin/python3
from scapy.all import *
import argparse
import time

parser=argparse.ArgumentParser(description='Pass args to Assignment 1')
parser.add_argument('sourceIP', metavar="sourceIP", type=str, help="Source IP")
parser.add_argument('destinationIP', metavar="destinationIP", type=str, help="Destination IP")
parser.add_argument('--dport', metavar="destinationPort", type=int, default=4443, help="Destination port (default 4443")

isn = []
deltaISN = []
wait = 0

def main():
    args = parser.parse_args()
    print( args )

    pkts = sniff( filter="src " + args.sourceIP + \
                " && dst " + args.destinationIP + \
                " && tcp dst port " + str(args.dport), \
                prn=process_packet )
    

def process_packet(packet):
    
    global isn
    global deltaISN
    global wait

    print(f"{len(isn)}")
    print(f"{len(deltaISN)}")
    
    isn.append(packet[TCP].seq)

    if len(isn) > 1:
        print(f"Debug: appending {abs(isn[-1] - isn[-2])} to delta." )
        deltaISN.append(abs(isn[-1] - isn [-2]))
    
    if len(deltaISN) > 5:
        print("Debug: trimming delta to 5")
        deltaISN = deltaISN[1:]
    
        if sum(deltaISN) / len(deltaISN) > 100:
            print("Unusual gap between ISNs detected. Throttling connection.")
            wait = 5
    
    time.sleep(wait)

    sendp(packet)


if __name__ == "__main__":
    main()
