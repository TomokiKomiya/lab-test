from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

filename = "C:/Users/komit/Documents/nagailab/input-raw-data/teat.raw"
Imagesize = (416, 421)
file = open(filename, "rb")
# rawdata = file.seek(403)
rawdata = file.read()
print(rawdata.n_frames)
file.close()

img = Image.frombytes('F', Imagesize, rawdata, "raw", 'F;16')
print(img)
img.save("test_2.tif")
print("success")

npimg = np.array(img)
print(npimg)
print(len(npimg))
plt.subplot(1,2,1)
plt.imshow(npimg, cmap="gray")

gaussian = cv2.GaussianBlur(npimg,(15,15),3)
plt.subplot(1,2,2)
plt.imshow(gaussian, cmap="gray")

plt.show()