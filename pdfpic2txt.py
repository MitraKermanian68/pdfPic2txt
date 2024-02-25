from pytesseract import *
from pdf2image import convert_from_path
import glob

pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

images = glob.glob(r"C:\Users\User\Desktop\mitra11111\pdf to jpg\introduction to orientalism\*.jpg")
for img in images:
    image_text = pytesseract.image_to_string(img)
    with open(f'{img}.txt', 'w') as the_file:
        the_file.write(image_text)