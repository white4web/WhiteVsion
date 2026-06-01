from modules.dns_audit import dns_lookup
from modules.tls_audit import tls_check
from modules.headers_audit import headers_check
from modules.tech_audit import detect_tech

def banner():
    print(r"""
██╗    ██╗██╗  ██╗██╗████████╗███████╗
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝
██║ █╗ ██║███████║██║   ██║   █████╗
██║███╗██║██╔══██║██║   ██║   ██╔══╝
╚███╔███╔╝██║  ██║██║   ██║   ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝

        WhiteVision v1.0
""")

banner()

domain = input("Target Domain: ").strip()

print("\n[+] DNS Audit")
dns_lookup(domain)

print("\n[+] TLS Audit")
tls_check(domain)

print("\n[+] Header Audit")
headers_check(domain)

print("\n[+] Technology Audit")
detect_tech(domain)