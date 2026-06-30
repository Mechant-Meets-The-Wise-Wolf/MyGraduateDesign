import sys
from MainWindow import *
from Login import LoginFace


def begin():  
    w= MostMainWindow()
    w.show()

if __name__ == '__main__':
#enable dpi scale
    app = QApplication(sys.argv)
    
    l=LoginFace()
    l.show()
    l.isloginlabel.textChanged.connect(begin)
    l.isloginlabel.textChanged.connect(l.close)

    app.exec_()
