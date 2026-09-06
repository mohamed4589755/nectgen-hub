with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

old_fetch = """                // Send registration data to Google Sheet
                fetch(GOOGLE_SHEET_WEBAPP_URL, {
                    method: 'POST',
                    mode: 'no-cors', // Bypasses CORS policy checks for Apps Script redirection
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(applicationData)
                })"""

new_fetch = """                // Send registration data to Google Sheet
                fetch(GOOGLE_SHEET_WEBAPP_URL, {
                    method: 'POST',
                    mode: 'no-cors', // Bypasses CORS policy checks for Apps Script redirection
                    headers: {
                        'Content-Type': 'text/plain' // Complies with no-cors allowed headers
                    },
                    body: JSON.stringify(applicationData)
                })"""

html = html.replace(old_fetch, new_fetch)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html fetch headers updated successfully!")
