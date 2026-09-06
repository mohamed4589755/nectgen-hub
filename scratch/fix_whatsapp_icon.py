with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the WhatsApp SVG in main.js
old_wa_svg = """    waBtn.innerHTML = `
        <svg viewBox="0 0 24 24" width="34" height="34" fill="currentColor">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.513 2.262 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.724-1.455L0 24zm6.59-4.846c1.66.986 3.284 1.489 4.936 1.49h.005c5.378 0 9.75-4.37 9.755-9.755a9.66 9.66 0 0 0-2.845-6.894 9.66 9.66 0 0 0-6.893-2.847c-5.383 0-9.754 4.373-9.759 9.756-.002 2.222.746 4.337 2.16 6.07l-.962 3.514 3.608-.944zm8.002-1.438c-.3-.15-1.78-.877-2.056-.977-.276-.1-.478-.15-.678.15-.2.3-.778.977-.954 1.177-.176.2-.351.226-.651.076-.3-.15-1.265-.467-2.41-1.485-.89-.794-1.492-1.775-1.667-2.076-.175-.3-.019-.462.13-.611.135-.135.3-.35.45-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.678-1.635-.93-2.244-.244-.589-.493-.509-.678-.509-.176 0-.376-.02-.577-.02-.2 0-.527.075-.803.376-.276.3-1.053 1.026-1.053 2.503 0 1.477 1.078 2.902 1.228 3.102.15.2 2.122 3.24 5.143 4.545.718.311 1.277.496 1.714.635.722.23 1.38.197 1.9.12.577-.087 1.78-.727 2.03-1.43.25-.701.25-1.302.176-1.43-.076-.127-.276-.202-.577-.352z"/>
        </svg>
    `;"""

new_wa_svg = """    waBtn.innerHTML = `
        <svg viewBox="0 0 24 24" width="60" height="60" style="filter: drop-shadow(0px 8px 16px rgba(0, 0, 0, 0.2));">
            <circle cx="12" cy="12" r="11" fill="white"/>
            <path fill="#25D366" d="M12.03 2c-5.52 0-10 4.48-10 10 0 1.78.47 3.5 1.35 5L2 22l5.12-1.34c1.46.8 3.12 1.22 4.82 1.22 5.52 0 10-4.48 10-10 0-5.52-4.48-10-10-10z"/>
            <path fill="white" d="M17.98 16.18c-.27-.13-1.58-.78-1.82-.87-.24-.09-.42-.13-.6.13-.18.27-.7 1.13-.86 1.3-.16.18-.33.2-.6.07-.27-.13-1.15-.43-2.2-1.36-.81-.72-1.36-1.62-1.52-1.9-.16-.27-.02-.42.12-.55.12-.13.27-.3.4-.46.13-.16.18-.28.27-.46.09-.18.04-.34-.02-.47-.07-.13-.6-1.44-.82-1.97-.22-.53-.48-.46-.6-.46-.12 0-.27-.02-.42-.02-.15 0-.39.06-.6.28-.21.22-.8.78-.8 1.9s.82 2.2 1.04 2.5c.22.3 1.62 2.48 3.93 3.48.55.24.98.38 1.32.49.56.18 1.07.15 1.47.09.45-.07 1.38-.56 1.57-1.1.2-.55.2-1.02.14-1.13-.06-.11-.24-.17-.51-.3z"/>
        </svg>
    `;"""

js = js.replace(old_wa_svg, new_wa_svg)

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("main.js successfully updated with official WhatsApp SVG!")


# Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

old_wa_css = """/* --- WHATSAPP FLOATING BUTTON --- */
.whatsapp-float {
    position: fixed;
    bottom: 24px;
    right: 24px;
    --wa-bg: #25D366;
    background-color: var(--wa-bg);
    color: white;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 24px rgba(37, 211, 102, 0.25);
    z-index: 9999;
    transition: var(--transition-smooth);
}

.whatsapp-float:hover {
    transform: scale(1.08) translateY(-3px);
    box-shadow: 0 12px 28px rgba(37, 211, 102, 0.35);
    --wa-bg: #20BA5A;
}"""

new_wa_css = """/* --- WHATSAPP FLOATING BUTTON --- */
.whatsapp-float {
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    transition: var(--transition-smooth);
    background: transparent;
    border: none;
}

.whatsapp-float:hover {
    transform: scale(1.08) translateY(-3px);
}"""

css = css.replace(old_wa_css, new_wa_css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css successfully updated with official WhatsApp wrapper styles!")
