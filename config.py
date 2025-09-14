import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

# App Configuration
APP_TITLE = "🚀 AI Marketing Generator"
APP_DESCRIPTION = "Generate compelling marketing copy and stunning visuals for your products"

# Generation Settings
DEFAULT_MODEL = "gpt-4o-mini"  # This works on free tier
MAX_TOKENS = 500
TEMPERATURE = 0.7

