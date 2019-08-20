# 一括でtiffデータを読み込む
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

filename = "C:/Users/komit/Documents/nagailab/input-raw-data/test_5.tif"

img = Image.open(filename)

fLength = img.n_frames

print(fLength)

for i in range(0,fLength):
    img.seek(i)
    img.save("C:/Users/komit/Documents/nagailab/input-raw-data/dataset/testdata_" + str(i) + ".tif")

