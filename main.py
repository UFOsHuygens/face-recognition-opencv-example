import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    faceCascade = cv2.CascadeClassifier("face.xml")
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
    #    print('detected')
    
    cv2.imshow("Result", img)
    cv2.waitKey(1)