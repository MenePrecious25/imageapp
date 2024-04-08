# Importing the required libraries

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from PIL import Image, ImageEnhance
import io
import streamlit as st

st.set_page_config(
    page_title="Image Processing App",
)



def image_uploader(img):
    try:
        pilimage = Image.open(img).convert("RGB")
        st.text("Original Image")
        return st.image(pilimage)
    except:
        return None



def blur_image(image, blur):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (blur, blur), 0)
    return blurred_image


def brightness(image, bright):
    # Create an enhancer object
    enhancer = ImageEnhance.Brightness(image)

    # Increase the brightness by the specified factor
    bright_image = enhancer.enhance(bright)
    
    return bright_image




def compress_image(input_image, quality=20):
    # Read the image
    image = cv2.imdecode(np.frombuffer(input_image.read(), np.uint8), 1)
    
    # Convert the image to JPEG format with specified quality
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, buffer = cv2.imencode('.jpg', image, encode_param)
    
    return buffer.tobytes()
