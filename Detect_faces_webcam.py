import cv2
video = cv2.VideoCapture(0)
success, frame = video.read()
face_cascade = cv2.CascadeClassifier('faces.xml')

height=frame.shape[0]
weidth = frame.shape[1]
cv2.startWindowThread()
cv2.namedWindow("Recording")
output = cv2.VideoWriter('Webcam.avi',cv2.VideoWriter_fourcc(*'DIVX'),15,(weidth,height))
while success:
    faces = face_cascade.detectMultiScale(frame,1.1,10)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    cv2.imshow("Recording",frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    output.write(frame)
    success, frame = video.read()

output.release()
video.release()
cv2.destroyAllWindows()
