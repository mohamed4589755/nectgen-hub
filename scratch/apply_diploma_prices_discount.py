with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

# Replace English prices
js = js.replace('diploma_cost_ai: "8000 EGP",', 'diploma_cost_ai: "6000 EGP",')
js = js.replace('diploma_cost_da: "7000 EGP",', 'diploma_cost_da: "5500 EGP",')
js = js.replace('diploma_cost_flutter: "7500 EGP",', 'diploma_cost_flutter: "5500 EGP",')
js = js.replace('diploma_cost_frontend: "7500 EGP",', 'diploma_cost_frontend: "5500 EGP",')

# Replace Arabic prices
js = js.replace('diploma_cost_ai: "٨٠٠٠ ج.م",', 'diploma_cost_ai: "٦٠٠٠ ج.م",')
js = js.replace('diploma_cost_da: "٧٠٠٠ ج.م",', 'diploma_cost_da: "٥٥٠٠ ج.م",')
js = js.replace('diploma_cost_flutter: "٧٥٠٠ ج.م",', 'diploma_cost_flutter: "٥٥٠٠ ج.م",')
js = js.replace('diploma_cost_frontend: "٧٥٠٠ ج.م",', 'diploma_cost_frontend: "٥٥٠٠ ج.م",')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js updated with discounted prices successfully!")
