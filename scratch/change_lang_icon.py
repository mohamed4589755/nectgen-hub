with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace button creation styling and SVG injection
old_btn_style = """            const btn = document.createElement('button');
            btn.id = 'langToggle';
            btn.className = 'btn';
            btn.style.padding = '4px 12px';
            btn.style.fontSize = '0.78rem';
            btn.style.background = 'var(--bg-secondary)';
            btn.style.border = '1px solid var(--glass-border)';
            btn.style.borderRadius = 'var(--radius-pill)';
            btn.style.cursor = 'pointer';
            btn.style.color = 'var(--text-main)';
            btn.style.fontWeight = '600';
            btn.style.marginLeft = '12px';
            btn.style.transition = 'var(--transition-smooth)';"""

new_btn_style = """            const btn = document.createElement('button');
            btn.id = 'langToggle';
            btn.className = 'btn';
            btn.style.width = '32px';
            btn.style.height = '32px';
            btn.style.padding = '0';
            btn.style.background = 'var(--bg-secondary)';
            btn.style.border = '1px solid var(--glass-border)';
            btn.style.borderRadius = '50%';
            btn.style.cursor = 'pointer';
            btn.style.color = 'var(--text-main)';
            btn.style.display = 'flex';
            btn.style.alignItems = 'center';
            btn.style.justifyContent = 'center';
            btn.style.marginLeft = '12px';
            btn.style.transition = 'var(--transition-smooth)';
            
            // Inject Feather Globe SVG
            btn.innerHTML = `<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="display: block; flex-shrink: 0;"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`;"""

js = js.replace(old_btn_style, new_btn_style)

# Remove the text toggle in applyLanguage
old_text_toggle = """        // Update language button label
        const toggleBtn = document.getElementById('langToggle');
        if (toggleBtn) {
            toggleBtn.textContent = lang === 'en' ? 'العربية' : 'English';
        }"""

js = js.replace(old_text_toggle, "")

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js successfully updated with globe icon switcher!")
