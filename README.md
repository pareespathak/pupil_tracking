## Problem Statement:  
### Development of an IoT-based gaze-detection device that identifies the region observed by the driver during his journey and use the data for driver’s behaviour analysis.

## Objective:  
1) To develop a Pupil Detection and Tracking pipeline for Gaze Tracking.  
2) To develop a pipeline for head pose orientation.  
3) To develop an algorithm for lane detection.  
4) To develop an algorithm for road sign detection.  

## Overview Of the Pipeline: 
<img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/69e406d4-12e3-4194-be04-ef67fb59b624" height="400">

## Pipeline:
### Camera Calibration  
To calculate Calibration matrix, Distortion coefficient, Rotational and Translational vectors using Zhang's method.
Printed the image of checkerboard on A4 sheet of paper. Captured images of the from different angles. Use calibration code to get the required calibrating parameters.  

Results:  
<img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/40971c8a-adce-4bca-a988-912335587168" height="400">


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

## Experimental Setup:
<img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/5a06e582-12b2-43ac-8f79-9e02777a4d37" height="300">  | <img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/de750605-c2dc-40cd-a0ba-588c12ded5ed" height="300">
-------------------------------------------------- | --------------------------------------------------------

### Results:
(pupil projection)
(mention source of test video)


### Heat Maps and Visualization
<img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/7d0bc57d-5095-4c7e-936b-599501c9b615" height="200">  |  <img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/ecb25457-da53-40cf-a4c1-fdb45c02ba63" height="200">  |  <img src="https://github.com/pareespathak/pupil_tracking/assets/64767345/199e756b-2164-4819-835c-60f9526198b5" height="200">
--------------- | -------------------- | ---------------------
Heat Map generated for pupil coordinates to identify areas of max concentration  |  Gaze projection on Dash Cam view for Visualization  |  Superimposed heat maps and cars dashcam view.


* For eye detection and tracking: https://github.com/antoinelame/GazeTracking


Contributors:
@SIDDXSingh  
@rajashreetekaday
