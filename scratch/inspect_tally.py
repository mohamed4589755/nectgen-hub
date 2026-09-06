import urllib.request
import re

url = "https://tally.so/r/obaeoN"
headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        html = response.geturl()
        print("Tally URL resolves to:", html)
        
        # Download public Tally form HTML
        req2 = urllib.request.Request(html, headers=headers)
        with urllib.request.urlopen(req2) as response2:
            body = response2.read().decode("utf-8")
            print("Tally Form downloaded. Length:", len(body))
            
            # Save raw HTML for inspection
            with open("scratch/tally_raw.html", "w", encoding="utf-8") as f:
                f.write(body)
            
            # Search for labels or input names
            # Tally renders as a react-based page. The questions list is stored inside window.__INITIAL_STATE__
            state_match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(.*?);\s*</script>', body)
            if state_match:
                print("Found Tally state data!")
                # Let's search for typical labels in the state string
                keywords = ["Name", "Email", "Phone", "University", "College", "Track", "Internship"]
                for kw in keywords:
                    if kw.lower() in body.lower():
                        print(f"Keyword '{kw}' found in form source.")
                    else:
                        print(f"Keyword '{kw}' NOT found.")
            else:
                print("Tally state data block not found.")
except Exception as e:
    print("Error:", e)
