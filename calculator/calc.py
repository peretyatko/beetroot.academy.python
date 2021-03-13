# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 434)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777211))
        MainWindow.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(20, 10, 431, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_result.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(20, 350, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(239, 350, 211, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(20, 280, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(130, 280, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(240, 280, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(20, 210, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(130, 210, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(240, 210, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(20, 140, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(130, 140, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(240, 140, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(350, 280, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(350, 210, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(350, 70, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(350, 140, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_mult.setObjectName("btn_mult")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(20, 70, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_del.setObjectName("btn_del")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(130, 350, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_positive = QtWidgets.QPushButton(self.centralwidget)
        self.btn_positive.setGeometry(QtCore.QRect(130, 70, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_positive.setFont(font)
        self.btn_positive.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_positive.setObjectName("btn_positive")
        self.btn_procent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_procent.setGeometry(QtCore.QRect(240, 70, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_procent.setFont(font)
        self.btn_procent.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_procent.setObjectName("btn_procent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PCalculator"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_mult.setText(_translate("MainWindow", "X"))
        self.btn_del.setText(_translate("MainWindow", "C"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_positive.setText(_translate("MainWindow", "+/-"))
        self.btn_procent.setText(_translate("MainWindow", "%"))
