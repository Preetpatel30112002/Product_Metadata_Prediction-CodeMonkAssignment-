import streamlit as st
import requests
from PIL import Image
import io

# Flask API URL
FLASK_API_URL = "http://127.0.0.1:9000/predict"

st.title("Fashion Attribute Prediction")

# Upload Image
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "png", "jpeg", "webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes.seek(0) 
    if st.button("Predict Fashion Attributes"):
        files = {"image": ("image.jpg", img_bytes, "image/jpeg")}
        
        try:
            # Send request to Flask API
            response = requests.post(FLASK_API_URL, files=files, timeout=30)  # Increased timeout
            response.raise_for_status()  # Raise error for HTTP failures

            try:
                result = response.json()
                st.success(" Prediction Successful!")
                st.write(f"**Base Colour:** {result.get('baseColour', 'N/A')}")
                st.write(f"**Article Type:** {result.get('articleType', 'N/A')}")
                st.write(f"**Season:** {result.get('season', 'N/A')}")
                st.write(f"**Gender:** {result.get('gender', 'N/A')}")
            except requests.exceptions.JSONDecodeError:
                st.error("Error: Invalid JSON response from server.")
                st.text(response.text)  # Show raw response for debugging

        except requests.exceptions.RequestException as e:
            st.error(f"Connection Error: {e}")