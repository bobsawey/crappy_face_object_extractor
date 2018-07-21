import numpy as np
import cv2
from matplotlib import pyplot as plt

import find_skin as skin
import detect_faces as faces

image_path = 'data_processed_1/1.png'
original = cv2.imread(image_path)
newimg = skin.find_skin(image_path)


#newimg = faces.detect_faces(image_path)



"""

cv2.imwrite('detect2.png',image)
cv2.imshow("Output", image)
cv2.waitKey(0)
"""

plt.subplot(121)
plt.imshow(original)
plt.title('Original')
plt.subplot(122)
plt.imshow(newimg)
plt.title('News')
plt.show()
""""""
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
