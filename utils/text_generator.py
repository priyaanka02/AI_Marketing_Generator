import requests
from typing import Dict
import config

class TextGenerator:
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        
    def generate_marketing_copy(self, product_name: str, product_description: str, 
                               target_audience: str = "general consumers") -> Dict[str, str]:
        
        prompt = f"""
        Create compelling marketing copy for:
        Product: {product_name}
        Description: {product_description}
        Target Audience: {target_audience}
        
        Generate:
        1. Catchy headline (max 10 words)
        2. Product tagline (max 15 words)  
        3. Short description (2-3 sentences)
        4. Key benefits (3 bullet points)
        5. Call-to-action phrase
        6. Social media post (max 280 characters)
        """
        
        headers = {
            "Content-Type": "application/json",
        }
        
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result["candidates"]["content"]["parts"]["text"]
                return {"content": content}
            else:
                return {"error": f"API Error: {response.status_code}"}
                
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}
    
    def generate_image_prompt(self, product_name: str, product_description: str) -> str:
        # Same Gemini API call but for image prompts
        prompt = f"Create a detailed image prompt for: {product_name}. Description: {product_description}. Make it suitable for AI image generation."
        
        # Similar API call structure as above
        # ... (implement same pattern)
        
        return f"{product_name}, {product_description}, professional product photography, high quality"

            
        except Exception as e:
            return f"{product_name}, {product_description}, professional product photography, high quality"

