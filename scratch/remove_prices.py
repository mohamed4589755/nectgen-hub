# Update diplomas.html
with open("diplomas.html", "r", encoding="utf-8") as f:
    diplomas = f.read()

diplomas = diplomas.replace("\r\n", "\n")

# Target cost strings to remove
cost_snippets = [
    ' &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_ai">8000 EGP</b>',
    ' &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_da">7000 EGP</b>',
    ' &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_flutter">7500 EGP</b>',
    ' &nbsp;|&nbsp; <span data-i18n="diploma_cost_label">Cost:</span> <b data-i18n="diploma_cost_frontend">7500 EGP</b>'
]

for snippet in cost_snippets:
    if snippet in diplomas:
        diplomas = diplomas.replace(snippet, "")
        print("Removed cost snippet from diplomas.html")
    else:
        print("WARNING: Could not find exact cost snippet:", snippet[:40])

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(diplomas)

print("diplomas.html prices removed successfully!")
