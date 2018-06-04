import cv2
import glob
import math
import csv
import pickle
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
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