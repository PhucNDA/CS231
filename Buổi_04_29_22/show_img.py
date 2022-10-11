import cv2

def show(img,name):
    print(name+' shape (W,H,C)=',img.shape)
    cv2.imshow(name+' shape (W,H,C)='+str(img.shape),img)
    cv2.waitKey(0)