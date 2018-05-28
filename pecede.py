import numpy as np
import cv2
import glob
import os
train_path="cinatallow\\training"
# fixed-sizes for image
fixed_size = tuple((100, 100))
# no.of.trees for Random Forests
num_trees = 100

# train_test_split size
test_size = 0.10

# seed for reproducing same results
seed = 9

# empty lists to hold feature vectors and labels
global_features = []
labels = []
def EkstraksiWarna(img):
    data=[]
    # Mencari rata-rata dan standar deviasi dari image (Library OpenCV)
    means,stdev = cv2.meanStdDev(img)
    # Dikonversi ke list
    stats = list(np.concatenate([means, stdev]).flatten())
    data[:]=stats

    return data
# get the training labels
train_labels = os.listdir(train_path)
for training_name in train_labels:
    # join the training data path and each species training folder
    dir = os.path.join(train_path, training_name)

    # get the current training label
    current_label = training_name
    # print dir
    k = 1
    for file in glob.glob("data/*.jpg"):
            # print (file)
            # get the image file name
            # file = dir + "\\" + str(x) + ".jpg"
            # print file
            # read the image and resize it to a fixed-size
            image = cv2.imread(file)
            image = cv2.resize(image, fixed_size)
            global_feature = np.hstack([EkstraksiWarna(image)])
            # update the list of labels and feature vectors
            labels.append(current_label)
            global_features.append(global_feature)
# for i in range(1, 15):
#     print i
#     print(global_features[i])

print len(global_features)

