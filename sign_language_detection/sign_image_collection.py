import cv2
from  os import mkdir
from os import path
import time
import uuid
 
images_path = 'ADD THE FOLDER WHERE IMAGES TO BE SAVED'
 
labels = ['A', 'B, 'C', 'D'] #ADD THE LABELS OF ALPHABETS
number_imgs = 30


for lable in labels :
    mkdir ('images_path' + lable)
    cap = cv2.VideoCapture(0)
    print('collicting images for {}'.format(lable))
    time.sleep(5)
    for imgnum in range (number_imgs):
        ret, frame = cap.read()
        row = frame.shape[1]
        col = frame.shape[0]
        cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
        cv2.imshow("frame",frame)
        cv2.imshow("ROI",frame[40:400,0:300])
        frame=frame[40:400,0:300]
        image_name = path.join(images_path, lable,lable+'.'+'{}.png'.format(uuid.uuid4()))
        cv2.imwrite(image_name, frame)
       
        time.sleep(3)
        
        
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
cap.release()

