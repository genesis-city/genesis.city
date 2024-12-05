from email.mime import image
from operator import truediv
import os
from PIL import Image

def main(image_src, image_dst):
    # preprocess.py start
    for count, filename in enumerate(os.listdir(image_src)):
        if 'DS_Store' in filename or 'Thumbs' in filename:
            continue
        n = 5
        zoom = 6
        pad = 30 #(2**zoom) / 2
        x, y = tuple(int(d) for d in filename.split(".")[0].split(","))
        dst = str(int(pad+(x//n))) + "," + str(int(pad-(y//n))) + ".jpg"
        src = image_src + '/' + filename
        dst = image_dst + str(zoom) + "/" + dst
        im = Image.open(src)
        print(src, "->", dst)
        im.save(dst)
    # preprocess.py end

    images = []
    size = 4
    original_side = 61
    full_image_size = 512
    half_image_size = int(full_image_size / 2)
    
    for zoomLevel in range(5, 0, -1):
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
                if os.path.isfile(image_dst + str(zoomLevel + 1) + '/' + path):
                    images.append(Image.open(image_dst + str(zoomLevel + 1) + '/' + path))
                else:
                    images.append(Image.new('RGB', (half_image_size, half_image_size), (26, 26, 26)))

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
            save_name = image_dst + str(zoomLevel) + '/' + str(int(x / 2)) + ',' + str(int(y / 2)) + '.jpg'
            new_im.save(save_name)
            print('Saved: ' + save_name)
        original_side = original_side / 2

if __name__ == '__main__':
    # Process Day Images
    main('raw', 'map/latest/')
    # Process Night Images
    main('raw-night', 'map-night/latest/')