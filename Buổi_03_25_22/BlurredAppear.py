import cv2

#Anh thu 1
img1=cv2.imread(r'C:\Users\ACER\Pictures\800px-Edsger_Wybe_Dijkstra.jpg')
print("Kich Thuoc Anh 1:",img1.shape)
#Anh thu 2
img2=cv2.imread(r'C:\Users\ACER\Pictures\Predator\Predator_Wallpaper_5000x2814.jpg')
print("Kich Thuoc Anh 2:",img2.shape)
#Chuyen hoa cung kich thuoc
img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))
print("Sau khi Reize")
print("Kich Thuoc Anh 1:",img1.shape)
print("Kich Thuoc Anh 2:",img2.shape)

result = img1.copy()
for alpha in range(0,200,1):
    al=alpha/200
    result[:,:,:] = img1[:,:,:] * al + img2[:,:,:] * (1 - al)
    cv2.imshow('Result', result)
    cv2.waitKey(5)
 

          