from PyQt5.QtWidgets import QWidget, QFileDialog,QTableWidgetItem
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate
from qfluentwidgets import InfoBar,InfoBarPosition,FluentIcon as FIF,MessageBox,MessageBoxBase
from UI_Visualization import Visualization_UI,SelectSaveDialog_UI
from DrawGraph import *
from SQLiteClass import SQLite
import matplotlib.pyplot as plt
import os,shutil

#设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

class VisualizationFace(QWidget, Visualization_UI):

    def __init__(self, parent=None):
        super(VisualizationFace, self).__init__(parent)
        self.setupUi(self)
        self.mydb=SQLite()   
        self.stackedWidget.setCurrentIndex(0)
        self.Pivot.setCurrentItem('vpage1')
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.InitTable()
        self.InitPivot()
        #是否已经导入;true数据库导入，false本地导入；结果的路径；结果的id；结果的名称；结果的备注
        self.OutputInfo=[False,False,'','未导入','未导入','']
        self.VisualizationInfo=False   
        self.ButtonSignal()
        self.LabelChange()
        self.VisualizationInfoUpdate()
        self.Showtime()
 
    #数据库导入
    def SelectOutput(self):
        selected_row = self.TableWidget.currentRow()
        if selected_row >= 0:
            row_data = []
            for col in range(self.TableWidget.columnCount()):
                item = self.TableWidget.item(selected_row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            
            #连接数据库
            self.mydb.connect()
            #查询结果
            condition={'output_id':row_data[0]}
            path=self.mydb.select("outputtable",["output_path"],condition)     
            self.mydb.close()
            self.OutputInfo=[True,True,path[0][0],row_data[0],row_data[1],'']
            self.LabelChange()
            self.VisualizationInfoUpdate()
            self.InforBar('选择计算结果','选择成功！现在可以准备开始可视化了。')
    #本地导入
    def ImportOutput(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            self.OutputInfo=[True,False,file_path,'null','','']
            self.LabelChange()
            self.VisualizationInfoUpdate()
            self.InforBar('导入计算结果','导入成功！现在可以准备开始可视化了。')
    #丢弃导入
    def DropOutput(self):
        title = '确定要丢弃这份计算结果吗?'
        content = """点击按钮将会丢弃这份计算结果文件，请确认！"""
        w = MessageBox(title, content, self)
        if w.exec():
            self.OutputInfo=[False,False,'','未导入','未导入','']
            self.LabelChange()
            self.VisualizationInfoUpdate()  
    #可视化!!!
    def Visualization(self):       
        #可视化
        create_canvas(self)
        clear_plot(self)     
        islegal=init_data(self,self.OutputInfo[2])
        if islegal:
            plot_data(self)
            self.InforBar('可视化','可视化成功！可以开始查看和保存了。')
            #更新可视化信息
            self.VisualizationInfo=True
            self.LabelChange()
            self.VisualizationInfoUpdate()    
        else:
            InfoBar.error(
                title='可视化',
                content='可视化失败！请检查结果文件是否正确！',
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
                )  
    #丢弃可视化
    def DropVisualization(self):
        title = '确定要丢弃这份可视化结果吗?'
        content = """点击按钮将会丢弃这份可视化结果文件，请确认！"""
        w = MessageBox(title, content, self)
        if w.exec():
            self.VisualizationInfo=False
            clear_plot(self)
            self.LabelChange()
            self.VisualizationInfoUpdate()           
    #编辑可视化信息
    def EditVisualizationInfo(self):
            w=SelectSaveDialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                self.SubtitleLabel_95.setText(w.mylist[0])
                self.SubtitleLabel_97.setText(w.mylist[1])
                save_dir = os.path.join('D:/GraduationDesign/source/Figure/', w.mylist[0])
                self.CaptionLabe_98.setText(save_dir)
                self.PrimaryPushButton_12.setEnabled(True)
                self.InforBar('信息编辑','信息编辑成功！,可以保存可视化了。')          
    #保存可视化
    def SaveVisualization(self):
        #先保存图片，文件夹名为： 可视化名_可视化ID为id
        save_figure(self,self.SubtitleLabel_95.text()+'_可视化ID为'+self.SubtitleLabel_94.text())

        self.mydb.connect()
        save_dir = os.path.join(self.current_dir, 'Figure',self.SubtitleLabel_95.text()+'_可视化ID为'+self.SubtitleLabel_94.text())
        if self.OutputInfo[3]=='null':
            self.OutputInfo[3]=None
        field={
            'output_id':int(self.OutputInfo[3]),
            'account_name':self.SubtitleLabel_93.text(),
            'visualization_id':int(self.SubtitleLabel_94.text()),
            'visualization_name':self.SubtitleLabel_95.text(),
            'visualization_creat_time':self.SubtitleLabel_96.text(),
            'visualization_note':self.SubtitleLabel_97.text(),
            'visualization_path':save_dir
        }
        self.mydb.insert("visualizationtable",field)
        self.InforBar('可视化保存','可视化保存成功！')
    #####################################完整分析组存储#######################################################
        #如果是数据库导入的结果，寻找对应的参数是否是数据库内的。
        if  self.OutputInfo[1]==True:
            condition={'output_id':self.OutputInfo[3]}
            self.mydb.connect()
            parameter_result=self.mydb.select("outputtable",["parameter_id"],condition)
            #如果参数id存在，说明是完整分析组，插入到grouptable中
            if parameter_result:
                result3=self.mydb.selectmax("grouptable","group_id")
            
                #这里是为了防止group_id重复，所以每次插入时都要获取最大的group_id，然后加1
                if result3[0]!=None:
                    new_group_id=result3[0]+1
                else:
                    new_group_id=1
                #插入到grouptable中
                field={
                    'group_id':new_group_id,
                    'group_name':'未命名',
                    'parameter_id':parameter_result[0][0],
                    'output_id':int(self.OutputInfo[3]),
                    'visualization_id':int(self.SubtitleLabel_94.text()),
                    'group_path':'未保存'
                    }
                self.mydb.insert("grouptable",field)
                #保存文件到group文件夹
                save_dir = os.path.join(self.current_dir, 'Group','未命名_分析组ID为'+str(new_group_id))
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                condition={'parameter_id':parameter_result[0][0]}
                p_path=self.mydb.select("parametertable",["parameter_path"],condition)
                condition={'output_id':int(self.OutputInfo[3])}
                o_path=self.mydb.select("outputtable",["output_path"],condition)
                f_path = os.path.join(self.current_dir, 'Figure',self.SubtitleLabel_95.text()+'_可视化ID为'+self.SubtitleLabel_94.text())
                if p_path and o_path and f_path:
                    shutil.copy(p_path[0][0],save_dir)
                    shutil.copy(o_path[0][0],save_dir)
                    # 构造目标路径，包含源文件夹的名字
                    destination_path = os.path.join(save_dir, os.path.basename(f_path))
                    # 如果目标路径已经存在，先删除它
                    if os.path.exists(destination_path):
                        shutil.rmtree(destination_path)
                    # 复制文件夹
                    shutil.copytree(f_path, destination_path)
                    # 更新grouptable中的group_path
                    field={'group_path':save_dir}
                    condition={'group_id':new_group_id}
                    self.mydb.update("grouptable",field,condition)
                    self.InforBar('完整分析组存储','本次可视化涉及一个完整分析组，完整分析组已存储成功！')

        self.mydb.close()
        self.SubtitleLabel_94.setText(str(int(self.SubtitleLabel_94.text())+1))
        self.PrimaryPushButton_12.setEnabled(False)
        
        
#基础功能
    def ButtonSignal(self):
        self.PrimaryPushButton.clicked.connect(self.SelectOutput)
        self.PrimaryPushButton_2.clicked.connect(self.ImportOutput)
        self.PrimaryPushButton_3.clicked.connect(self.DropOutput)
        self.PrimaryPushButton_4.clicked.connect(self.Visualization)
        self.PrimaryPushButton_10.clicked.connect(self.DropVisualization)
        self.PrimaryPushButton_5.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.PrimaryPushButton_5.clicked.connect(lambda:self.Pivot.setCurrentItem('vpage1'))
        self.PrimaryPushButton_5.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.PrimaryPushButton_11.clicked.connect(self.EditVisualizationInfo)
        self.PrimaryPushButton_12.clicked.connect(self.SaveVisualization)
        #第二页
        self.current_page_index=0
        self.PrimaryPushButton_8.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_9.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_13.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_14.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_15.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_16.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_17.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_18.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_19.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.PrimaryPushButton_20.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))

        self.PrimaryPushButton_6.clicked.connect(self.previous_page)
        self.PrimaryPushButton_7.clicked.connect(self.next_page)
        #pivot页面
        self.stackedWidget_2.currentChanged.connect(self.onStackedWidgetChanged)
    def next_page(self):
        self.current_page_index = (self.current_page_index + 1) % self.stackedWidget_2.count()
        self.stackedWidget_2.setCurrentIndex(self.current_page_index)
    def previous_page(self):
        self.current_page_index = (self.current_page_index - 1) % self.stackedWidget_2.count()
        self.stackedWidget_2.setCurrentIndex(self.current_page_index)
    def LabelChange(self):
        #如果仍未导入
        if self.OutputInfo[0]==False:
            self.PrimaryPushButton.setEnabled(True)
            self.PrimaryPushButton_2.setEnabled(True)
            self.IconWidget_6.setIcon(FIF.UNPIN)
            self.TitleLabel_3.setText("未选取计算结果")
            self.PrimaryPushButton_3.setEnabled(False)
            self.SubtitleLabel_6.setText('')
            self.StrongBodyLabel.setText('')
            self.PrimaryPushButton_4.setEnabled(False)
            self.PrimaryPushButton_10.setVisible(False)
            self.IconWidget_9.setVisible(False)
            self.TitleLabel_4.setVisible(False)
            self.IconWidget_11.setIcon(FIF.HIDE)
            self.PrimaryPushButton_5.setEnabled(False)
            self.PrimaryPushButton_11.setEnabled(False)
            self.PrimaryPushButton_12.setEnabled(False)
        #如果已经导入
        elif self.OutputInfo[0]==True:
            self.PrimaryPushButton.setEnabled(False)
            self.PrimaryPushButton_2.setEnabled(False)
            self.IconWidget_6.setIcon(FIF.PIN)
            self.TitleLabel_3.setText("已选取计算结果")
            self.PrimaryPushButton_3.setEnabled(True)
            self.PrimaryPushButton_4.setEnabled(True)
            #如果是数据库导入
            if self.OutputInfo[1]==True:
                self.SubtitleLabel_6.setText("结果来自数据库")
                self.StrongBodyLabel.setText("结果ID: "+self.OutputInfo[3]+'结果名称: '+self.OutputInfo[4])    
            #如果是本地导入
            elif self.OutputInfo[1]==False:
                self.SubtitleLabel_6.setText("结果来自本地,结果路径:")
                self.StrongBodyLabel.setText(self.OutputInfo[2])

            #如果结果已经可视化
            if self.VisualizationInfo==True:
                self.PrimaryPushButton_3.setEnabled(False)
                self.PrimaryPushButton_4.setEnabled(False)
                self.IconWidget_9.setVisible(True)
                self.IconWidget_9.setIcon(FIF.CHECKBOX)
                self.TitleLabel_4.setVisible(True)
                self.TitleLabel_4.setText("可视化已生成！")
                self.PrimaryPushButton_10.setVisible(True)
                self.PrimaryPushButton_10.setEnabled(True)
                self.IconWidget_11.setIcon(FIF.VIEW)
                self.PrimaryPushButton_5.setEnabled(True)
                self.PrimaryPushButton_11.setEnabled(True)
                self.PrimaryPushButton_12.setEnabled(False)
            #如果结果未可视化
            elif self.VisualizationInfo==False:               
                self.PrimaryPushButton_3.setEnabled(True)
                self.PrimaryPushButton_4.setEnabled(True)
                self.IconWidget_9.setVisible(False)
                self.TitleLabel_4.setVisible(False)
                self.PrimaryPushButton_10.setVisible(False)
                self.PrimaryPushButton_10.setEnabled(False)
                self.IconWidget_11.setIcon(FIF.HIDE)
                self.PrimaryPushButton_5.setEnabled(False)
                self.PrimaryPushButton_11.setEnabled(False)
                self.PrimaryPushButton_12.setEnabled(False)
    def VisualizationInfoUpdate(self):
        self.mydb.connect()

        lasttime=self.mydb.selectmax("usertable","lastlogin_time")
        condition={"lastlogin_time":lasttime[0]}
        result1=self.mydb.select("usertable",["account_name"],condition)
        #此次可视化的账户名
        self.SubtitleLabel_93.setText(result1[0][0])
        
        #查询最新可视化id
        result2=self.mydb.selectmax("visualizationtable","visualization_id") 
        #此次可视化的id
        if result2[0]!=None:
                self.SubtitleLabel_94.setText(str(int(result2[0])+1))
        else:
                self.SubtitleLabel_94.setText('1')
        self.mydb.close()
        #路径        
        self.CaptionLabe_98.setText('未输入')
        #如果未导入
        if self.OutputInfo[0]==False:
            self.SubtitleLabel_91.setText('未导入')
            self.SubtitleLabel_92.setText('未导入')
            self.SubtitleLabel_95.setText('未输入')
            self.SubtitleLabel_97.setText('未输入')
        #如果导入了
        elif self.OutputInfo[0]==True:
            self.SubtitleLabel_95.setText('未输入')
            self.SubtitleLabel_97.setText('未输入')          
            self.SubtitleLabel_91.setText(self.OutputInfo[3])
            self.SubtitleLabel_92.setText(self.OutputInfo[4])  
                     
    def InitTable(self):
        self.mydb.connect()
        field=['output_id', 'output_name', 'account_name']
        result=self.mydb.select("outputtable",field)
        self.mydb.close()

        #设置表格样式
        self.TableWidget.setBorderVisible(True)
        self.TableWidget.setBorderRadius(8)
        self.TableWidget.verticalHeader().hide()
        self.TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #重要，设置列数和行数，设置列宽以及表头
        self.TableWidget.setColumnCount(3)
        self.TableWidget.setRowCount(100)
        self.TableWidget.setHorizontalHeaderLabels(['结果ID', '结果名','用户'])
        self.TableWidget.setColumnWidth(0, 136)
        self.TableWidget.setColumnWidth(1, 136)
        self.TableWidget.setColumnWidth(2, 136)    
        # 设置表格内容,i为行数，row为每行数据,j为列数
        for i, row in enumerate(result):
            for j in range(3):
                str_data=str(row[j])
                self.TableWidget.setItem(i, j, QTableWidgetItem(str_data))
    def InitPivot(self):
        self.Pivot.addItem(
            routeKey='vpage1',
            text='最小油膜厚度',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage1)
        )
        self.Pivot.addItem(
            routeKey='vpage2',
            text='油膜承载力',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage2)
        )
        self.Pivot.addItem(
            routeKey='vpage3',
            text='微凸体承载力',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage3)
        )
        self.Pivot.addItem(
            routeKey='vpage4',
            text='润滑油膜剪切力',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage4)
        )
        self.Pivot.addItem(
            routeKey='vpage5',
            text='微凸体摩擦力',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage5)
        )
        self.Pivot.addItem(
            routeKey='vpage6',
            text='总摩擦力',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage6)
        )
        self.Pivot.addItem(
            routeKey='vpage7',
            text='瞬时摩擦损失功率',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage7)
        )
        self.Pivot.addItem(
            routeKey='vpage8',
            text='温度分布',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage8)
        )
        self.Pivot.addItem(
            routeKey='vpage9',
            text='油膜压力分布',
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(self.vpage9)
        )
    def onStackedWidgetChanged(self):
        current = self.stackedWidget_2.currentWidget()
        if current == self.vpage1:
            self.Pivot.setCurrentItem('vpage1')
        elif current == self.vpage2:
            self.Pivot.setCurrentItem('vpage2')
        elif current == self.vpage3:
            self.Pivot.setCurrentItem('vpage3')
        elif current == self.vpage4:  
            self.Pivot.setCurrentItem('vpage4')
        elif current == self.vpage5:
            self.Pivot.setCurrentItem('vpage5')
        elif current == self.vpage6:
            self.Pivot.setCurrentItem('vpage6')
        elif current == self.vpage7:
            self.Pivot.setCurrentItem('vpage7')   
        elif current == self.vpage8:
            self.Pivot.setCurrentItem('vpage8')
        elif current == self.vpage9:
            self.Pivot.setCurrentItem('vpage9')
    def Showtime(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # 更新日期和时间的间隔为1秒
        self.update_datetime()  # 初始化日期和时间显示          
    def update_datetime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        display_text = current_date.toString('yyyy-MM-dd') + ' ' + current_time.toString('hh:mm:ss')
        self.SubtitleLabel_96.setText(display_text)
    def InforBar(self,title,content):
            InfoBar.success(
                title=title,
                content=content,
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
                )
class SelectSaveDialog(MessageBoxBase,SelectSaveDialog_UI):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        self.mylist = [p1,p2]
