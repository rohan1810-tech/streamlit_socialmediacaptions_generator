import streamlit as st
import google.generativeai as genai

st.title("Social Media Caption Generator")

# Load API key safely
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

description = st.text_input("Enter product/service description")
tone = st.selectbox("Select tone", ["Witty", "Professional", "Casual"])

if st.button("Generate Captions"):
    prompt = f"""
    Write 3 social media captions under 30 words.
    Tone: {tone}
    Topic: {description}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    st.write("### Captions:")
    st.write(response.text)
