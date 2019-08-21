
import cv2
import matplotlib.pyplot as plt

def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2, minNeighbors=5)
    print(len(face_rects))
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,0,0), 3)
       
    return face_img,len(face_rects)

face_cascade = cv2.CascadeClassifier('G:/desktop_important/ml_datasets_and_libraries/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

#frame = cv2.imread('../../DATA/tshirt.jpg')
#frame = detect_face(frame)
#
#cv2.imshow('Face Detection', frame)
#cv2.waitKey(0)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame,times = detect_face(frame)
    cv2.putText(frame, "face detected"+str(times), (50, 150),cv2.FONT_HERSHEY_SIMPLEX,1 , (0, 0, 255))
    cv2.imshow('Video Face Detection', frame)

    if(cv2.waitKey(1)&0xFF==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
