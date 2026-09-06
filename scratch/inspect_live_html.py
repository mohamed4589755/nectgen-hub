import urllib.request
import urllib.error

url = "https://mohamed4589755.github.io/nectgen-hub/internships.html"
headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
        print("HTML length:", len(html))
        # Search for GOOGLE_SHEET_WEBAPP_URL
        if "GOOGLE_SHEET_WEBAPP_URL" in html:
            idx = html.find("GOOGLE_SHEET_WEBAPP_URL")
            print("Found GOOGLE_SHEET_WEBAPP_URL at index", idx)
            print("Context:")
            print(html[idx-100:idx+250])
        else:
            print("GOOGLE_SHEET_WEBAPP_URL NOT FOUND in live page!")
except Exception as e:
    print("Error fetching:", e)
