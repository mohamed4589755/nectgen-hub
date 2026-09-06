import re
import ast

with open("scratch/form_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the FB_PUBLIC_LOAD_DATA_ block
match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);\s*</script>', html)
if match:
    data_str = match.group(1)
    
    # Pre-process JavaScript literals to Python literals
    data_str = data_str.replace("null", "None")
    data_str = data_str.replace("true", "True")
    data_str = data_str.replace("false", "False")
    
    try:
        # Safely evaluate the literal string as a Python list
        data = ast.literal_eval(data_str)
        questions_list = data[1][1] # data[1] contains list of form items
        
        print("Google Form Fields Extracted:")
        for q in questions_list:
            if not q or len(q) < 5 or not q[1]:
                continue
            title = q[1]
            try:
                # The input entry ID is inside q[4][0][0]
                entry_id = q[4][0][0]
                print(f"- '{title}' -> entry.{entry_id}")
            except Exception:
                print(f"- '{title}' -> Entry ID not found")
    except Exception as e:
        print("Evaluation failed:", e)
else:
    print("Could not find data block")
