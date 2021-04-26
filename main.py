import cv2
import numpy as np
import blob_detection
import blob as BLOB



cap = cv2.VideoCapture("test2.mp4")


ret, first = cap.read()

old = blob_detection.find_blobs(first)

path = np.zeros_like(first)




def hsv_track(val):
    blob_detection.set_upper(cv2.getTrackbarPos("Upper H", "Settings"), cv2.getTrackbarPos("Upper S", "Settings"), cv2.getTrackbarPos("Upper V", "Settings"))
    blob_detection.set_lower(cv2.getTrackbarPos("Lower H", "Settings"), cv2.getTrackbarPos("Lower S", "Settings"), cv2.getTrackbarPos("Lower V", "Settings"))








cv2.namedWindow("Settings")
cv2.createTrackbar("Upper H", "Settings", 0, 255, hsv_track)
cv2.createTrackbar("Upper S", "Settings", 0, 255, hsv_track)
cv2.createTrackbar("Upper V", "Settings", 0, 359, hsv_track)
cv2.createTrackbar("Lower H", "Settings", 0, 255, hsv_track)
cv2.createTrackbar("Lower S", "Settings", 0, 255, hsv_track)
cv2.createTrackbar("Lower V", "Settings", 0, 359, hsv_track)

while(cap.isOpened()):

    ret, frame = cap.read()

    blobs = blob_detection.find_blobs(frame)
    
    
    BLOB.find_change(old, blobs, None)
    print(len(blobs))

    for blob in blobs:

        l,r = blob.get_bounding_box_int()
        frame = cv2.rectangle(frame, l, r, blob.col, 3)
        # continue

        if(blob.prev != None):
            path = cv2.line(path, blob.pos_int(), blob.prev.pos_int(), blob.col,1)
            l,r = blob.prev.get_bounding_box_int()
            frame = cv2.rectangle(frame, l, r, blob.prev.col, 3)

    frame = cv2.add(frame,path)

    old = blobs
     
    cv2.imshow("blobs", frame)
    key = cv2.waitKey(10) & 0xFF
    if(key == ord('q')):
        break
    elif(key == ord('r')):
        path = np.zeros_like(first)

