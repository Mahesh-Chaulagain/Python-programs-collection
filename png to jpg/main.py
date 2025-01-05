from PIL import Image

# input image in png format
im = Image.open("1.png")
rgb_im = im.convert("RGB")

# output image in jpeg format
rgb_im.save("1.jpg")