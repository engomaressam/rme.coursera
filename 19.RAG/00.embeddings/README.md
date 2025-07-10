# Jina Embeddings v4 Downloader

This folder contains a script to download the Jina Embeddings v4 model from Hugging Face and store it in your backup directory for offline use.

## How to Use

1. **Install requirements:**
   ```bash
   pip install transformers>=4.52.0 torch>=2.6.0 peft>=0.15.2 torchvision pillow
   ```

2. **Run the download script:**
   ```bash
   python download_jina_v4.py
   ```
   This will download the model and tokenizer to:
   ```
   H:\Projects Control (PC)\10 Backup\05 Models\jina4
   ```

3. **Copy the folder** to your GPU machine if needed.

4. **Load the model offline:**
   ```python
   from transformers import AutoModel, AutoTokenizer
   local_dir = r"H:\\Projects Control (PC)\\10 Backup\\05 Models\\jina4"
   model = AutoModel.from_pretrained(local_dir, trust_remote_code=True)
   tokenizer = AutoTokenizer.from_pretrained(local_dir, trust_remote_code=True)
   ```

   Or with sentence-transformers:
   ```python
   from sentence_transformers import SentenceTransformer
   model = SentenceTransformer(local_dir, trust_remote_code=True)
   ```

## Reference
- [Jina Embeddings v4 on Hugging Face](https://huggingface.co/jinaai/jina-embeddings-v4) 