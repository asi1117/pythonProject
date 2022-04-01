import sys
import datetime
import time

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QSplashScreen,
    QToolButton,
    QToolTip,
    QWidget,
    QMessageBox,
    QAction,
    QFileDialog,
)
from PyQt5.QtWidgets import (
    QTableWidget,
    QProgressBar,
    QLineEdit,
    QComboBox,
    QFrame,
    QTableWidgetItem,
    QStatusBar,
)
from PyQt5.QtGui import (
    QIntValidator,
    QDoubleValidator,
    QPixmap,
    QRegExpValidator,
    QColor,
    QBrush,
    QIcon,
)
from PyQt5.QtCore import QRegExp, QThread, QSize
from PyQt5.QtCore import QDate, QDateTime, QTime, QDir

from win32com import client as wc
import docx
import Ui_open_word as open_word


class call_open_word(QWidget, open_word.Ui_Open_word):
    def __init__(self, parent=None):
        super().__init__()
        self.child = open_word.Ui_Open_word()
        self.child.setupUi(self)

    def open_word(self):
        word = wc.Dispatch('Word.Application')
        word.visible = 0

        my_file_path = QFileDialog.getOpenFileName(self, u'打开文件', '/')
        print(my_file_path)
        if my_file_path[0][-4:] == '.doc' or my_file_path[0][-5:] == '.docx':
            my_worddoc = word.Documents.Open(my_file_path[0].replace('/', '\\'))
            my_count = my_worddoc.Paragraphs.Count
            for i in range(my_count):
                my_pr = my_worddoc.Paragraphs[i].Range
                # print(my_pr)
                self.child.word_content_te.append(my_pr.text)
            my_worddoc.Close()
        elif my_file_path[0][-4:] == '.txt':
            f = open(my_file_path[0])
            my_data = f.read()
            f.close()
            self.child.word_content_te.append(my_data)
        else:
            QMessageBox.information(self, u'提示', '不支持的文件格式,只支持 doc、docx、txt')

    def open_word_no_os(self):
        my_file_path = QFileDialog.getOpenFileName(self, u'打开文件', '/')
        print(my_file_path)
        if my_file_path[0][-4:] == '.doc' or my_file_path[0][-5:] == '.docx':
            doc = docx.Document(my_file_path[0].replace(u'/', u'\\'))
            for my_paragraph in doc.paragraphs:
                my_pr = my_paragraph.text
                # print(my_pr)
                self.child.word_content_te.append(my_pr)
        elif my_file_path[0][-4:] == '.txt':
            f = open(my_file_path[0])
            my_data = f.read()
            f.close()
            self.child.word_content_te.append(my_data)
        else:
            QMessageBox.information(self, u'提示', '不支持的文件格式,只支持 doc、docx、txt')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = call_open_word()
    myWin.show()

    sys.exit(app.exec_())