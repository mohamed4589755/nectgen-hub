keywords = ["Name", "Email", "Phone", "University", "College", "Track", "Internship", "الاسم", "الايميل", "الكلية", "الجامعة"]

with open("scratch/tally_raw.html", "r", encoding="utf-8") as f:
    body = f.read().lower()

print("Tally Form Keywords Analysis:")
for kw in keywords:
    if kw.lower() in body:
        print(f"- '{kw}': Found")
    else:
        print(f"- '{kw}': Not Found")
