import cv2
import imageio

#Anh foreground
fg=cv2.imread(r'C:\Users\ACER\Pictures\800px-Edsger_Wybe_Dijkstra.jpg')
print("Kich Thuoc Anh ForeGround:",fg.shape)
#Anh Mask
ms=cv2.imread(r'C:\Users\ACER\Pictures\800px-Edsger_Wybe_Dijkstra-removebg-preview.png')
print("Kich Thuoc Anh Mask:",ms.shape)
#Chuyen hoa cung kich thuoc
h,w,c=ms.shape
fg=cv2.resize(fg,(w,h))
print("Sau khi Reize")
print("Kich Thuoc Anh ForeGround:",fg.shape)
print("Kich Thuoc Anh Mask:",ms.shape)
#Load Gif
url = "https://media0.giphy.com/media/2vmiW6mcYgKst3QVDK/giphy.gif"
frames = imageio.mimread(imageio.core.urlopen(url).read(), '.gif')
#frames = imageio.mimread(r'C:\Users\ACER\Pictures\firework-2.gif')

#Cat frame

# fg_h, fg_w, fg_c = fg.shape
# bg_h, bg_w, bg_c = frames[0].shape
# top = int((bg_h-fg_h)/2)
# left = int((bg_w-fg_w)/2)
# bgs = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]
print(frames[0].shape)
bgs=[]
for frame in frames:
    bgs.append(cv2.resize(frame,(w,h)))

print(fg.shape)
print(ms.shape)
print(bgs[0].shape)
print(frames[0].shape)
#Chen background
results = []
alpha = 0.3
for i in range(len(bgs)):
    result = fg.copy()
    result[ms[:,:,2] != 0] = alpha * result[ms[:,:,2] != 0]
    bgs[i][ms[:,:,2] == 0] = 0
    bgs[i][ms[:,:,2] != 0] = (1-alpha)*bgs[i][ms[:,:,2] != 0]
    result = result + bgs[i][:,:,0:3]
    results.append(result)
imageio.mimsave(r'C:\Users\ACER\Pictures\result.gif', results)