from GUI.Ui_MainWindow import Ui_MainWindow
from Libraries import *
class Controller():
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    c = Controller()
    c.run()

