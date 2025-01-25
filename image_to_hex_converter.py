from PIL import Image
import numpy as np


image_path = 'output_image.png'  
output_file = 'output_hex.txt'


image = Image.open(image_path).convert('L')


image = image.resize((128, 128))


image_array = np.array(image)


pixel_values = image_array.flatten()


hex_values = [format(value, '02x') for value in pixel_values]


with open(output_file, 'w') as file:
    file.write(' '.join(hex_values)) 

print(f"Hexadecimal values saved to {output_file}")
