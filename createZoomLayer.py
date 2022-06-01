from email.mime import image
from operator import truediv
import os
from PIL import Image

def main():
    images = []
    size = 4
    original_side = 61
    full_image_size = 512
    half_image_size = int(full_image_size / 2)
    grouped = []

    for i in range(int((original_side) / 2) + 1):
        for j in range(int((original_side) / 2) + 1):
            x = int(i * size / 2)
            y = int(j * size / 2)
            c1 = str(x) + ',' + str(y) + '.jpg'
            c2 = str(x+1) + ',' + str(y) + '.jpg'
            c3 = str(x) + ',' + str(y+1) + '.jpg'
            c4 = str(x+1) + ',' + str(y+1) + '.jpg'
            grouped.append([c1, c2, c3, c4])
            exit
        exit
    
    for group in grouped:
        new_im = Image.new('RGB', (full_image_size, full_image_size))

        images = []
        for path in group:
            if os.path.isfile("map/latest/6/" + path):
                images.append(Image.open("map/latest/6/" + path))
            else:
                images.append(Image.new('RGB', (half_image_size, half_image_size), (112, 112, 112)))

        for index, image in enumerate(images):
            im = image.resize((int(half_image_size), int(half_image_size)))
            match index:
                case 0:
                    new_im.paste(im, (0, 0))
                case 1:
                    new_im.paste(im, (half_image_size, 0))
                case 2:
                    new_im.paste(im, (0, half_image_size))
                case 3:
                    new_im.paste(im, (half_image_size, half_image_size))

        x, y = tuple(int(d) for d in group[0].split(".")[0].split(","))
        save_name = 'map/latest/5/' + str(int(x / 2)) + ',' + str(int(y / 2)) + '.jpg'
        new_im.save(save_name)
        print('Saved: ' + save_name)

if __name__ == '__main__':
    main()