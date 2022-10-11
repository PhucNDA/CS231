from statistics import median
import numpy as np
import math
import cv2

image =cv2.imread('tuquy_3.jpg',0)
print(type(image))
(W,H)=image.shape
kernel=cv2.imread('chat_co1.jpg.png',0)
(M,N)=kernel.shape

result=0
pos=[0,0]

feat=np.zeros(shape=(W-M,H-N))
for i in range(0,W-M):
        for j in range(0,H-N):
            s=0
            tmp=np.array(image[i:i+M,j:j+N])
            tmp1=np.array(kernel[0:M,0:N])
            tmp=tmp.flatten()
            tmp1=tmp1.flatten()

            tmp=tmp.astype(int)
            tmp1=tmp1.astype(int)
            combine=tmp*tmp1
            combine=np.sum(combine)

            tmp=tmp**2
            tmp=np.sum(tmp)
            tmp=tmp**0.5

            tmp1=tmp1**2
            tmp1=np.sum(tmp1)
            tmp1=tmp1**0.5

            feat[i][j]=combine/(tmp*tmp1)

print(feat)

for i in range(0,W-M):
        for j in range(0,H-N):
                if(feat[i][j]>result):
                        pos=[i,j]
                        result=feat[i][j]           

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