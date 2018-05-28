import cv2
import glob
import math
import numpy as np
import csv

def EkstraksiWarna(img):
    data=[]
    # Mencari rata-rata dan standar deviasi dari image (Library OpenCV)
    means,stdev = cv2.meanStdDev(img)
    # Dikonversi ke list
    stats = list(np.concatenate([means]).flatten())
    data[:]=stats
    return data

def entropy(img):
    """calculate the entropy of an image"""
    clr = ('b', 'g', 'r')
    for i, col in enumerate(clr):
        histBGR = cv2.calcHist([img], [i], None, [256], [0, 256])
    histLength = sum(histBGR)
    samples_probability = [float(h) / histLength for h in histBGR]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])


#read gambar
imgs = sorted(glob.glob('data/*.jpg'))

# EKSTRAKSI FITUR
hasilentropi = []
hasilrgb = []
for img in imgs:
    image = cv2.imread(img)
    #Entropi
    #kalau fungsi ekstraksi fitur sudah ada semua, penulisan bagian entropi jadi gini:
    # semuaFitur = np.hstack([fitur1, fitur2, fitur3, dst.]), sisanya menyesuaikan
    # dan sebelumnya memanggil semua fungsi ekstraksi
    entropi = entropy(image)
    hasilentropi.append(entropi)

    #RGB
    rataanrgb = EkstraksiWarna(image)
    hasilrgb.append(rataanrgb)

for i in range(0,len(hasilrgb)):
    print(hasilrgb[i])




# csv.write("data",fitur)
var1 = 3.3333
var2 = 50284
var3 = 2929292

#Write to CSV
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['No']+['Entropy'] + ['RGB'] + ['Tekstur'])
    for i in range(1,len(imgs)):
        var1+=1.054353
        var2+=1.08898
        var3+=1.087775
        spamwriter.writerow([i,hasilentropi[i][0], hasilrgb[i], var3])
