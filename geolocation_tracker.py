import sys
import requests
import argparse
from pathlib import Path
import webbrowser

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
    import csv
    write_header = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if write_header:
            w.writeheader()
        w.writerow(row)

def make_map(lat: float, lon: float, label: str, outfile: Path) -> Path:
    try:
        import folium
    except ImportError:
        raise SystemExit("folium not installed. Run: pip install folium")
    m = folium.Map(location=[lat, lon], zoom_start=12, tiles="OpenStreetMap")
    folium.Marker([lat, lon], tooltip="Location", popup=label).add_to(m)
    m.save(outfile.as_posix())
    return outfile

def print_row(row: dict):
    loc = ", ".join([p for p in [row["city"], row["region"], row["country"]] if p])
    coords = f"{row['latitude']}, {row['longitude']}" if row["latitude"] is not None and row["longitude"] is not None else "Unknown"
    print(f"IP: {row['ip']}")
    print(f"Location: {loc or 'Unknown'}")
    print(f"Coordinates: {coords}")
    if row["org"]:
        print(f"ISP/Org: {row['org']}")
    if row["timezone"]:
        print(f"Timezone: {row['timezone']}")
    if row["postal"]:
        print(f"Postal: {row['postal']}")

def parse_args(argv):
    p = argparse.ArgumentParser(description="Geolocation Tracker (IP-based)")
    p.add_argument("ip", nargs="?", help="IP address to look up (default: your public IP)")
    p.add_argument("--csv", metavar="PATH", help="Append result to CSV file")
    p.add_argument("--no-map", action="store_true", help="Do not generate/open map")
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    try:
        ip = args.ip or get_public_ip()
        geo = get_geo(ip)
        row = normalize_row(ip, geo)
        print_row(row)

        if args.csv:
            save_csv(row, Path(args.csv))
            print(f"Saved CSV to {Path(args.csv).resolve()}")

        lat, lon = row["latitude"], row["longitude"]
        if not args.no_map and lat is not None and lon is not None:
            outfile = Path("map.html")
            label = f"{row['ip']} — {', '.join([p for p in [row['city'], row['region'], row['country']] if p])}"
            make_map(float(lat), float(lon), label, outfile)
            print(f"Saved map to {outfile.resolve()}")
            webbrowser.open(outfile.resolve().as_uri())
        elif not args.no_map:
            print("No coordinates available; map not created.")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()