import sys
from scapy.all import rdpcap, IP, TCP, Raw


if len(sys.argv) != 2:
    print("Usage: python scripts/pcap_http_summary.py <pcap_file>")
    sys.exit()


pcap_file = sys.argv[1]
packets = rdpcap(pcap_file)

print("PCAP HTTP Summary")
print("=" * 50)
print(f"Total packets: {len(packets)}")
print("=" * 50)

found_http = 0

for number, packet in enumerate(packets, start=1):
    if IP not in packet or TCP not in packet or Raw not in packet:
        continue

    data = bytes(packet[Raw].load).decode("utf-8", errors="ignore")

    if data.startswith(("GET", "POST", "HEAD")):
        found_http += 1

        lines = data.splitlines()
        request_line = lines[0]

        host = "-"
        user_agent = "-"

        for line in lines:
            if line.lower().startswith("host:"):
                host = line.split(":", 1)[1].strip()

            if line.lower().startswith("user-agent:"):
                user_agent = line.split(":", 1)[1].strip()

        print(f"Packet #{number}")
        print("Type: HTTP Request")
        print(f"Request: {request_line}")
        print(f"Host: {host}")
        print(f"User-Agent: {user_agent}")
        print(f"Source: {packet[IP].src}:{packet[TCP].sport}")
        print(f"Destination: {packet[IP].dst}:{packet[TCP].dport}")
        print("-" * 50)

    elif data.startswith("HTTP/"):
        found_http += 1

        status_line = data.splitlines()[0]

        print(f"Packet #{number}")
        print("Type: HTTP Response")
        print(f"Status: {status_line}")
        print(f"Source: {packet[IP].src}:{packet[TCP].sport}")
        print(f"Destination: {packet[IP].dst}:{packet[TCP].dport}")
        print("-" * 50)


if found_http == 0:
    print("No HTTP packets found.")
else:
    print(f"Detected HTTP packets: {found_http}")