import streamlit as st
import cv2
import numpy as np
import PIL
from PIL import Image


def dodge(x, y):
  return cv2.divide(x, 255-y, scale=256)


def pencilsketch(input_image):
    img_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21,21),sigmaX = 0, sigmaY = 0)
    final_img_sketch = dodge(img_gray, img_smoothing)
    return(final_img_sketch)


st.title("PHOTO TO SKETCH :pencil:") 
st.write("Convert Your Beautiful Photos to Amazinng Pencil Sketches")
st.write("You can Now Upload or even click the photo which you want to convert in sketch")
st.write("Photo uploader present in sidebar")

file_image = st.sidebar.file_uploader("upload your photo",type = ['jpeg','jpg','png'])

if file_image is None:
    st.write("No image uploaded as of now")
else:
    input_img = Image.open(file_image)
    final_img_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("Photo Uploaded")
        st.image(file_image,use_column_width=True)
    
    with two:
        st.write("Sketch")
        st.image(final_img_sketch,use_column_width=True)

    st.write("Check out this [link](https://www.linkedin.com/in/luckshaya-kem/)")

file_image_1 = st.camera_input(label = "Click a pic for Sketch",)

if file_image_1 is None:
    st.write("No image uploaded as of now")
else:
    input_img = Image.open(file_image_1)
    final_img_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("Photo Uploaded")
        st.image(file_image_1,use_column_width=True)
    
    with two:
        st.write("Sketch")
        st.image(final_img_sketch,use_column_width=True)

    st.write("Check out this [link](https://www.linkedin.com/in/luckshaya-kem/)")