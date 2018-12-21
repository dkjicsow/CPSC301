from PIL import Image


def average_rgb(input_list):
    """(tuple)-> float
        
    It will calculate the average of the sum of the tuple or list.
    >>> average_rgb((0, 1, 1, 2, 2))
    1
    >>> average_rgb([0, 1, 1, 4, 4])
    2
    
    """
    list_in = list(input_list)
    total = len(list_in)
    sum = 0
    for i in list_in:
        sum += i
    average = float(sum/total)
    return average

image = Image.open("test_image.jpg")

width = image.size[0]
height = image.size[1]

for x in range(width):
    for y in range(height):
        get_colors = image.getpixel((x,y))
        new_grey = int(average_rgb(get_colors))
        new_colors = (new_grey, new_grey, new_grey)
        image.putpixel((x,y), new_colors)
    
image.save("grey_image.png")