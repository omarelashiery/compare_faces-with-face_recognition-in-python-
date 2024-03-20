import cv2
import face_recognition

#read your image and convert it to RGB
img =cv2.imread("omar.jpg")
img2 =cv2.imread("omar2.jpeg")
rgp=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rgp2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# load your image with face_encodings
img_encoding = face_recognition.face_encodings(rgp)[0]
img_encoding2 = face_recognition.face_encodings(rgp2)[0]
result=face_recognition.compare_faces([img_encoding],img_encoding2)
print("result:",result)
cv2.imshow("img",img)
cv2.imshow("img 2",img2)
cv2.waitKey(0)

# remember that free palastine 
