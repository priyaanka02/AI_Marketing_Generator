import streamlit as st
from utils.text_generator import TextGenerator
from utils.image_generator import ImageGenerator
import config

# Page configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="🚀",
    layout="wide"
)

def main():
    # Header
    st.title(config.APP_TITLE)
    st.markdown(config.APP_DESCRIPTION)
    
    # Sidebar for inputs
    with st.sidebar:
        st.header("Product Details")
        product_name = st.text_input("Product Name", placeholder="e.g., EcoSmart Water Bottle")
        product_description = st.text_area("Product Description", 
                                         placeholder="Brief description of your product...")
        target_audience = st.selectbox("Target Audience", 
                                     ["General Consumers", "Young Adults", "Professionals", 
                                      "Parents", "Tech Enthusiasts", "Fitness Enthusiasts"])
        
        generate_button = st.button("🎨 Generate Marketing Materials", type="primary")
    
    # Main content area
    if generate_button and product_name and product_description:
        
        # Initialize generators
        text_gen = TextGenerator()
        image_gen = ImageGenerator()
        
        # Create two columns for output
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.header("📝 Marketing Copy")
            with st.spinner("Generating marketing copy..."):
                copy_result = text_gen.generate_marketing_copy(
                    product_name, product_description, target_audience
                )
                
                if "error" not in copy_result:
                    st.markdown(copy_result["content"])
                else:
                    st.error(copy_result["error"])
        
        with col2:
            st.header("🖼️ Product Visual")
            with st.spinner("Generating product image..."):
                # Generate optimized image prompt
                image_prompt = text_gen.generate_image_prompt(product_name, product_description)
                st.write(f"**Image Prompt:** {image_prompt}")
                
                # Generate image
                image_result = image_gen.generate_image(image_prompt)
                
                if image_result["success"]:
                    st.image(image_result["image"], caption=f"{product_name} - AI Generated", use_column_width=True)
                else:
                    st.error(f"Image generation failed: {image_result['error']}")
    
    elif generate_button:
        st.warning("Please fill in both product name and description.")
    
    # Instructions
    with st.expander("📖 How to Use"):
        st.markdown("""
        1. **Enter Product Details**: Provide your product name and description
        2. **Select Target Audience**: Choose who you're marketing to
        3. **Generate**: Click the button to create marketing copy and visuals
        4. **Use the Results**: Copy the marketing text and download the image for your campaigns
        
        **Tips for Best Results:**
        - Be specific in your product description
        - Include key features and benefits
        - Mention materials, colors, or unique aspects
        """)

if __name__ == "__main__":
    main()
