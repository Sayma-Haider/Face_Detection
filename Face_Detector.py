import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#this face detection from image

"""
img = cv2.imread('lot.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt=convert

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256) ,randrange(256)), 5)

#print(face_coordinates)

cv2.imshow("Face detection", img)
cv2.waitKey()

"""

#face detection using video

video  = cv2.VideoCapture('her.mp4')

while True:
    
    successful_frame_read, frame = video.read()

    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256) ,randrange(256)), 5)

    cv2.imshow('Hermione sassing people', frame)

    key  = cv2.waitKey(60)

    if key == 81 or key == 113:
        break

video.release()