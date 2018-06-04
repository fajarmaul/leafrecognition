import cv2
import glob
import math
import csv
import pickle
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from function import preprocess,accuracy,extract
fixed_size = tuple((150, 250))

imgs1 = sorted(glob.glob('data/Chinese Tallow 1/*.jpg'))
imgs2 = sorted(glob.glob('data/Euphorbia Mili 2/*.jpg'))
imgs3 = sorted(glob.glob('data/Excoecaria 3/*.jpg'))
imgs4 = sorted(glob.glob('data/Garden Croton 4 - Copy/*.jpg'))
imgs5 = sorted(glob.glob('data/Hevea Brasilinsis 5 - Copy/*.jpg'))


# EKSTRAKSI FITUR
image1=extract(imgs1)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(image1, test_size=0.3)
#data train &test dimasukan/diextend ke array
fiturTrain=X_train
fiturX=X_test

image2=extract(imgs2)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(image2, test_size=0.3)
#data train &test dimasukan/diextend ke array
fiturTrain.extend(X_train)
fiturX.extend(X_test)

image3=extract(imgs3)
X_train, X_test = train_test_split(image3, test_size=0.3)
#data train &test dimasukan/diextend ke array
fiturTrain.extend(X_train)
fiturX.extend(X_test)
X_train=[]
X_test=[]
image4=extract(imgs4)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(image4, test_size=0.3)
#data train &test dimasukan/diextend ke array
fiturTrain.extend(X_train)
fiturX.extend(X_test)

image5=extract(imgs5)
#data fitur displit menjadi data training dan data test
X_train, X_test = train_test_split(image5, test_size=0.3)
#data train &test dimasukan/diextend ke array
fiturTrain.extend(X_train)
fiturX.extend(X_test)


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

acc=accuracy(prediksi,0,89,1)
acc2=accuracy(prediksi,90,179,2)
acc3=accuracy(prediksi,180,269,3)
acc4=accuracy(prediksi,270,359,4)
acc5=accuracy(prediksi,360,449,5)
print((acc+acc2+acc3+acc4+acc5)/450*100)



# #Data test
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
# prediksi = loaded_model.predict(fiturTest)
# print(prediksi)