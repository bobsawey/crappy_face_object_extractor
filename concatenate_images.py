import numpy as np, cv2

imageFile1 = "data_processed_1/1.png"
imageFile2 = "data_processed_1/2.png"

img1 = cv2.imread(imageFile1)
img2 = cv2.imread(imageFile2)

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

#create empty matrix
vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

#combine 2 images
vis[:h1, :w1,:3] = img1
vis[:h2, w1:w1+w2,:3] = img2

cv2.imshow("test", vis)
cv2.waitKey()
