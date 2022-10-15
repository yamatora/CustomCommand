import os
import sys
from unittest import result
from PIL import Image # pip install pillow

def get_filled_image(image, ratio):
    # create image
    w_dst = int(image.width * (1.0/ratio))
    # dst = Image.new('RGB', (w_dst, image.height), (255, 255, 255))    # 白埋め
    dst = Image.new('RGBA', (w_dst, image.height), (0, 0, 0, 0))        # 透明

    # paste
    xpos = int((w_dst - image.width)/2)
    dst.paste(image, (xpos, 0))
    return dst

def main(args):
    # var
    path_input = args[1]
    base_name = os.path.splitext(os.path.basename(path_input))[0]
    percentage = int(args[2])
    ratio = float(percentage) / 100.0

    # load
    image = Image.open(path_input)
    # split
    result = get_filled_image(image, ratio)
    # save images
    fname = f'./{base_name}_filled.png'
    result.save(fname)
    print(f'output "{fname}"')

if __name__ == '__main__':
    args = sys.argv
    try:
        main(args)
    except:
        print('error: invalid args')
