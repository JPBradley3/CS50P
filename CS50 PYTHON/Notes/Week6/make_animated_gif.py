#### Python can use binary files like

#### This program creates an animated GIF file
import sys

#### This is PILLOW a framework that allow us to work with data of many types because it translates it to binary.
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

