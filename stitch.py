from PIL import Image
import os

side = 100
result_side = 61*side
maxsize = (side, side)
result_size = (result_side, result_side)

def merge_images(result, file1, x, y):
    with Image.open("map/latest/6/"+file1) as im:
        im.thumbnail(maxsize)
        result.paste(im=im, box=(x*side, y*side))


result = Image.new('RGB', result_size)
for count, input_img_path in enumerate(os.listdir("map/latest/6")):
    if 'DS_Store' in str(input_img_path):
        continue
    x, y = tuple(int(d) for d in input_img_path.split(".")[0].split(","))
    print(x, y)
    merge_images(result, input_img_path, x, y)

result.save("full/2020-12-25.png", "png")


