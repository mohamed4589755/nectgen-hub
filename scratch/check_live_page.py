import urllib.request

url = "https://mohamed4589755.github.io/nectgen-hub/styles.css"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as response:
        css_content = response.read().decode('utf-8')
    
    # Check variables
    if "--accent-blue: #1663d9;" in css_content:
        print("SUCCESS: Deployed CSS contains the new blue color #1663d9!")
    else:
        print("WARNING: Deployed CSS does NOT contain the new blue color yet.")
        # Print root variables
        start_idx = css_content.find(":root {")
        if start_idx != -1:
            print(css_content[start_idx:start_idx+300])
except Exception as e:
    print(f"Error fetching CSS: {e}")
