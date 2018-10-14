#Face Recognition
import cv2

#Loading Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Gray - grayscale image
#frame - original image
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray , 1.3 , 5)
    for ( x , y , w , h ) in faces : 
        cv2.rectangle(frame, (x,y) , (x+w , y+h) , ( 255 , 0 , 0 ) , 2)
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1 , 3)
        for ( ex , ey , ew , eh ) in eyes:
            cv2.rectangle(roi_color , (ex,ey) , (ex+ew , ey+eh) , ( 0 , 255 , 0 ) , 2)
            