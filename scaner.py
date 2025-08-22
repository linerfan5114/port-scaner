import socket

def port_scanner(target):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target.")
        return

    print(f"Scanning target: {target} ({ip})")
    for port in range(0, 65536):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            break
        except socket.error:
            print("Could not connect to target.")
            break

if __name__ == "__main__":
    target_input = input("Enter target (IP or URL (in url dont use https)): ")
    port_scanner(target_input)
