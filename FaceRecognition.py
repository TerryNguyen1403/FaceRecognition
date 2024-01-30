# importing the required libraries
import cv2

#Loading the haar cascde algorithm file into alg variable
alg = "models/haarcascade_frontalface_default.xml"

# capturing the video feed from the camera
cam = cv2.VideoCapture(0)

cam.set(3, 480) # Width
cam.set(4, 640) # Height

while True:
    success, img = cam.read()

    text = 'Face is not recognized'

    # passing the algorithm to OpenCV
    haar_cascade = cv2.CascadeClassifier(alg)

    #convert a color image to gray image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # display the text on the image
    image = cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Face Recognition', img)

    key = cv2.waitKey(10)

    # If user press Esc, the program'll be close
    if key == 27:
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()