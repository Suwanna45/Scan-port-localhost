import socket

def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        return s.connect_ex((host, port)) == 0
    finally:
        s.close()

def main():
    host = "127.0.0.1"
    print("==================")
    print("Host :", host)

    try:
        port = int(input("Entrez un numéro de port à scanner : "))
        if port < 0 or port > 65535: #la limite des ports
            raise ValueError
    except ValueError:
        print("❌ Numéro de port invalide")
        return

    if scan_port(host, port):
        print(f"Port {port} : OUVERT")
    else:
        print(f"Port {port} : FERMÉ")

if __name__ == "__main__":
    main()