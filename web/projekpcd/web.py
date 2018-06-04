#!/usr/bin/env python
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

# imgs1 = sorted(glob.glob('data/Chinese Tallow 1/*.jpg'))
# imgs2 = sorted(glob.glob('data/Euphorbia Mili 2/*.jpg'))
# imgs3 = sorted(glob.glob('data/Excoecaria 3/*.jpg'))
# imgs4 = sorted(glob.glob('data/Garden Croton 4/*.jpg'))
# imgs5 = sorted(glob.glob('data/Hevea Brasilinsis 5/*.jpg'))

singlefolder =  sorted(glob.glob('singleimage/*.jpg'))


# EKSTRAKSI FITUR
fitur = []
fiturTrain=[]
fiturX=[]
count = 0
for img in singlefolder:
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
    count = count + 1
    print(str((count))+" "+ str(semuaFitur))
    fitur.append(semuaFitur)
#data fitur displit menjadi data training dan data test
X_test = fitur
#data train &test dimasukan/diextend ke array
fiturX=X_test

# # load the model from disk
filename = 'modelSVM3.sav' #-->menamai model dengan 'modelSVM.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print(loaded_model)
prediksi = loaded_model.predict(fiturX)


print(prediksi[0])
