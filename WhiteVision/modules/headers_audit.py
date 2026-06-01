import requests

def headers_check(domain):

    url = f"https://{domain}"

    try:
        r = requests.get(url, timeout=10)

        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]

        for h in security_headers:

            if h in r.headers:
                print(f"[OK] {h}")
            else:
                print(f"[MISSING] {h}")

    except Exception as e:
        print(e)