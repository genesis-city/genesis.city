import os

from PIL import Image


def main():
    for count, filename in enumerate(os.listdir("raw")):
        if 'DS_Store' in filename or 'Thumbs' in filename:
            continue
        n = 5
        zoom = 6
        pad = 30 #(2**zoom) / 2
        x, y = tuple(int(d) for d in filename.split(".")[0].split(","))
        dst = str(int(pad+(x//n))) + "," + str(int(pad-(y//n))) + ".jpg"
        src = 'raw/' + filename
        dst = 'map/latest/' + str(zoom) + "/" + dst
        
        if (os.path.isfile(dst)):
            print("skipping", dst)
            continue

        im = Image.open(src)
        
        print(src, "->", dst)

        im.save(dst)


if __name__ == '__main__':
    main()
