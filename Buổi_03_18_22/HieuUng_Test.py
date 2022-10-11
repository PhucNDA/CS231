import matplotlib.pyplot as plt
import cv2
import os
import imageio

# ---Read Image
img1=cv2.imread(r"C:\Users\ACER\Pictures\273946852_730729951621099_1256031793857665890_n.jpg")
img2=cv2.imread(r"C:\Users\ACER\Pictures\275410373_681804783244660_7871257484937981892_n.jpg")
# ---Get image info
h1,w1,c1=img1.shape
h2,w2,c2=img2.shape

h=min(h1,h2,600)
w=min(w1,w2,1000)
# ---Resize image
img1 = cv2.resize(img1,(w,h))
img2 = cv2.resize(img2,(w,h))

# ---Show image
# cv2.imshow('Anh 1',img1)
# cv2.imshow('Anh 2',img2)
# cv2.waitKey(0)

# --- Uncover Effect
speed=3
results=[]
for D in range(0,w+1,speed):
    result=img1.copy()
    result[:,0:w-D,:] = img1[:,D:w,:]
    result[:,w-D:w,:] = img2[:,w-D:w,:]
    results.append(result)

imageio.mimsave(r"C:\Users\ACER\Pictures\test.gif",results)
print("ok")
