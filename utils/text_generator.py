from openai import OpenAI
from typing import Dict
import config

class TextGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        
    def generate_marketing_copy(self, product_name: str, product_description: str, 
                               target_audience: str = "general consumers") -> Dict[str, str]:
        """Generate comprehensive marketing copy for a product"""
        
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
        
        try:
            response = self.client.chat.completions.create(
                model=config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": "You are a creative marketing copywriter."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=config.MAX_TOKENS,
                temperature=config.TEMPERATURE
            )
            
            return {"content": response.choices.message.content}
            
        except Exception as e:
            return {"error": f"Failed to generate copy: {str(e)}"}
    
    def generate_image_prompt(self, product_name: str, product_description: str) -> str:
        """Generate optimized prompt for image generation"""
        
        prompt = f"""
        Create a detailed image prompt for: {product_name}
        Description: {product_description}
        
        Generate a concise prompt (max 100 words) for AI image generation including:
        - Product appearance and features
        - Professional marketing aesthetic
        - High quality, clean composition
        """
        
        try:
            response = self.client.chat.completions.create(
                model=config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": "You are an expert at creating prompts for AI image generation."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.5
            )
            
            return response.choices.message.content.strip()
            
        except Exception as e:
            return f"{product_name}, {product_description}, professional product photography, high quality"
