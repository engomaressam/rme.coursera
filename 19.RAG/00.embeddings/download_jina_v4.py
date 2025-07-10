import os
# Bypass SSL verification (not recommended for production)
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

from transformers import AutoModel, AutoTokenizer

# Target directory for model download
TARGET_DIR = r"H:\Projects Control (PC)\10 Backup\05 Models\jina4"

os.makedirs(TARGET_DIR, exist_ok=True)

print(f"Downloading model to: {TARGET_DIR}")

# Download model and tokenizer
model = AutoModel.from_pretrained("jinaai/jina-embeddings-v4", trust_remote_code=True, cache_dir=TARGET_DIR)
tokenizer = AutoTokenizer.from_pretrained("jinaai/jina-embeddings-v4", trust_remote_code=True, cache_dir=TARGET_DIR)

print("Download complete. Model and tokenizer are saved in:", TARGET_DIR) 