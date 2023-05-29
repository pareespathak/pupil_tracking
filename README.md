## Problem Statement:  
### Development of an IoT-based gaze-detection device that identifies the region observed by the driver during his journey and use the data for driver’s behaviour analysis.

## Objective:  
1) To develop a Pupil Detection and Tracking pipeline for Gaze Tracking.  
2) To develop a pipeline for head pose orientation.  
3) To develop an algorithm for lane detection.  
4) To develop an algorithm for road sign detection.  

## Overview Of the Pipeline: 
![Gaze Tracking PPT](https://github.com/pareespathak/pupil_tracking/assets/64767345/69e406d4-12e3-4194-be04-ef67fb59b624)

## Pipeline:
### Camera Calibration  
To calculate Calibration matrix, Distortion coefficient, Rotational and Translational vectors using Zhang's method.
Printed the image of checkerboard on A4 sheet of paper. Captured images of the from different angles. Use calibration code to get the required calibrating parameters.  

Results:  
![ezgif com-gif-maker (1)](https://github.com/pareespathak/pupil_tracking/assets/64767345/40971c8a-adce-4bca-a988-912335587168)


### Pupil Detection and Tracking  
1) Pupil Segmentation - Different threshold values are applied to the preprocessed images. 
Pupil segmentation is performed for each value by detecting contours, blob, and Hough transform.  
2) Evaluation of best threshold - Segmentation results are evaluated by measuring precision, recall, and F1-score metrics by comparing the ground truth pupil region.  
3) Detecting Eye key points - 
To find eye key points we use dlib to detect facial points. Then select the eye outlines to get the extreme ends of eyes.  
4) Predicting coordinates - Horizontal and vertical coordinates of eyes are calculated for each frame and compared with previous frames by template matching.  

#### Results 

Pupil left right centre 
gif


### Head Pose Results
 
pics 

### Lane and Road Sign Detection Results 


## Experimental Setup:
![Gaze Tracking PPT](https://github.com/pareespathak/pupil_tracking/assets/64767345/5a06e582-12b2-43ac-8f79-9e02777a4d37) | ![ezgif com-optimize](https://github.com/pareespathak/pupil_tracking/assets/64767345/de750605-c2dc-40cd-a0ba-588c12ded5ed)
-------------------------------------------------- | --------------------------------------------------------

### Results:
(pupil projection)
(mention source of test video)

### Heat Maps and Visualization


* For eye detection and tracking: https://github.com/antoinelame/GazeTracking
