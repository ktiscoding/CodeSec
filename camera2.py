import cv2

cap = ""

#Checks that it can access the camera

while cap == "":
    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print('Could not open video device')
        cap = ""
        
""" 
Takes a picture from the webcam and shows it to the user until they press a key. If they enter a y, the
picture will be kept. Else, a new picture will be taken.
"""

valid = "n"

while valid != "y":
    print("Show letter to camera")
    ret, frame = cap.read()
    cv2.imshow('letter',frame)
    cv2.waitKey(0)
    valid = input()

#Saves the image to a file

cv2.imwrite("letter.png", frame)

cap.release()

cv2.destroyAllWindows()
