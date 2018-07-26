import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys

img = cv.imread(sys.argv[1],0)
# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create(5)
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
cv.imwrite('fast_true.png',img2)
cv.imshow('gwash', img2)
cv.waitKey(0)
# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
cv.imshow('gwash', img3)
cv.waitKey(0)
cv.imwrite('fast_false.png',img3)
