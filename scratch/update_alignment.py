import os

html_dir = r"C:\NextGen Hub Website"
files = ["index.html", "internships.html", "bootcamps.html", "diplomas.html", "about.html", "contact.html"]

for filename in files:
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Replace Subpage Hero Banners: <div class="container text-center"> with <div class="container">
    # We only want to target the hero container and CTA containers
    # Let's do selective replacements
    
    # Subpage Hero Banner container replacement
    content = content.replace('<!-- Subpage Hero Banner -->\n    <section class="section-padding" style="padding-top: 150px;', '<!-- Subpage Hero Banner -->\n    <section class="section-padding" style="padding-top: 150px; text-align: left;')
    # Wait, instead of inline styling, we can just replace the `<div class="container text-center">` inside the Hero banner.
    # Let's replace the block:
    # <div class="container text-center">
    #         <span class="section-tag"
    # To do this safely for all files:
    content = content.replace('<div class="container text-center">\n            <span class="section-tag"', '<div class="container">\n            <span class="section-tag"')
    
    # Also replace for Contact Page hero:
    # <div class="container text-center">
    #         <span class="section-tag"
    # Wait, it is the same.
    
    # 2. Replace Index Page CTA:
    # <section class="section-padding">\n        <div class="container text-center">\n            <h2 class="section-title" style="margin-bottom: 24px;" data-i18n="index_cta_title">
    content = content.replace('<div class="container text-center">\n            <h2 class="section-title" style="margin-bottom: 24px;" data-i18n="index_cta_title">', '<div class="container">\n            <h2 class="section-title" style="margin-bottom: 24px;" data-i18n="index_cta_title">')
    
    # 3. Replace Bootcamps Page CTA button container:
    content = content.replace('<div style="margin-top: 48px;" class="text-center">', '<div style="margin-top: 48px;">')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated alignment in {filename}")
