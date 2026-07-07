import re

def modify_styles():
    with open("styles.css", "r", encoding="utf-8") as f:
        content = f.read()

    # Button padding
    content = content.replace(
        'padding: 10px 24px;',
        'padding: 14px 28px;'
    )

    # Button hover/active scaling (append to .btn definition)
    if '.btn:hover' not in content:
        btn_block = re.search(r'\.btn \{[^\}]+\}', content).group(0)
        btn_hover_active = """
.btn:hover {
    transform: scale(1.02);
}
.btn:active {
    transform: scale(0.98);
}"""
        content = content.replace(btn_block, btn_block + btn_hover_active)

    # Cards (assuming they have .service-card, .feature-card, etc)
    # I will add global card styles or just search for common card classes.
    card_classes = ['.service-card', '.feature-card', '.portfolio-card', '.stat-card', '.blog-card', '.testimonial-card', '.card']
    for cc in card_classes:
        if cc + " {" in content:
            # Change padding or border-radius if explicit
            pass
            
    # Instead, let's inject a global hover for any card class
    # Add a generic block at the end if not exists
    if '.feature-card:hover' not in content:
        content += """
/* Global Card Hovers */
.service-card, .feature-card, .portfolio-card, .stat-card, .blog-card, .testimonial-card, .pricing-card {
    transition: var(--transition-smooth);
    border-radius: var(--radius-lg);
    border: 1px solid var(--glass-border);
}
.service-card:hover, .feature-card:hover, .portfolio-card:hover, .stat-card:hover, .blog-card:hover, .testimonial-card:hover, .pricing-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-hover);
}

.portfolio-card img, .blog-card img, .service-card img {
    transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
}
.portfolio-card:hover img, .blog-card:hover img, .service-card:hover img {
    transform: scale(1.05);
}

/* Sections spacing */
section {
    padding: 120px 0;
}
"""

    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Components and sections updated successfully!")

modify_styles()
