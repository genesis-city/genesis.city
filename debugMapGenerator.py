import os
from PIL import Image

def main():
    targetGridSize = 30
    zoomFolder = 5
    full_image_size = 512
    color = (255, 180, 180)
    
    new_im = Image.new('RGB', (full_image_size, full_image_size), color)

    for x in range(targetGridSize + 1):
        for y in range(targetGridSize + 1):
            save_name = 'map/latest/' + str(zoomFolder) + '/' + str(x) + ',' + str(y) + '.jpg'
            new_im.save(save_name)
            print('Saved: ' + save_name)

if __name__ == '__main__':
    main()