import shutil
import os
import errno
import pipeit
import pipeui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


#version .002 adding class a base ui
#ultraMove For moving files from one place to the other and doing other fancy stuff.

pipeit.ultraShout("you")


class pipeApp(QtWidgets.QMainWindow, pipeui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(pipeApp, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnUltraMove.clicked.connect(self.ui_ultraCopy)



    def browse_folder(self):
        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget
    def ui_ultraCopy (self):
        print ("what")
        self.shutil.copy("c:\\sandbox\\source", "c:\\sandbox\\target")










def main():
    app = QtWidgets.QApplication(sys.argv)
    form = pipeApp()
    form.show()
    app.exec_()



if __name__ == "__main__":
    main()
# Directories are the same
##source = 'C:\\sandbox\\source'
#destination = 'C:\\sandbox\\target'
#ignored=""

#ultraCopy(source,destination,ignored)
