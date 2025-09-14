import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration - ALL FREE!
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# App Configuration
APP_TITLE = "🚀 AI Marketing Generator"
APP_DESCRIPTION = "Generate compelling marketing copy and stunning visuals for your products"

# Generation Settings
MAX_TOKENS = 500
TEMPERATURE = 0.7


