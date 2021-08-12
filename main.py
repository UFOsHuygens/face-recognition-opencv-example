import cv2

cap = cv2.VideoCapture(0)

while True:
    cascade = cv2.CascadeClassifier("xml/palm.xml")
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in objects:
        cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
    #    print('detected')
    
    cv2.imshow("Result", img)
    cv2.waitKey(1)