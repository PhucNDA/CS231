from statistics import median
import numpy as np
import math
import cv2

# image is an image
# kernel: kernel size <normally be a square so assert that it's a square even size>
image =cv2.imread('oggy.jpg',0)
image=cv2.resize(image,(800,700))
print(type(image))
(W,H)=image.shape
kernel=(4,4)

def Max_pooling(kernel_size,img):
    I=img
    (W,H)=I.shape
    (m,n)=kernel_size
    T=I
    T=cv2.resize(T,(H-n+1,W-m+1))
    for i in range(0,W-m):
        for j in range(0,H-n):
            res=0
            for u in range(0,m):
                for v in range(0,n):
                    res=max(res,I[i+u,j+v])
            T[i,j]=res
    return T

def Average_pooling(kernel_size,img):
    I=img
    (W,H)=I.shape
    (m,n)=kernel_size
    T=I
    T=cv2.resize(T,(H-n+1,W-m+1))
    for i in range(0,W-m):
        for j in range(0,H-n):
            res=0
            for u in range(0,m):
                for v in range(0,n):
                    res+=I[i+u,j+v]
            T[i,j]=res//(m*n)
    return T

def Median_pooling(kernel_size,img):
    I=img
    (W,H)=I.shape
    (m,n)=kernel_size
    T=I
    T=cv2.resize(T,(H-n+1,W-m+1))
    for i in range(0,W-m):
        for j in range(0,H-n):
            res=[]
            for u in range(0,m):
                for v in range(0,n):
                    res.append(I[i+u,j+v])
            res.sort()
            T[i,j]=median(res)
    return T

Final=Average_pooling(kernel,image)
cv2.imshow('ok',Final)
cv2.waitKey(0)

