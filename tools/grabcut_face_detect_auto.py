#!/usr/bin/env python


# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import sys
import time
ts = int(time.time())
import tools.detect_faces as faces

BLUE = [255,0,0]        # rectangle color
RED = [0,0,255]         # PR BG
GREEN = [0,255,0]       # PR FG
BLACK = [0,0,0]         # sure BG
WHITE = [255,255,255]   # sure FG

DRAW_BG = {'color' : BLACK, 'val' : 0}
DRAW_FG = {'color' : WHITE, 'val' : 1}
DRAW_PR_FG = {'color' : GREEN, 'val' : 3}
DRAW_PR_BG = {'color' : RED, 'val' : 2}

# setting up flags
rect = (0, 0, 1, 1)
drawing = False         # flag for drawing curves
rectangle = False       # flag for drawing rect
rect_over = False       # flag to check if rect drawn
rect_or_mask = 100      # flag for selecting rect or mask mode
value = DRAW_FG         # drawing initialized to FG
thickness = 3           # brush thickness

'''
input: STRING image path
output: IMAGE processed image
'''


def cutout_face(image_path):

    face_rect, rectangle, portrait = faces.get_rects(image_path)
    if not portrait:
        return [], False
    img = cv.imread(image_path)
    print(face_rect)
    img2 = img.copy()                               # a copy of original image

    mask = np.zeros(img.shape[:2], dtype=np.uint8) # mask initialized to PR_BG

    output = np.zeros(img.shape, np.uint8)           # output image to be sho

    bgdmodel = np.zeros((1,65),np.float64)
    fgdmodel = np.zeros((1,65),np.float64)


    # cv.rectangle(img,rectangle[0],rectangle[1],BLUE,2)

    # use grabCut to remove background of image
    cv.grabCut(img2,mask,face_rect,bgdmodel,fgdmodel,1,cv.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==1) + (mask==3),255,0).astype('uint8')
    output = cv.bitwise_and(img2,img2,mask=mask2)

    #cv.imwrite(f"grab_cut_tests/{ts}.{filename[8:]}.0.output.png", output)

    return output, True
