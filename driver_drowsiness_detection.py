import numpy as np
import dlib
import cv2
import math

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("G:/desktop_important/ml_datasets_and_libraries/shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:

        landmarks = predictor(gray, face)
        left_point1 = (landmarks.part(36).x, landmarks.part(36).y)
        right_point1 = (landmarks.part(39).x, landmarks.part(39).y)
        center_top1 = midpoint(landmarks.part(37), landmarks.part(38))
        center_bottom1 = midpoint(landmarks.part(41), landmarks.part(40))
        
        center_top2=midpoint(landmarks.part(43),landmarks.part(44))
        center_bottom2=midpoint(landmarks.part(47),landmarks.part(46))
        
        lips_48=(landmarks.part(48).x,landmarks.part(48).y)
        lips_60=(landmarks.part(60).x,landmarks.part(60).y)
        lips_51=(landmarks.part(51).x,landmarks.part(51).y)
        lips_57=(landmarks.part(57).x,landmarks.part(57).y)
        mouth_ver1=midpoint(landmarks.part(50),landmarks.part(52))
        mouth_ver2=midpoint(landmarks.part(58),landmarks.part(56))
        lips_54=(landmarks.part(54).x,landmarks.part(54).y)

        left_point2 = (landmarks.part(42).x, landmarks.part(42).y)
        right_point2 = (landmarks.part(45).x, landmarks.part(45).y)
        
        cv2.line(frame,mouth_ver1,mouth_ver2,(0,255,0),2)

        cv2.circle(frame, left_point1, 3, (0,0,255),2)
        cv2.circle(frame, right_point1, 3, (0,0,255),2)
        cv2.line(frame, left_point1, right_point1, (0, 255, 0), 2)
        
        cv2.circle(frame,lips_48,3,(0,0,255),2)
        cv2.circle(frame,lips_54,3,(0,0,255),2)

        cv2.circle(frame, left_point2, 3, (0,0,255),2)
        cv2.circle(frame, right_point2, 3, (0,0,255),2)
        cv2.line(frame, left_point2, right_point2, (0, 255, 0), 2)

        cv2.line(frame, center_top1, center_bottom1, (0, 255, 0), 2)
        
        cv2.line(frame,center_top2,center_bottom2,(0,255,0),2)
        

        lenv1=math.sqrt((center_top1[0] - center_bottom1[0])**2 + (center_top1[1] - center_bottom1[1]) **2)
        lenh1=math.sqrt((left_point1[0] - right_point1[0])**2 + (left_point1[1] - right_point1[1]) **2)
        
        lenv2=math.sqrt((left_point2[0]-right_point2[0])**2+(left_point2[1]-right_point2[1])**2)
        lenh2=math.sqrt((center_top2[0]-center_bottom2[0])**2+(center_top2[1]-center_bottom2[1])**2)
        
        lenmv=math.sqrt((mouth_ver1[0]-mouth_ver2[0])**2+(mouth_ver1[1]-mouth_ver2[1])**2)
        font=cv2.FONT_HERSHEY_PLAIN
        #lennv = math.hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
        #lennh = math.hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        rat1=lenh1/lenv1
        if(lenmv>40 and rat1>3.5):
            cv2.putText(frame,"DROWSINESS DETECTED", (50, 150),font , 2, (0, 0,255))

        print(lenh1,">>>>",lenv1,">>>>",rat1,">>>>",lenmv)

    cv2.imshow("Frame", frame)

    if(cv2.waitKey(1)&0xFF==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
