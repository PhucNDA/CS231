import cv2

class Image:
    def __init__(self, imgg, time=500, size=500):
        self.size = size
        self.time = time
        self.shifted = 0.0
        self.img = imgg
        self.height, self.width, _ = self.img.shape
        if self.width < self.height:
            self.height = int(self.height*size/self.width)
            self.width = size
            self.img = cv2.resize(self.img, (self.width, self.height))
            self.shift = self.height - size
            self.shift_height = True
        else:
            self.width = int(self.width*size/self.height)
            self.height = size
            self.shift = self.width - size
            self.img = cv2.resize(self.img, (self.width, self.height))
            self.shift_height = False
        self.delta_shift = self.shift/self.time

    def get_frame(self):
        if self.shift_height:
            roi = self.img[int(self.shifted):int(self.shifted) + self.size, :, :]
        else:
            roi = self.img[:, int(self.shifted):int(self.shifted) + self.size, :]
        self.shifted += self.delta_shift
        if self.shifted > self.shift:
            self.shifted = self.shift
        if self.shifted < 0:
            self.shifted = 0
        return roi


path='./Images/image'
images=[]
for name in range(1,11,1):
    pic=cv2.imread(path+str(name)+'.jpg')
    images.append(Image(pic))

out = cv2.VideoWriter('./output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, (500, 500))

prev_image=images[9]
for img in images:
    for it in range(100):
        alpha = it/100
        beta = 1.0 - alpha
        fig = cv2.addWeighted(img.get_frame(), alpha, prev_image.get_frame(), beta, 0)
        cv2.imshow("Slide", fig)
        cv2.waitKey(4)
        out.write(fig)
    prev_image=img
    
out.release()