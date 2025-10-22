# 🌍 HexSoftwares Project - Geolocation Tracker

A simple and powerful **Python-based IP Geolocation Tracker** that identifies your **public IP address**, fetches detailed **location data**, and can visualize it on an interactive **map (HTML)** using [Folium](https://python-visualization.github.io/folium/).

You can also export the data to a CSV file for logging or analysis.

---

## 🚀 Features

| Feature | Description |
|----------|-------------|
| 🌐 Auto-detect Public IP | Fetches your current public IP automatically. |
| 🗺️ IP Geolocation Lookup | Retrieves detailed info such as city, region, country, ISP, and coordinates. |
| 🧭 Interactive Map | Generates a `map.html` file with your location pinned. |
| 📄 CSV Logging | Append geolocation results to a `.csv` file for later use. |
| ⚙️ CLI Options | Flexible command-line arguments for automation. |

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/kalonjic34/HexSoftwares_Project_Geolocation-Tracker.git
cd HexSoftwares_Project_Geolocation-Tracker
````

2. Install dependencies:

```bash
pip install requests folium
```

---

## 🧪 Usage

### 🟢 Basic Usage (Your Own IP)

```bash
python geolocation_tracker.py
```

This will:

* Detect your **public IP**
* Display location info in the terminal
* Generate an interactive map (`map.html`)
* Automatically open it in your browser

---

### 🔍 Lookup a Specific IP Address

```bash
python geolocation_tracker.py 8.8.8.8
```

Output example:

```
IP: 8.8.8.8
Location: Mountain View, California, United States
Coordinates: 37.386, -122.0838
ISP/Org: Google LLC
Timezone: America/Los_Angeles
Postal: 94035
Saved map to map.html
```

---

### 💾 Save Results to CSV

```bash
python geolocation_tracker.py 8.8.8.8 --csv results.csv
```

Creates or appends to `results.csv`:

| ip      | city          | region     | country       | latitude | longitude | org        | timezone            | postal |
| ------- | ------------- | ---------- | ------------- | -------- | --------- | ---------- | ------------------- | ------ |
| 8.8.8.8 | Mountain View | California | United States | 37.386   | -122.0838 | Google LLC | America/Los_Angeles | 94035  |

---

### 🗺️ Disable Map Generation

```bash
python geolocation_tracker.py --no-map
```

Skips generating or opening `map.html`.

---

## ⚙️ Command-Line Options

| Argument     | Description                                                   | Example          |
| ------------ | ------------------------------------------------------------- | ---------------- |
| `ip`         | IP address to look up (optional). Defaults to your public IP. | `8.8.8.8`        |
| `--csv PATH` | Save results to a CSV file.                                   | `--csv logs.csv` |
| `--no-map`   | Disable map generation and browser opening.                   | `--no-map`       |

---

## 🧱 Project Structure

```
HexSoftwares_Project_Geolocation-Tracker/
│── geolocation_tracker.py   # Main script
│── README.md                # Documentation (this file)
│── map.html (generated)     # Interactive map output
│── results.csv (optional)   # CSV log file (if used)
```

---

## 📜 Dependencies

* **Python 3.8+**
* [requests](https://pypi.org/project/requests/)
* [folium](https://pypi.org/project/folium/)

Install them all at once:

```bash
pip install -r requirements.txt
```

> (If no `requirements.txt` file exists, you can manually install the libraries.)

---

## 🧠 How It Works

1. Retrieves your IP via [ipify API](https://api.ipify.org).
2. Uses [ipapi.co](https://ipapi.co/) to get geolocation info.
3. Normalizes data into a consistent structure.
4. Displays results in terminal, saves optional CSV, and generates `map.html`.

---

## 🧭 Example Output

```
IP: 102.133.55.21
Location: Johannesburg, Gauteng, South Africa
Coordinates: -26.2041, 28.0473
ISP/Org: Vodacom
Timezone: Africa/Johannesburg
Postal: 2000
Saved map to map.html
```

---

## 🛠️ Future Enhancements

* [ ] Reverse IP lookup for domains
* [ ] Batch IP processing from file
* [ ] IP reputation scoring
* [ ] Custom map themes and layers

---

## 📜 License

This project is currently **unlicensed**.
You can request me to add an **MIT License** for open use and contribution.

---

Built with ❤️ by **[@kalonjic34](https://github.com/kalonjic34)**
Part of the **HexSoftwares Project Series** 🌐

```
