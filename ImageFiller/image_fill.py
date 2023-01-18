import os
import sys
from unittest import result
from PIL import Image # pip install pillow
from argparse import ArgumentParser

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
    path_input = os.path.abspath(args.image)
    base_name = os.path.splitext(os.path.basename(path_input))[0]
    percentage = int(args.percentage)
    ratio = float(percentage) / 100.0

    # load
    image: Image = Image.open(path_input)
    # split
    result = get_filled_image(image, ratio)
    # save images
    if args.overwrite:  # 上書き
        fname = path_input
        backup = f"./{base_name}_base.png"
        if not os.path.exists(backup):
            image.save(backup)
    else:               # 別名
        fname = f"./{base_name}_filled.png"
    result.save(fname)
    print(f'output "{fname}"')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("image", help="base image")
    parser.add_argument("percentage", type=int, help="ratio of base image")
    parser.add_argument("-o", "--overwrite", action="store_true", help="Whether overwrite or not")
    option = parser.parse_args()
    try:
        main(option)
    except:
        print('error: invalid args')