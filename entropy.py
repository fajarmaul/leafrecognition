import cv2
import glob
import math
import numpy as np

def entropy(img):
    """calculate the entropy of an image"""
    clr = ('b', 'g', 'r')
    for i, col in enumerate(clr):
        histBGR = cv2.calcHist([img], [i], None, [256], [0, 256])

    histLength = sum(histBGR)
    samples_probability = [float(h) / histLength for h in histBGR]

    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

imgs = sorted(glob.glob('data/*.jpg'))
# csv = open(data.csv, "w")

# EKSTRAKSI FITUR
fitur = []
for img in imgs:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    fitur.append(entropi)
    # csv.write(entropi)

print(fitur)
print(fitur[0])
