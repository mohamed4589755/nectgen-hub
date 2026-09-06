import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# A regex to match emoji characters (Unicode ranges)
emoji_pattern = re.compile(
    "["
    "\U0001f600-\U0001f64f"  # Emoticons
    "\U0001f300-\U0001f5ff"  # Misc Symbols and Pictographs
    "\U0001f680-\U0001f6ff"  # Transport and Map Symbols
    "\U0001f1e0-\U0001f1ff"  # Regional Flags
    "\u2700-\u27bf"          # Dingbats
    "\u2600-\u26ff"          # Misc Symbols
    "\u2b50"                 # Star
    "]+", flags=re.UNICODE
)

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all emojis in the HTML
    matches = emoji_pattern.findall(content)
    # Filter out common stuff or show them
    if matches:
        print(f"{filepath} emojis: {set(matches)}")

    # Check for other places with class contain 'icon'
    icon_tags = re.findall(r'<[^>]*class="[^"]*icon[^"]*"[^>]*>(.*?)</[^>]*>', content)
    if icon_tags:
        # Clean tags from inside
        clean_tags = [re.sub(r'<[^>]+>', '', t).strip() for t in icon_tags]
        clean_tags = [t for t in clean_tags if t]
        print(f"{filepath} icon tags text: {clean_tags}")
