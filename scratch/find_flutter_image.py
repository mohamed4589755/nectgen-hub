import os
import glob
import time

artifact_dir = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252"
print("Image files in artifacts folder sorted by time:")
if os.path.exists(artifact_dir):
    files = []
    for f in glob.glob(os.path.join(artifact_dir, "*")):
        if os.path.isfile(f) and (f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp")):
            files.append((f, os.path.getmtime(f)))
    
    # Sort files by modification time (newest first)
    files.sort(key=lambda x: x[1], reverse=True)
    
    for f, mtime in files[:5]:
        print(f"  {os.path.basename(f)} - modified: {time.ctime(mtime)} - size: {os.path.getsize(f)} bytes")
