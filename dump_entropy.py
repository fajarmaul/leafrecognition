import cv2
import glob
import math
import csv
import pickle
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from function import EkstraksiWarna,preprocess,entropy
fixed_size = tuple((150, 250))
#Fungsi hitung entropi
def preprocess(img):
    def subgraygray(gray1, gray2):
        # catatan ukuran gray 1 dan 2 harus sama dan inten sitas gray2 berupa 0 atau 255 (treshold)
        row, col = gray2.shape
        output = np.zeros((row, col, 1), np.uint8)
        for i in range(0, row):
            for j in range(0, col):
                if int(gray1[i, j]) - int(gray2[i, j]) < 0:
                    output.itemset((i, j, 0), 0)
                else:
                    output.itemset((i, j, 0), int(gray1[i, j]) - int(gray2[i, j]))
        return output

    def subrgbgray(rgb, treshold):
        row, col, raw = rgb.shape
        # print row*col
        output = np.zeros((row, col, 3), np.uint8)
        for i in range(0, row):
            for j in range(0, col):
                if treshold[i, j] != 255:
                    output.itemset((i, j, 0), 255)
                    output.itemset((i, j, 1), 255)
                    output.itemset((i, j, 2), 255)
                else:
                    output[i, j] = rgb[i, j]
        return output
        kernel24 = np.ones((1, 1), np.uint8)
        tomat = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        b, g, r = cv2.split(tomat)
        tomat_segmented = cv2.subtract(g, b)
        ret, tomat_segmented = cv2.threshold(tomat_segmented, 10, 255, cv2.THRESH_BINARY)
        tomat_segmented = cv2.morphologyEx(tomat_segmented, cv2.MORPH_OPEN, kernel24)
        tomat_segmented = subrgbgray(tomat, tomat_segmented)
        return tomat_segmented

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

#Bagian yang di komen panjang di bawah ini = baca semua data, kemarin belum berhasil pake cara yg otomastinya
imgs1 = sorted(glob.glob('data/Chinese Tallow 1/*.jpg'))
imgs2 = sorted(glob.glob('data/Euphorbia Mili 2/*.jpg'))
imgs3 = sorted(glob.glob('data/Excoecaria 3/*.jpg'))
imgs4 = sorted(glob.glob('data/Garden Croton 4 - Copy/*.jpg'))
imgs5 = sorted(glob.glob('data/Hevea Brasilinsis 5 - Copy/*.jpg'))

# EKSTRAKSI FITUR
fitur = []
fiturTrain=[]
fiturX=[]
for img in imgs1:
    image = cv2.imread(img)
    height, width, channels = image.shape
    if height < width:
        image = np.rot90(image)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    # image = cv2.resize(image, fixed_size)
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
fiturTrain=X_train
fiturX=X_test
fitur = []
X_train=[]
X_test=[]
for img in imgs2:
    image = cv2.imread(img)
    # image = cv2.resize(image, fixed_size)
    if height < width:
        image = np.rot90(image)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
fiturTrain.extend(X_train)
fiturX.extend(X_test)
fitur = []
X_train=[]
X_test=[]
for img in imgs3:
    image = cv2.imread(img)
    height, width, channels = image.shape
    if height < width:
        image = np.rot90(image)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    # image = cv2.resize(image, fixed_size)
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
fiturTrain.extend(X_train)
fiturX.extend(X_test)
fitur = []
X_train=[]
X_test=[]
for img in imgs4:
    image = cv2.imread(img)
    height, width, channels = image.shape
    if height < width:
        image = np.rot90(image)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    # image = cv2.resize(image, fixed_size)
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
fiturTrain.extend(X_train)
fiturX.extend(X_test)
fitur = []
X_train=[]
X_test=[]
for img in imgs5:
    image = cv2.imread(img)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    # image = cv2.resize(image, fixed_size)
    height, width, channels = image.shape
    if height < width:
        image = np.rot90(image)
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
fiturTrain.extend(X_train)
fiturX.extend(X_test)
fitur = []
X_train=[]
X_test=[]
# print(fitur)
# print(fitur[0])

#Generate kelas untuk data di atas (1 sampe 5, masing2 300)
kelas = []
for i in range(1,6):
    for j in range(1,211):
        kelas.append(i)

print(kelas)
print(len(kelas))
# X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
# print(X_train[0])
clf = svm.SVC() #-->menjadikan variabel clf berisi fungsi SVM
clf.fit(fiturTrain, kelas) #-->membuat model di variabel clf dengan data=fitur dan kelas dari data=kelas
print(clf) #-->print modelnya

# save the model to disk
filename = 'modelSVM3.sav' #-->menamai model dengan 'modelSVM.sav'
# pickle.dump(clf, open(filename, 'wb'))  #-->simpan model dengan penamaan di atas ke storage

# # load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
print(loaded_model)

##Data test
# imgs6 = sorted(glob.glob('data/Data Train Buat Test - Copy/*.jpg'))
# fiturTest = []
# for img in imgs6:
#     image = cv2.imread(img)
#     # print(img)
#     #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
#     # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
#     # dan sebelumnya memanggil semua fungsi ekstraksi
#     height, width, channels = image.shape
#     if height < width:
#         image=np.rot90(image)
#     image = cv2.resize(image, fixed_size)
#     entropi = entropy(image)
#     rgb = EkstraksiWarna(image)
#     semuaFitur = np.hstack([entropi, rgb])
#     fiturTest.append(semuaFitur)

#predict dataTest dengan model yg sudah diload ke variabel loaded_model
prediksi = loaded_model.predict(fiturX)
# bagiansatu=prediksi[360:449]
# print(bagiansatu)
print(prediksi)
