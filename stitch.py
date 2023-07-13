from PIL import Image
import os

side = 100
result_side = 61*side
maxsize = (side, side)
result_size = (result_side, result_side)

def merge_images(result, folder, file1, x, y):
    with Image.open(folder + "/" + file1) as im:
        im.thumbnail(maxsize)
        result.paste(im=im, box=(x*side, y*side))


result_day = Image.new('RGB', result_size)
result_night = Image.new('RGB', result_size)

# Process day images
print("Processing day images . . .")
for count, input_img_path in enumerate(os.listdir("map/latest/6")):
    if 'DS_Store' in str(input_img_path):
        continue
    x, y = tuple(int(d) for d in input_img_path.split(".")[0].split(","))
    print(x, y)
    merge_images(result_day, "map/latest/6", input_img_path, x, y)

# Process night images
print("Processing night images . . .")
for count, input_img_path in enumerate(os.listdir("map-night/latest/6")):
    if 'DS_Store' in str(input_img_path):
        continue
    x, y = tuple(int(d) for d in input_img_path.split(".")[0].split(","))
    print(x, y)
    merge_images(result_night, "map-night/latest/6", input_img_path, x, y)

result_day.save("full/day.png", "png")
print("Full day image saved > full/day.png")
result_night.save("full/night.png", "png")
print("Full night image saved > full/night.png")
