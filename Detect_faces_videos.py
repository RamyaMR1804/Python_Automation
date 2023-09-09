import cv2
video = cv2.VideoCapture("video.mp4")
success, frame = video.read()
face_cascade = cv2.CascadeClassifier('faces.xml')

height=frame.shape[0]
weidth = frame.shape[1]

output = cv2.VideoWriter('Output.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(weidth,height))
while success:
    faces = face_cascade.detectMultiScale(frame,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
    output.write(frame)
    success, frame = video.read()

output.release()
