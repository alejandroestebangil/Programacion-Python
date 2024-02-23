import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection attempt
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter starting port number: "))
    end_port = int(input("Enter ending port number: "))

    print(f"Scanning ports {start_port} to {end_port} on {target_ip}...")
    open_ports = scan_ports(target_ip, start_port, end_port)
    if len(open_ports) == 0:
        print("No open ports found.")
    else:
        print("Open ports:", open_ports)

if __name__ == "__main__":
    main()
