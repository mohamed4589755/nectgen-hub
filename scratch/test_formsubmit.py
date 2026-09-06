import urllib.request
import json

url = "https://formsubmit.co/ajax/nextgeninstitute.careers@gmail.com"
data = {
    "name": "Live Verification Test",
    "email": "student@example.com",
    "subject": "Inquiry Test Post-Activation",
    "message": "Testing message delivery after clicking activation link.",
    "_captcha": "false"
}

req = urllib.request.Request(
    url,
    data=json.dumps(data).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Origin': 'https://nextgenhub.dev',
        'Referer': 'https://nextgenhub.dev/contact.html'
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        res_text = resp.read().decode('utf-8')
        print("RESPONSE:", res_text)
except urllib.error.HTTPError as e:
    print("HTTP ERROR:", e.code, e.read().decode('utf-8'))
except Exception as e:
    print("ERROR:", e)
