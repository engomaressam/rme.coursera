import os
import subprocess
import sys

TARGET_DIR = r"H:\Projects Control (PC)\10 Backup\05 Models\jina4"
REPO_URL = "https://huggingface.co/jinaai/jina-embeddings-v4"

print(f"Target directory: {TARGET_DIR}")

if os.path.exists(TARGET_DIR) and os.listdir(TARGET_DIR):
    print(f"[INFO] Target directory already exists and is not empty: {TARGET_DIR}")
    response = input("Do you want to delete and re-clone it? (y/n): ").strip().lower()
    if response == 'y':
        print("[INFO] Removing existing directory...")
        import shutil
        shutil.rmtree(TARGET_DIR)
    else:
        print("[INFO] Exiting without changes.")
        sys.exit(0)

print("[INFO] Cloning the repository with git lfs...")
try:
    # Run git lfs install (safe to run multiple times)
    subprocess.run(["git", "lfs", "install"], check=True)
    # Clone the repo
    process = subprocess.Popen([
        "git", "clone", REPO_URL, TARGET_DIR
    ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end="")
    process.wait()
    if process.returncode != 0:
        print("[ERROR] git clone failed.")
        sys.exit(1)
    print("[INFO] Repository cloned successfully.")
except Exception as e:
    print(f"[ERROR] {e}")
    sys.exit(1)

print("[INFO] All files (including large model files) should now be in:")
print(f"    {TARGET_DIR}")
print("You can now use the model locally in your Python code.") 