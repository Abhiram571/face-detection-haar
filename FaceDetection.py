import cv2
import os
face_path=input("enter path of Face XML file:")
if  not os.path.exists(face_path):
    print("File path error")
    exit()
else:
    face=cv2.CascadeClassifier(face_path)
    if face.empty():
        print("file loading failed")
        exit()
    else:
        video=cv2.VideoCapture(0)
        if not video.isOpened():
            print("Camera Failure")
            exit()
        else:
            while True:
                ret,frame=video.read()
                if not ret:
                    break
                gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                face_detection=face.detectMultiScale(gray,1.1,7,minSize=(60,60))
                if len(face_detection)>0:
                    for (x,y,w,h) in face_detection:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        cv2.putText(frame,"Face Detected",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,123,255),2)
                cv2.imshow("Face Detection",frame)
                if cv2.waitKey(1) & 0xFF==ord("q"):
                    break          
        video.release()
        cv2.destroyAllWindows()
    
