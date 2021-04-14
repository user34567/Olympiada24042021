from PIL import Image
import pytesseract
import numpy
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = Image.open("D:\\Python_project\\text.png")
text = pytesseract.image_to_string(im,lang = "eng")
print(text)