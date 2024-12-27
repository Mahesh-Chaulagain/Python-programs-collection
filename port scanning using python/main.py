# port scanning is common task in cybersecurity to identify open ports on a network

import socket

def port_scanner(target, ports):
    # get the IP address of the target
    coding = socket.gethostbyname(target)
    print(f"scanning {target} ({coding})")

    for port in ports:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((coding, port))
        if result == 0:
            print(f"Port {port}: Open")
        
        sock.close()

target = 'google.com'
ports = [22, 80, 443, 8080]
port_scanner(target, ports)
