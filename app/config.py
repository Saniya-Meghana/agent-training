import os

# Paths
DATA_DIR = os.getenv('DATA_DIR', 'data/documents')
EMBEDDINGS_DIR = os.getenv('EMBEDDINGS_DIR', 'data/embeddings')

# Model Settings
MODEL_NAME = os.getenv('MODEL_NAME', 'gemma-2b')
DEVICE = os.getenv('DEVICE', 'mps')

# Hugging Face Token (optional)
HF_TOKEN = os.getenv('HF_TOKEN', None)
