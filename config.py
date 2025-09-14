import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration - ALL FREE!
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")  # Hugging Face token
MODELSLAB_API_KEY = os.getenv("MODELSLAB_API_KEY", "")  # ModelsLab key

# App Configuration
APP_TITLE = "🚀 AI Marketing Generator"
APP_DESCRIPTION = "Generate compelling marketing copy and stunning visuals for your products"

# Generation Settings
MAX_TOKENS = 500
TEMPERATURE = 0.7
