import requests

def detect_tech(domain):

    try:
        r = requests.get(f"https://{domain}",
                         timeout=10)

        server = r.headers.get("Server", "Unknown")

        print("Server:", server)

        powered = r.headers.get(
            "X-Powered-By",
            "Not Disclosed"
        )

        print("X-Powered-By:", powered)

    except Exception as e:
        print(e)