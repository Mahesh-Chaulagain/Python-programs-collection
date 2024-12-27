from scapy.all import IP, ICMP, sr1

def ping(host):
    packet = IP(dst=host)/ICMP()  # Create IP packet with ICMP (ping) payload
    response = sr1(packet, timeout=2, verbose=0)  # Send packet and wait for a response (or timeout after 2 seconds)
    if response:
        return f"{host} is online"  # If response received, host is online
    else: 
        return f"{host} is offline"  # If no response received, host is offline
    
host_to_scan = "google.com"
result = ping(host_to_scan)
print(result)
