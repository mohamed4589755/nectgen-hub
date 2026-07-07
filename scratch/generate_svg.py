svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
    <!-- Modern, minimal tech-education 'N' arrow icon -->
    <g fill="#1E6BFF">
        <!-- Left vertical stem -->
        <rect x="20" y="30" width="22" height="65" rx="6" />
        
        <!-- Right vertical stem -->
        <rect x="74" y="45" width="22" height="50" rx="6" />
        
        <!-- Diagonal connecting stem -->
        <path d="M 37 36 L 81 89 A 6 6 0 0 0 92 84 L 46 31 A 6 6 0 0 0 37 36 Z" />
        
        <!-- Upward Arrow Head on the top right -->
        <path d="M 64 26 L 98 12 L 95 48 A 4 4 0 0 0 102 49 L 108 10 A 4 4 0 0 0 102 4 L 59 18 A 4 4 0 0 0 64 26 Z" />
    </g>
</svg>"""

with open("assets/icon.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
    
print("SVG generated successfully!")
