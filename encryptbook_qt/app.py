import os
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import configparser

Config = configparser.ConfigParser()
Config.read("../data/config.ini")

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'EncryptBook'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.createMenuBar()
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        #entityList = self.QListWidget()

        entityList = QWidget.QListWidget

        addEntitiesToList(entityList)

        entityList.addItems(entityList)

        self.show()
    
    #def createMenuBar(self):
    #    self.myMenubar = self.menuBar()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def addEntitiesToList(iList):
    lists = []
    with open("../data/entities.json", "r") as jsonFile:
        data = json.load(jsonFile)
        for doc in data['entities']:
            first = doc['first']
            middle = doc['middle']
            last = doc['last']
            if Config.get('SETTINGS', 'order_by') == 'last':
                lists.append(last + ", " + first + " " + middle)
            elif Config.get('SETTINGS', 'order_by') == 'first':
                lists.append(first + ' ' + middle + ' ' + last)
            else:
                lists.append(last + "," + first + " " + middle)
    
    if Config.get('SETTINGS', 'alphabetically_sort') == 'ascending':
        lists.sort(reverse=False)
    elif Config.get('SETTINGS', 'alphabetically_sort') == 'descending':
        lists.sort(reverse=True)
    else:
        lists.sort(reverse=False)
    
    objList = []
    for name in lists:
        objList.append(QListWidgetItem(name))
    
    return objList