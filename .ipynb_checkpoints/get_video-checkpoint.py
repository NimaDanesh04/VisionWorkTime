import cv2
import os
from natsort import natsorted

image_folder = '/home/rasa/new/pred_4'  
output_video = 'output_video5.mp4'
fps = 5 


images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
images = natsorted(images)

first_frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

for image in images:
    frame = cv2.imread(os.path.join(image_folder, image))
    video.write(frame)

video.release()
print(f"Video saved as {output_video}")
