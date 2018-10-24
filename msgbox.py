import sys
from PyQt5 import QtWidgets, QtCore

class MsgBox(QtWidgets.QDialog):
    def __init__(self, prompt="prompt", title="title"):
        """
        param::prompt describes what u want
        param:: title
        """
        super().__init__()
        self.title = title
        self.left = 50
        self.top = 50
        self.width = 400
        self.height = 140
        self.prompt = prompt

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.center()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    @staticmethod
    def get_password(prompt="Info", title="Window"):
        app = QtWidgets.QApplication(sys.argv)
        msgbox = MsgBox(prompt,title)
        app.exec_()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    msgbox = MsgBox()
    app.exec_()


