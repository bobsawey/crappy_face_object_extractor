import numpy as np
import cv2
from matplotlib import pyplot as plt

import find_skin as skin
import detect_faces as faces

original, newimg = skin.find_skin('data_processed_1/1.png')
original, newimg = faces.detect_faces('data_processed_1/1.png')

plt.subplot(121)
plt.imshow(original)
plt.title('Original')
plt.subplot(122)
plt.imshow(newimg)
plt.title('News')
plt.show()
#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
#  Find skin module
#
#
# !/usr/bin/env python
# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        test
# Author:      xiezhanghua (xiezhanghua111@j163.com)
# Created:     2017/8/13下午12:06
# -------------------------------------------------------------------------------
