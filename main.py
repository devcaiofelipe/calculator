import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        style_btn = 'background: rgb(96, 150, 251); color: #fff; font-size: 15pt; border-radius: 5px'
        style_operators = 'background: rgb(108, 94, 247); color: #fff; font-size: 15pt; border-radius: 5px'
        style_numbers = 'background: rgb(139, 139, 139); color: rgb(0, 0, 0); font-size: 15pt; border-radius: 5px'
        style_others = 'background: rgb(250, 114, 114); color: #fff; font-size: 15pt; border-radius: 5px'

        self.setWindowTitle('Calculadora do Caio')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('background: white; color: #000; font-size: 30px;')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, style=style_operators)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''), style_btn)

        self.add_btn(QPushButton('4'), 2, 0, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, style=style_operators)
        self.add_btn(QPushButton('←'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]), style_btn)

        self.add_btn(QPushButton('1'), 3, 0, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('÷'), 3, 3, 1, 1, style=style_operators)
        self.add_btn(QPushButton(''), 3, 4, 1, 1, style=style_btn)

        self.add_btn(QPushButton(''), 4, 0, 1, 1, style=style_others)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1, style=style_numbers)
        self.add_btn(QPushButton('.'), 4, 2, 1, 1, style=style_others)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, style=style_operators)
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.eval_igual, style=style_others)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            btn.setStyleSheet(style)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
            print(self.display)
        except Exception as Error:
            self.display.setText('Conta inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()