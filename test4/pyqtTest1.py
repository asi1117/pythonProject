import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__=='__main__':
    #创建Qapplication类的实列
    app =QApplication(sys.argv)
    #创建窗口
    w=QWidget()
    #设置窗口的尺寸
    w.resize(300,150)
    #移动窗口
    w.move(300,300)
    #设置窗口的标题
    w.setWindowTitle('第一个基于Pyqt5的桌面应用')
    #显示窗口
    w.show()
    #进入程序的主循环，并用exit函数确保主循环安全的结束
    sys.exit(app.exec_())