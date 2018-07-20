import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

img = cv2.imread('data/butts.png',0)
edges = cv2.Canny(img,5,50)
fig = plt.figure()

#Slider
'''
axcolor = 'lightgoldenrodyellow'
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

def update(val):
    amp = samp.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

samp.on_changed(update)
'''
#endSlider

plt.subplot(661),plt.imshow(img,cmap = 'gray')
for x in range(2,36):

plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(662)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(663)
plt.title('1, 200'), plt.xticks([]), plt.yticks([])
edges = cv2.Canny(img,1,200)
im1 = plt.imshow(edges,cmap = 'gray')

plt.subplot(664),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(665)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(666)
plt.title('1, 200'), plt.xticks([]), plt.yticks([])
edges = cv2.Canny(img,1,200)
im1 = plt.imshow(edges,cmap = 'gray')
plt.show()
