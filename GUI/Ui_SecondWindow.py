import csv
import os
import shutil
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QApplication

from manager.FinalGrade import FinalGrade
from manager.Image_information import Image_information


class Ui_SecondWindow(object):
    def __init__(self,images_path):
        self.images_path = images_path

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setEnabled(True)
        self.MainWindow.resize(1331, 820)
        self.MainWindow.setMinimumSize(QtCore.QSize(1331, 820))
        self.MainWindow.setMaximumSize(QtCore.QSize(1331, 820))

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")

        # Add your widgets and layouts to centralwidget
        self.addBackground()

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 140, 1231, 671))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.eventsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.eventsLayout.setContentsMargins(0, 0, 0, 0)
        self.eventsLayout.setObjectName("eventsLayout")

        self.eventsLayout.setColumnStretch(0, 1)
        self.eventsLayout.setColumnStretch(1, 1)
        self.eventsLayout.setColumnStretch(2, 1)

        self.selectImportanceWindow()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def addBackground(self):
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

    def selectImportanceWindow(self):
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(110, 120, 971, 41))
        self.text_1.setStyleSheet("color: rgb(24,0,139); font-size: 30px")
        self.text_1.setText("Choose the level of importance of each quality check:")
        self.text_1.setObjectName("text_1")

        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(110, 170, 521, 21))
        self.text_2.setStyleSheet("color: rgb(24,0,139); font-size: 20px")
        self.text_2.setText(" it is recommended to use the default for best results.")
        self.text_2.setObjectName("text_2")

        self.buttonGroups = {}
        self.buttonGroupDefault = {}
        self.lines = {}

        self.content_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.content_layout.setObjectName("content_layout")
        self.centralwidget.setLayout(self.content_layout)

        # Set stretch factors for layout adjustment
        self.content_layout.setStretch(0, 1)  # Spacer stretch factor
        self.content_layout.setStretch(1, 0)  # content_layout stretch factor

        self.gridLayout = QtWidgets.QGridLayout()
        self.content_layout.addLayout(self.gridLayout)
        self.content_layout.setContentsMargins(110, 0, 110, 0)
        self.centralwidget.setLayout(self.content_layout)

        self.saveSelections = QtWidgets.QPushButton(self.centralwidget)
        self.saveSelections.setGeometry(QtCore.QRect(1090, 740, 200, 41))
        self.saveSelections.setStyleSheet(
            "background-color: rgb(24,0,139); color: white; border-radius: 10px;   font-size: 20px")
        self.saveSelections.setObjectName("saveSelectionsButton")
        self.saveSelections.setText("Save and Continue")
        self.saveSelections.clicked.connect(self.saveImportanceSelections)

        # Create radio rows from file
        self.createRadioRowsFromFile()
        self.MainWindow.setCentralWidget(self.centralwidget)

    # ======================================================================================
    def createRadioRow(self, label_text, radio_buttons, default_selection, y_position):
        line = QtWidgets.QLabel(self.centralwidget)
        line.setStyleSheet("font-size: 20px;color: rgb(24,0,139);")
        line.setObjectName(f"label_{label_text}")
        line.setText(label_text)
        # save the line object in the linesGroup dictionary
        self.lines[label_text] = line

        self.buttonGroups[label_text] = QtWidgets.QButtonGroup(self.centralwidget)
        self.gridLayout.addWidget(line, y_position, 0, 1, 1)
        x_position = 1
        for radio_button in radio_buttons:
            radio_button.setStyleSheet("font-size: 15px;")
            self.buttonGroups[label_text].addButton(radio_button)
            # Set default selection
            if radio_button.text() == default_selection:
                radio_button.setChecked(True)
            self.gridLayout.addWidget(radio_button, y_position, x_position, 1, 1)
            x_position += 1

    # ======================================================================================
    def createRadioRowsFromFile(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_path, '..', 'manager', 'components.txt')
        # Read file and create radio rows
        with open(file_path, 'r') as file:
            lines = file.readlines()

        y_position = 0  # Starting Y position for the first row of radio buttons

        for line in lines:
            parts = line.strip().split(', ')
            if len(parts) == 2:
                label_text = parts[1]
                default_selection = parts[0]

                radio_buttons = [
                    QtWidgets.QRadioButton("low"),
                    QtWidgets.QRadioButton("medium"),
                    QtWidgets.QRadioButton("high")
                ]

                self.createRadioRow(label_text, radio_buttons, default_selection, y_position)
                y_position += 2

    def saveImportanceSelections(self):
        # block the save button
        self.saveSelections.setDisabled(True)
        # set the text of the button to "loading..."
        self.saveSelections.setText("loading...")



        # Remove elements created inside selectImportanceWindow
        self.text_1.deleteLater()
        self.text_2.deleteLater()

        for button_group in self.buttonGroups.values():
            for radio_button in button_group.buttons():
                radio_button.deleteLater()
        # Remove the line elements
        for line in self.lines.values():
            line.deleteLater()
        self.saveSelections.deleteLater()

        # Clear the layout of the central widget
        self.clearLayout(self.content_layout)

        self.MainWindow.setCentralWidget(self.centralwidget)

        #QApplication.processEvents()
        self.fillInformation()

    def fillInformation(self):
        gradeComponents = {"high": [], "medium": [], "low": []}  # default

        for label_text, button_group in self.buttonGroups.items():
            selected_button = button_group.checkedButton()
            if selected_button:
                gradeComponents[selected_button.text()].append(label_text)
        fillImagesInfo = Image_information(self.images_path, FinalGrade(gradeComponents))
        fillImagesInfo.fill_information()
        self.current_image_index = 0

        self.eventsWindow()

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def eventsWindow(self):

        # read the csv file and extract one image path from each category
        self.read_paths_from_file()

        # show one image from each category
        self.show_event_images(self.image_data)
        # add eventsLayout to the central widget
        self.centralwidget.setLayout(self.eventsLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)

    def read_paths_from_file(self):
        # Read the CSV file and extract the image paths
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
        # close the csv file
        csvfile.close()

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
            delete_button.setMouseTracking(True)
            delete_button.setStyleSheet(
                "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")
            delete_button.clicked.connect(lambda checked, img_data=data: self.delete_img(img_data))  # Pass the event number
            button_layout.addWidget(delete_button)  # Add the delete button to the layout

            change_button = QtWidgets.QPushButton(f"Change", self.centralwidget)
            change_button.setMouseTracking(True)
            change_button.setStyleSheet(
                "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")
            change_button.clicked.connect(
                lambda checked, num=category, sub=sub_category: self.change_img(num, sub))  # Pass the event number
            button_layout.addWidget(change_button)  # Add the change button to the layout

            self.eventsLayout.addLayout(button_layout, row + 1, col)  # Add the button layout to the grid layout

            col += 1
            if col >= 3:  # Display 3 columns, then move to the next row
                col = 0
                row += 2
        # After adding all the image widgets, create a button widget
        button = QtWidgets.QPushButton("Save", self.centralwidget)
        button.setMouseTracking(True)
        button.setStyleSheet("background-color: rgb(24,0,139); color: white; border-radius: 10px;   font-size: 20px;")
        button.clicked.connect(self.save)  # Connect the button to a function

        # Add the button to the layout
        self.eventsLayout.addWidget(button, row + 2, 0)

    def load_previous_images(self):
        if self.current_image_index > 5:
            self.clearGridLayout()
            self.current_image_index -= 6
            self.change_selected_img()

    def load_next_images(self):
        if self.current_image_index <= len(self.sub_category_images) - 6:
            self.clearGridLayout()
            self.current_image_index += 6
            self.change_selected_img()

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

        # clear the grid layout
        self.clearGridLayout()

        # Create QLabel for the message
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 150, 801, 491))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("saveMsg.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        # Create QPushButton for going back
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet(
            "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px; width: 100;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("go back to choose another event")
        self.pushButton.clicked.connect(self.go_back)

        # Create QPushButton for closing
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(24,0,139); color: white; border-radius: 10px; font-size: 20px; width: 100;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("close")
        self.pushButton_2.clicked.connect(self.close)

        # Add widgets to the eventsLayout
        self.eventsLayout.addWidget(self.label_2, 0, 0)  # Add message label at row 0, column 0
        self.eventsLayout.addWidget(self.pushButton, 1, 0)  # Add first button at row 1, column 0
        self.eventsLayout.addWidget(self.pushButton_2, 2,0)  # Add second button at row 2, column 0

    def go_back(self):
        # clear the grid layout
        self.clearGridLayout()
        # show the images again
        self.show_event_images(self.image_data)

    def close(self):
        # close the application
        sys.exit()

    def delete_img(self, img_data):
        # Delete the image from self.selected_image
        self.selected_image = [data for data in self.selected_image if data != img_data]
        # Check if there are images left in self.selected_image that in the same  category
        if not any(d['category'] == img_data['category']  for d in self.selected_image):

            self.go_back()
        else:
            # Clear the grid layout
            self.clearGridLayout()
            # Update the grid layout with the remaining images
            self.show_image_event()

    def change_img(self, num, sub):
        # Clear the grid layout
        self.clearGridLayout()
        # get all the images the in same category and the same sub category from the csv file
        self.sub_category_images = []
        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)
            for row in self.csvreader:
                if int(row[1]) == num and int(row[2]) == sub:
                    print(row[0])
                    self.sub_category_images.append(
                        {'image_path': row[0], 'category': int(row[1]), 'sub category': int(row[2])})
        csvfile.close()
        self.change_selected_img()

    def change_selected_img(self):
        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0
        # # clear the grid layout
        # self.clearGridLayout()  #######

        # show six images in the grid layout
        # Load and display images
        images_to_display = self.sub_category_images[self.current_image_index:self.current_image_index + 6]

        for data in images_to_display:
            image_path = data['image_path']
            category = data['category']
            sub_category = data['sub category']
            radio_button = QtWidgets.QRadioButton("", self.centralwidget)
            # check if date is already in self.selected_image
            if any(d['image_path'] == image_path for d in self.selected_image):
                # set the radio button to checked
                radio_button.setChecked(True)
            radio_button.clicked.connect(
                lambda checked, path=image_path, cat=category, sub=sub_category: self.select(path, cat, sub))
            # check if the image is already selected

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
        # Create a layout for the buttons
        button_layout2 = QtWidgets.QHBoxLayout()
        # if self.current_image_index >= 6:
        previous_button = QtWidgets.QPushButton("Previous", self.centralwidget)
        previous_button.setStyleSheet(
            "background-color: rgb(0, 128, 0); color: white; border-radius: 5px; font-size: 20px;")
        previous_button.clicked.connect(self.load_previous_images)
        button_layout2.addWidget(previous_button)

        # Create "Next" button
        # if self.current_image_index + 6 < len(self.selected_image):
        next_button = QtWidgets.QPushButton("Next", self.centralwidget)
        next_button.setStyleSheet(
            "background-color: rgb(0, 128, 0); color: white; border-radius: 5px; font-size: 20px;")
        next_button.clicked.connect(self.load_next_images)
        button_layout2.addWidget(next_button)

        # After adding all the image widgets, create a button widget
        save_button = QtWidgets.QPushButton("Save Change", self.centralwidget)
        save_button.setMouseTracking(True)
        save_button.setStyleSheet(
            "background-color: rgb(24,0,139); color: white; border-radius: 5px;   font-size: 20px;")
        save_button.clicked.connect(
            lambda checked, cat=category: self.submit_button_clicked(cat))  # Connect the button to a function
        button_layout2.addWidget(save_button)
        # Add the button to the layout
        self.eventsLayout.addLayout(button_layout2, row + 2, 0)

    def submit_button_clicked(self, category):
        self.clearGridLayout()

        self.show_image_event()

    def select(self, path, cat, sub):
        # replace the image in self.selected_image that have the same category and sub category with the new image
        for data in self.selected_image:
            if data['category'] == cat and data['sub category'] == sub:
                data['image_path'] = path
                break

    def show_event_images(self, image_data):
        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0

        for data in image_data:
            image_path = data['image_path']
            category = data['category']

            self.showImg(image_path, row, col)
            event_button = QtWidgets.QPushButton(f"Event {category}", self.centralwidget)
            event_button.setMouseTracking(True)
            event_button.setStyleSheet(
                "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")

            event_button.clicked.connect(
                lambda checked, num=category: self.show_specific_event(num))  # Pass the event number

            self.eventsLayout.addWidget(event_button, row + 1, col)

            col += 1
            if col >= 3:  # Display 3 columns, then move to the next row
                col = 0
                row += 2

    def showImg(self, image_path, row, col):
        image_size = QtCore.QSize(300, 300)

        # Create a widget to contain the image
        image_container = QtWidgets.QWidget(self.centralwidget)
        image_container.setFixedSize(image_size)
        image_container.setStyleSheet(
            " background-color: rgba(173, 216, 230, 100);")  # Transparent light blue

        self.image_label = QtWidgets.QLabel(image_container)
        pixmap = QtGui.QPixmap(image_path)
        pixmap = pixmap.scaled(image_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)  # Center the image

        # Create a layout for the container and add the label
        container_layout = QtWidgets.QVBoxLayout(image_container)
        container_layout.addWidget(self.image_label, alignment=QtCore.Qt.AlignCenter)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        # Add the container widget to the main layout
        self.eventsLayout.addWidget(image_container, row, col)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Second Window"))

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

    def show_specific_event(self, category):
        self.clearGridLayout()
        print("category: ", category)
        # Reopen the CSV file
        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)  # Skip header row

            self.selected_image = []
            for row in self.csvreader:
                if int(row[1]) == category:
                    if not any(d['sub category'] == int(row[2]) for d in self.selected_image):
                        print(row[0])
                        self.selected_image.append(
                            {'image_path': row[0], 'category': int(row[1]), 'sub category': int(row[2]),
                             'final grade': int(row[3])})
                    else:
                        for i in self.selected_image:
                            if i['sub category'] == int(row[2]):
                                if i['final grade'] < int(row[3]):
                                    i['final grade'] = int(row[3])
                                    i['image_path'] = row[0]

            self.show_image_event()
            # Close the CSV file
            csvfile.close()
