# import
from PIL import Image

# open image
circle_img = Image.open('img/circle.png')

# convert image
circle_img = circle_img.convert('RGBA')

# load pixel data
pixels = circle_img.load()

# iterate through the image to remove background
for i in range(circle_img.width):
    for j in range(circle_img.height):
        # if current pixel is white, change it to transparent
        r, g, b, a = pixels[i, j]
        if r > 0:
            # replace with transparent pixel
            pixels[i, j] = (0, 0, 0, 0)


# save
circle_img.save('img/circle_bg.png')

# close
circle_img.close()