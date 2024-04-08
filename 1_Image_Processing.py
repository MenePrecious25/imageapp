import streamlit as st
import numpy as np
import io
import cv2
from PIL import Image, ImageEnhance
# from Home import image_uploader
from Home import blur_image
from Home import brightness
from Home import compress_image


def image_uploader(img):
    try:
        pilimage = Image.open(img)
        st.text("Original Image")
        return st.image(pilimage)
    except:
        return None

def convert_rgb(imag):
    return pilimage.convert('RGB')
image_file = st.file_uploader("Upload Image", type=['jpeg', 'png', 'jpeg'])

pilimage = image_uploader(image_file)
# data = cv2.imread(pilimage)
# st.write(data)
# data = np.array(pilimage)
if image_file is not None:
    enhance_type = st.sidebar.selectbox('Enhance Type', ['Original', 'Gray-Scale', 'Contrast', 'Blur', 'Brightness', 'Compress', 'Create GiFF'])
    if enhance_type == "Gray-Scale":
        if st.button('Process'):
            pilimage = Image.open(image_file)
            our_img = np.array(convert_rgb(pilimage))
            img1 = cv2.cvtColor(our_img, 1)
            gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            st.write('Gray-Scale Image')
            st.image(gray_image)
    elif enhance_type == 'Contrast':
        c_rate = st.sidebar.slider('Contrast', 1, 10)
        if st.button('Process'):
            image = Image.open(image_file)
            enhance = ImageEnhance.Contrast(image)
            img_output = enhance.enhance(c_rate)
            st.image(img_output)
    elif enhance_type == 'Blur':
        b_rate = st.sidebar.slider('Blur', 1, 11, step = 2)
        if st.button('Process'):
            pilimage = Image.open(image_file)
            our_img = np.array(convert_rgb(pilimage))
            blur_img = blur_image(our_img, b_rate)
            st.write('Blurred Image')
            st.image(blur_img, caption=f'Blurred Image (Blur Radius: {b_rate})', use_column_width=True)

            

    elif enhance_type == 'Brightness':
        # right = (0.5, 1.0, 1.5, 2.0)
        bright = st.sidebar.slider('Brightness', 1.0, 3.5)
        if st.button('Process'):
            # Convert PIL image to OpenCV format

            processed_image = brightness(pilimage, bright)
            # Display processed image
            
            st.image(processed_image, caption=f'Processed Image (Blur Radius: {bright})')
            
    elif enhance_type == 'Compress':
        quality = st.sidebar.slider("Select Compression Quality (1-100)", 1, 100, 20)
        if st.button('Process'):
            compressed = compress_image(image_file, quality=quality)
            st.image(compressed, caption='Compressed Image')



