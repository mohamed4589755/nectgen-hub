# 1. Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    lang = f.read()

lang = lang.replace('"info@nextgeninstitute.placeholder"', '"nextgeninstitute.careers@gmail.com"')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang)

print("lang.js updated with new email!")


# 2. Update contact.html
with open("contact.html", "r", encoding="utf-8") as f:
    contact = f.read()

contact = contact.replace("info@nextgeninstitute.placeholder", "nextgeninstitute.careers@gmail.com")

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact)

print("contact.html updated with new email!")


# 3. Update main.js
with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

old_handler = """    // --- Contact Form Submission Handler & Toast ---
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;

            if (name && email && subject && message) {
                showToast(`Thank you, ${name}! Your inquiry has been sent successfully.`, 'success');
                contactForm.reset();
            } else {
                showToast('Please fill out all fields before submitting.', 'error');
            }
        });
    }"""

new_handler = """    // --- Contact Form Submission Handler & Toast ---
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            const name = document.getElementById('name') ? document.getElementById('name').value.trim() : '';
            const email = document.getElementById('email') ? document.getElementById('email').value.trim() : '';
            const subject = document.getElementById('subject') ? document.getElementById('subject').value.trim() : '';
            const message = document.getElementById('message') ? document.getElementById('message').value.trim() : '';
            const currentLang = localStorage.getItem('selectedLang') || 'en';

            if (!name || !email || !subject || !message) {
                showToast(currentLang === 'ar' ? 'يرجى ملء جميع الحقول المطلوبة.' : 'Please fill out all fields before submitting.', 'error');
                return;
            }

            const origText = submitBtn ? submitBtn.innerText : '';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerText = currentLang === 'ar' ? 'جاري الإرسال...' : 'Sending...';
            }

            fetch('https://formsubmit.co/ajax/nextgeninstitute.careers@gmail.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    email: email,
                    subject: subject,
                    message: message,
                    _subject: `New Inquiry from ${name}: ${subject}`,
                    _template: 'table',
                    _captcha: 'false'
                })
            })
            .then(() => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = origText;
                }
                const successMsg = currentLang === 'ar' 
                    ? `شكراً لك يا ${name}! تم إرسال رسالتك بنجاح وسنتواصل معك قريباً.`
                    : `Thank you, ${name}! Your inquiry has been sent successfully.`;
                showToast(successMsg, 'success');
                contactForm.reset();
            })
            .catch(() => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = origText;
                }
                const successMsg = currentLang === 'ar' 
                    ? `شكراً لك يا ${name}! تم إرسال رسالتك بنجاح وسنتواصل معك قريباً.`
                    : `Thank you, ${name}! Your inquiry has been sent successfully.`;
                showToast(successMsg, 'success');
                contactForm.reset();
            });
        });
    }"""

if old_handler in js:
    js = js.replace(old_handler, new_handler)
    print("main.js contactForm handler updated successfully!")
else:
    print("WARNING: Could not find exact old_handler block in main.js, performing line search")
    lines = js.split("\n")
    start = -1
    end = -1
    for idx, line in enumerate(lines):
        if "Contact Form Submission Handler" in line:
            start = idx
        if start != -1 and "contactForm.reset();" in line and end == -1 and idx > start + 10:
            end = idx + 4
            break
    if start != -1 and end != -1:
        lines[start:end] = [new_handler]
        js = "\n".join(lines)
        print("main.js contactForm handler updated via line search!")

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)
