# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\projects\pipe\temp\qt_designer\pipeui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 150, 231, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.btnBrowse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.verticalLayout.addWidget(self.btnBrowse)
        self.projTreeView = QtWidgets.QTreeView(self.centralwidget)
        self.projTreeView.setGeometry(QtCore.QRect(20, 10, 256, 501))
        self.projTreeView.setObjectName("projTreeView")
        self.setroot = QtWidgets.QPushButton(self.centralwidget)
        self.setroot.setGeometry(QtCore.QRect(20, 520, 251, 21))
        self.setroot.setObjectName("setroot")
        self.btnUltraMove = QtWidgets.QPushButton(self.centralwidget)
        self.btnUltraMove.setGeometry(QtCore.QRect(20, 560, 251, 21))
        self.btnUltraMove.setObjectName("btnUltraMove")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBrowse.setText(_translate("MainWindow", "Pick a folder"))
        self.setroot.setText(_translate("MainWindow", "set project root"))
        self.btnUltraMove.setText(_translate("MainWindow", "ultra move"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

