import requests
import sys
import csv
from pathlib import Path
from typing import Optional

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

def normalize_row(ip: str, geo: dict) -> dict:
    return {
        "ip": ip,
        "city": geo.get("city"),
        "region": geo.get("region"),
        "country": geo.get("country_name"),
        "latitude": geo.get("latitude"),
        "longitude": geo.get("longitude"),
        "org": geo.get("org"),
        "timezone": geo.get("timezone"),
        "postal": geo.get("postal"),
    }

def save_csv(row: dict, path: Path):
    write_header = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if write_header:
            w.writeheader()
        w.writerow(row)

def format_geo(row: dict) -> str:
    loc = ", ".join([p for p in [row["city"], row["region"], row["country"]]if p])
    coords = f"{row['latitude']}, {row['longitude']}" if row["latitude"] is not None and row["longitude"] is not None else "Unknown"
    lines = [
        f"IP: {row['ip']}",
        f"Location: {loc or 'Unknown'}",
        f"Coordinates: {coords}",
    ]
    if row["org"]:
        lines.append(f"ISP/Org: {row['org']}")
    if row["timezone"]:
        lines.append(f"Timezone: {row['timezone']}")
    if row["postal"]:
        lines.append(f"Postal: {row['postal']}")
    return "\n".join(lines)

def main():
    try:
        ip = sys.argv[1] if len(sys.argv)>1 else get_public_ip()
        csv_path: Optional[Path] = Path(sys.argv[2]) if len(sys.argv)> 2 else None

        geo = get_geo(ip)
        row = normalize_row(ip, geo)
        print(format_geo(row))

        if csv_path:
            save_csv(row, csv_path)
            print(f"Saved to {csv_path.resolve()}")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()