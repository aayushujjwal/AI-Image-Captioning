# pip install streamlit
# pip install transformers
# pip install Pillow
# !pip install streamlit
# !pip install tensorflow
# !pip install pillow
# !pip installl transformers
# !pip install tf-keras
import transformers
import PIL
import streamlit as st
# from transformers import pipeline
# from PIL import Image

# Create the caption pipeline
caption = transformers.pipeline("image-to-text", model="ydshieh/vit-gpt2-coco-en")

# Display the image using Streamlit
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_image is not None:
    image = PIL.Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate the caption
    if st.button("Generate Caption"):
        captions = caption(image)
        st.write(captions[0]["generated_text"])
