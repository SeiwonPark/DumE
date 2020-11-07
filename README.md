# DumE   
Hi, Dum E!

**ABSTRACT**   
This is the project of making Dum-E. And it's still going on. I've commented explanations just for in case I've forgot the code later. To get the point, it would not be that detailed.   

&nbsp; Dum-E version 1 : It has a pan-tilt body without a camera. It can track a face using openCV.   
&nbsp; Dum-E version 2 :    


## Index   
+ [1. Settings](#1-settings)   
+ [2. Introduction](#2-introduction)   
    + [2.1 Dum-E version 1](#21-dum-e-version-1)   

<br/>   

## 1. Settings   
### Download Arduino Application   
`Arduino IDE 1.8.13`   

### Install Python Libraries   
`pip install pyserial`     
`pip install cv2`   

<br/>   

## 2. Introduction   
### 2.1 Dum-E version 1   
With the data `haarcascade_frontalface_default.xml`, Dum-E tracks the face. The camera you set in `dum-e.py` captures your face image using openCV, so it can detect your face and draw a rectangle around your face. Then `dum-e.py` file sends the encoded data of the center of the rectangle to the arduino you connected. (`dum-e.py` is based on [cascade classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) and its codes are [here](https://github.com/opencv/opencv/tree/master/data/haarcascades). You can also check other functions of cascade classifier [here](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html))       

<br/>   
