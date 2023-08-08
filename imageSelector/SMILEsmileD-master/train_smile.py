from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.utils import img_to_array
from keras.utils import to_categorical
#from pyimagesearch.nn.conv import LeNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import imutils
import cv2
import os
# construct the argument parse and parse the arguments
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset of faces")
ap.add_argument("-m", "--model", required=True,
	help="path to output model")
args = vars(ap.parse_args())
# initialize the list of data and labels
data = []
labels = []