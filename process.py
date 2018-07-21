import numpy as np
import cv2

#for list of files to process
from os import listdir
from os.path import isfile, join

#for plotting
from matplotlib import pyplot as plt

#our local modules
import find_skin as skin
import detect_faces as faces

data_path = 'data_processed_1'
images_to_process = [f for f in listdir(data_path) if isfile(join(data_path, f))]

print(len(images_to_process))
print(images_to_process)

#process all images and save to new directory if does not yet exist
for filename in images_to_process:

    #set image path
    image_path = "{}/{}".format(data_path, filename))

    #create and store output directory path
    output_dir = "processed_images"
    os.mkdir(output_dir, 755) if !os.path.isdir(output_dir) else print(output_dir)

    #
    original = cv2.imread(image_path)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    newimg = skin.find_skin(image_path)
    newimg = skin.show_skin(image_path)

#newimg = faces.detect_faces(image_path)
#newimg = cv2.cvtColor(newimg, cv2.COLOR_BGR2RGB)




"""
math.ceil(math.sqrt(IMAGES.COUNT))
int(numpy.ceil(numpy.sqrt(IMAGES.COUNT)))

"""
"""
FOR EACH IMAGE FROM IMAGES
    new = process_image_with_1(IMAGE)
    plot(new)
    process_image_with_2(IMAGE)
"""


"""
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(imgSkin), plt.title('Transformed YCbCr Skin Image'), plt.xticks([]), plt.yticks([])
plt.show()
"""
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
plt.title('Newww')
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
