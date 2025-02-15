# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbconnect.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 190, 391, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonCreateDb = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonCreateDb.setObjectName("pushButtonCreateDb")
        self.horizontalLayout_2.addWidget(self.pushButtonCreateDb)
        self.pushButtonDbcon = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonDbcon.setObjectName("pushButtonDbcon")
        self.horizontalLayout_2.addWidget(self.pushButtonDbcon)
        self.labelResult = QtWidgets.QLabel(Form)
        self.labelResult.setGeometry(QtCore.QRect(10, 260, 381, 21))
        self.labelResult.setObjectName("labelResult")

        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def create_database(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=""
                )
            cursor = mydb.cursor()
            dbname = self.lineEdit.text()
            cursor.execute("CREATE DATABASE {}".format(dbname))
            self.labelResult.setText("Database {} created ".format(dbname))
        except mc.Error as e:
            self.labelResult.setText("Database creation failed")
            
    def db_connect(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjulan2"
                )
            self.labelResult.setText("There is Connection")
        except mc.Error as err:
            self.labelResult.setText("Error In Connection")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CREATE DATABASE"))
        self.pushButtonCreateDb.setText(_translate("Form", "DATABASE CREATION"))
        self.pushButtonDbcon.setText(_translate("Form", "DATABASE CONNECTION"))
        self.labelResult.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
