import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# Load the image

filename = sys.argv[1]
img = cv2.imread(filename, 3)

# Create a blank image of zeros (same dimension as img)
# It should be grayscale (1 color channel)
marker = np.zeros_like(img[:,:,0]).astype(np.int32)

# This step is manual. The goal is to find the points
# which create the result we want. I suggest using a
# tool to get the pixel coordinates.

# Dictate the background and set the markers to 1
marker[55][851] = 1
marker[409][757] = 1
marker[18][620] = 1
marker[522][213] = 1
marker[288][142] = 1
marker[177][76] = 1
marker[282][706] = 1

# Dictate the area of interest
# I used different values for each part of the car (for visibility)
marker[405][411] = 255    # car body
marker[480][325] = 64     # left eye
marker[313][327] = 64     # right eye
marker[391][648] = 128     # left ear
marker[391][225] = 128    # right ear

# right anterior shoulder pad
marker[658][75] = 128
marker[658][142] = 128
marker[658][252] = 128

# front wheel
marker[658][660] = 192
marker[658][762] = 192

# rear wheel
marker[76][312] = 192
marker[54][312] = 192
marker[140][640] = 192

marker[405, 395] = 32
marker[428, 515] = 32
marker[378, 553] = 32
marker[59, 595] = 32
marker[105, 630] = 32
marker[163, 663] = 32
marker[222, 665] = 32
marker[278, 670] = 32
marker[308, 669] = 32
marker[246, 659] = 32
marker[185, 661] = 32
marker[124, 642] = 32
marker[80, 611] = 32
marker[48, 565] = 32
marker[28, 516] = 32
marker[146, 451] = 32
marker[185, 324] = 32
marker[229, 293] = 32
marker[303, 260] = 32
marker[348, 232] = 32
marker[403, 241] = 32
marker[212, 221] = 32
marker[135, 238] = 32
marker[96, 274] = 32
marker[53, 324] = 32
marker[28, 391] = 32
marker[39, 440] = 32
marker[131, 410] = 32
marker[198, 394] = 32
marker[407, 310] = 32
marker[501, 322] = 32
marker[562, 346] = 32
marker[596, 462] = 32
marker[503, 553] = 32
marker[424, 590] = 32
marker[324, 486] = 32
marker[333, 315] = 32
marker[364, 667] = 32
marker[429, 638] = 32
marker[439, 606] = 32
marker[502, 598] = 32
marker[575, 572] = 32
marker[604, 543] = 32
marker[630, 403] = 32
marker[588, 336] = 32
marker[497, 296] = 32
marker[439, 272] = 32
marker[556, 276] = 32
marker[630, 32] = 32
marker[626, 97] = 32
marker[572, 200] = 32
marker[585, 201] = 32
marker[596, 143] = 32
marker[553, 627] = 32
marker[566, 701] = 32
marker[594, 775] = 32
marker[608, 827] = 32
marker[560, 670] = 32


# Now we have set the markers, we use the watershed
# algorithm to generate a marked image
marked = cv2.watershed(img, marker)

# Plot this one. If it does what we want, proceed;
# otherwise edit your markers and repeat
plt.imshow(marked, cmap='gray')
plt.show()

# Make the background black, and what we want to keep white
marked[marked == 1] = 0
marked[marked > 1] = 255

# Use a kernel to dilate the image, to not lose any detail on the outline
# I used a kernel of 3x3 pixels
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(marked.astype(np.float32), kernel, iterations = 1)


# Now we have set the markers, we use the watershed
# algorithm to generate a marked image
marked = cv2.watershed(img, marker)

# Plot this one. If it does what we want, proceed;
# otherwise edit your markers and repeat
plt.imshow(marked, cmap='gray')
plt.show()

# Make the background black, and what we want to keep white
marked[marked == 1] = 0
marked[marked > 1] = 255

# Use a kernel to dilate the image, to not lose any detail on the outline
# I used a kernel of 3x3 pixels
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(marked.astype(np.float32), kernel, iterations = 1)

# Plot again to check whether the dilation is according to our needs
# If not, repeat by using a smaller/bigger kernel, or more/less iterations
pltilate(marked.astype(np.float32), kernel, iterations = 1)

# Plot again to check whether the dilation is according to our needs
# If not, repeat by using a smaller/bigger kernel, or more/less iterations
plt.imshow(dilation, cmap='gray')
plt.show()

# Now apply the mask we created on the initial image
final_img = cv2.bitwise_and(img, img, mask=dilation.astype(np.uint8))

# cv2.imread reads the image as BGR, but matplotlib uses RGB
# BGR to RGB so we can plot the image with accurate colors
b, g, r = cv2.split(final_img)
final_img = cv2.merge([r, g, b])

# Plot the final result
plt.imshow(final_img)
plt.show()
