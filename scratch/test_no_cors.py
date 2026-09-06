import urllib.request
import json

url = "https://script.google.com/macros/s/AKfycbzlz-6eCzexIEdjU-jy4FFuZ7_boVgnlCpFwq7HndFIjyknxuY2TLK6hsXgglY9FT0l/exec"
data = {
    "name": "Test No-CORS TextPlain",
    "email": "nocors@test.com",
    "phone": "9876543210",
    "university": "Cairo University, Science",
    "track": "Data Analytics Internship"
}

# Sending as text/plain to simulate no-cors content-type override
req = urllib.request.Request(
    url, 
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "text/plain"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8")
        with open("scratch/nocors_response.txt", "w", encoding="utf-8") as f:
            f.write(html)
        print("CORS test finished. Response saved.")
except Exception as e:
    print("Error:", e)
