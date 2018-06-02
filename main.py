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

    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
#data train &test dimasukan/diextend ke array
fiturTrain=X_train
fiturX=X_test
fitur = []
X_train=[]
X_test=[]
for img in imgs2:
    image = cv2.imread(img)
    if height < width:
        image = np.rot90(image)
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
#data train &test dimasukan/diextend ke array
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
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
#data train &test dimasukan/diextend ke array
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
    # kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
#data train &test dimasukan/diextend ke array
fiturTrain.extend(X_train)
fiturX.extend(X_test)
fitur = []
X_train=[]
X_test=[]
for img in imgs5:
    image = cv2.imread(img)
    # kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    height, width, channels = image.shape
    if height < width:
        image = np.rot90(image)
    entropi = entropy(image)
    rgb = EkstraksiWarna(image)
    semuaFitur = np.hstack([entropi, rgb])
    fitur.append(semuaFitur)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(fitur, test_size=0.3, random_state=42)
#data train &test dimasukan/diextend ke array
fiturTrain.extend(X_train)
fiturX.extend(X_test)
fitur = []
X_train=[]
X_test=[]

#Generate kelas untuk data di atas (1 sampe 5, masing2 300)
kelas = []
for i in range(1,6):
    for j in range(1,211):
        kelas.append(i)

print(kelas)
print(len(kelas))
clf = svm.SVC() #-->menjadikan variabel clf berisi fungsi SVM
clf.fit(fiturTrain, kelas) #-->membuat model di variabel clf dengan data=fitur dan kelas dari data=kelas
print(clf) #-->print modelnya

# save the model to disk
filename = 'modelSVM3.sav' #-->menamai model dengan 'modelSVM.sav'
pickle.dump(clf, open(filename, 'wb'))  #-->simpan model dengan penamaan di atas ke storage
# # load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
print(loaded_model)
prediksi = loaded_model.predict(fiturX)
print(prediksi)