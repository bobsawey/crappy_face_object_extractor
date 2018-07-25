import sys
import numpy as np
import cv2
import time
ts = int(time.time())
import autocanny

original = cv2.imread(sys.argv[1])
cv2.imwrite(f"ws_tests/{ts}.0.original.png", original)
autocanny_img =  autocanny.canny_op(sys.argv[1],2)
tightcanny_img =  autocanny.canny_op(sys.argv[1],1)
widecanny_img =  autocanny.canny_op(sys.argv[1],0)

cv2.imwrite(f"ws_tests/{ts}.0.auto_canny.png", autocanny_img)
cv2.imwrite(f"ws_tests/{ts}.0.tight_canny.png", tightcanny_img)
cv2.imwrite(f"ws_tests/{ts}.0.wide_canny.png", widecanny_img)
#cv2.imwrite(f"ws_tests/{ts}.0.show_skin.png", show_skin_img)
