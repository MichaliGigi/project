import csv
import os
import shutil
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from manager.FinalGrade import FinalGrade
from manager.Image_information import Image_information


class Ui_SecondWindow(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path

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
        self.text_1.setObjectName("label_4")

        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(110, 170, 521, 21))
        self.text_2.setStyleSheet("color: rgb(24,0,139); font-size: 20px")
        self.text_2.setText(" it is recommended to use the default for best results.")
        self.text_2.setObjectName("label_3")

        self.buttonGroups = {}
        self.buttonGroupDefault = {}
        self.lines= {}

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
        gradeComponents = {"high": [], "medium": [], "low": []}  # default

        for label_text, button_group in self.buttonGroups.items():
            selected_button = button_group.checkedButton()
            if selected_button:
                gradeComponents[selected_button.text()].append(label_text)

        # Remove elements created inside selectImportanceWindow
        self.text_1.deleteLater()
        self.text_2.deleteLater()

        self.saveSelections.deleteLater()
        for button_group in self.buttonGroups.values():
            for radio_button in button_group.buttons():
                radio_button.deleteLater()
        # Remove the line elements
        for line in self.lines.values():
            line.deleteLater()

        # Clear the layout of the central widget
        self.clearLayout(self.content_layout)

        fillImagesInfo = Image_information(self.folder_path, FinalGrade(gradeComponents))
        fillImagesInfo.fill_information()

        # # Create the scroll area
        # scroll_area = QScrollArea(self.centralwidget)
        # scroll_area.setGeometry(QtCore.QRect(0, 100, self.MainWindow.width(), self.MainWindow.height() - 100))
        # scroll_area.setWidgetResizable(True)  # Allow the widget inside to resize
        # scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)  # Show vertical scrollbar
        # scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Hide horizontal scrollbar
        #
        # # Create a widget for the scroll area content
        # scroll_content_widget = QtWidgets.QWidget()
        # scroll_area.setWidget(scroll_content_widget)
        #
        # # Create a layout for the scroll content widget
        # scroll_content_layout = QVBoxLayout(scroll_content_widget)
        # scroll_content_layout.setObjectName("scroll_content_layout")
        #
        # # Add your content to the scroll content layout
        # self.gridLayoutWidget.setParent(scroll_content_widget)  # Reparent the existing gridLayoutWidget
        # scroll_content_layout.addWidget(self.gridLayoutWidget)
        #
        # # Add the scroll area to the content layout of the central widget
        # self.content_layout.addWidget(scroll_area)

        self.eventsWindow()

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def eventsWindow(self):

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
        # close the csv file
        csvfile.close()

        self.show_image(self.image_data)
        # add eventsLayout to the central widget
        self.centralwidget.setLayout(self.eventsLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)


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
            delete_button.setStyleSheet("background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")
            delete_button.clicked.connect(lambda checked, num=category: self.delete_img(num))  # Pass the event number
            button_layout.addWidget(delete_button)  # Add the delete button to the layout

            change_button = QtWidgets.QPushButton(f"Change", self.centralwidget)
            change_button.setMouseTracking(True)
            change_button.setStyleSheet("background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")
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
        self.eventsLayout.addWidget(button, row+2, 0)

        # # After adding all the image widgets and button layouts, create the "Save" button widget
        # button = QtWidgets.QPushButton("Save", self.centralwidget)
        # button.setMouseTracking(True)
        # button.setStyleSheet("background-color: rgb(24,0,139); color: white; border-radius: 10px;   font-size: 20px;")
        # button.clicked.connect(self.save)  # Connect the button to a function
        #
        # # Add the "Save" button to the layout
        # self.eventsLayout.addWidget(button, row + 5, 0)  # Place it below the last event row

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
        # clear the grid layout
        self.clearGridLayout()
        # show the images again
        self.show_image(self.image_data)

    def close(self):
        # close the application
        sys.exit()

    def delete_img(self, num):
        # Delete the image from self.selected_image
        self.selected_image = [data for data in self.selected_image if data['sub category'] != num]

        # Clear the grid layout
        self.clearGridLayout()

        # Update the grid layout with the remaining images
        self.show_image_event()

    def change_img(self, num, sub):
        # Clear the grid layout
        self.clearGridLayout()
        # get all the images the in same category and the same sub category from the csv file
        image_data = []
        with open(self.csv_file_path, 'r') as csvfile:
            self.csvreader = csv.reader(csvfile)
            next(self.csvreader)
            for row in self.csvreader:
                if int(row[1]) == num and int(row[2]) == sub:
                    print(row[0])
                    image_data.append({'image_path': row[0], 'category': int(row[1]), 'sub category': int(row[2])})
        csvfile.close()
        self.change_selected_img(num, image_data)

    def change_selected_img(self, num, image_data):
        # Create and arrange widgets in the gridLayoutWidget
        row = 0
        col = 0
        for data in image_data:
            image_path = data['image_path']
            category = data['category']
            sub_category = data['sub category']
            radio_button = QtWidgets.QRadioButton("", self.centralwidget)
            radio_button.clicked.connect(
                lambda checked, path=image_path, cat=category, sub=sub_category: self.select(path, cat, sub))

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
        save_button = QtWidgets.QPushButton("Save Change", self.centralwidget)
        save_button.setMouseTracking(True)
        save_button.setStyleSheet(
            "background-color: rgb(24,0,139); color: white; border-radius: 10px;   font-size: 20px;")

        save_button.clicked.connect(lambda checked, cat=category: self.submit_button_clicked(cat))  # Connect the button to a function

        # Add the button to the layout
        self.eventsLayout.addWidget(save_button, row, col)

    def submit_button_clicked(self, category):
        self.clearGridLayout()

        self.show_image_event()

    def select(self, path, cat, sub):
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
            event_button = QtWidgets.QPushButton(f"Event {category}", self.centralwidget)
            event_button.setMouseTracking(True)
            event_button.setStyleSheet(
                "background-color: rgb(205,0,142); color: white; border-radius: 10px; font-size: 20px;")

            event_button.clicked.connect(lambda checked, num=category: self.showEventImg(num))  # Pass the event number

            self.eventsLayout.addWidget(event_button, row + 1, col)

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

    def showEventImg(self, category):
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
                             'final grade': int(row[11])})
                    else:
                        for i in self.selected_image:
                            if i['sub category'] == int(row[2]):
                                if i['final grade'] < int(row[11]):
                                    i['final grade'] = int(row[11])
                                    i['image_path'] = row[0]

            self.show_image_event()
            # Close the CSV file
            csvfile.close()
