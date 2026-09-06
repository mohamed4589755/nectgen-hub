from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size

# Crop the icon region (x=0 to x=80, y=0 to y=height)
# The icon is on the left
icon_crop = img.crop((0, 0, 80, height))
w, h = icon_crop.size
pixels = icon_crop.load()

# We will perform a BFS flood fill to find background pixels.
# Any pixel connected to the corners with small color difference between neighbors is background.
visited = [[False for _ in range(h)] for _ in range(w)]
queue = []

# Add the 4 corners of the cropped icon to the queue
corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
for cx, cy in corners:
    queue.append((cx, cy))
    visited[cx][cy] = True

# BFS traversal
while queue:
    cx, cy = queue.pop(0)
    curr_color = pixels[cx, cy]
    
    # Check 4-connectivity neighbors
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
            n_color = pixels[nx, ny]
            # Calculate Euclidean color distance between neighbor and current background pixel
            dist = sum((n_color[i] - curr_color[i])**2 for i in range(3))**0.5
            
            # Since background is a smooth gradient, neighbor difference is very small (usually < 5)
            # The icon edges have a large difference (> 20)
            if dist < 8.0:
                visited[nx][ny] = True
                queue.append((nx, ny))

# Now, set all visited pixels to transparent
for x in range(w):
    for y in range(h):
        if visited[x][y]:
            pixels[x, y] = (0, 0, 0, 0)

# Auto-crop (trim) transparent edges
bbox = icon_crop.getbbox()
if bbox:
    icon_final = icon_crop.crop(bbox)
else:
    icon_final = icon_crop

# Save the final icon
icon_final.save('assets/icon.png')
print("Cropped transparent icon via flood-fill saved to assets/icon.png! Size:", icon_final.size)
