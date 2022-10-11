from statistics import median
import numpy as np
import math
import cv2

# image is an image
# kernel: kernel size <normally be a square so assert that it's a square odd size>
image =cv2.imread('oggy.jpg',0)
image=cv2.resize(image,(800,700))
print(type(image))
(W,H)=image.shape
kernel=(5,5)

def Max_pooling(kernel_size,img):
    I=img
    (W,H)=I.shape
    (m,n)=kernel_size
    it = (n-1)//2
    T=I
    T=cv2.resize(T,(H-2*it,W-it*2))
    for i in range(it,W-it):
        for j in range(it,H-it):
            res=0
            for u in range(-it,it+1):
                for v in range(-it,it+1):
                    res=max(res,I[i+u,j+v])
            T[i-it,j-it]=res
    return T

def Average_pooling(kernel_size,img):
    I=img
    (W,H)=I.shape
    (m,n)=kernel_size
    it = (n-1)//2
    T=I
    T=cv2.resize(T,(H-2*it,W-it*2))
    for i in range(it,W-it):
        for j in range(it,H-it):
            res=0
            for u in range(-it,it+1):
                for v in range(-it,it+1):
                    res+=I[i+u,j+v]
            T[i-it,j-it]=res//(m*n)
    return T

def Median_pooling(kernel_size,img):
    I=img
    (W,H)=I.shape
    (m,n)=kernel_size
    it = (n-1)//2
    T=I
    T=cv2.resize(T,(H-2*it,W-it*2))
    for i in range(it,W-it):
        for j in range(it,H-it):
            res=[]
            for u in range(-it,it+1):
                for v in range(-it,it+1):
                    res.append(I[i+u,j+v])
            res.sort()
            T[i-it,j-it]=median(res)
    return T

Final=Median_pooling(kernel,image)
cv2.imshow('ok',Final)
cv2.waitKey(0)

