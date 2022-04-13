from distutils.log import warn
from email.mime import image
from tkinter import Scale
import cv2
import numpy as np
from numpy import linalg as la
import math

SCALE = 10

# Perlin noise
def test():
    return 10
def get_perlin_noise(width, height):
    # color = np.zeros((height, width, ch), np.uint8)
    image = np.zeros((height, width), np.uint8)     # gray
    for y in range(height):
        for x in range(width):
            res = __get_perlin(x,y)
            if not (0 <= res <= 1):
                print(f'x: {x}\ty: {y}\t{res}')
            val = int(res * 255)
            image[y, x] = val
    return image

def __dummy(_u, _v):
    print('')
def __get_perlin(_u, _v):
    vec = __vec2(_u, _v)
    # def
    #p = np.floor(vec)
    p = (vec - (vec % SCALE)) # local原点
    f = (vec % SCALE)         # local座標
    #print(f)
    # u = f*f*(3.0-2.0*f)
    u = f / SCALE
    # random vector 疑似乱数
    #print(p)
    v00 = __random2(p+__vec2(  0.0,   0.0))
    v01 = __random2(p+__vec2(  0.0, SCALE))
    v10 = __random2(p+__vec2(SCALE,   0.0))
    v11 = __random2(p+__vec2(SCALE, SCALE))
    #print(v00)
    # calc 中央からのベクトルと内積をとる
    da = np.dot(v00, f-__vec2(  0.0,   0.0))
    db = np.dot(v10, f-__vec2(  SCALE,   0.0))
    la = lerp(da, db, u[0]) # 左上, 右上
    dc = np.dot(v01, f-__vec2(  0.0, SCALE))
    dd = np.dot(v11, f-__vec2(SCALE, SCALE))
    lb = lerp(dc, dd, u[0]) # 左下, 右下
    # if f[0] == 0 and f[1] == 0:
    #     print(da)

    #print(f'{la}\t{lb}')
    # result
    return lerp(la, lb, u[1]) / SCALE + 0.5 # 上下

def lerp(a, b, r):
    if not (0 <= r <= 1):
        warn('ratio: out of range\r\n r: 0 <= r <= 1')
    return (1-r)*a + r*b

def __random2(vec):
    v0 = np.dot(vec, __vec2(127.1, 311.7))
    v1 = np.dot(vec, __vec2(269.5, 183.3))
    #result = -1.0 + 2.0*__frac(np.sin(__vec2(v0, v1))*43758.5453123)   # -1.0~1.0
    result = __frac(np.sin(__vec2(v0, v1))*43758.5453123)   # 0.0~1.0
    #result = __vec2(1, 1)
    return result
def __vec2(x, y):
    return np.array([x, y])
def __frac(val):
    return val - np.floor(val)
