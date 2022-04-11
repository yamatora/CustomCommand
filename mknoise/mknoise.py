import sys
import cv2
import numpy as np

import noise_perlin as n_perlin
import noise_fbm as n_fbm

args = sys.argv

if 2 > len(args):
    print(f'Insufficient args: ex. $ python {args[0]} [width] [height]')
    exit()

width = int(args[1])
height = int(args[2])

print(f'make {width}x{height} noise')

# img = n_perlin.get_perlin_noise(width, height)
img = n_fbm.get_fbm_noise(width, height)

cv2.imwrite('C:\\Users\\yamada\\CustomCommands\\mknoise\\test.jpg', img)