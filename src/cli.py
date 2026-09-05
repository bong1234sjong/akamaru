from scapy.all import *
from scapy.all import PcapReader
import argparse
import logging
import sys
from pathlib import Path
import os

def main():

    parser = argparse.ArgumentParser(
        prog="akamaru",
        description="CLI Network Packet Analyzer and Capturer",
        epilog="Give a treat to %(prog)s!",
    )

    subparsers = parser.add_subparsers(dest='command')
    parser.add_argument("--version", action="version", version="%(prog)s 0.0.1")

    # LOAD
    load = subparsers.add_parser('load', help='Load and analyze pcap files')
    load.add_argument("filename",
                        type=Path,
                        metavar="FILE",
                        help="Path to pcap file"
    )

    #Capture
    capture = subparsers.add_parser('capture', help="Capture packets")
    capture.add_argument("count",
                        type=int,
                        metavar="COUNT",
                        help="Number of packets to capture"
    )
    capture.add_argument("filename",
                        type=str,
                        metavar="FILENAME",
                        help="Name of output file"
    )


    # Should have -a for automation analysis, for checking against pre determined rules, or -m manual packet checking

    args = parser.parse_args()

    def checkFile(pcap: Path):
        extensions = ('.pcapng', '.pcap')
        if not (pcap.is_file() and pcap.suffix in extensions):
            raise ValueError("Please provide a Pcap File")

    if (args.command == 'load'):
        pcapfile = args.filename
        try:
            checkFile(pcapfile)
            packets = PcapReader(str(pcapfile))
            for packet in packets:
                packet.show()  
        except (ValueError, FileNotFoundError, Scapy_Exception) as err:
            print(err)
            sys.exit(1)
    elif (args.command == 'capture'):
        print(args)
        capture = sniff(count=args.count)
        wrpcap(args.filename, capture)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

#Capture
# sniff has a prn that allows to pass a function that executes with each packet sniffed, could make it so, sniff
# packets into direct analysis of that package afterwards




