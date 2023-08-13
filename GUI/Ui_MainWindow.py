import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from GUI.Ui_SecondWindow import Ui_SecondWindow
from imageSelector.imageSelectorManager import imageSelectorManager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 679)
        MainWindow.setMinimumSize(QtCore.QSize(742, 679))
        MainWindow.setMaximumSize(QtCore.QSize(742, 679))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 741, 681))
        self.label.setStyleSheet("background-color: white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 470, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet(
            "background-color: rgb(24,0,139); color: white; border-radius: 10px;   font-size: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 400, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_second_window)  # Connect button click to open_second_window function
        self.pushButton_3.clicked.connect(self.select_folder_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.pushButton_3.setText(_translate("MainWindow", "select folder"))

    def open_second_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def select_folder_clicked(self):
        folder_path = QFileDialog.getExistingDirectory(self.centralwidget, "Select Directory")
        if folder_path:
            self.folder_path = folder_path
            self.get_images_in_folder()
            i = imageSelectorManager(self.folder_path, self.images_path)

    def get_images_in_folder(self):
        self.images_path = []
        for root, dirs, filenames in os.walk(self.folder_path):
            for filename in filenames:
                if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                    self.images_path.append(filename)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
