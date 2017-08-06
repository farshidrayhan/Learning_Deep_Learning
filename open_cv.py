import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()
frame_counter = 0
while(True):
    frame_counter += 1
    screen = np.array(  ImageGrab.grab(bbox=(50,50,640,480)) )
    # printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    # .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
    cv2.imshow('streaming',cv2.cvtColor( screen,cv2.COLOR_BGR2RGB ) )
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    if float( format(time.time()-last_time) ) >= 1:
        print('FPS : ',frame_counter)
        last_time = time.time()
        frame_counter = 0
