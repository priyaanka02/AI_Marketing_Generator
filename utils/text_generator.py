import requests
from typing import Dict
import config

class TextGenerator:
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        
    def generate_marketing_copy(self, product_name: str, product_description: str, 
                               target_audience: str = "general consumers") -> Dict[str, str]:
        """Generate comprehensive marketing copy for a product using Gemini API"""
        
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
        
        Format each section clearly.
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
                return self._generate_fallback_copy(product_name, product_description, target_audience)
                
        except Exception as e:
            return self._generate_fallback_copy(product_name, product_description, target_audience)
    
    def _generate_fallback_copy(self, product_name: str, product_description: str, target_audience: str) -> Dict[str, str]:
        """Fallback copy generation when API fails"""
        
        content = f"""
🎯 **HEADLINE:** {product_name} - Premium Quality That Delivers

✨ **TAGLINE:** Innovation Designed for {target_audience}

📝 **DESCRIPTION:** 
{product_description} This exceptional product combines cutting-edge technology with thoughtful design, delivering exactly what {target_audience.lower()} need for their modern lifestyle.

💪 **KEY BENEFITS:**
• Superior quality and long-lasting durability
• Perfectly designed for {target_audience.lower()} needs
• Trusted by thousands of satisfied customers worldwide

🔥 **CALL TO ACTION:** Get Yours Today - Limited Time Offer!

📱 **SOCIAL MEDIA POST:** 
Just discovered {product_name} and it's everything I hoped for! Perfect for {target_audience.lower()} who want quality that lasts. This is definitely a game-changer! 🔥 #QualityFirst #MustHave
        """
        
        return {"content": content}
    
    def generate_image_prompt(self, product_name: str, product_description: str) -> str:
        """Generate optimized prompt for image generation"""
        
        prompt = f"""
        Create a detailed image prompt for: {product_name}
        Description: {product_description}
        
        Generate a concise prompt for AI image generation including:
        - Product appearance and key features
        - Professional marketing aesthetic
        - High quality, clean composition
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
                return result["candidates"]["content"]["parts"]["text"].strip()
            else:
                return f"{product_name}, {product_description}, professional product photography, high quality, clean background"
                
        except Exception as e:
            return f"{product_name}, {product_description}, professional product photography, high quality, clean background"
