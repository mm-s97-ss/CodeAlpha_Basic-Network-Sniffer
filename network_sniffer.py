# THIS SCRIPT IS FORMED BY MUHAMMAD SIDDIQUE.

# THIS SCRIPT IS USED FOR NETWORK SNIFFER.

# This script automate the Network Sniffer Task.


# One thing is important in the python scripts which is indentation.


from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):

    # Check if the packet contains an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_num = packet[IP].proto

        # Map protocol numbers to human-readable names
        protocol_name = "Other"
        if packet.haslayer(TCP):
            protocol_name = "TCP"
            
        elif packet.haslayer(UDP):
            protocol_name = "UDP"
            
        elif packet.haslayer(ICMP):
            protocol_name = "ICMP"

        print(f"\n[+] {protocol_name} Packet: {src_ip} -> {dst_ip}")

        # Display details of port (if available)
        
        if packet.haslayer(TCP):
            print(f"    Src Port: {packet[TCP].sport} | Dst Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    Src Port: {packet[UDP].sport} | Dst Port: {packet[UDP].dport}")

        # Display Payload Data (if present)
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            # Truncate payload output to keep logs clean
            print(f"    Payload: {payload[:50]!r}")

def main():
    print("Starting Packet Sniffer... Press Ctrl+C to stop.")
    # 'prn' specifies the callback function for every captured packet
    # 'store=0' prevents holding captured packets in memory
    sniff(prn=process_packet, store=0)

if __name__ == "__main__":
    main()