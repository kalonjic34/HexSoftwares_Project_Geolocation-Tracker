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

def format_geo(geo: dict) -> str:
    city = geo.get("city")
    region = geo.get("region")
    country = geo.get("country_name")
    lat = geo.get("latitude")
    lon = geo.get("longitude")
    org = geo.get("org")
    tz = geo.get("timezone")
    postal = geo.get("postal")

    lines = []
    lines.append(f"IP: {geo.get('ip') or geo.get('ip_address') or 'unknown'}")
    loc = ", ".join([p for p in [city, region, country]if p])
    lines.append(f"Location: {loc or 'Unknown'}")
    coords = f"{lat}, {lon}" if lat is not None and lon is not None else"Unknown"
    lines.append(f"Coordinates: {coords}")
    if org: lines.append(f"ISP/Org: {org}")
    if tz: lines.append(f"Timezone: {tz}")
    if postal: lines.append(f"Postal: {postal}")
    return "\n".join(lines)

def main():
    try:
        ip = sys.argv[1] if len(sys.argv)>1 else get_public_ip()
        geo = get_geo(ip)
        geo["ip"] = ip
        print(format_geo(geo))
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()