import requests
import base64
from PIL import Image
from io import BytesIO
import config

class ImageGenerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        self.headers = {"Authorization": f"Bearer {config.HF_TOKEN}"}
        
    def generate_image(self, prompt: str) -> dict:
        """Generate image using Hugging Face's FREE Stable Diffusion API"""
        
        payload = {
            "inputs": prompt,
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                # Convert response bytes to PIL Image
                image = Image.open(BytesIO(response.content))
                return {"success": True, "image": image}
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}
                
        except Exception as e:
            return {"success": False, "error": f"Request failed: {str(e)}"}
