import cv2

def Push(img1, img2):
    h,w,c=img1.shape
    speed=2
    alpha=0
    speedalpha=2
    for D in range(0,h+1,speed):
        result=img1.copy()
        al=alpha/h
        result[0:h-D,:,:]=img1[D:h,:,:]*(1-al)
        result[h-D:h,:,:]=img2[0:D,:,:]*al
        alpha=min(h,alpha+speedalpha)
        cv2.imshow("Slide",result)
        cv2.waitKey(10)

def Wipe(img1, img2):
    h,w,c=img1.shape
    speed=2
    alpha=0
    speedalpha=2
    for D in range(0,w+1,speed):
        result=img1.copy()
        al=alpha/w
        result[:,0:w-D,:]=img1[:,D:w,:]*(1-al)
        result[:,w-D:w,:]=img2[:,0:D,:]*al
        alpha=min(h,alpha+speedalpha)
        cv2.imshow("Slide",result)
        cv2.waitKey(10)

def Uncover(img1, img2):
    h,w,c=img1.shape
    speed=2
    alpha=0
    speedalpha=2
    for D in range(0,w+1,speed):
        result=img1.copy()
        al=alpha/w
        result[:,0:w-D,:] = img1[:,D:w,:]*(1-al)
        result[:,w-D:w,:] = img2[:,w-D:w,:]*al
        alpha=min(h,alpha+speedalpha)
        cv2.imshow("Slide",result)
        cv2.waitKey(10)

def Blur(img1,img2):
    result = img2.copy()
    for alpha in range(0,300,1):
        al=alpha/300
        result[:,:,:] = img2[:,:,:] * al + img1[:,:,:] * (1 - al)
        cv2.imshow('Slide', result)
        cv2.waitKey(5)

path='./Images/image'
fig=[]
for name in range(1,11,1):
    pic=cv2.imread(path+str(name)+'.jpg')
    print('Already Proccessed: ' + path+str(name)+'.jpg')
    pic=cv2.resize(pic,(800,800))
    fig.append(pic)


# Blur(fig[1],fig[2])
# Uncover(fig[2],fig[3])
# Push(fig[3],fig[4])
# Wipe(fig[4],fig[5])
# Blur(fig[5],fig[6])
# Uncover(fig[6],fig[7])
# Push(fig[7],fig[8])
# Blur(fig[8],fig[9])