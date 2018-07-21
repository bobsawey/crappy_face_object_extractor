import numpy as np
import cv2
import itertools
#random words for filenames
from random_word import RandomWords


#for list of files to process
from os import listdir
from os import mkdir
from os import chown
from os import chmod
from os.path import isfile, join, isdir
import pwd
import grp

#for plotting
from matplotlib import pyplot as plt
import matplotlib as mpl

#our local modules
import find_skin as skin
import detect_faces as faces
import autocanny

data_path = 'data_processed_1'
mpl.rcParams['savefig.pad_inches'] = 0
images_to_process = [f for f in listdir(data_path) if isfile(join(data_path, f))]

#process all images and save to new directory if does not yet exist
for filename in images_to_process:

    def plot_image(ax, processed_image, fontsize=12, nodec=False):
        ax.plot([1, 2])
        ax.imshow(processed_image)

        ax.locator_params(nbins=3)
        if not nodec:
            ax.set_xlabel('x-label', fontsize=fontsize)
            ax.set_ylabel('y-label', fontsize=fontsize)
            ax.set_title('Title', fontsize=fontsize)
        else:
            ax.set_xticklabels('')
            ax.set_yticklabels('')

    #set image path
    image_path = "{}/{}".format(data_path, filename)

    #create and store output directory path
    output_dir = "processed_images"

    #random word for filenames
    r = RandomWords()

    #get random word for filenames
    filename_random_word = r.get_random_word()

    #output_filname_and_path
    output_path_and_filename = "{}/{}.{}".format(output_dir, filename_random_word, filename )
    print(output_path_and_filename)


    #variables for chowning after creating the directory
    uid = pwd.getpwnam("normalcereal").pw_uid
    gid = grp.getgrnam("normalcereal").gr_gid

    #mkdir(output_dir, 493)
    chown(output_dir, uid, gid)
    chmod(output_dir, 493)
    #

    fig, axs = plt.subplots(4, 4, constrained_layout=True)

    count = 0

    # Note on axs.flatten():
        # axs is an array([1,2,3,4],[5,6,7,8],...[13,14,15,16])
            # this is because subplots are 4,4
        # to make the array 16 items long, we use axs.flatten()

    switcher = {
            1: skin.find_skin(image_path),
            2: skin.show_skin(image_path),
            3: faces.detect_faces(image_path)(image_path),
            4: autocanny.auto_canny(image_path,0), # 0 = wide_canny
            5: autocanny(image_path,1), # 1 = tight_canny
            6: autocanny(image_path,2), # 2 = auto_canny
            7: cv2.imread(image_path),
            8: cv2.imread(image_path),
            9: cv2.imread(image_path),
            10: cv2.imread(image_path),
            11: cv2.imread(image_path),
            12: cv2.imread(image_path),
            13: cv2.imread(image_path),
            14: cv2.imread(image_path),
            15: cv2.imread(image_path),
            16: cv2.imread(image_path),
        }
    for ax in axs.flatten():
        count+=1
        print(count)
        #run one of 16 processes on each image
        new_image = switcher.get(count, lambda:"invalid image processor")

        plot_image(ax, new_image ,nodec=True)
        ax.set_xticklabels('')
        ax.set_yticklabels('')
    fig.set_constrained_layout_pads(w_pad=4./72., h_pad=4./72.,
            hspace=0., wspace=0.)



    '''
    plt.autoscale(tight=True)
    plt.rcParams['savefig.facecolor'] = ".3"
    plt.subplot(441)
    plt.subplots_adjust(hspace = .001)
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(original)
    plt.title('Original')
    plt.subplot(442)
    plt.subplots_adjust(hspace = .001)
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(newimg)
    plt.title('Newww')
    plt.axis('off')
    plt.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
    '''
    plt.savefig(output_path_and_filename)
    plt.show()
    break
    #plt.show()

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

cv2.imwrite('detect2.png',iplt.imshow(original)
plt.title('Original')
plt.subplot(122)mage)
cv2.imshow("Output", image)
cv2.waitKey(0)
"""


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
