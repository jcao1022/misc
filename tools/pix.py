from PIL import Image
import pytesseract

# text = pytesseract.image_to_string(Image.open(r"C:\Users\jcao\Desktop\1.png"), lang='chi_sim')
# print(text)

im = Image.open(r"1.png")

print(im.format, im.size, im.mode)











