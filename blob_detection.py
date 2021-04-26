import numpy as np
import cv2
import blob

def get_params():
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 50
    params.maxThreshold = 225


    params.filterByArea = True
    params.minArea = 1600
    params.maxArea = 150000


    params.filterByCircularity = True
    params.minCircularity = 0.65


    params.filterByConvexity = True
    params.minConvexity = 0.7


    params.filterByInertia = True
    params.minInertiaRatio = 0.1

    return params

def get_detector():
    return cv2.SimpleBlobDetector.create(get_params())



lower = np.array([0,0,0])
upper = np.array([359,200, 50])

def set_lower(h,s,v):
    global lower
    lower = np.array([h,s,v])

def set_upper(h,s,v):
    global upper
    upper = np.array([h,s,v])


detector = get_detector()

def find_blobs(frame):


    blurred = frame
    blurred = cv2.GaussianBlur(blurred, (9,9), 100)
    blurred = cv2.bilateralFilter(blurred, 9, 75, 75)
    bordered = cv2.copyMakeBorder(blurred, 5,5,5,5,cv2.BORDER_CONSTANT, None, [255,255,255])
    hsv = cv2.cvtColor(bordered,cv2.COLOR_BGR2HSV)
    
    

    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.GaussianBlur(mask, (21,21), 100)
    mask = cv2.bitwise_not(mask)
    keypoints = detector.detect(mask)

    cv2.imshow("Blurred", blurred)
    cv2.imshow("Blob Detection", mask)

    blobs=[]
    for keypoint in keypoints:
        blobs.append(blob.create_blob_from_keypoint(keypoint))
    


    return blobs