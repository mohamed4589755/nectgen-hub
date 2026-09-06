from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783562264793.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size

# Crop the icon region (left side, x=0 to x=76)
icon_crop = img.crop((0, 0, 76, height))
w, h = icon_crop.size
pixels = icon_crop.load()

# Perform BFS flood fill to find and remove the gradient wall background
visited = [[False for _ in range(h)] for _ in range(w)]
queue = []

# Corner starting points
corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
for cx, cy in corners:
    queue.append((cx, cy))
    visited[cx][cy] = True

while queue:
    cx, cy = queue.pop(0)
    curr_color = pixels[cx, cy]
    
    # 4-connectivity
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
            n_color = pixels[nx, ny]
            # Euclidean distance in RGB
            dist = sum((n_color[i] - curr_color[i])**2 for i in range(3))**0.5
            
            # Since it's a smooth wall, background variations between neighbors are tiny (< 4)
            # Icon borders/shadows are much higher
            if dist < 6.0:
                visited[nx][ny] = True
                queue.append((nx, ny))

# Apply transparency to background
for x in range(w):
    for y in range(h):
        if visited[x][y]:
            pixels[x, y] = (0, 0, 0, 0)

# Trim transparent margins
bbox = icon_crop.getbbox()
if bbox:
    icon_final = icon_crop.crop(bbox)
else:
    icon_final = icon_crop

icon_final.save('assets/icon.png')
print("Cropped transparent 3D icon saved to assets/icon.png! Size:", icon_final.size)
