import re

def final_css_touches():
    with open("styles.css", "r", encoding="utf-8") as f:
        content = f.read()

    # Add section divider if not exists
    if 'border-bottom: 1px solid var(--glass-border);' not in content.split('section {')[1][:100]:
        content = content.replace('section {\n    padding: 120px 0;\n}', 'section {\n    padding: 120px 0;\n    position: relative;\n    border-bottom: 1px solid var(--glass-border);\n}')

    # Ambient orbs using body pseudo-elements
    if 'body::before' not in content:
        ambient_orbs = """
body::before, body::after {
    content: '';
    position: fixed;
    width: 60vw;
    height: 60vw;
    border-radius: 50%;
    filter: blur(120px);
    opacity: 0.05;
    z-index: -1;
    pointer-events: none;
}
body::before {
    top: -20vw;
    left: -20vw;
    background: var(--accent-blue);
}
body::after {
    bottom: -20vw;
    right: -20vw;
    background: var(--accent-cyan);
}
"""
        content += ambient_orbs

    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Final CSS touches added successfully!")

final_css_touches()
