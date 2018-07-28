# USAGE
# python detect_faces.py --image rooster.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
import numpy as np
import argparse
import cv2
import math

def detect_faces(image_path):

    args_prototxt = 'models/detect_faces.deploy.prototxt.txt'
    args_model = 'models/detect_faces.res10_300x300_ssd_iter_140000.caffemodel'
    args_confidence = 0.9;

    # load our serialized model from disk
    print("[INFO] loading model...")
    net = cv2.dnn.readNetFromCaffe(args_prototxt, args_model)

    # load the input image and construct an input blob for the image
    # by resizing to a fixed 300x300 pixels and then normalizing it
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the detections and
    # predictions
    print("[INFO] computing object detections...")
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > args_confidence:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 2.250, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the bounding box of the face along with the associated
            # probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            #cv2.rectangle(image, (startX, startY), (endX, endY),
                #(0, 0, 255), 1)
            padding = 30
            crop = image[(startY-padding):endY+padding,startX-padding:endX+padding]
            cv2.imshow("cropped", crop)
            cv2.waitKey(0)
            image = crop
            cv2.rectangle(image, (startX-padding, startY-padding), (endX+padding, endY+padding),
                (0, 0, 255), 1)
            print(startX, startY,endX,endY)
            #cv2.putText(image, text, (startX, y),
                #cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    # show the output image
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


def get_rects(image_path):

    args_prototxt = 'models/detect_faces.deploy.prototxt.txt'
    args_model = 'models/detect_faces.res10_300x300_ssd_iter_140000.caffemodel'
    args_confidence = 0.9;

    # load our serialized model from disk
    print("[INFO] loading model...")
    net = cv2.dnn.readNetFromCaffe(args_prototxt, args_model)

    # load the input image and construct an input blob for the image
    # by resizing to a fixed 300x300 pixels and then normalizing it
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the detections and
    # predictions
    print("[INFO] computing object detections...")
    net.setInput(blob)
    detections = net.forward()

    rect_tuple = (0,0,0,0)
    tup_tup =  ((0,0),(0,0))
    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > args_confidence:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the bounding box of the face along with the associated
            # probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            #cv2.rectangle(image, (startX, startY), (endX, endY),
                #(0, 0, 255), 1)

            paddingY = int((startY/4)*math.e)
            paddingX = int((startX/4)*math.e/2)

            print((startY-paddingY))
            print(endY+paddingY)
            print(f"endy{endY}")
            print(paddingY)
            print(image)
            print(endY+endY+paddingY)
            #crop = image[(startY-padding):endY+padding,startX-padding:endX+padding]

            #IT MUST BE IN BOUNDS!
            crop = image[startY-paddingY:endY+endY+paddingY,startX-paddingX:endX+endX+paddingX]
            #print(crop)
            print(paddingY)
            #cv2.imshow("cropped", crop)paddingX
            #cv2.waitKey(0)
            image = crop
            rect_tuple = (startX-paddingX, startY-paddingY, int(endX+((500-endX)/4)*math.e), 500 )
            tup_tup = (startX-paddingX, startY-paddingY),( int( endX+ ((500-endX)  /4)  *math.e), 500)
            #ftangle = cv2.rectangle(image, (startX-padding, startY-padding), (endX+padding, endY+padding),
            #    (0, 0, 255), 1)
            print(startX, startY,endX,endY)
            #cv2.putText(image, text, (startX, y),
                #cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    # show the output image
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return rect_tuple, tup_tup
