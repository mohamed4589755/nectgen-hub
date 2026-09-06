import re
import json

with open("scratch/form_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for the form action URL first
action_match = re.search(r'action="([^"]+/formResponse)"', html)
action_url = action_match.group(1) if action_match else "Not found"
print("Form Action URL:", action_url)

# Google Forms structure in FB_PUBLIC_LOAD_DATA_:
# It is a nested array. The questions and their entry IDs are stored inside it.
# We can find the FB_PUBLIC_LOAD_DATA_ script block
match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);\s*</script>', html)
if match:
    data_str = match.group(1)
    try:
        # Clean up some JS objects if necessary, but usually it's valid JSON
        # Let's parse it
        data = json.loads(data_str)
        # The structure is: data[1] contains list of form items
        items = data[1]
        print(f"Found {len(items)} items in the form:")
        for idx, item in enumerate(items):
            # item[1] is the title of the question
            # item[4] contains the nested list which has the entry ID
            title = item[1]
            try:
                # The entry ID is usually inside item[4][0][0]
                entry_id = item[4][0][0]
                print(f"Question {idx+1}: '{title}' -> entry.{entry_id}")
            except Exception as e:
                print(f"Question {idx+1}: '{title}' -> Entry ID structure not standard: {e}")
    except Exception as je:
        print("JSON parse failed, parsing using regex search...")
        # Fallback to regex search
        # Look for question titles and find the nearest entry number
        questions = ["الاسم الكامل", "البريد الإلكتروني", "رقم الهاتف", "الجامعة والكلية", "المسار المختار", 
                     "Full Name", "Email", "Phone", "University & College", "Track"]
        for q in questions:
            # Find index of question text
            pos = html.find(q)
            if pos != -1:
                # Look for numbers of 8-10 digits in the surrounding area
                surrounding = html[pos:pos+3000]
                entries = re.findall(r'(\d{9,10})', surrounding)
                print(f"Question '{q}' nearby entry IDs: {list(set(entries))}")
else:
    print("FB_PUBLIC_LOAD_DATA_ script block not found!")
