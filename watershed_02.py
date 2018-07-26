import sys
import cv2
import numpy
from scipy.ndimage import label
numpy.seterr(divide='ignore', invalid='ignore')
import time
ts = int(time.time())


def segment_on_dt(a, img):
    border = cv2.dilate(img, None, iterations=135)
    cv2.imwrite(f"ws_tests/{ts}.1.border.png", border)
    border = border - cv2.erode(border, None)
    cv2.imwrite(f"ws_tests/{ts}.2.border_erode.png", border)

    dt = cv2.distanceTransform(img,2,3)
    cv2.imwrite(f"ws_tests/{ts}.3.dt.png", dt)
    dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(numpy.uint8)
    _, dt = cv2.threshold(dt, 180, 255, cv2.THRESH_BINARY)
    lbl, ncc = label(dt)
    lbl = lbl * (255 / (ncc + 1))
    # Completing the markers now.
    lbl[border == 255] = 255


    lbl = lbl.astype(numpy.int32)
    cv2.imwrite(f"ws_tests/{ts}.4.lbl.png", lbl)
    cv2.watershed(a, lbl)

    lbl[lbl == -1] = 0
    lbl = lbl.astype(numpy.uint8)
    return 255 - lbl


img = cv2.imread(sys.argv[1])

# Pre-processing.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255,
        cv2.THRESH_OTSU)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN,
        numpy.ones((29,29), dtype=int))

result = segment_on_dt(img, img_bin)
cv2.imshow('burp',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(f"ws_tests/{ts}.5.segment_on_dt.png", result)
result[result != 0] = 255
cv2.imwrite(f"ws_tests/{ts}.6.mask.png", result)

#result[result != 255] = 0
cv2.imshow('burp',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
result = cv2.dilate(result, None)
img[result != 0 ] = 255
cv2.imshow('burp',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(f"ws_tests/{ts}.7.dilate.png", img)
