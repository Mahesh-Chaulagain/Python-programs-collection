import pyqrcode
from PIL import Image

link = input("Enter anything to generate QR:")
qr_code = pyqrcode.create(link)
qr_code.png("QRcode.png", scale=5)
img = Image.open("QRcode.png")
img.show()  # Opens the generated QR code image using the default image viewer
