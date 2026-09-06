import urllib.request
import re

url = "https://docs.google.com/spreadsheets/d/14IL5ncCQCYAtGpcjVGoTUQIyVQoZyfscUmhLT9WSRCs/edit?usp=sharing"
headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
        print("Sheet page fetched. Length:", len(html))
        # Search for sheet names or grid names
        # Google Sheets uses JSON data structure containing sheetNames inside the page source
        matches = re.findall(r'"sheetName"\s*:\s*"([^"]+)"', html)
        if matches:
            print("Found sheet tabs:")
            for m in set(matches):
                print("-", m)
        else:
            # Fallback search for sheet metadata
            matches_alt = re.findall(r'name\s*:\s*"([^"]+)"\s*,\s*sheetId', html)
            if matches_alt:
                print("Found tabs (alt):")
                for m in set(matches_alt):
                    print("-", m)
            else:
                print("No sheet tab names found in HTML source.")
except Exception as e:
    print("Error:", e)
