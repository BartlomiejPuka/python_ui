import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

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
        self.width = 250
        self.height = 120
        self.prompt = prompt
        self.password = ""
        self.state = False
        self.fontHiddenMode = True

        
        self.__initUI()


    def __initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel("prompt", self)
        
        self.label.adjustSize()

        self.inputLine = QLineEdit(self)
        self.inputLine.setFixedSize(220,25)
        self.inputLine.setEchoMode(QLineEdit.Password)
        self.inputLine.setText = ""

        self.okButton = QPushButton("Ok",self)
        self.okButton.clicked.connect(self.__okClick)

        self.cancelButton = QPushButton("Cancel",self)
        self.cancelButton.clicked.connect(self.__cancelClick)

        self.showButton = QPushButton("Show",self)
        self.showButton.clicked.connect(self.__showClick)

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
        self.vbox.addStretch(2)
        self.vbox.addLayout(self.buttonsBox)
        
        self.setLayout(self.vbox)


        self.setFixedSize(self.size())
        self.__center()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.show()

    def __okClick(self):
        if self.inputLine.text() != "":
            self.password = self.inputLine.text()
            self.state = True
            self.accept()

    def __cancelClick(self):
            self.state = False
            self.reject()

    def __showClick(self):
        if not self.fontHiddenMode:
            if self.inputLine.text() != "":
                self.inputLine.setEchoMode(QLineEdit.Password)
                self.fontHiddenMode = not self.fontHiddenMode
        else:
            if self.inputLine.text() != "":
                self.inputLine.setEchoMode(QLineEdit.Normal)
                self.fontHiddenMode = not self.fontHiddenMode

    @staticmethod
    def get_password(prompt="Info", title="Window"):
        app = QtWidgets.QApplication(sys.argv)
        msgbox = MsgBox(prompt,title)
        app.exec_()
        return (msgbox.password, msgbox.state)
        
    def __center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
if __name__ == '__main__':
    
    password, state = MsgBox.get_password()
    print(password, state)


