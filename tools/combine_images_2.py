#!/usr/bin/python3


# original snippet found
from scipy import misc
import cv2
import numpy as np
from PIL import Image
from seam_carver import intelligent_resize
from random_word import RandomWords
# adding random integeger support
from random import randint

import matplotlib.pyplot as plt
import find_skin as skin
rnum = randint

img_dir = './_data_2'
list_im = [f"{img_dir}/{rnum(1,200)}.png", f"{img_dir}/{rnum(1,200)}.png"]
imgs = [Image.open(i) for i in list_im]

# pick the image which is the smallest
# and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted([(np.sum(i.size), i.size)for i in imgs])[0][1]
imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

# save that beautiful picture
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('Trifecta.jpg')

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack(
    (np.asarray
        (i.resize(min_shape))
        for i in imgs))
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('Trifecta_vertical.jpg')


def gallery(array, ncols=4):
    nindex, height, width, intensity = array.shape
    nrows = nindex//ncols
    assert nindex == nrows*ncols
    # want result.shape = (height*nrows, width*ncols, intensity)
    result = (array.reshape(nrows, ncols, height, width, intensity)
              .swapaxes(1, 2)
              .reshape(height*nrows, width*ncols, intensity))
    return result


def make_array():
    from PIL import Image
    from os import listdir
    from os.path import isfile, join
    import detect_faces as faces

    data_path = '_data_2'
    list_im = [
        f for f in listdir(data_path) if isfile(join(data_path, f))]
    #return np.array([np.asarray(Image.open(f'{data_path}/{i}').convert('RGB')) for i in list_im[:16]])
    return np.array([np.asarray(faces.detect_faces(f'{data_path}/{i}')) for i in list_im[:16]])



array = make_array()
print(array)
result = gallery(array)
plt.imshow(result)
plt.show()

def find_skin_from_array():
    import find_skin


result = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
cv2.imshow('image',result)



cv2.waitKey(0)
cv2.destroyAllWindows()
dr = RandomWords()

#get random word for filenames
rdmwd1 = dr.get_random_word()
rdmwd2 = dr.get_random_word()
indy_img_dir= "{}/{}.{}.png".format("processed_images/individual_images", rdmwd1, rdmwd2 )
cv2.imwrite(f"{indy_img_dir}",result)
