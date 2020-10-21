# face detector for videos

import cv2

face_detection_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# VideoCapture(0) targets the webcam 
webcam = cv2.VideoCapture(0)

while True:
    
    # boolean frame was read true or false, frame
    frame_read, frame = webcam.read()

    # convert grayscale because our training was done in grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # we apply the classifier at every frame 
    face_coordinates = face_detection_model.detectMultiScale(grayscale_frame)
    
    # and we get the rectangle
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
    
    cv2.imshow('webcam', frame)
    key == cv2.waitKey(1)
    if key == 81 or key == 113:
        break
# let the webcam go
webcam.release()
