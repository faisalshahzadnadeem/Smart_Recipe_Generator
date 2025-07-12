# 🧠 Smart Recipe Generator AI 🍽️

A Streamlit-powered AI app that generates professional, personalized recipes from a list of ingredients — either uploaded via image or entered as text.

Built using:
- 🔥 [Google Gemini 2.0 Flash](https://aistudio.google.com/)
- 🤖 [Agno Agent Framework](https://github.com/n4ze3m/agno)
- 🧠 DuckDuckGo AI tools for research (optional)
- 🧾 Nutrition, dietary filters, cooking time, and cuisine detection
- 🐍 Python + Streamlit UI for easy deployment

---

## 🚀 Features

### ✅ Input Options:
- Upload an image of ingredients (from your kitchen or fridge)
- OR type ingredients manually (e.g., `chicken, tomato, onion`)

### 🍽️ AI Output:
- Recipe name based on ingredients
- Estimated ingredient quantities
- Step-by-step cooking instructions
- Total preparation & cooking time
- Nutrition facts:
  - Calories
  - Protein
  - Fat
  - Carbohydrates

### 🌎 Filters:
- Cuisine: Indian, Italian, Chinese, Mexican, etc.
- Dietary: Vegetarian, Vegan, Gluten-Free, Halal, Keto

---

## 🧑‍💻 How It Works

This app uses **Google Gemini 2.0 Flash** via the [Agno agent framework](https://github.com/n4ze3m/agno) to analyze the ingredients and generate a rich, beginner-friendly recipe. The recipe is formatted in Markdown for clarity and can include research and facts using DuckDuckGo search.

---


## 🔧 Setup Instructions

1. **Clone this repo** or copy the code file:

```bash
git clone https://github.com/faisalshahzadnadeem /smart-recipe-generator.git
cd smart-recipe-generator
