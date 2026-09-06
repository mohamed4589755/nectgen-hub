with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Fix hero background
css = css.replace("background: #FFFFFF;\n}", "background: var(--bg-primary);\n}", 1)

# 2. Fix floating-badge styling
old_floating_badge = """.floating-badge {
    position: absolute;
    padding: 10px 18px;
    border-radius: var(--radius-sm);
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid rgba(0, 0, 0, 0.06);"""

new_floating_badge = """.floating-badge {
    position: absolute;
    padding: 10px 18px;
    border-radius: var(--radius-sm);
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);"""

css = css.replace(old_floating_badge, new_floating_badge)

# 3. Fix slide-btn background & border
old_slide_btn = """.slide-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid rgba(0, 0, 0, 0.08);"""

new_slide_btn = """.slide-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);"""

css = css.replace(old_slide_btn, new_slide_btn)

# 4. Fix hero-slider-dots background & border
old_dots = """.hero-slider-dots {
    position: absolute;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 8px;
    z-index: 10;
    background: rgba(255, 255, 255, 0.6);
    padding: 6px 12px;
    border-radius: var(--radius-pill);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 0, 0, 0.05);"""

new_dots = """.hero-slider-dots {
    position: absolute;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 8px;
    z-index: 10;
    background: var(--glass-bg);
    padding: 6px 12px;
    border-radius: var(--radius-pill);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);"""

css = css.replace(old_dots, new_dots)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css has been successfully updated with variable-based backgrounds!")
