import sys
from PIL import Image

def remove_small_n():
    img = Image.open('assets/icon.png').convert('RGBA')
    w, h = img.size
    pixels = img.load()
    visited = set()
    components = []
    
    for y in range(h):
        for x in range(w):
            if pixels[x, y][3] > 0 and (x, y) not in visited:
                comp = []
                q = [(x, y)]
                visited.add((x, y))
                while q:
                    cx, cy = q.pop(0)
                    comp.append((cx, cy))
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
                        nx, ny = cx+dx, cy+dy
                        if 0<=nx<w and 0<=ny<h and pixels[nx, ny][3] > 0 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))
                components.append(comp)
                
    # Identify the small component (Component 1)
    for i, comp in enumerate(components):
        if len(comp) < 5000: # Component 1 size is 2325
            # Erase it
            for x, y in comp:
                pixels[x, y] = (0, 0, 0, 0)
                
    img.save('assets/icon.png')
    print("Small 'N' erased successfully!")

remove_small_n()
