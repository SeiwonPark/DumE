from serial import Serial
import time
import cv2  # this project uses openCV library

arduino = Serial(port='/dev/cu.usbmodem14201', baudrate=9600)  # port='the port your arduino is connected'
time.sleep(2)
print("Connected to Arduino...")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # uses face_cascade detector
cap = cv2.VideoCapture(0)  # cv2.VideoCapture('index') 
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
print("Getting camera image...")

#Read the captured image, convert it to Gray image and find faces
while True:
    ret, img = cap.read()
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img', 640,480)
    #cv2.line(img,(500,250),(0,250),(0,255,0),1)
    #cv2.line(img,(250,0),(250,500),(0,255,0),1)
    #cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

#detect the face and make a rectangle around it.
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        roi_gray  = gray[y:y+h, x:x+w]  # roi : region of interesting
        roi_color = img[y:y+h, x:x+w]

        # print values
        # arr = {y:y+h, x:x+w}
        # print (arr)
        #
        # print ('X :' +str(x))
        # print ('Y :'+str(y))
        # print ('x+w :' +str(x+w))
        # print ('y+h :' +str(y+h))

# Center of roi (Rectangle)   
        xx = int(x+(x+h)/2)
        yy = int(y+(y+w)/2)
        # print (xx)
        # print (yy)
        center = (xx, yy)

# sending data to arduino
#         print("Center of Rectangle is :", center)
        data = "X{0:d}Y{1:d}Z".format(xx, yy)
        # print ("output = '" +data+ "'")
        arduino.write(data.encode())

#Display the stream.
    cv2.imshow('img', img)


#Hit 'Esc' to terminate execution
    if cv2.waitKey(1) & 0xFF == ord('q'):  # cv2.waitKey('delay') returns 32 bit int value   
       break                               # 0xFF is equal to 11111111   
                                           # Thus, cv2.waitKey(1) & 0xFF returns the last 8 binary number of 'pressed key' as 0xFF is 11111111   
                                           # So, if you press the key 'q', it'll break the while loop   
