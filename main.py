import sys
import os
from PIL import Image

images_path = sys.argv[1]
output_path = sys.argv[2]

if not os.path.exists(output_path):
    os.mkdir(output_path)

for file in os.listdir(images_path):
    image = Image.open(f"{images_path}{file}")
    image_name = os.path.splitext(file)[0]
    image.save(f"{output_path}{image_name}.png", "PNG")
    print(f"{image_name}.png created")
