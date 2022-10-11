import numpy as np
import cv2
import imutils

def prep_img(img):
    #include border (0,0,0) around an image
    tmp=np.zeros((img.shape[0]+2,img.shape[1]+2,img.shape[2]))
    W,H,C=img.shape[0],img.shape[1],img.shape[2]
    tmp[1:W+1,1:H+1,:]=img[:,:,:]
    tmp=tmp.astype(np.uint8)
    print('Finished Preparing Image')
    return img,tmp

def energy(img):
    #Based on gradient each dimension
    W,H,C=img.shape[0],img.shape[1],img.shape[2]
    #0,H-1,W-1 ~ border
    E=np.zeros((W-2,H-2))
    for i in range(1,W-1):
        for j in range(1,H-1):
            fia=img[i+1,j,:].astype(np.int64)
            fia=np.sum(fia)
            fib=img[i-1,j,:].astype(np.int64)
            fib=np.sum(fib)
            fi=fia-fib

            sea=img[i,j+1,:].astype(np.int64)
            sea=np.sum(sea)
            seb=img[i,j-1,:].astype(np.int64)
            seb=np.sum(seb)
            se=sea-seb

            E[i-1,j-1]=np.abs(fi)+np.abs(se)
    print('Finished Creating Energy Map')
    return E

def hash_pair(A):
    return A[0]*10000+A[1]

def dynamic_ngang(E):
    W,H=E.shape
    table=np.zeros((W,H))
    table[0,:]=E[0,:]
    for i in range (1,W):
        for j in range (0,H):
            table[i][j]=table[i-1][j]
            if(j-1>=0):
                table[i][j]=min(table[i][j],table[i-1][j-1])
            if(j+1<=H-1):
                table[i][j]=min(table[i][j],table[i-1][j+1])
            table[i][j]=table[i][j]+E[i][j]
    #trace back
    cur=[W-1,0]
    for j in range(0,H):
        if(table[W-1][j]<=table[cur[0]][cur[1]]):
            cur[1]=j 
    result={hash_pair(cur)}
    while cur[0]>0:
        tmp=table[cur[0]][cur[1]]-E[cur[0]][cur[1]]
        for j in range(-1,2,1):
            if(cur[1]+j>=0 and cur[1]+j<=H-1 and table[cur[0]-1][cur[1]+j]==tmp):
                cur=[cur[0]-1,cur[1]+j]
                result.add(hash_pair(cur))
                break
    print('Finished Running Algorithm')
    return result
    
def draw_seam(I,result):
    #Transform I->T
    W,H,C=I.shape
    T=np.zeros((W,H,C))
    for i in range (0,W):
        for j in range (0,H):
            if(hash_pair([i,j]) not in result):
                T[i,j,:]=I[i,j,:]
            else:
                T[i,j,:]=[255,255,255]
    T=T.astype(np.uint8)
    return T

def seam_ngang(I,result):
    #Transform I->T
    W,H,C=I.shape
    T=np.zeros((W,H-1,C))
    for i in range (0,W):
        for j in range (0,H):
            if(hash_pair([i,j]) not in result):
                T[i,j,:]=I[i,j,:]
            else:
                for jj in range(j+1,H):
                    T[i,jj-1,:]=I[i,jj,:]
                break
    T=T.astype(np.uint8)
    return T

def proceed_ngang(name,pix):
    image=cv2.imread(name)
    if(pix>image.shape[1]):
        print('SL pixels > axis[1]')
        return
    tmp=image
    cnt=0
    while cnt<pix:
        cnt=cnt+1
        print('-----Phase ',cnt)
        tmp,temp=prep_img(tmp)
        tmp=seam_ngang(tmp,dynamic_ngang(energy(temp)))
        print('-----Completed Phase ',cnt)
    return image,tmp

def rotate(image,deg):
    for ang in range(90,deg+1,90):
        image = np.rot90(image)
    return image

def proceed_doc(name,pix):
    image_goc=cv2.imread(name)
    # if(pix>image_goc.shape[0]):
    #     print('SL pixels > axis[0]')
    #     return
    image=rotate(image_goc,90)
    tmp=image
    cnt=0
    while cnt<pix:
        cnt=cnt+1
        print('-----Phase ',cnt)
        tmp,temp=prep_img(tmp)
        tmp=seam_ngang(tmp,dynamic_ngang(energy(temp)))
        print('-----Completed Phase ',cnt)
    tmp=rotate(tmp,270)
    return image_goc,tmp