import cv2

cap = ""

#Checks that it can access the camera

while cap == "":
    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print('Could not open video device')
        cap = ""
        
#Takes a picture from the webcam

ret, frame = cap.read()

#Saves the image to a file

cv2.imwrite("letter.png", frame)

cap.release()

cv2.destroyAllWindows()
