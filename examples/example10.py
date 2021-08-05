# https://es.stackoverflow.com/questions/348170/como-convertir-un-qlineedit-de-pyqt5-en-float-para-usarlos-luego-en-una-ecuacion?rq=1

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(317, 220)
        self.centralwidget = QtWidgets.QWidget(self)

        self.line_ingresar = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ingresar.setGeometry(QtCore.QRect(10, 50, 113, 32))
        self.line_ingresar.setValidator(QtGui.QDoubleValidator())

        self.label = QtWidgets.QLabel("² =", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)

        self.line_resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.line_resultado.setGeometry(QtCore.QRect(190, 50, 113, 32))
        self.line_resultado.setReadOnly(True)

        self.btn_calcular = QtWidgets.QPushButton("Calcular", self.centralwidget)
        self.btn_calcular.setGeometry(QtCore.QRect(110, 100, 88, 34))
        self.btn_calcular.clicked.connect(self.calcular)

        self.setCentralWidget(self.centralwidget)

    @QtCore.pyqtSlot() 
    def calcular(self):
        num_str = self.line_ingresar.text()
        if not num_str:
            self.line_resultado.setText("NaN")
        else:
            num = float(num_str)
            cuadrado = num ** 2
            self.line_resultado.setText(round(str(cuadrado), 2))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    app.exec_()