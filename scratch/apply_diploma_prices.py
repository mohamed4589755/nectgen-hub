# 1. Update lang.js with pricing translations
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

# English insertion
en_old = 'diploma_duration_5m: "5 Months",'
en_new = """diploma_duration_5m: "5 Months",
        diploma_cost_label: "Cost:",
        diploma_cost_ai: "8000 EGP",
        diploma_cost_da: "7000 EGP",
        diploma_cost_flutter: "7500 EGP",
        diploma_cost_frontend: "7500 EGP","""

# Arabic insertion
ar_old = 'diploma_duration_5m: "٥ أشهر",'
ar_new = """diploma_duration_5m: "٥ أشهر",
        diploma_cost_label: "التكلفة:",
        diploma_cost_ai: "٨٠٠٠ ج.م",
        diploma_cost_da: "٧٠٠٠ ج.م",
        diploma_cost_flutter: "٧٥٠٠ ج.م",
        diploma_cost_frontend: "٧٥٠٠ ج.م","""

js = js.replace(en_old, en_new)
js = js.replace(ar_old, ar_new)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js updated with diploma prices successfully!")


# 2. Update diplomas.html card footers
with open("diplomas.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Card 1 AI & ML Footer
card1_old = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b></span>\n                            <a href="contact.html?diploma=AI_ML"'
card1_new = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b> &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_ai">8000 EGP</b></span>\n                            <a href="contact.html?diploma=AI_ML"'

# Card 2 Data Analytics Footer
card2_old = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b></span>\n                            <a href="contact.html?diploma=Data_Analytics"'
card2_new = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b> &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_da">7000 EGP</b></span>\n                            <a href="contact.html?diploma=Data_Analytics"'

# Card 3 Flutter Footer
card3_old = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b></span>\n                            <a href="contact.html?diploma=Flutter_Dev"'
card3_new = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b> &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_flutter">7500 EGP</b></span>\n                            <a href="contact.html?diploma=Flutter_Dev"'

# Card 4 Front-End Footer
card4_old = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b></span>\n                            <a href="contact.html?diploma=Frontend_Dev"'
card4_new = '<span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_5m">5 Months</b> &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_frontend">7500 EGP</b></span>\n                            <a href="contact.html?diploma=Frontend_Dev"'

html = html.replace(card1_old, card1_new)
html = html.replace(card2_old, card2_new)
html = html.replace(card3_old, card3_new)
html = html.replace(card4_old, card4_new)

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(html)

print("diplomas.html updated with cost metadata fields successfully!")
