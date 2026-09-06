import os
import glob
import time

# Check workspace assets folder
print("Files in assets/ folder:")
if os.path.exists("assets"):
    for f in glob.glob("assets/*"):
        mtime = time.ctime(os.path.getmtime(f))
        print(f"  {f} - modified: {mtime} - size: {os.path.getsize(f)} bytes")

# Check brain/conversation artifacts folder
artifact_dir = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252"
print("\nFiles in artifacts folder:")
if os.path.exists(artifact_dir):
    for f in glob.glob(os.path.join(artifact_dir, "*")):
        if os.path.isfile(f) and (f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp")):
            mtime = time.ctime(os.path.getmtime(f))
            print(f"  {os.path.basename(f)} - modified: {mtime} - size: {os.path.getsize(f)} bytes")
