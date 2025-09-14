import requests
import base64
from PIL import Image
from io import BytesIO
import config

class ImageGenerator:
    def __init__(self):
        self.api_key = config.STABILITY_API_KEY
        self.base_url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"
        
    def generate_image(self, prompt: str) -> dict:
        """Generate image using Stable Diffusion API"""
        
        headers = {
            "authorization": f"Bearer {self.api_key}",
            "accept": "image/*"
        }
        
        data = {
            "prompt": prompt,
            "output_format": "png",
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, files={"none": ''}, data=data)
            
            if response.status_code == 200:
                # Convert response to PIL Image
                image = Image.open(BytesIO(response.content))
                return {"success": True, "image": image}
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}
                
        except Exception as e:
            return {"success": False, "error": f"Request failed: {str(e)}"}
