import cv2
import numpy

img = cv2.imread('processed_images/individual_images/138.png.verts.planters.png')
mask = cv2.imread('ws_tests.1532508636.6.mask.png',0)
res = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow('burp',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
