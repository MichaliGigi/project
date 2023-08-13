import csv
import os
import shutil
import sys

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
        self.image_data = []
        # Get the path of the current script file
        script_path = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the CSV file using os.path.join
        self.csv_file_path = os.path.join(script_path, '..', 'manager', 'images_info.csv')

        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)  # Skip header row
            for row in self.csvreader:
                # check in image_data that the category number is not already present
                if not any(d['category'] == int(row[1]) for d in self.image_data):
                    self.image_data.append({'image_path': row[0], 'category': int(row[1])})
        #close the csv file
        csvfile.close()

        self.show_image( self.image_data)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def show_image_event(self):
        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0
        for data in self.selected_image:
            image_path = data['image_path']
            category = data['category']
            sub_category = data['sub category']

            self.showImg(image_path, row, col)
            button_layout = QtWidgets.QHBoxLayout()  # Create a horizontal layout for buttons

            delete_button = QtWidgets.QPushButton(f"Delete", self.centralwidget)
            delete_button.clicked.connect(lambda checked, num=category: self.delete_img(num))  # Pass the event number
            button_layout.addWidget(delete_button)  # Add the delete button to the layout

            change_button = QtWidgets.QPushButton(f"Change", self.centralwidget)
            change_button.clicked.connect(lambda checked, num=category,sub=sub_category: self.change_img(num,sub))  # Pass the event number
            button_layout.addWidget(change_button)  # Add the change button to the layout

            self.eventsLayout.addLayout(button_layout, row + 1, col)  # Add the button layout to the grid layout

            col += 1
            if col >= 3:  # Display 3 columns, then move to the next row
                col = 0
                row += 2
        # After adding all the image widgets, create a button widget
        button = QtWidgets.QPushButton("Save", self.centralwidget)
        button.clicked.connect(self.save)  # Connect the button to a function

        # Add the button to the layout
        self.eventsLayout.addWidget(button, row, col)
    def save(self):

        # get the folder path where the images are stored
        folder_path = os.path.dirname(self.selected_image[0]['image_path'])
        # Save the selected images to in new folder called selected_images in the folder_path
        selected_images_folder = os.path.join(folder_path, 'selected_images')
        if not os.path.exists(selected_images_folder):
            os.makedirs(selected_images_folder)
        for data in self.selected_image:
            image_path = data['image_path']
            # get the image name
            image_name = os.path.basename(image_path)
            # get the new path of the image
            new_image_path = os.path.join(selected_images_folder, image_name)
            # copy the image to the new path
            shutil.copy(image_path, new_image_path)
        # Assuming the following snippet is within your class where you have the centralwidget and eventsLayout:

        # clear the grid layout
        self.clearGridLayout()

        # Create QLabel for the message
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 150, 801, 491))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("saveMsg.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        # Create QPushButton for going back
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet(
            "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("go back to choose another event")
        self.pushButton.clicked.connect(self.go_back)

        # Create QPushButton for closing
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(24,0,139); color: white; border-radius: 10px; font-size: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("close")
        self.pushButton_2.clicked.connect(self.close)

        # Add widgets to the eventsLayout
        self.eventsLayout.addWidget(self.label_2, 0, 0)  # Add message label at row 0, column 0
        self.eventsLayout.addWidget(self.pushButton, 1, 0)  # Add first button at row 1, column 0
        self.eventsLayout.addWidget(self.pushButton_2, 2, 0)  # Add second button at row 2, column 0

    def go_back(self):
        #clear the grid layout
        self.clearGridLayout()
        #show the images again
        self.show_image(self.image_data)
    def close(self):
        #close the application
        sys.exit()



    def delete_img(self, num):
        # Delete the image from self.selected_image
        self.selected_image = [data for data in self.selected_image if data['sub category'] != num]

        # Clear the grid layout
        self.clearGridLayout()

        # Update the grid layout with the remaining images
        self.show_image_event()

    def change_img(self, num,sub):
        # Clear the grid layout
        self.clearGridLayout()
        # get all the images the in same category and the same sub category from the csv file
        image_data = []
        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)
            for row in self.csvreader:
                if int(row[1]) == num and int(row[2]) == sub:
                    image_data.append({'image_path': row[0], 'category': int(row[1]), 'sub category': int(row[2])})
        csvfile.close()
        self.change_selected_img(num,image_data)
    def change_selected_img(self,num,image_data):
        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0
        for data in image_data:
            image_path = data['image_path']
            category = data['category']
            sub_category = data['sub category']
            radio_button = QtWidgets.QRadioButton("", self.centralwidget)
            radio_button.clicked.connect(lambda checked, path=image_path,cat=category,sub=sub_category: self.select(path,cat,sub))

            image_label = self.showImg(image_path, row, col)  # Call your showImg function and get the image label
            # Create a vertical layout for the cell
            cell_layout = QtWidgets.QVBoxLayout()

            # Align the radio button to the top-left corner
            radio_layout = QtWidgets.QHBoxLayout()
            radio_layout.addWidget(radio_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

            # Add the radio layout and image label to the cell layout
            cell_layout.addLayout(radio_layout)
            cell_layout.addWidget(image_label)

            # Add the cell layout to the grid layout
            self.eventsLayout.addLayout(cell_layout, row, col)

            col += 1
            if col >= 3:  # Display 3 columns, then move to the next row
                col = 0
                row += 2
        # After adding all the image widgets, create a button widget
        button = QtWidgets.QPushButton("Save Change", self.centralwidget)
        button.clicked.connect(lambda checked,  cat=category:self.submit_button_clicked(cat))  # Connect the button to a function

        # Add the button to the layout
        self.eventsLayout.addWidget(button, row, col)

    def submit_button_clicked(self,category):
        self.clearGridLayout()

        self.show_image_event()


    def select(self,path,cat,sub):
        # replace the image in self.selected_image that have the same category and sub category with the new image
        for data in self.selected_image:
            if data['category'] == cat and data['sub category'] == sub:
                data['image_path'] = path
                break




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
            elif isinstance(item.layout(), QtWidgets.QLayout):
                sublayout = item.layout()
                for j in reversed(range(sublayout.count())):
                    subitem = sublayout.itemAt(j)
                    if isinstance(subitem.widget(), QtWidgets.QWidget):
                        subitem.widget().deleteLater()
                    elif isinstance(subitem.layout(), QtWidgets.QLayout):
                        subsublayout = subitem.layout()
                        for k in reversed(range(subsublayout.count())):
                            subsubitem = subsublayout.itemAt(k)
                            if isinstance(subsubitem.widget(), QtWidgets.QWidget):
                                subsubitem.widget().deleteLater()

    def showEventImg(self, category):
        self.clearGridLayout()

        # Reopen the CSV file
        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)  # Skip header row

            self.selected_image = []
            for row in self.csvreader:
                if int(row[1]) == category:
                    if not any(d['sub category'] == int(row[2]) for d in self.selected_image):
                        self.selected_image.append({'image_path': row[0],'category':int(row[1]), 'sub category': int(row[2]), 'final grade': int(row[11])})
                    else:
                        for i in self.selected_image:
                            if i['sub category'] == int(row[2]):
                                if i['final grade'] < int(row[11]):
                                    i['final grade'] = int(row[11])
                                    i['image_path'] = row[0]

            self.show_image_event()
            # Close the CSV file
            csvfile.close()



