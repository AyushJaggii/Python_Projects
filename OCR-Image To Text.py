# Importing necessary libraries
import pytesseract
import os
from PIL import Image

# Setting the path for Tesseract OCR software
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    img = Image.open(r'E:\1. Tech\Python - Vs Code\Projects\OCR- Image to Text\download.jpeg')       # Opening the image file using PIL library
    text = pytesseract.image_to_string(img)                                                         # Using Tesseract OCR to extract text from the image

    print(text)

convert()