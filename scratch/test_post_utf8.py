import urllib.request
import urllib.error
import json

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
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8")
        with open("scratch/response_out.txt", "w", encoding="utf-8") as f:
            f.write("Success! Response:\n")
            f.write(html)
        print("Success! Written to scratch/response_out.txt")
except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8")
    with open("scratch/response_out.txt", "w", encoding="utf-8") as f:
        f.write(f"HTTPError: {e.code} - {e.reason}\n")
        f.write("Error body:\n")
        f.write(err_body)
    print("HTTPError! Written to scratch/response_out.txt")
except Exception as e:
    with open("scratch/response_out.txt", "w", encoding="utf-8") as f:
        f.write(f"Exception: {str(e)}\n")
    print("General Exception! Written to scratch/response_out.txt")
