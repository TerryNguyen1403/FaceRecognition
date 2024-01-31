import cv2

alg = "models/haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

# Read the photo from the file
img_path = 'D:/projectRecognition/sample.jpg'
img = cv2.imread(img_path)

#Convert to gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Face Recognition 
face_detect = haar_cascade.detectMultiScale(img_gray, 1.1, 4)

#Draw a rectangle
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#Output
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()