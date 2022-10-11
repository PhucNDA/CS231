import cv2
from cv2 import sqrt
import numpy as np

# Bước 1: Load ảnh lên và hiển thị ảnh
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global img,refPt, cropping, lst_rois,img
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    clone=img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        lst_rois.append(refPt)

img = cv2.imread('sample1.jpg')
cv2.imshow("Input image", img)
cv2.setMouseCallback("Input image", click_and_crop)

# Bước 2: Chọn một vài pixel thuộc vùng nền
lst_rois = []
refPt=[]
cropping = False
while True:
    # display the image and wait for a keypress
    cv2.imshow("Input image", img)

    key = cv2.waitKey(1) & 0xFF
    # if the 'c' key is pressed, break from the loop
    if key == ord("c"):
        break
# if there are two reference points, then crop the region of interest
# from teh image and display it
print(lst_rois)
for item in lst_rois: 
    if len(item) == 2:
        clone=img.copy()
        roi = clone[item[0][1]:item[1][1], item[0][0]:item[1][0]]
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)
# close all open windows
cv2.destroyAllWindows()

# Bước 3: Tính giá trị màu đại diện
avg=np.zeros(3,dtype=float)
for item in lst_rois:
    if len(item) == 2:
        clone=img.copy()
        tmp=np.average(clone[item[0][1]:item[1][1], item[0][0]:item[1][0]],axis=(0,1)).astype(float)
        avg=np.add(avg,tmp)

avg/=(len(lst_rois))
print(avg)
# Bước 4: Tính độ lệch (threshold)
sum=0
var=np.zeros(3,dtype=float)
for item in lst_rois:
    if len(item) == 2:
        clone=img.copy()
        clone=clone[item[0][1]:item[1][1], item[0][0]:item[1][0]]
        w,h,c=clone.shape
        sum=sum+w*h
        for i in range (0,w):
            for j in range (0,h):
                temp=np.zeros(3,dtype=float)
                for z in range(0,3):
                    tmp=clone[i,j,z]-avg[z]
                    tmp=tmp*tmp
                    temp[z]=tmp
                for z in range(0,3):
                    var[z]+=temp[z]
for z in range(0,3):
    var[z]/=(sum)
var=np.sqrt(var)
print(var)



w,h,c=img.shape
# Bước 5: Bắt đầu phân đoạn ảnh với
# giá trị màu đại diện và độ lệch
for i in range (0,w):
    for j in range (0,h):
        f=0
        for z in range(0,3):
            if(img[i,j,z]>=avg[z]-2*var[z])and(img[i,j,z]<=avg[z]+2*var[z]):
                f+=1
        if f==3:
            img[i,j]=(255,255,255)


# Bước 6: THay vùng nền bằng ảnh bất kỳ

back=cv2.imread('background.jpg')
back=cv2.resize(back,(h,w))
for i in range (0,w):
    for j in range (0,h):
        if(img[i,j,0]==255 and img[i,j,1]==255 and img[i,j,2]==255):
            img[i,j]=back[i,j]

cv2.imshow('result',img)
cv2.waitKey(0)