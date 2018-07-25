import numpy as np
import cv2
import itertools
from random import shuffle
from itertools import product
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
import matplotlib.gridspec as gridspec

#our local modules
import find_skin as skin
import detect_faces as faces
import autocanny

data_path = 'data_processed_1'
mpl.rcParams['savefig.pad_inches'] = 0
images_to_process = [f for f in listdir(data_path) if isfile(join(data_path, f))]

current_count = 0
#process all images and save to new directory if does not yet exist

shuffle(images_to_process)
for filename in images_to_process:

    #set image path
    image_path = "{}/{}".format(data_path, filename)

    #original image
    original = cv2.imread(image_path)
    image_heap = cv2.imread(image_path)



    original = cv2.cvtColor(original, cv2.COLOR_RGB2BGR)
    gray_af = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    happy_tree = cv2.applyColorMap(gray_af, cv2.COLORMAP_HSV)
    sonic_fux = cv2.applyColorMap(gray_af, cv2.COLORMAP_RAINBOW)
    plt.rcParams['savefig.facecolor'] = "0.8"
    def plot_image(ax, fontsize=12, nodec=False):
        global image_heap

        #im sure this means *something*
        ax.plot([1, 2])

        #switches between processes to run on images
        switcher = {
                1: skin.find_skin(image_path),
                2: skin.show_skin(image_path),
                3: faces.detect_faces(image_path),
                4: autocanny.canny_op(image_path,0), # 0 = wide_canny
                5: autocanny.canny_op(image_path,1), # 1 = tight_canny
                6: autocanny.canny_op(image_path,2), # 2 = auto_canny
                7: cv2.cvtColor(original, cv2.COLOR_RGB2BGR),
                8: sonic_fux,
                9: happy_tree,
                #10: cv2.imread(image_path),
                #11: cv2.imread(image_path),
                #12: cv2.imread(image_path),
                #13: cv2.imread(image_path),
                #14: cv2.imread(image_path),
                #15: cv2.imread(image_path),
                #16: cv2.imread(image_path),
            }

        #assign new image based on an operation, see bove
        new_image = switcher.get(count, lambda:"invalid image processor")

        dr = RandomWords()

        #get random word for filenames
        rdmwd1 = dr.get_random_word()
        rdmwd2 = dr.get_random_word()
        indy_img_dir= "{}/{}.{}.{}.png".format("processed_images/individual_images",  filename, rdmwd1, rdmwd2 )




        #add new_image to this
        #ax.imshow(new_image)
        #no idea what this does
        ax.locator_params(nbins=3)

        status = cv2.imwrite(indy_img_dir, new_image)

        print("Image written to file-system : ",status)

        #no idea what this does
        if not nodec:
            ax.set_xlabel('x-label', fontsize=fontsize)
            ax.set_ylabel('y-label', fontsize=fontsize)
            ax.set_title('Title', fontsize=fontsize)

        #not a f_cking clue.
        else:
            ax.set_xticklabels('')
            ax.set_yticklabels('')

    #create and store output directory path
    output_dir = "processed_images"

    #random sonic_fuxword for filenames
    r = RandomWords()

    #get random word for filenames
    filename_random_word = r.get_random_word()

    #output_filname_and_path
    output_path_and_filename = "{}/{}.{}".format(output_dir, filename_random_word, filename )


    #variables for chowning after creating the directory
    uid = pwd.getpwnam("normalcereal").pw_uid
    gid = grp.getgrnam("normalcereal").gr_gid

    #mkdir(output_dir, 493)
    chown(output_dir, uid, gid)
    chmod(output_dir, 493)
    #

    fig, axs = plt.subplots(3, 3, constrained_layout=True)

    plt.rcParams['savefig.facecolor'] = "0.8"
    count = 0

    # Note on axs.flatten():
        # axs is an array([1,2,3,4],[5,6,7,8],...[13,14,15,16])
            # this is because subplots are 4,4
        # to make the array 16 items long, we use axs.flatten()

    #RUN A PLOT OF 9 IMAGES FOR EACH IMAGE
        # THEN SAVE
    for ax in axs.flatten():
        count+=1
        #run one of 9 processes on each image
        plot_image(ax, nodec=True)
        ax.set_xticklabels('')
        ax.set_yticklabels('')

    #SOME B_LLSH1T ABOUT CONSTRAINTS
    #fig.set_constrained_layout_pads(w_pad=4./72., h_pad=4./72.,
    #        hspace=0., wspace=0.)


    #make the bg gray and not total eyeball murde
    #save the fig with unique png name
    fig.set_size_inches(10,10);
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.savefig(output_path_and_filename)




    #plt.show()

    """
    - THIS IS TO GET A GRID LOOKING SWELL IF I REALLY START CARING THAT MUCH
    -
    fig = plt.figure(figsize=(8, 8))

    # gridspec inside gridspec
    outer_grid = gridspec.GridSpec(4, 4, wspace=0.0, hspace=0.0)

    for i in range(16):
        inner_grid = gridspec.GridSpecFromSubplotSpec(
          3, 3, subplot_spec=outer_grid[i], wspace=0.0, hspace=0.0)
        a, b = int(i/4)+1, i % 4+1
        for j, (c, d) in enumerate(product(range(1, 4), repeat=2)):
            ax = plt.Subplot(fig, inner_grid[j])
            ax.imshow(new_image)
            #ax.plot(*squiggle_xy(a, b, c, d))
            ax.set_xticks([])
            ax.set_yticks([])
            fig.add_subplot(ax)

    all_axes = fig.get_axes()

    # show only the outside spines
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
        if ax.is_first_row():
            ax.spines['top'].set_visible(True)
        if ax.is_last_row():
            ax.spines['bottom'].set_visible(True)
        if ax.is_first_col():
            ax.spines['left'].set_visible(True)
        if ax.is_last_col():
            ax.spines['right'].set_visible(True)

    plt.show()
    #plt.show()
    """

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
