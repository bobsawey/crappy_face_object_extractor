#!/bin/bash
for filename in _data_3/*.png; do
    python3 grabcut_face_detect_auto.py "$filename"
    python3 save_show_skin.py "$filename"
done
