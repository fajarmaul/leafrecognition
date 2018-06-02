import cv2
import numpy as np
#from matplotlib import pyplot as plt
import glob
import csv
fixed_size = tuple((150, 250))
def subgraygray (gray1, gray2):
    #catatan ukuran gray 1 dan 2 harus sama dan inten sitas gray2 berupa 0 atau 255 (treshold)
    row, col = gray2.shape
    output = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if int(gray1[i,j])-int(gray2[i,j]) < 0 :
                output.itemset((i,j,0),0)
            else:
                output.itemset((i,j,0),int(gray1[i,j])-int(gray2[i,j]))
    return output

def subrgbgray(rgb,treshold):
    row, col , raw = rgb.shape
    #print row*col
    output = np.zeros((row,col,3), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if treshold[i,j] != 255:
                output.itemset((i,j,0),255)
                output.itemset((i,j,1),255)
                output.itemset((i,j,2),255)
            else:
                output[i,j]=rgb[i,j]
    return output

kernel3 = np.ones((3,3),np.uint8)
imgnames=sorted(glob.glob('data/Hevea Brasilinsis 5/*.jpg'))
data=[]
for imgname in imgnames:
    kernel24 = np.ones((1, 1), np.uint8)
    tomat = cv2.imread(imgname)
    tomat = cv2.resize(tomat, (0,0), fx=0.5, fy=0.5)
    height, width, channels = tomat.shape
    if height < width:
        np.rot90(tomat)
    tomat = cv2.resize(tomat, fixed_size)
    b,g,r = cv2.split( tomat )
    tomat_segmented = cv2.subtract(g,b)
    ret, tomat_segmented = cv2.threshold(tomat_segmented, 8,255,cv2.THRESH_BINARY)
    tomat_segmented = cv2.morphologyEx(tomat_segmented, cv2.MORPH_OPEN, kernel24)
    tomat_segmented = subrgbgray(tomat, tomat_segmented)
    cv2.imwrite(imgname,tomat_segmented)
    cv2.waitKey()

cv2.destroyAllWindows()
