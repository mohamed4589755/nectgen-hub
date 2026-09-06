import urllib.request
import json

url = "https://script.google.com/macros/s/AKfycbzlz-6eCzexIEdjU-jy4FFuZ7_boVgnlCpFwq7HndFIjyknxuY2TLK6hsXgglY9FT0l/exec"

data = {
    "name": "Direct Webapp Test Student",
    "email": "webapp_test@nextgen.dev",
    "phone": "01234567890",
    "university": "Cairo University, Faculty of Engineering",
    "track": "Data Analytics Internship"
}

encoded_data = json.dumps(data).encode("utf-8")

req = urllib.request.Request(
    url,
    data=encoded_data,
    headers={"Content-Type": "text/plain"},
    method="POST"
)

try:
    print("Sending direct POST payload to Apps Script Web App...")
    with urllib.request.urlopen(req, timeout=15) as response:
        # Note: Google Apps Script Web App redirects (HTTP 302) to another URL to return the response.
        # urllib handles redirects automatically.
        res_data = response.read().decode("utf-8")
        print("Response received from Apps Script:")
        print(res_data)
except Exception as e:
    print("Error during request:", e)
