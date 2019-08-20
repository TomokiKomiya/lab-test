import numpy as np
import cv2

import sys, os
from PIL import Image
img_pil = Image.open("/Users/tomokikomiya/Documents/nagai.lab/input-raw-data/correct/testdata_1.tif")
FITC = []

try:
    count = 30
    while count<=100:
        img_pil.seek(count)
        img = np.asarray(img_pil)
        img.flags.writeable = True
        img = cv2.resize(img,(512,512))
        FITC.append(img)
        count += 1
        print(count,end=",")
except EOFError:
    pass

FITC = np.array(FITC)
print(FITC.shape)