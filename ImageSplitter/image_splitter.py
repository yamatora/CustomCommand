import os
import sys
from PIL import Image # pip install pillow

def get_split_images(image, xnum, ynum):
    # division num
    w_split = image.width/xnum
    h_split = image.height/ynum

    # left -> right : top -> bottom
    results = []
    for y in range(ynum):
        for x in range(xnum):
            left = x * w_split
            top = y * h_split
            crop = image.crop((left, top, left + w_split, top + h_split))
            results.append(crop)

    return results

def main(args):
    # check dir
    if not os.path.exists('./output'):
        print('make dir')
        os.makedirs('./output')

    # var
    path_input = args[1]
    base_name = os.path.splitext(os.path.basename(path_input))[0]
    x_num = int(args[2])
    y_num = int(args[3])

    # load
    image = Image.open(path_input)
    # split
    results = get_split_images(image, x_num, y_num)
    # save images
    for i in range(len(results)):
        results[i].save(f'./output/{base_name}{i:03}.jpg')
    print(f'output {len(results)} images')

if __name__ == '__main__':
    args = sys.argv
    try:
        main(args)
    except:
        print('error: invalid args')