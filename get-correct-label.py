from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

filenames = os.listdir("/Users/tomokikomiya/Documents/nagai.lab/input-raw-data/correct")

num_files = len(filenames)

correct_data = []
t = np.zeros((num_files),dtype='int32') #教師データの箱を用意し
# #画像名から好き嫌い度を読み取って教師データをつくる
for i,filename in zip(range(num_files),filenames):
    print(i)
    print(filename)
    number = int(filename.split("_")[1].split(".")[0])
    print(type(number))
    if number == 0:
      t[i] = 0
    if number == 1:
      t[i] = 1
    if number == 2:
      t[i] = 2
    if number == 3:
      t[i] = 3
    if number == 4:
      t[i] = 4
    print(filename)
    im = np.array(Image.open('/Users/tomokikomiya/Documents/nagai.lab/input-raw-data/correct/' + filename))
    print(im)
    correct_data.append(im)

print(correct_data)
print(correct_data[2])
plt.imshow(correct_data[2], cmap="gray")
plt.show()