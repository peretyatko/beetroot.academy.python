from PyQt5 import QtWidgets

from calc import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.btn_zero.clicked.connect(self.digit_pressed)
        self.btn_1.clicked.connect(self.digit_pressed)
        self.btn_2.clicked.connect(self.digit_pressed)
        self.btn_3.clicked.connect(self.digit_pressed)
        self.btn_4.clicked.connect(self.digit_pressed)
        self.btn_5.clicked.connect(self.digit_pressed)
        self.btn_6.clicked.connect(self.digit_pressed)
        self.btn_7.clicked.connect(self.digit_pressed)
        self.btn_8.clicked.connect(self.digit_pressed)
        self.btn_9.clicked.connect(self.digit_pressed)

        self.btn_dot.clicked.connect(self.dot_pressed)

        self.btn_positive.clicked.connect(self.unary_operation_pressed)
        self.btn_procent.clicked.connect(self.unary_operation_pressed)

        self.btn_plus.clicked.connect(self.binary_operation_pressed)
        self.btn_minus.clicked.connect(self.binary_operation_pressed)
        self.btn_mult.clicked.connect(self.binary_operation_pressed)
        self.btn_divide.clicked.connect(self.binary_operation_pressed)

        self.btn_equal.clicked.connect(self.equals_pressed)

        self.btn_del.clicked.connect(self.clear_pressed)

        self.btn_plus.setCheckable(True)
        self.btn_minus.setCheckable(True)
        self.btn_mult.setCheckable(True)
        self.btn_divide.setCheckable(True)




    def digit_pressed(self):
        button = self.sender()

        if ((self.btn_plus.isChecked() or self.btn_minus.isChecked() or
                self.btn_mult.isChecked() or self.btn_divide.isChecked()) and (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True

        else:
            if (('.' in self.label_result.text()) and (button.text()== '0')):
                newLabel = format(float(self.label_result.text() + button.text()), '.15g')

            else:
                 newLabel = format(float(self.label_result.text() + button.text()), '.15g')

        self.label_result.setText(newLabel)

    def dot_pressed(self):
        self.label_result.setText(self.label_result.text() + '.')


    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.label_result.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else:
            labelNumber = labelNumber * 0.01

        newLable = format(labelNumber, '.15g')
        self.label_result.setText(newLable)

    def binary_operation_pressed(self):
        button = self.sender()

        self.firstNum = float(self.label_result.text())

        button.setChecked(True)


    def equals_pressed(self):
        secondNum = float(self.label_result.text())

        if self.btn_plus.isChecked():
            labeNumber = self.firstNum + secondNum
            newLabel = format(labeNumber, '.15g')
            self.label_result.setText(newLabel)
            self.btn_plus.setChecked(False)
        elif self.btn_minusisChecked():
            labeNumber = self.firstNum -  secondNum
            newLabel = format(labeNumber, '.15g')
            self.label_result.setText(newLabel)
            self.btn_minus.setChecked(False)
        elif self.btn_mult.isChecked():
            labeNumber = self.firstNum * secondNum
            newLabel = format(labeNumber, '.15g')
            self.label_result.setText(newLabel)
            self.btn_mult.setChecked(False)
        elif self.btn_divide.isChecked():
            labeNumber = self.firstNum / secondNum
            newLabel = format(labeNumber, '.15g')
            self.label_result.setText(newLabel)
            self.btn_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_pressed(self):
        self.btn_plus.setChecked(False)
        self.btn_minus.setChecked(False)
        self.btn_mult.setChecked(False)
        self.btn_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.label_result.setText('0')

