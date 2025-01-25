import numpy as np
from PIL import Image


with open('select=3.txt', 'r') as file:
    data = file.read()


pixel_values = [int(value, 16) for value in data.split()]

width = 256
height = 256


image_array = np.array(pixel_values, dtype=np.uint8).reshape((height, width))


image = Image.fromarray(image_array)


image.save('select=3output.png')
print("Image saved as select=3output.png")
