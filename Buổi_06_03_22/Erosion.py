import cv2
import numpy as np
import sys

sys.setrecursionlimit(1000000)
img =cv2.imread('hongcau.jpg')

#--Convert Binary Image
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

img = bw_img.copy()
cv2.imshow('Anh Ban Dau',img)
cv2.waitKey(0)

#--Median_blur
# img = cv2.medianBlur(img, 3) 
# cv2.imshow('Anh Sau Median_blur',img)
# cv2.waitKey(0)

#--Enrode
kernel = np.ones((15, 15), np.uint8)
img = cv2.dilate(img, kernel) 
cv2.imshow('Anh Sau Eroded',img)
cv2.waitKey(0)

W,H,C=img.shape
print(W,H,C)
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

cnt=0

def dfs(x,y,vis,img):
    global cnt
    q=[]
    q.append((x,y))
    while(len(q)!=0):
        x,y=q[-1]
        q.pop()
        vis[x,y]=1
        for i in range(8):
            xx=x+dx[i]
            yy=y+dy[i]
            if(xx>=0 and xx<=W-1 and yy>=0 and yy<=H-1 and vis[xx,yy]==0 and img[xx,yy,0]==0):
                q.append((xx,yy))
                cnt+=1

def demtplt(img):
    global cnt
    W,H,C=img.shape
    vis=np.zeros((W,H))
    dem=0
    sum=0
    for i in range(W):
        for j in range(H):
            if(vis[i,j]==0 and img[i,j,0]==0):
                cnt=0
                dfs(i,j,vis,img)
                sum+=cnt
                dem+=1
    return [dem,sum]

ans=demtplt(img)
print("So thanh phan lien thong: ",ans[0])
print("Dien tich cac te bao mau: ",ans[1])
