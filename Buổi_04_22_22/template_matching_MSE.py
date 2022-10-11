from statistics import median
import numpy as np
import math
import cv2

image =cv2.imread('tuquy_3.jpg',0)
print(type(image))
(W,H)=image.shape
kernel=cv2.imread('chat_co1.jpg.png',0)
(M,N)=kernel.shape

result=9999999999
pos=[0,0]

for i in range(0,W-M):
        for j in range(0,H-N):
            s=0
            tmp=np.array(image[i:i+M,j:j+N])
            tmp1=np.array(kernel[0:M,0:N])
            s=np.array(((tmp1 - tmp)**2))
            s=np.sum(s)
            s=s//(M*N)
            if(s<=result):
                    result=s
                    pos=[i,j]

x_left_top,y_left_top=pos[0],pos[1]
x_right_top,y_right_top=pos[0],pos[1]+N-1,
x_left_bottom,y_left_bottom=pos[0]+M-1,pos[1]
x_right_bottom,y_right_bottom=pos[0]+M-1,pos[1]+N-1


cv2.line(image,(y_left_top,x_left_top),(y_right_top,x_right_top),(255, 0, 0), 1, 1)
cv2.line(image,(y_left_top,x_left_top),(y_left_bottom,x_left_bottom),(255, 0, 0), 1, 1)
cv2.line(image,(y_left_bottom,x_left_bottom),(y_right_bottom,x_right_bottom),(255, 0, 0), 1, 1)
cv2.line(image,(y_right_bottom,x_right_bottom),(y_right_top,x_right_top),(255, 0, 0), 1, 1)

cv2.imshow('result',image)
cv2.waitKey(0)