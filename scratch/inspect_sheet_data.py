import urllib.request

# Export Google Sheet as CSV directly
sheet_id = "14IL5ncCQCYAtGpcjVGoTUQIyVQoZyfscUmhLT9WSRCs"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(url, headers=headers)

try:
    print("Fetching Google Sheet CSV export...")
    with urllib.request.urlopen(req, timeout=10) as response:
        csv_data = response.read().decode("utf-8")
        print("\n--- GOOGLE SHEET FIRST TAB CONTENTS ---")
        lines = csv_data.splitlines()
        print(f"Total rows found: {len(lines)}")
        for idx, line in enumerate(lines[:15]):  # Show first 15 lines
            print(f"Row {idx+1}: {line}")
        print("---------------------------------------\n")
except Exception as e:
    print("Error fetching sheet data:", e)
