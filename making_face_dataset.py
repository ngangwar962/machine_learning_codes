import cv2
import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
counter=0
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        cropped = frame[y:y1,x:x1]
        cv2.imwrite('G:/desktop_important/ml_datasets_and_libraries/face_recognition_dataset/pandey_ji/pandey_ji_9_'+str(counter)+".jpg",cropped)
        counter+=1
    cv2.imshow("DLIB Frame", frame)
    if(cv2.waitKey(1)&0xFF==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
