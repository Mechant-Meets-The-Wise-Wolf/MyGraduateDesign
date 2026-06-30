from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import  QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
from qfluentwidgets import InfoBar,InfoBarPosition
from UI_Login import Ui_LoginFace
from SQLiteClass import SQLite
from datetime import datetime
class LoginFace(QtWidgets.QWidget,Ui_LoginFace):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.mydb=SQLite()
        self.initui()
        self.initSignals()
      
    def initSignals(self):
        self.ToolButton.clicked.connect(self.close)
        self.ToolButton_2.clicked.connect(self.showMinimized)
        self.PrimaryPushButton_2.clicked.connect(self.login)
        self.PrimaryPushButton.clicked.connect(self.register)
          
    def login(self):

        self.mydb.connect()
        result=self.mydb.userlogin(self.LineEdit_4.text(),self.LineEdit_5.text())
    
        if result:
            # 记录登录日志
            updata_field={"lastlogin_time":datetime.now()}
            condition={"account_name":self.LineEdit_4.text()}
            self.mydb.update("usertable",updata_field,condition)
            # 登录成功，设置信号标签
            self.InforBar("登录", "登录成功！", True)
            timer = QTimer()
            timer.singleShot(1000,lambda: self.isloginlabel.setText("1"))
            
        else:
            self.InforBar("登录", "用户名或密码错误！", False)
        self.mydb.close()
           
    def register(self):
        if self.islegal():
            self.mydb.connect()
            field={"account_name":self.LineEdit.text(),
                   "pass_word":self.LineEdit_2.text(),
                   "create_time":datetime.now()}
            self.mydb.insert("usertable",field)
            self.mydb.close()
            self.InforBar("注册", "注册成功！现在可以登录了！", True)

    def islegal(self):
        username=self.LineEdit.text()
        password=self.LineEdit_2.text()
        confpassword=self.LineEdit_3.text()
        if username == "" or len(username) >= 10:
            self.InforBar("注册", "注册失败！请检查用户名是否为空或长度大于10。", False)
            return False
        elif password != confpassword or password == "":
            self.InforBar("注册", "注册失败！密码为空或两次输入的密码不一致。。", False)
            return False

        # 如果数据库中存在与输入的账户名相同的记录，则返回 True，否则返回 False
        self.mydb.connect()
        result=self.mydb.usercheck(username)
        if result:
            self.InforBar("注册", "注册失败！用户名已存在！", False)
            return False
        self.mydb.close()
        return True
     
    def UserCheck(self) :
        
        self.mydb.connect()
        field=["account_name","create_time"]
        result=self.mydb.select("usertable",field)
        self.mydb.close()
        for i, row in enumerate(result):
            for j in range(2):
                self.TableWidget.setItem(i, j, QTableWidgetItem(row[j]))
        self.InforBar("账户库", "账户库加载成功！", True)
        return True

    def initui(self):
        self.setWindowIcon(QIcon('d:\\GraduationDesign\\新的ui设计-二维图工程\\../images/圆形图标spice.png'))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 无边框窗口
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.old_pos = None  # 存储窗口的初始位置
        self.Pivot.addItem(
            routeKey='Login',
            text='登录',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page)
        )
        self.Pivot.addItem(
            routeKey='Register',
            text='注册',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_2)
        )
        self.Pivot.addItem(
            routeKey='Cheak',
            text='账户库',
            onClick=self.setusercheackface
        )
        self.Pivot.setCurrentItem('Login')
        self.stackedWidget.setCurrentWidget(self.page)
    
    def setusercheackface(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.UserCheck()

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.old_pos = event.globalPos()  # 记录鼠标按下时的全局位置

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.old_pos:
            delta = event.globalPos() - self.old_pos  # 计算鼠标移动的距离
            self.move(self.pos() + delta)  # 移动窗口到新的位置
            self.old_pos = event.globalPos()  # 更新鼠标位置

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None  # 释放鼠标按钮时清空位置信息
    
    def InforBar(self,title,content,issuccess):
          if issuccess:
            InfoBar.success(
                title=title,
                content=content,
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
                )
          else:
            InfoBar.error(
                title=title,
                content=content,
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
                )