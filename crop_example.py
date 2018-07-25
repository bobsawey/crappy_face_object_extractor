'''
Crop an image to box
^^^^^^^^^^^^^^^^^^^^

The following script uses box coordinates to crop an image using a centered box.
The cropping box is 1/2th the size of the image, and aspect ratio is preserved.

A 400x400 image will crop to 200x200 using the 4-tuple (100,100,300,300)

.. code-block:: python
'''

from PIL import Image

test_image = "test_image.jpg"

original = Image.open(test_image)
original.show()

width, height = original.size   # Get dimensions

left = width/4
top = height/4
right = 3 * width/4
bottom = 3 * height/4

#preserve aspect ratio, crop center box at 1/4th size of original
cropped_example = original.crop((left, top, right, bottom))

cropped_example.show()
