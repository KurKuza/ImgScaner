import pytesseract
from PIL import Image

img = Image.open('./img/photo-timetable.png')

# For Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# ----
tessdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'

text = pytesseract.image_to_string(img, lang= 'rus', config=tessdata_dir_config)
print(text)