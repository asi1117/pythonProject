import  sys
import MainWinHorizontalLayout
from  PyQt5.QtWidgets import QApplication,QMainWindow
if __name__=='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=MainWinHorizontalLayout.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())