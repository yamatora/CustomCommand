from email.mime import image
from posixpath import basename
from PIL import Image # pip install pillow
import os
import sys

from datetime import datetime

def img_split(image, xnum, ynum):
    # 読み込んだ画像を200*200のサイズで54枚に分割する
    w_split = image.width/ynum
    h_split = image.height/xnum

    results = []

    for x in range(xnum):
        for y in range(ynum):
            left = x * w_split
            top = y * h_split
            crop = image.crop((left, top, left + w_split, top + h_split))
            results.append(crop)

    return results

    # # 縦の分割枚数
    # for h1 in range(3):
    #     # 横の分割枚数
    #     for w1 in range(3):
    #         w2 = h1 * width
    #         h2 = w1 * height
    #         # print(w2, h2, width + w2, height + h2)
    #         c = im.crop((w2, h2, width + w2, height + h2))
    #         buff.append(c)
    # return buff

if __name__ == '__main__':
    if not os.path.exists('./output'):
        print('make dir')
        os.makedirs('./output')

    args = sys.argv
    path_input = args[1]
    base_name = os.path.splitext(os.path.basename(path_input))[0]
    x_num = int(args[2])
    y_num = int(args[3])

    # 画像の読み込み
    image = Image.open(path_input)
    results = img_split(image, x_num, y_num)
    for i in range(len(results)):
        # 保存先フォルダの指定
        #img.save("./output/out" + datetime.now().strftime("%Y%m%d_%H%M%S%f_") +".jpg", "JPEG")
        # print(f'./output/{base_name}_{i:03}.jpg')
        results[i].save(f'./output/{base_name}{i:000}.jpg')