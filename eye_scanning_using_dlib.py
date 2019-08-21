import cv2
import numpy as np
import dlib
import math
cap=cv2.VideoCapture()
predictor=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor('address .xml')



while(True):
    frame=cv2.flip(frame,1)
    gray=cv2.
for face in faces:
    landmarks=predictor(gray,face)
    left_point1=(landmarks.part(36).x,landmarks.part(36).y)
    right_point1=(landmarks.part(39).x,landmarks.part(39).y)
    
    left_point2=(landmarks.part(36).x,landmarks.part(36).y)
    right_point2=(landmarks.part(39).x,landmarks.part(39).y)
    
    cv2.circle(frame,left_point1,3,(0,0,255),2)
    cv2.circle(frame,right_point1,3,(0,0,255),2)
    
    cv2.circle(frame,left_point2,3,(0,0,255),2)
    cv2.circle(frame,right_point2,3,(0,0,255),2)
    
    cv2.line(frame,left_point1,right_point1,(0,255,0),2)
    cv2.line(frame,left_point2,right_point2,(0,255,0),2)