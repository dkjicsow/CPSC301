from PIL import Image

im = Image.open("baboon.png")

width = im.size[0]
height = im.size[1]

for i in range(height):
    im.putpixel((width//2, i), (0, 0, 0))

im.save("baboon_sample.png")

