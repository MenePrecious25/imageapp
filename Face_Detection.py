import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import streamlit as st
from Home import image_uploader


st.subheader("Face Detection")
def main():        
    image_file = st.file_uploader("Upload Image", type=['jpeg', 'png', 'jpeg'])
    if image_file is not None:
        image_uploader(image_file)
        activities = ['Detection', 'RealTime Face Capture', 'Passport snap']
        choice = st.sidebar.selectbox("Select Activity", activities)
        if choice == 'Detection':
            detect_type = st.sidebar.radio('Detect Type', ['Original', 'Face Detection', 'Eyes Detection', 'Nose Detection'])



        elif choice == "RealTime Face Capture":
            pass
        elif choice == "Passport snap":
            pass




if __name__ =='__main__':
    main()
