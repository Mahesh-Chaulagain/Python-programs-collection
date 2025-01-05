from PIL import Image
from tkinter.filedialog import *

fl = askopenfilenames()
img = Image.open(fl[0])
img.save("co.jpg", "JPEG", optimize = True,quality = 10)
Image.open("co.jpg")