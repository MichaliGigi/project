import csv
import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
       # MainWindow.setStyleSheet("background-color: white;")
        MainWindow.resize(1331, 820)
        MainWindow.setMinimumSize(QtCore.QSize(1331, 820))
        MainWindow.setMaximumSize(QtCore.QSize(1331, 820))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, 0, 1341, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("backup.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(16, 13, 81, 61))
        self.camera.setText("")
        self.camera.setPixmap(QtGui.QPixmap("camera.png"))
        self.camera.setScaledContents(True)
        self.camera.setObjectName("camera")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 140, 1231, 671))  # Adjusted geometry
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.eventsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)

        self.eventsLayout.setContentsMargins(0, 0, 0, 0)
        self.eventsLayout.setObjectName("eventsLayout")

        # Read the CSV file and extract image paths and categories
        image_data = []
        # Get the path of the current script file
        script_path = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the CSV file using os.path.join
        self.csv_file_path = os.path.join(script_path, '..', 'manager', 'images_info.csv')

        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)  # Skip header row
            for row in self.csvreader:
                # check in image_data that the category number is not already present
                if not any(d['category'] == int(row[1]) for d in image_data):
                    image_data.append({'image_path': row[0], 'category': int(row[1])})
        #close the csv file
        csvfile.close()

        self.show_image( image_data)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def show_image_event(self, image_data):
        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0
        for data in image_data:
            image_path = data['image_path']
            category = data['sub category']

            self.showImg(image_path, row, col)
            delete_button = QtWidgets.QPushButton(f"delete", self.centralwidget)
            delete_button.clicked.connect(lambda checked, num=category: self.delete_img(num))  # Pass the event number

            self.eventsLayout.addWidget(delete_button, row + 1, col)
            change_button = QtWidgets.QPushButton(f"change", self.centralwidget)
            change_button.clicked.connect(lambda checked, num=category: self.change_img(num))  # Pass the event number

            self.eventsLayout.addWidget(change_button, row + 1, col)

            col += 1
            if col >= 3:  # Display 3 columns, then move to the next row
                col = 0
                row += 2
    def delete_img(self, num):
        print("delete"+num)
    def change_img(self, num):
        print("change"+num)

    def show_image(self, image_data):

        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0
        for data in image_data:
            image_path = data['image_path']
            category = data['category']

            self.showImg(image_path, row, col)
            button = QtWidgets.QPushButton(f"Event {category}", self.centralwidget)
            button.clicked.connect(lambda checked, num=category: self.showEventImg(num))  # Pass the event number

            self.eventsLayout.addWidget(button, row + 1, col)

            col += 1
            if col >= 3:  # Display 3 columns, then move to the next row
                col = 0
                row += 2

    def showImg(self, image_path, row, col):
        image_size = QtCore.QSize(300, 300)

        image_label = QtWidgets.QLabel(self.centralwidget)
        pixmap = QtGui.QPixmap(image_path)
        pixmap = pixmap.scaled(image_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignCenter)  # Center the image
        image_label.setStyleSheet("background-color: rgba(173, 216, 230, 100);")  # Transparent light blue

        self.eventsLayout.addWidget(image_label, row, col)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Second Window"))

    def clearGridLayout(self):
        for i in reversed(range(self.eventsLayout.count())):
            item = self.eventsLayout.itemAt(i)
            if isinstance(item.widget(), QtWidgets.QWidget):
                item.widget().deleteLater()

    def showEventImg(self, category):
        self.clearGridLayout()

        # Reopen the CSV file
        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)  # Skip header row

            image = []
            for row in self.csvreader:
                if int(row[1]) == category:
                    if not any(d['sub category'] == int(row[2]) for d in image):
                        image.append({'image_path': row[0], 'sub category': int(row[2]), 'final grade': int(row[11])})
                    else:
                        for i in image:
                            if i['sub category'] == int(row[2]):
                                if i['final grade'] < int(row[12]):
                                    i['final grade'] = int(row[12])
                                    i['image_path'] = row[0]

            self.show_image_event(image)



