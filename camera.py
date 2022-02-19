import cv2

cap = ""

#Checks that it can access the camera

while cap == "":
    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print('Could not open video device')
        cap = ""
        
#Takes a picture from the webcam and shows it to the user until they press a key

print("Show letter to camera")
ret, frame = cap.read()
cv2.imshow('letter',frame)

cv2.waitKey(0)

#Saves the image to a file

cv2.imwrite("letter.png", frame)

cap.release()

cv2.destroyAllWindows()
