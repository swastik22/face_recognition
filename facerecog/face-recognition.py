import os
import face_recognition
from cv2 import cv2

dataset="dataset"
images=os.listdir(dataset) 
img=face_recognition.load_image_file("RobertDowney.jpg")
unknow_encode=face_recognition.face_encodings(img)[0]
(top,right,bottom,left)=face_recognition.face_locations(img)[0]
cv2.rectangle(img,(left,top+32),(right,bottom),(0,345,0),3)
for image in images:
    path=os.path.join(image)
    know_image=face_recognition.load_image_file(path)
    know_encode=face_recognition.face_encodings(know_image)[0]
    result=face_recognition.compare_faces([know_encode],unknow_encode)
    if result[0]==True:
        name=image.split(".")[0]
        print(name)
        cv2.putText(img,name,(left,top),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(156,21,255),3)
        re=cv2.resize(img,(0,0),None,0.25,0.25)
        cv2.imshow("recog",re)
        cv2.waitKey(0)
        break

    else:
        print("unkown person")