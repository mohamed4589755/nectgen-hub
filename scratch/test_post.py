import urllib.request
import json
import sys

url = "https://script.google.com/macros/s/AKfycbzlz-6eCzexIEdjU-jy4FFuZ7_boVgnlCpFwq7HndFIjyknxuY2TLK6hsXgglY9FT0l/exec"
data = {
    "name": "Test Student Python",
    "email": "test_py@test.com",
    "phone": "0123456789",
    "university": "Cairo University, Engineering",
    "track": "Data Analytics Internship"
}

req = urllib.request.Request(
    url, 
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    print("Sending POST request to Google Sheet Web App...")
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8")
        print("Response received:")
        print(html)
except Exception as e:
    print("Error:", e, file=sys.stderr)
