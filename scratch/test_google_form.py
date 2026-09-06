import urllib.request
import urllib.parse

url = "https://docs.google.com/forms/d/e/1FAIpQLSdCA-mxNAnhtxBgmf0PnZGKLWqX1e495YEDBvAWUsLetZRY_A/formResponse"

# Map the exact entry IDs we extracted from the Form HTML metadata
data = {
    "entry.1171089655": "Antigravity Agent Test",
    "entry.46744813": "agent_form@nextgen.dev",
    "entry.1536865297": "01122334455",
    "entry.2072862761": "Alexandria University",
    "entry.389164000": "Faculty of Science"
}

# Encode to urlencoded format (matching browser form submissions)
encoded_data = urllib.parse.urlencode(data).encode("utf-8")

req = urllib.request.Request(
    url,
    data=encoded_data,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    method="POST"
)

try:
    print("Sending test submission to Google Form action endpoint...")
    with urllib.request.urlopen(req, timeout=15) as response:
        code = response.getcode()
        print("HTTP Status Code returned:", code)
        if code == 200:
            print("Submission accepted by Google Form! Row should be added to your Google Sheet.")
except Exception as e:
    print("Error during form submission:", e)
