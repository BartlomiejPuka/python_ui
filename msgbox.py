import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class MsgBox(QtWidgets.QWidget):
    def __init__(self, prompt="prompt", title="title"):
        """
        param::prompt describes what u want
        param:: title
        """
        super().__init__()
        self.title = title
        self.left = 50
        self.top = 50
        self.width = 280
        self.height = 120
        self.prompt = prompt

        
        self.__initUI()


    def __initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel("promptaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", self)
        
        self.label.adjustSize()

        self.inputLine = QLineEdit(self)
        self.inputLine.setFixedHeight(25)

        self.okButton = QPushButton("Ok",self)
        self.cancelButton = QPushButton("Cancel",self)
        self.showButton = QPushButton("Show",self)

        self.labelBox = QHBoxLayout()
        self.labelBox.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBox.addWidget(self.label)

        self.inputLineBox = QHBoxLayout()
        self.labelBox.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLineBox.addWidget(self.inputLine)



        self.buttonsBox = QHBoxLayout()
        self.buttonsBox.addWidget(self.okButton)
        self.buttonsBox.addStretch(1)
        self.buttonsBox.addWidget(self.showButton)
        self.buttonsBox.addStretch(2)
        self.buttonsBox.addWidget(self.cancelButton)


        self.vbox = QVBoxLayout(self)
        self.vbox.addLayout(self.labelBox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.inputLineBox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.buttonsBox)
        
        self.setLayout(self.vbox)


        self.setFixedSize(self.size())
        self.__center()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    @staticmethod
    def get_password(prompt="Info", title="Window"):
        app = QtWidgets.QApplication(sys.argv)
        msgbox = MsgBox(prompt,title)
        app.exec_()

    def __center(self):
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


