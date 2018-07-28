#!/bin/bash
for filename in _data_3/*.png; do
    python3 canny_save.py "$filename"
    python3 save_show_skin.py "$filename"
    python3 grabcut_face_detect_auto.py "$filename"
done
