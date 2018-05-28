import cv2
import glob
import math
import numpy as np
import csv

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
for i in range(0,len(fitur)):
    print(fitur[i])



# csv.write("data",fitur)
var1 = 3.3333
var2 = 50284
var3 = 2929292

#Write to CSV
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['No']+['Entropy'] + ['RGB'] + ['Tekstur'])
    for i in range(1,len(fitur)):
        var1+=1.054353
        var2+=1.08898
        var3+=1.087775
        spamwriter.writerow([i,fitur[i][0], var2, var3])
