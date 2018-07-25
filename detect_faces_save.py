import sys
import numpy as np
import cv2
import time
ts = int(time.time())

import detect_faces_solid_rect as faces

original = cv2.imread(sys.argv[1])
print(f"ws_tests/{ts}.0.original.png")
cv2.imwrite(f"ws_tests/{ts}.0.original.png", original)
faces_images = faces.detect_faces(sys.argv[1])
print(f"ws_tests/{ts}.0.original.png")

cv2.imwrite(f"ws_tests/{ts}.0.detected_faces_solid.png", faces_images)
