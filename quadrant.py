from PIL import Image

def off(pixels, channel_off):
    rgb = image.getpixel(pixels)
    rgb = list(rgb)
    rgb[channel_off] = 0
    rgb = tuple(rgb)
    return rgb  

image = Image.open("test_image.jpg")

width = image.size[0]
height = image.size[1]

for x in range(width):
    for y in range(height):
        if x <= (width/2) and y <= (height/2):
            no_red = off((x,y), 0)
            image.putpixel((x,y), no_red)
        elif x > (width/2) and y > (height/2):
            no_red = off((x,y), 0)
            image.putpixel((x,y), no_red)
            no_rb = off((x,y), 2)
            image.putpixel((x,y), no_rb)
        elif x <= (width/2) and y > (height/2):
            no_green = off((x,y), 1)
            image.putpixel((x,y), no_green)
            
            
image.save("quadrant_image.png")