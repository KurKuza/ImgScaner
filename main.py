import pytesseract
from PIL import Image

img = Image.open('./img/photo-timetable.png')

# For Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# ----
custom_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
# custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang= 'rus', config=custom_config)
print(text)