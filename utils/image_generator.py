import requests
from PIL import Image
from io import BytesIO
import urllib.parse

class ImageGenerator:
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt/"
        
    def generate_image(self, prompt: str) -> dict:
        """Generate image using Pollinations AI - 100% FREE, no API key needed"""
        
        try:
            # Clean and encode the prompt
            clean_prompt = urllib.parse.quote(prompt)
            
            # Pollinations API parameters for better quality
            params = "?width=512&height=512&model=flux&enhance=true"
            
            # Build the full URL
            image_url = f"{self.base_url}{clean_prompt}{params}"
            
            # Get the image directly
            response = requests.get(image_url, timeout=30)
            
            if response.status_code == 200:
                # Convert response to PIL Image
                image = Image.open(BytesIO(response.content))
                return {"success": True, "image": image}
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}
                
        except Exception as e:
            return {"success": False, "error": f"Request failed: {str(e)}"}
