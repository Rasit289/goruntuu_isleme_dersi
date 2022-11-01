import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('gunes.jpg',0)
cv2.imshow("original_resim",image)


[h,w] = image.shape

for i in range(h):
    for j in range(w):
        image[i,j] = np.max(image) - image[i,j]

cv2.imshow("goruntunun_tersi",image)
cv2.waitKey()