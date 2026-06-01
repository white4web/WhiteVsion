import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
    except Exception as e:
        print(e)