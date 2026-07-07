import glob
import re

def modify_html():
    for filepath in glob.glob("*.html"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Add scroll progress
        if '<div class="scroll-progress"' not in content:
            content = content.replace('<body>', '<body>\n    <div class="scroll-progress" id="scrollProgress"></div>')

        # 2. Add Back to Top button before </body>
        if 'id="backToTop"' not in content:
            content = content.replace('</body>', '    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>\n</body>')

        # 3. Add fade-up to sections
        # Match <section class="something"> or <section id="something" class="something">
        # Replace <section with <section class="fade-up " if it doesn't already have it
        def add_fade_up(match):
            m = match.group(0)
            if 'fade-up' not in m:
                if 'class="' in m:
                    return m.replace('class="', 'class="fade-up ')
                else:
                    return m.replace('<section', '<section class="fade-up"')
            return m
            
        content = re.sub(r'<section[^>]*>', add_fade_up, content)

        # 4. Add stagger classes to cards
        card_matches = list(re.finditer(r'<div[^>]*class="[^"]*(?:service-card|feature-card|portfolio-card|stat-card|blog-card|testimonial-card|pricing-card)[^"]*"[^>]*>', content))
        # Group cards by their parent section roughly, or just assign stagger-1 to 5 cyclically
        stagger_idx = 1
        offset = 0
        new_content = ""
        last_end = 0
        for m in card_matches:
            new_content += content[last_end:m.start()]
            matched_str = m.group(0)
            if 'stagger-' not in matched_str:
                matched_str = matched_str.replace('class="', f'class="stagger-{stagger_idx} ')
            new_content += matched_str
            last_end = m.end()
            
            stagger_idx += 1
            if stagger_idx > 5:
                stagger_idx = 1
                
        new_content += content[last_end:]
        content = new_content

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("HTML files updated successfully!")

modify_html()
