import cv2

cap = ""

#what happens below

while cap == "":
    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print('Could not open video device')
        cap = ""
        
#what happens below

print("Show letter to camera")
ret, frame = cap.read()
cv2.imshow('preview',frame)

cv2.waitKey(0)

#what happens below
    

cv2.imwrite("pic.png", frame)

cap.release()

cv2.destroyAllWindows()
