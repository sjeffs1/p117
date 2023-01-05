import os
import cv2

video = cv2.VideoCapture(0)
if video.isOpened()==False:
    print("Unable to read the page")
    
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps)

