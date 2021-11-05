from PIL import Image
import pathlib
maxsize = (400, 400)
for input_img_path in pathlib.Path("map").iterdir():
    with Image.open(input_img_path) as im:
        w,h = im.size
        if (w,h) != maxsize:
            print(input_img_path, w,h)
