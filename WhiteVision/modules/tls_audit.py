import ssl
import socket

def tls_check(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock,
                                     server_hostname=domain) as ssock:

                print("TLS Version:", ssock.version())

    except Exception as e:
        print(e)