import urllib.request
import re

short_url = "https://forms.gle/mvW6b1XRHeaVdMQs8"
headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(short_url, headers=headers)

try:
    print("Resolving shortlink...")
    with urllib.request.urlopen(req) as response:
        full_url = response.geturl()
        print("Full URL resolved to:", full_url)
        
        # Now fetch the HTML of the full URL
        req2 = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req2) as response2:
            html = response2.read().decode("utf-8")
            print("Form HTML downloaded. Length:", len(html))
            
            # Save raw HTML to file for examination
            with open("scratch/form_raw.html", "w", encoding="utf-8") as f:
                f.write(html)
            
            # Find the formResponse URL
            action_match = re.search(r'action="([^"]+/formResponse)"', html)
            if action_match:
                print("Found Form Action URL:", action_match.group(1))
            else:
                print("Form Action URL not found directly, trying fallback...")
            
            # Search for entry IDs inside JavaScript data block (FB_PUBLIC_LOAD_DATA_)
            # Google Forms stores form questions metadata in a variable called FB_PUBLIC_LOAD_DATA_
            public_data_match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);</script>', html)
            if public_data_match:
                print("Found FB_PUBLIC_LOAD_DATA_ metadata block!")
                # Let's inspect names and IDs
                # General regex to extract entry numbers e.g. [,[[123456789,
                entries = re.findall(r'(\d{8,12})', html)
                print("Possible entry IDs found:", list(set(entries)))
            else:
                print("FB_PUBLIC_LOAD_DATA_ block not found.")
                
except Exception as e:
    print("Error:", e)
