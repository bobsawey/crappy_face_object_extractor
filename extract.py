#!/usr/bin/env python3

# python3 extract.py data_in data_out
import sys
import cv2
import shutil
import logging
from os import listdir
from os.path import isfile, join, isdir
import time

ts = int(time.time())

from tools.grabcut_face_detect_auto import cutout_face

logging.basicConfig(filename='extraction.log', level=logging.INFO)

image_in_dir = sys.argv[1]
image_out_dir = sys.argv[2]

# TODO: needs to check if images
images_to_process = [f for f in listdir(image_in_dir) if isfile(join(image_in_dir, f))]

logging.info(f'Beginning For Loop')

for image_path in images_to_process:

    logging.info(f'Starting Cutout for {image_path}')

    cutout, status = cutout_face(f"{image_in_dir}/{image_path}")

    # if cutout comes back False, next item

    if not status:
        # move {image_in_dir}/{image_path} {image_in_dir}/error/
        logging.info(f'Cutting not working for {image_path} ')
        shutil.move(f'{image_in_dir}/{image_path}', f'{image_in_dir}/error/')
        continue

    logging.info('Cutout complete. ')
    logging.info('Saving new Image. ')

    cv2.imwrite(f"{image_out_dir}/{ts}.{image_path}.0.face_cut.png", cutout)
    logging.info('Image saved.')
