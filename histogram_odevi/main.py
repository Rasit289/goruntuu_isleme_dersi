import cv2
import numpy as np
from numpy import zeros, shape
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

foto = cv2.imread("gul.jpg",0)


s=foto.shape

#dizimizi tanımloyoruz
Hist = np.zeros(shape=(256,1))

#dizide satır ve sütunları geziyoruz
for v in range (s[0]):
    for u in range (s[1]):
        #dizideki her bir pikselin sayısal değerini buluyoruz
        i= foto[v,u]
        #historam dizimizi bir arttıyoruz.
        Hist[i]=Hist[i]+1
#dizimizin histogramının sayısal değerlerini yazdırıyoruz
for t in range(256):
    print(Hist [t])
#histogramı gösteriyoruz
plt.plot(Hist)
plt.show()
cv2.waitKey()

