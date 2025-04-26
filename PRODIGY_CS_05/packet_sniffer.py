from scapy.all import sniff, wrpcap, IP, TCP, UDP, ICMP
import argparse
import os
import ctypes
import logging
from datetime import datetime
import subprocess
import sys

# Suppress Scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

# Global stats counters
stats = {
    "total": 0,
    "tcp": 0,
    "udp": 0,
    "icmp": 0,
    "http": 0
}

packets = []

def show_banner():
    print(r"""
  _   _      _                      _        _   _             
 | \ | | ___| |___      _____  _ __| | _____ | \ | | _____      __
 |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ / _ \|  \| |/ _ \ \ /\ / /
 | |\  |  __/ |_ \ V  V / (_) | |  |   < (_) | |\  |  __/\ V  V / 
 |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\___/|_| \_|\___| \_/\_/  
=========================================================================                                                                 
      Ultimate Packet Sniffer – Developed by: Ayush Thakur (Hunter001x)
             GitHub: https://github.com/aayushthakur001
==========================================================================
    """)

def process_packet(packet, display_data=False, log_file=None):
    stats["total"] += 1
    packets.append(packet)

    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        if proto == 6:
            protocol = "TCP"
            stats["tcp"] += 1
        elif proto == 17:
            protocol = "UDP"
            stats["udp"] += 1
        elif proto == 1:
            protocol = "ICMP"
            stats["icmp"] += 1
        else:
            protocol = "Other"

        payload = bytes(packet[IP].payload)

        now = datetime.now()
        log_entry = f"Time: {now} Protocol: {protocol} Source: {src_ip} Destination: {dst_ip} Payload: {payload[:50]}..."
        print(f"\n[+] {log_entry}")
        
        if log_file:
            print(log_entry, file=log_file)

        # HTTP detection inside TCP payload
        if packet.haslayer(TCP):
            payload_text = str(payload)
            if "HTTP" in payload_text or "GET" in payload_text or "POST" in payload_text:
                stats["http"] += 1
                print(f"\n🌐 HTTP Payload Detected:\n{payload_text[:300]}...")
                if log_file:
                    print(f"HTTP Payload: {payload_text[:300]}...", file=log_file)

def main():
    show_banner()

    # Check for administrator privileges
    if os.name == 'nt':  # Windows
        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise SystemExit("Error: Permission denied. This application requires administrator privileges to run.")
    else:  # Unix-like systems
        if os.getuid() != 0:
            raise SystemExit("Error: Permission denied. This application requires administrator privileges to run.")

    # User input for interface, packet count, timeout, protocol filter, and log file
    net_iface = input("* Enter the interface on which to run the sniffer (e.g., 'eth0'): ")
    pkt_to_sniff = int(input("* Enter the number of packets to capture (0 for infinite): "))
    time_to_sniff = int(input("* Enter the number of seconds to run the capture: "))
    proto_sniff = input("* Enter the protocol to filter by (tcp|udp|icmp|0 for all): ")
    file_name = input("* Please give a name to the log file: ")

    # Open log file for writing
    log_file = open(file_name, "a")

    # Set interface to promiscuous mode
    try:
        subprocess.call(["ifconfig", net_iface, "promisc"], stdout=None, stderr=None, shell=False)
        print(f"\nInterface {net_iface} was set to PROMISC mode.\n")
    except:
        print("\nFailed to configure interface as promiscuous.\n")

    print("\n* Starting the capture...")

    try:
        sniff(
            iface=net_iface,
            count=pkt_to_sniff if pkt_to_sniff > 0 else None,
            timeout=time_to_sniff if time_to_sniff > 0 else None,
            filter=proto_sniff if proto_sniff != "0" else None,
            prn=lambda pkt: process_packet(pkt, display_data=True, log_file=log_file)
        )
    except KeyboardInterrupt:
        print("\n❌ Capture interrupted by user (CTRL+C)")

    # Close log file
    log_file.close()

    # Final stats
    print("\n📊 Capture Summary:")
    print(f"    - Total Packets Captured: {stats['total']}")
    print(f"    - TCP Packets: {stats['tcp']}")
    print(f"    - UDP Packets: {stats['udp']}")
    print(f"    - ICMP Packets: {stats['icmp']}")
    print(f"    - HTTP Packets Detected: {stats['http']}")
    print(f"\n* Please check the {file_name} file to see the captured packets.\n")

if __name__ == "__main__":
    main()
