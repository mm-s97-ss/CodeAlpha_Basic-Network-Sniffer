# Network Sniffer

A Python-based network packet sniffer using Scapy that automates network monitoring and packet analysis.

**Author:** Muhammad Siddique

## Features

- 📡 Captures and analyzes network packets in real-time
- 🔍 Supports TCP, UDP, and ICMP protocols
- 🎯 Displays source/destination IPs and ports
- 📦 Shows payload data (truncated for readability)
- ⚙️ Efficient packet processing with minimal memory overhead

## Requirements

- Python 3.x
- Scapy 2.4.5+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mm-s97-ss/network-sniffer.git
cd network-sniffer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with elevated privileges (required for packet sniffing):

```bash
sudo python3 network_sniffer.py
```

Press `Ctrl+C` to stop the packet sniffer.

## Example Output

```
Starting Packet Sniffer... Press Ctrl+C to stop.

[+] TCP Packet: 192.168.1.100 -> 8.8.8.8
    Src Port: 54321 | Dst Port: 443
    Payload: b'\x16\x03\x01\x00\xa5\x01\x00\x00\xa1...'

[+] UDP Packet: 192.168.1.100 -> 1.1.1.1
    Src Port: 53891 | Dst Port: 53
```

## Important Notes

- **Administrator/Root Access Required:** Packet sniffing requires elevated system privileges
- **Python Indentation:** Ensure proper indentation when modifying the script
- **Memory Efficient:** Uses `store=0` to prevent storing captured packets in memory

## License

MIT License

---

For questions or contributions, feel free to open an issue or pull request!