import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from GUI.Ui_SecondWindow import Ui_SecondWindow
from imageSelector.imageSelectorManager import imageSelectorManager
from manager.Image_information import Image_information

class Ui_MainWindow(object):
    def setupUi(self, main_window):
        # definition of the main window
        self.main_window = main_window
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(742, 679)
        self.main_window.setMinimumSize(QtCore.QSize(742, 679))
        self.main_window.setMaximumSize(QtCore.QSize(742, 679))
        self.main_window.setStyleSheet("")
        self.images_path = []

        self.setupWidgets()
        self.connectSignals()

    def setupWidgets(self):
        # the central widget
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.central_widget.setObjectName("centralwidget")

        # background label
        self.background_label = QtWidgets.QLabel(self.central_widget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 741, 681))
        self.background_label.setStyleSheet("background-color: white;")
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("background.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        self.start_button = QtWidgets.QPushButton(self.central_widget)
        self.setupButtonStyle(self.start_button, "Start",(24,0,139),QtCore.QRect(370,470,251,31),"start_button")

        self.select_folder_button = QtWidgets.QPushButton(self.central_widget)
        self.setupButtonStyle(self.select_folder_button, "Select Folder",(205,0,142),QtCore.QRect(370,400,251,51),"select_folder_button")

        self.main_window.setCentralWidget(self.central_widget)

    def setupButtonStyle(self, button, text,rgb,geometry,objectName):
        button.setGeometry(geometry)
        button.setStyleSheet("background-color: rgb"+str(rgb)+";color: white; border-radius: 10px; font-size: 20px;"
        )
        button.setText(text)
        button.setObjectName(objectName)


    def connectSignals(self):
        self.start_button.clicked.connect(self.openSecondWindow)
        self.select_folder_button.clicked.connect(self.selectFolderClicked)

    def openSecondWindow(self):

        if self.images_path !=[]:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SecondWindow(self.images_path)
            self.ui.setupUi(self.window)
            self.window.show()
            self.main_window.close()
        else:
            self.error_in_folder()



    def selectFolderClicked(self):
        folder_path = QFileDialog.getExistingDirectory(self.central_widget, "Select Directory")
        if folder_path:
            self.folder_path = folder_path
            self.images_path = []
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(
                            ".jpeg") or filename.endswith(".JPG") or filename.endswith(".PNG") or filename.endswith(
                            ".JPEG"):
                        self.images_path.append(os.path.join(root, filename))


    def error_in_folder(self):
        self.select_folder_button.setStyleSheet("background-color: rgb(255,0,0);color: white; border-radius: 10px; font-size: 20px;")
        self.select_folder_button.setText("Please select folder")
        self.select_folder_button.setObjectName("select_folder_button")
