# Update main.js
with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

old_block = """            fetch('https://formsubmit.co/ajax/nextgeninstitute.careers@gmail.com', {
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
            });"""

new_block = """            fetch('https://formsubmit.co/ajax/nextgeninstitute.careers@gmail.com', {
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
            .then(res => res.json())
            .then(data => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = origText;
                }
                if (data.success === "true" || data.success === true) {
                    const successMsg = currentLang === 'ar' 
                        ? `شكراً لك يا ${name}! تم إرسال رسالتك بنجاح وسنتواصل معك قريباً.`
                        : `Thank you, ${name}! Your inquiry has been sent successfully.`;
                    showToast(successMsg, 'success');
                    contactForm.reset();
                } else if (data.message && data.message.includes('Activation')) {
                    const warnMsg = currentLang === 'ar'
                        ? 'تنبيه: يرجى فتح الإيميل nextgeninstitute.careers@gmail.com والضغط على رابط التفعيل (Activate Form) لمرة واحدة.'
                        : 'Form needs activation! Please check nextgeninstitute.careers@gmail.com inbox to activate.';
                    showToast(warnMsg, 'error');
                } else {
                    const errorMsg = currentLang === 'ar'
                        ? 'حدث خطأ أثناء الإرسال، يرجى المحاولة لاحقاً.'
                        : 'An error occurred while sending. Please try again.';
                    showToast(errorMsg, 'error');
                }
            })
            .catch(() => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = origText;
                }
                const errorMsg = currentLang === 'ar' 
                    ? 'حدث خطأ أثناء الإرسال، يرجى المحاولة لاحقاً.'
                    : 'An error occurred while sending. Please try again.';
                showToast(errorMsg, 'error');
            });"""

if old_block in js:
    js = js.replace(old_block, new_block)
    print("Updated main.js fetch handling successfully!")
else:
    print("WARNING: Could not find exact old_block in main.js")

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)
