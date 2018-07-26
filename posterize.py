import numpy as np
import cv2
import time
import sys
ts = int(time.time())

im = cv2.imread(sys.argv[1])

n = 3  # Number of levels of quantization

indices = np.arange(0,256)   # List of all colors

divider = np.linspace(0,255,n+1)[1] # we get a divider

quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors

color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..

palette = quantiz[color_levels] # Creating the palette

im2 = palette[im]  # Applying palette on image

im2 = cv2.convertScaleAbs(im2) # Converting image back to uint8
cv2.imwrite(f"ws_tests/{ts}.0.posterize.png", im2)
cv2.imshow('im2',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
