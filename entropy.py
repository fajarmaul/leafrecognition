import cv2
import glob
import math
import csv
import pickle
import numpy as np
from sklearn import svm

#Fungsi hitung entropi
def entropy(img):
    """calculate the entropy of an image"""
    clr = ('b', 'g', 'r')
    for i, col in enumerate(clr):
        histBGR = cv2.calcHist([img], [i], None, [256], [0, 256])
    histLength = sum(histBGR)
    samples_probability = [float(h) / histLength for h in histBGR]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

#Fungsi hitung nilai rata2 R, G, dan B
def EkstraksiWarna(img):
    data=[]
    # Mencari rata-rata dan standar deviasi dari image (Library OpenCV)
    means,stdev = cv2.meanStdDev(img)
    # Dikonversi ke list
    stats = list(np.concatenate([means]).flatten())
    data[:]=stats
    return data

##Bagian yang di komen panjang di bawah ini = baca semua data, kemarin belum berhasil pake cara yg otomastinya
# imgs1 = sorted(glob.glob('data/Chinese Tallow 1/*.jpg'))
# imgs2 = sorted(glob.glob('data/Euphorbia Mili 2/*.jpg'))
# imgs3 = sorted(glob.glob('data/Excoecaria 3/*.jpg'))
# imgs4 = sorted(glob.glob('data/Garden Croton 4/*.jpg'))
# imgs5 = sorted(glob.glob('data/Hevea Brasilinsis 5/*.jpg'))
#
# # EKSTRAKSI FITUR
# fitur = []
# for img in imgs1:
#     image = cv2.imread(img)
#     #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
#     # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
#     # dan sebelumnya memanggil semua fungsi ekstraksi
#     entropi = entropy(image)
#     rgb = EkstraksiWarna(image)
#     semuaFitur = np.hstack([entropi, rgb])
#     fitur.append(semuaFitur)
#
# for img in imgs2:
#     image = cv2.imread(img)
#     #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
#     # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
#     # dan sebelumnya memanggil semua fungsi ekstraksi
#     entropi = entropy(image)
#     rgb = EkstraksiWarna(image)
#     semuaFitur = np.hstack([entropi, rgb])
#     fitur.append(semuaFitur)
#
# for img in imgs3:
#     image = cv2.imread(img)
#     #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
#     # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
#     # dan sebelumnya memanggil semua fungsi ekstraksi
#     entropi = entropy(image)
#     rgb = EkstraksiWarna(image)
#     semuaFitur = np.hstack([entropi, rgb])
#     fitur.append(semuaFitur)
#
# for img in imgs4:
#     image = cv2.imread(img)
#     #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
#     # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
#     # dan sebelumnya memanggil semua fungsi ekstraksi
#     entropi = entropy(image)
#     rgb = EkstraksiWarna(image)
#     semuaFitur = np.hstack([entropi, rgb])
#     fitur.append(semuaFitur)
#
# for img in imgs5:
#     image = cv2.imread(img)
#     #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
#     # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
#     # dan sebelumnya memanggil semua fungsi ekstraksi
#     entropi = entropy(image)
#     rgb = EkstraksiWarna(image)
#     semuaFitur = np.hstack([entropi, rgb])
#     fitur.append(semuaFitur)
#
# # print(fitur)
# # print(fitur[0])

##Generate kelas untuk data di atas (1 sampe 5, masing2 300)
# kelas = []
# for i in range(1,6):
#     for j in range(1,301):
#         kelas.append(i)

# print(kelas)
# print(len(kelas))

# clf = svm.SVC() #-->menjadikan variabel clf berisi fungsi SVM
# clf.fit(fitur, kelas) #-->membuat model di variabel clf dengan data=fitur dan kelas dari data=kelas
# print(clf) #-->print modelnya

# # save the model to disk
filename = 'modelSVM.sav' #-->menamai model dengan 'modelSVM.sav'
# pickle.dump(clf, open(filename, 'wb'))  #-->simpan model dengan penamaan di atas ke storage

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
print(loaded_model)

##Data test
imgs6 = sorted(glob.glob('data/Data Train Buat Test/*.jpg'))
fiturTest = []
for img in imgs6:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fiturTest.append(semuaFitur)

#predict dataTest dengan model yg sudah diload ke variabel loaded_model
prediksi = loaded_model.predict(fiturTest)
print(prediksi)
