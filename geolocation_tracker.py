import requests
import sys

IP_API = "https://api.ipify.org?format=json"
GEO_API = "https://ipapi.co/{ip}/json/"

def get_public_ip() -> str:
    r = requests.get(IP_API, timeout=10)
    r.raise_for_status()
    return r.json()["ip"]

def get_geo(ip: str) -> dict:
    r = requests.get(GEO_API.format(ip=ip), timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    ip = sys.argv[1] if len(sys.argv) > 1 else get_public_ip()
    geo = get_geo(ip)
    print(geo)

if __name__ == "__main__":
    main()