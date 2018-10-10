#Face Recognition
import cv2

#Loading Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_caseace = cv2.CascadeClassifier('haarcascade_eye.xml')