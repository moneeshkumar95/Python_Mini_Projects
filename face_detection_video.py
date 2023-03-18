import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# SELECTING CAMERA
camera = cv.VideoCapture(1)

while True:
    _, frame = camera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', frame)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyWindow()