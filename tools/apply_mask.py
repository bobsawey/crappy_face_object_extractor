import sys
import cv2
import numpy
import time
ts = int(time.time())

img = cv2.imread(sys.argv[1])
mask = cv2.imread(sys.argv[2],0)
#

mask[mask != 255 ] = 0
mask = cv2.bitwise_not(mask)

cv2.imwrite(f"ws_tests/{ts}.0.mask.png", mask)
cv2.imshow('burp',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.bitwise_not(img)
res = cv2.bitwise_not(img,img,mask = mask)

cv2.imwrite(f"ws_tests/{ts}.0.apply_mask.png", res)
cv2.imshow('burp',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
