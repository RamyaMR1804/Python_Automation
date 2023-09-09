import cv2
import numpy as np
def img_2_greyscale():
    color = cv2.imread('Image.jpg',0)
    cv2.imwrite('Image-grey.jpeg',color)

def img_resize(scale_percentage):
    img=cv2.imread('Image.jpg',1)
    print(img.shape)
    new_width=int(img.shape[1]*scale_percentage/100)
    new_height=int(img.shape[0]*scale_percentage/100)
    new_size=(new_width,new_height)  
    resized_image=cv2.resize(img,new_size) 
    print(resized_image.shape)
    cv2.imwrite('Resize_image.jpg',resized_image)

def detect_faces():
    img=cv2.imread('humans.jpeg',1)
    face_cascade = cv2.CascadeClassifier('faces.xml')
    faces = face_cascade.detectMultiScale(img,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),4)
    cv2.imwrite('human_faces.jpeg',img)

def add_watermark():
    img = cv2.imread('elfs.jpeg')
    watermark = cv2.imread('watermark.png')
    x=img.shape[1]-watermark.shape[1]
    y=img.shape[0]-watermark.shape[0]
    watermark_place=img[y:,x:]
    blend=cv2.addWeighted(watermark_place,0.5,watermark,0.5,0)
    img[y:,x:]= blend
    cv2.imwrite('elfs-watermarked.jpeg',img)

def image_background():
    foreground = cv2.imread("giraffe.jpeg")
    background = cv2.imread("safari.jpeg")

    print(foreground[40, 40])
    width = foreground.shape[1]
    height = foreground.shape[0]
    print(foreground.shape)


    resized_background = cv2.resize(background, (width, height))

    for i in range(width):
        for j in range(height):
            pixel = foreground[j, i]
            # print(type(pixel))
            if np.any(pixel == [2, 255, 1]):
                foreground[j, i] = resized_background[j, i]

    cv2.imwrite('output.jpeg', foreground)

image_background()