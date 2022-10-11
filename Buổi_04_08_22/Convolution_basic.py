import numpy as np
import math
import cv2

# I is an image
# F is a filter (always a squrae)
I=np.array([[7,9,15,20],[8,10,19,30],[15,20,19,3]])
F=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

(W,H)=I.shape
(m,n)=F.shape

it = (n-1)//2
T=np.zeros(shape=(W-it*2,H-2*it))
for i in range(it,W-it):
    for j in range(it,H-it):
        res=0
        for u in range(-it,it+1):
            for v in range(-it,it+1):
                res=res+I[i-u,j-v]*F[u+it,v+it]
        T[i-it,j-it]=res

print(T)