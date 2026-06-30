from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import QSize,QEventLoop,QTimer
from PyQt5.QtGui import QPalette, QPixmap,QBrush
from PyQt5.QtWidgets import QApplication,QLabel

from qfluentwidgets import FluentIcon as FIF,MSFluentWindow,SplashScreen,InfoBar,InfoBarPosition,NavigationItemPosition

from UI_MainWindow import CustomMainFaceTitle

from Home import HomeFace
from Input import InputFace
from Caculation import CaculationFace
from Visualization import VisualizationFace
from DataManage import DataManageFace
import sqlite3,os

class MostMainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        #初始化窗口
        self.initwindows()
        #设置界面的跨界面按钮信号
        self.initJumpSignal()
                                  
    def initwindows(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('d:\\GraduationDesign\\新的ui设计-二维图工程\\../images/圆形图标spice.png'))
        self.setWindowIcon(icon)
        
        #窗口居中
        self.resize(1440, 880)
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w/2 - self.width()/2, h/2 - self.height()/2)

        #添加上方菜单栏
        self.setTitleBar(CustomMainFaceTitle(self))
        #创建启动页面
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))
        self.show()

        
        #添加左侧home页面
        self.HomeFace=HomeFace(self)
        self.addSubInterface(self.HomeFace,FIF.HOME,'Home')
        #添加左侧参数输入界面

        self.InputFace=InputFace(self)
        self.addSubInterface(self.InputFace,FIF.LABEL,'参数输入')
        #添加左侧计算页面
        self.CaculationFace=CaculationFace(self)
        self.addSubInterface(self.CaculationFace,FIF.DEVELOPER_TOOLS,'计算')
        #添加左侧可视化页面
        self.VisualizationFace=VisualizationFace(self)
        self.addSubInterface(self.VisualizationFace,FIF.UNIT,'可视化')
        #添加左侧数据管理页面
        self.DataManageFace=DataManageFace(self)
        self.addSubInterface(self.DataManageFace,FIF.LIBRARY,'数据管理')
        #添加底部工具栏的方法
        self.libraryInterface = QLabel(self)
        self.libraryInterface.setObjectName('libraryInterface')
        #self.addSubInterface(self.libraryInterface, FIF.BOOK_SHELF, '库', FIF.LIBRARY_FILL, NavigationItemPosition.BOTTOM)
        loop = QEventLoop(self)
        QTimer.singleShot(1500, loop.quit)
        loop.exec()
        #隐藏启动页面
        self.splashScreen.finish()

        #登录成功提示
        InfoBar.success(
            title='登录',
            content="登录成功！可以开始使用了。",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=4000,
            parent=self
            )
        
    def initJumpSignal(self):
        
        self.HomeFace.rdhl2_PrimaryPushButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.InputFace))
        self.HomeFace.rdhl3_Button.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.CaculationFace))
        self.HomeFace.rdhl4_Button.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.VisualizationFace))
        self.HomeFace.rdhl5_Button.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.DataManageFace))
        #self.HomeFace.rdhl6_Button.clicked.connect()

        self.InputFace.PrimaryPushButton_16.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.CaculationFace))
        self.InputFace.PrimaryPushButton_15.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.VisualizationFace))
        self.InputFace.PrimaryPushButton_19.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.DataManageFace))

        self.CaculationFace.PrimaryPushButton_9.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.VisualizationFace))
        self.VisualizationFace.PrimaryPushButton_9.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.DataManageFace))

    #切换页面触发页面刷新
        self.stackedWidget.currentChanged.connect(self.Pagefresh)   

    def Pagefresh(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        path=os.path.join(self.current_dir,'Database.db')
        conn = sqlite3.connect(database=path)
        cursor = conn.cursor()
    #参数输入界面的id刷新
        # 使用 SQL 查询语句查找最大的 id 并加一
        sql = "SELECT MAX(Parameter_id) AS max_Parameter_id \
        FROM Parametertable \
        WHERE Parameter_id != 'null';"
        cursor.execute(sql)
        result = cursor.fetchone()
        #此次参数的ID
        if result[0]!=None:
                self.InputFace.SubtitleLabel_1038.setText(str(int(result[0])+1))
        else:
                self.InputFace.SubtitleLabel_1038.setText('1')    

    #计算页面的id刷新
        sql = "SELECT MAX(output_id) AS max_output_id \
        FROM outputtable \
        WHERE output_id != 'null';"
        cursor.execute(sql)
        result3 = cursor.fetchone()
        if result3[0]!=None:
                self.CaculationFace.SubtitleLabel_17.setText(str(int(result3[0])+1))
        else:
                self.CaculationFace.SubtitleLabel_17.setText('1')
    #可视化页面的id刷新
        sql = "SELECT MAX(visualization_id) AS max_visualization_id \
        FROM visualizationtable \
        WHERE visualization_id != 'null';"
        cursor.execute(sql)
        result3 = cursor.fetchone()
        #此次可视化的id
        if result3[0]!=None:
                self.VisualizationFace.SubtitleLabel_94.setText(str(int(result3[0])+1))
        else:
                self.VisualizationFace.SubtitleLabel_94.setText('1')

    #计算页面的table刷新
        self.CaculationFace.InputTableInit()
    #可视化页面的table刷新
        self.VisualizationFace.InitTable()
    #数据管理页面的table刷新
        self.DataManageFace.InitTable()