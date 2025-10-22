import requests
IP_API = "https://api.ipify.org?format=json"

def get_public_ip() -> str:
    r = requests.get(IP_API, timeout=10)
    r.raise_for_status()
    return r.json().get("ip")

def main():
    ip = get_public_ip()
    print(ip)

if __name__ == "__main__":
    main()
