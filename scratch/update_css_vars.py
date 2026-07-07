import re

def modify_styles():
    with open("styles.css", "r", encoding="utf-8") as f:
        content = f.read()

    # Update border radii
    content = re.sub(r'--radius-sm: 8px;', '--radius-sm: 12px;', content)
    content = re.sub(r'--radius-md: 16px;', '--radius-md: 18px;', content)
    content = re.sub(r'--radius-pill: 980px;', '--radius-pill: 9999px;', content)

    # Add --shadow-hover if not exists
    if '--shadow-hover' not in content:
        content = content.replace(
            '--shadow-soft: 0 8px 30px rgba(0, 0, 0, 0.04);',
            '--shadow-soft: 0 12px 40px rgba(0, 0, 0, 0.05);\n    --shadow-hover: 0 24px 60px rgba(0, 0, 0, 0.08);'
        )

    # Typography line height
    content = content.replace(
        'line-height: 1.47059;',
        'line-height: 1.6;'
    )
    
    # Add transition for images in globals
    if '.img-wrapper' not in content:
        content += """
/* --- GLOBAL REDESIGN UTILS --- */
.fade-up {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
}
.fade-up.visible {
    opacity: 1;
    transform: translateY(0);
}
.stagger-1 { transition-delay: 0.1s; }
.stagger-2 { transition-delay: 0.2s; }
.stagger-3 { transition-delay: 0.3s; }
.stagger-4 { transition-delay: 0.4s; }
.stagger-5 { transition-delay: 0.5s; }

.scroll-progress {
    position: fixed;
    top: 0;
    left: 0;
    width: 0%;
    height: 3px;
    background: var(--accent-blue);
    z-index: 10000;
    transition: width 0.1s;
}

.back-to-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: var(--bg-primary);
    box-shadow: var(--shadow-hover);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 9000;
    opacity: 0;
    visibility: hidden;
    transform: translateY(20px);
    transition: var(--transition-smooth);
    color: var(--text-main);
    text-decoration: none;
}
.back-to-top:hover {
    transform: translateY(15px) scale(1.05);
}
.back-to-top.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.bg-light-gray {
    background-color: var(--bg-tertiary);
}

.ambient-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(120px);
    opacity: 0.15;
    z-index: -1;
    pointer-events: none;
}
"""

    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(content)
        
    print("styles.css modified successfully!")

modify_styles()
