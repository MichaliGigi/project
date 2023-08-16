from __future__ import print_function  # זיהוי דמויות
import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
import face_recognition
import os
import csv
import sys
# gui packages
from GUI.Ui_SecondWindow import Ui_SecondWindow
from imageSelector.imageSelectorManager import imageSelectorManager

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

