import streamlit as st
from PIL import Image
import numpy as np
import google.generativeai as genai
from ultralytics import YOLO
import os

# ----------------------
# CONFIGURATION
# ----------------------
DEFAULT_MODEL = "gemini-2.0-flash"  # Free tier model

# ----------------------
# INGREDIENT DETECTION (YOLOv8)
# ----------------------
def detect_ingredients_yolo(image):
    try:
        model = YOLO("yolov8n.pt")
        results = model.predict(image)
        detected_items = []
        
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls)
                detected_items.append(result.names[class_id])
        
        unique_items = list(set(detected_items))
        return ", ".join(unique_items) if unique_items else "No ingredients detected"
    except Exception as e:
        st.error(f"Error in ingredient detection: {str(e)}")
        return ""

# ----------------------
# RECIPE GENERATOR
# ----------------------
def generate_recipe(ingredients, cuisine=None, dietary=None):
    try:
        prompt = f"""Generate a detailed recipe using these ingredients: {ingredients}
        
        Include:
        - Recipe name
        - Complete ingredients list with quantities
        - Step-by-step instructions
        - Cooking time estimate
        - Nutrition information (calories, protein, carbs, fat)
        """
        
        if cuisine and cuisine != "Any":
            prompt += f"\nCuisine style: {cuisine}"
        if dietary and dietary != "None":
            prompt += f"\nDietary requirements: {dietary}"
        
        model = genai.GenerativeModel(DEFAULT_MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating recipe: {str(e)}"

# ----------------------
# STREAMLIT UI
# ----------------------
st.set_page_config(page_title="🍲 Smart Recipe Generator", layout="wide")
st.title("🍽️ Smart Recipe Generator")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")
    use_yolo = st.checkbox("Enable ingredient detection (YOLOv8)", value=True)
    st.markdown("[Get free API key](https://aistudio.google.com/app/apikey)")

# Main content
uploaded_image = st.file_uploader("📷 Upload ingredients image", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)
with col1:
    cuisine = st.selectbox("🍛 Cuisine", ["Any", "Indian", "Italian", "Chinese", "Mexican", "American"])
with col2:
    dietary = st.selectbox("🥗 Dietary", ["None", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "Halal"])

if uploaded_image:
    try:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated parameter
        
        if api_key:
            genai.configure(api_key=api_key)
            
            ingredients = ""
            if use_yolo:
                with st.spinner("🔍 Detecting ingredients..."):
                    ingredients = detect_ingredients_yolo(np.array(image))
            
            if not ingredients:
                ingredients = "Ingredients from the uploaded image"
            else:
                st.success(f"Detected: {ingredients}")
            
            with st.spinner("🧑‍🍳 Generating recipe..."):
                recipe = generate_recipe(
                    ingredients=ingredients,
                    cuisine=cuisine,
                    dietary=dietary
                )
            
            st.success("✅ Recipe Generated!")
            st.subheader("📋 Recipe")
            st.markdown(recipe)
        else:
            st.warning("Please enter your Gemini API key")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Instructions
with st.expander("ℹ️ Instructions"):
    st.markdown("""
    1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
    2. Upload an image of ingredients
    3. Select preferences
    4. Get your custom recipe!
    
    **Note:** First run downloads YOLO model (~200MB)
    """)