import cv2

def get_video_information():
    video = cv2.VideoCapture("video.mp4")
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("width: ",width)
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("height: ",height)
    nr_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
    print("No of Frames: ", nr_frame)
    fps = video.get(cv2.CAP_PROP_FPS)
    print("FPS: ",fps)
    
def get_video_frames():
    video = cv2.VideoCapture("video.mp4")
    success, frame = video.read()
    count = 1
    while success:
        cv2.imwrite(f'Video_Frames/{count}.jpg',frame)
        count = count + 1
        success, frame = video.read()
get_video_frames()