from GUI.Ui_MainWindow import Ui_MainWindow
from Libraries import *
class Controller():
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    c = Controller()
    c.run()


