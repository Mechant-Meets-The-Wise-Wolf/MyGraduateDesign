
from PyQt5.QtGui import QColor,QIcon
from PyQt5.QtWidgets import QHBoxLayout

from qfluentwidgets import ( MSFluentTitleBar,SubtitleLabel,
                              setFont,
                            setTheme,  isDarkTheme)
import sqlite3,os

class CustomMainFaceTitle(MSFluentTitleBar):

    def __init__(self, parent):
        super().__init__(parent)
        self.setIcon(QIcon('d:\\GraduationDesign\\新的ui设计-二维图工程\\../images/透明图标spice.png'))
        self.setTitle('摩擦性能分析-数据管理与可视化')
        self.toolButtonLayout = QHBoxLayout()
        color = QColor(206, 206, 206)

        #self.forwardButton = TransparentToolButton(FIF.RIGHT_ARROW.icon(color=color), self)
        #self.backButton = TransparentToolButton(FIF.LEFT_ARROW.icon(color=color), self)
        #上栏显示最近登录的用户名
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        path=os.path.join(self.current_dir,'Database.db')
        conn = sqlite3.connect(database=path)
        cursor = conn.cursor()
        # 使用 SQL 查询语句查找最大的 lastlogin_time 和对应的 account_name
        sql = "SELECT account_name \
        FROM usertable \
        WHERE lastlogin_time = (SELECT MAX(lastlogin_time) FROM usertable)\
        AND account_name!='null'"
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.close()
        self.name=SubtitleLabel(result[0]+',欢迎您使用该系统！',self)    

        self.toolButtonLayout.setContentsMargins(20, 0, 20, 0)
        self.toolButtonLayout.setSpacing(10)
        self.toolButtonLayout.addSpacing(10)
        self.toolButtonLayout.addWidget(self.name)

        #hboxlayout是这个类自带的
        self.hBoxLayout.insertLayout(4, self.toolButtonLayout)
        
       
        

