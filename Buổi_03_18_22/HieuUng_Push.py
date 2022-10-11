import matplotlib.pyplot as plt
import cv2

# ---Read Image
img1=cv2.imread(r"C:\Users\ACER\Pictures\Predator\Planet9_Wallpaper_5000x2813.jpg")
img2=cv2.imread(r"C:\Users\ACER\Pictures\Predator\Predator_Wallpaper_5000x2814.jpg")
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

# --- Push Effect
speed=3
for D in range(0,h+1,speed):
    result=img1.copy()
    result[0:h-D,:,:]=img1[D:h,:,:]
    result[h-D:h,:,:]=img2[0:D,:,:]
    cv2.imshow("Push",result)
    cv2.waitKey(5)
