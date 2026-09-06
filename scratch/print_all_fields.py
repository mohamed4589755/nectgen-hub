import re
import ast

with open("scratch/form_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);\s*</script>', html)
if match:
    data_str = match.group(1)
    data_str = data_str.replace("null", "None").replace("true", "True").replace("false", "False")
    
    try:
        data = ast.literal_eval(data_str)
        # In Google Forms metadata:
        # data[1][1] contains the list of all form elements/questions
        form_elements = data[1][1]
        print(f"Total elements found: {len(form_elements)}")
        for idx, elem in enumerate(form_elements):
            if not elem or len(elem) < 2 or not elem[1]:
                continue
            title = elem[1]
            elem_type = elem[3] # 0 = text, 1 = paragraph, 2 = multiple choice, etc.
            entry_id = "None"
            try:
                entry_id = elem[4][0][0]
            except Exception:
                pass
            print(f"{idx+1}. Question Title: '{title}' (Type: {elem_type}) -> entry.{entry_id}")
    except Exception as e:
        print("Error evaluating JS data:", e)
else:
    print("Could not find data block")
