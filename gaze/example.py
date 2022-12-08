"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
_, frame = webcam.read()
# Define the codec and create VideoWriter object
height, width = frame.shape[:2]
print(height, width, "cam")
############## Dash cam
cap1 = cv2.VideoCapture("/home/parees/pupil/My_Movie2.mp4")
ret, frame1 = cap1.read()
ht,wd = frame1.shape[:2]
print(ht,wd, "size of dash")
Video_Fps = webcam.get(cv2.CAP_PROP_FPS)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter('output_pup_ppt.mp4',fourcc, 20.0, (width,height)) #width, height
out1 = cv2.VideoWriter('output_dash_ppt.mp4',fourcc, 20.0, (wd,ht)) #width, height
scale_x = 1#int(wd/width)
scale_y = 1#int(ht/height)
'''
i = 0
src, dst = [], []
#homography_mat, Mask = cv2.findHomography(np.float32(src), np.float32(dst), method = cv2.RANSAC)
def draw_coordinates(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        text = str(i+1)
        cv2.putText(frame1, text, (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        x_image.append(x)
        y_image.append(y)
        cv2.circle(image_ref, (x,y), 7, (0,0,255), -1)
        src.append([x,y])
        i = i + 1
        if len(x_image) >= 2:
            cv2.line(image_ref, (x_image[-1],y_image[-1]), (x_image[-2], y_image[-2]), (0, 200, 200), 3)

x_image, y_image = [], []
image_ref = frame1
cv2.namedWindow("Double click to mark, press (q) after marking")
cv2.setMouseCallback("Double click to mark, press (q) after marking",draw_coordinates)
while (1):
    cv2.imshow('Double click to mark, press (q) after marking',image_ref)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imwrite('detection.jpg',image_ref)
'''
src_l = [[263, 247], [247,246], [230,266], [242,285]]
dst_l = [[0,0],[1920,0], [1080,1920], [0,1920]]
src_r = [[373,244], [357,246], [340,267], [354,285]]
dst_r = [[0,0],[1920,0], [1080,1920], [0,1920]]
homography_mat_left, Mask_left = cv2.findHomography(np.float32(src_l), np.float32(dst_l), method = cv2.RANSAC)
homography_mat_right, Mask_right = cv2.findHomography(np.float32(src_r), np.float32(dst_r), method = cv2.RANSAC)

while True:
    try:
        # We get a new frame from the webcam
        ret, frame1 = cap1.read()
        cv2.imshow("Dash_view", frame1)
        _, frame = webcam.read()    

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        # Radius of circle
        radius = 15
        thickness = -1
        #print(type(left_pupil), left_pupil)
        #print(right_pupil, left_pupil, 'before')
        #left_pupil = np.array([[left_pupil[0]],[left_pupil[1]], [1]])
        #right_pupil = np.array([[right_pupil[0]],[right_pupil[1]], [1]])
        #left_pupil = np.dot(homography_mat_left, left_pupil)
        #right_pupil = np.dot(homography_mat_right, right_pupil)
        #print(left_pupil[0]/-1*(left_pupil[2]+1e-8), 'after')
        frame1 = cv2.circle(frame1, (left_pupil[0],left_pupil[1]), radius, (0, 0, 255), thickness)
        frame1 = cv2.circle(frame1, (right_pupil[0], right_pupil[1]), radius, (0, 255, 255), thickness)
        #frame1 = cv2.circle(frame1, (left_pupil[0]/-1*(left_pupil[2]+1e-8),left_pupil[1]/-1*(left_pupil[2]+1e-8)), radius, (0, 0, 255), thickness)
        #frame1 = cv2.circle(frame1, (right_pupil[0]/-1*(right_pupil[2]+1e-8), right_pupil[1]/-1*(right_pupil[2]+1e-8)), radius, (0, 255, 255), thickness)
        # Displaying the image
        cv2.imshow("Demo", frame)
    except:
        print("err")
        pass
        
    if cv2.waitKey(1) == 27:
        break
    out.write(frame)
    out1.write(frame1)
    
webcam.release()
cap1.release()
cv2.destroyAllWindows()
