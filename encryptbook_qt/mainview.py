# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryptbook-mainview-1'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidgetEntities = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetEntities.setGeometry(QtCore.QRect(10, 20, 256, 531))
        self.listWidgetEntities.setObjectName("listWidgetEntities")
        self.listViewDetailedView = QtWidgets.QListView(self.centralwidget)
        self.listViewDetailedView.setGeometry(QtCore.QRect(300, 20, 481, 531))
        self.listViewDetailedView.setObjectName("listViewDetailedView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_New_Contact = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Contact.setObjectName("actionAdd_New_Contact")
        self.actionRemove_Contact = QtWidgets.QAction(MainWindow)
        self.actionRemove_Contact.setObjectName("actionRemove_Contact")
        self.actionEdit_Contact = QtWidgets.QAction(MainWindow)
        self.actionEdit_Contact.setObjectName("actionEdit_Contact")
        self.menufile.addAction(self.actionSettings)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionQuit)
        self.menuhelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionAdd_New_Contact)
        self.menuEdit.addAction(self.actionRemove_Contact)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEdit_Contact)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EncrptBook"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAdd_New_Contact.setText(_translate("MainWindow", "Add New Contact"))
        self.actionRemove_Contact.setText(_translate("MainWindow", "Remove Contact"))
        self.actionEdit_Contact.setText(_translate("MainWindow", "Edit Contact"))
