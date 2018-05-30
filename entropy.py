import cv2
import glob
import math
import csv
import numpy as np
from sklearn import svm

def entropy(img):
    """calculate the entropy of an image"""
    clr = ('b', 'g', 'r')
    for i, col in enumerate(clr):
        histBGR = cv2.calcHist([img], [i], None, [256], [0, 256])
    histLength = sum(histBGR)
    samples_probability = [float(h) / histLength for h in histBGR]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

def EkstraksiWarna(img):
    data=[]
    # Mencari rata-rata dan standar deviasi dari image (Library OpenCV)
    means,stdev = cv2.meanStdDev(img)
    # Dikonversi ke list
    stats = list(np.concatenate([means]).flatten())
    data[:]=stats
    return data

imgs1 = sorted(glob.glob('data/Chinese Tallow 1/*.jpg'))
imgs2 = sorted(glob.glob('data/Euphorbia Mili 2/*.jpg'))
imgs3 = sorted(glob.glob('data/Excoecaria 3/*.jpg'))
imgs4 = sorted(glob.glob('data/Garden Croton 4/*.jpg'))
imgs5 = sorted(glob.glob('data/Hevea Brasilinsis 5/*.jpg'))

# EKSTRAKSI FITUR
fitur = []
for img in imgs1:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)

for img in imgs2:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)

for img in imgs3:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)

for img in imgs4:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)

for img in imgs5:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)

# print(fitur)
# print(fitur[0])

kelas = []
for i in range(1,6):
    for j in range(1,301):
        kelas.append(i)

print(kelas)
print(len(kelas))

clf = svm.SVC()
clf.fit(fitur, kelas)
print(clf)

# prediksi = clf.predict(fitur[0:10])
# print(prediksi)
