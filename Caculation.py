from PyQt5.QtWidgets import QWidget, QFileDialog,QTableWidgetItem
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5 import QtWidgets, QtCore
from qfluentwidgets import FluentIcon as FIF,MessageBox,InfoBar,InfoBarPosition,SubtitleLabel,MessageBoxBase
from UI_Caculation import CaculationFace_UI,SelectSaveDialog_UI
from SQLiteClass import SQLite
import json,os



class CaculationFace(QWidget,CaculationFace_UI):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
    #初始化变量
        self.mydb=SQLite()     
        #self.InputjsonInfo=[true数据库导入false本地导入,参数输入id，参数输入名称]
        self.InputjsonInfo=[False,'未导入','未导入']
        self.InputjsonPath=''
        self.OutputjsonInfo=False
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        
        

    #初始化控件
        self.InputTableInit()
        self.Showtime()
        self.LabelChange()
        self.ButtonSignal()
        self.OutputInfoUpdate()
        self.SubtitleLabel_100=SubtitleLabel(self)
        self.SubtitleLabel_100.setVisible(False)
        self.SubtitleLabel_100.setText('未输入')
        
    def ButtonSignal(self):
        self.PrimaryPushButton.clicked.connect(self.SelectInput)
        self.PrimaryPushButton_2.clicked.connect(self.ImportInput)
        self.PrimaryPushButton_3.clicked.connect(self.BeginCaculation)
        self.PrimaryPushButton_4.clicked.connect(self.EditOutput)
        self.PrimaryPushButton_6.clicked.connect(self.SaveOutput)
        self.PrimaryPushButton_7.clicked.connect(self.DropInput)
        self.PrimaryPushButton_8.clicked.connect(self.DropOutput)
    def InputTableInit(self):
        self.mydb.connect()
        field=['parameter_id','parameter_name','account_name']
        result=self.mydb.select('parametertable',field)
        
        #设置表格样式
        self.TableWidget.setBorderVisible(True)
        self.TableWidget.setBorderRadius(8)
        self.TableWidget.verticalHeader().hide()
        self.TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #重要，设置列数和行数，设置列宽以及表头
        self.TableWidget.setColumnCount(3)
        self.TableWidget.setRowCount(100)
        self.TableWidget.setHorizontalHeaderLabels(['参数ID', '参数名','用户'])
        self.TableWidget.setColumnWidth(0, 136)
        self.TableWidget.setColumnWidth(1, 136)
        self.TableWidget.setColumnWidth(2, 136)    
        # 设置表格内容,i为行数，row为每行数据,j为列数
        for i, row in enumerate(result):
            for j in range(3):
                str_data = str(row[j])
                self.TableWidget.setItem(i, j, QTableWidgetItem(str_data))

    #数据库导入
    def SelectInput(self):
        # 获取选中行的数据
        selected_row = self.TableWidget.currentRow()
        if selected_row >= 0:
            row_data = []
            for col in range(self.TableWidget.columnCount()):
                item = self.TableWidget.item(selected_row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            self.InputjsonInfo=[True,row_data[0],row_data[1]]
            self.InputjsonPath=''
            self.LabelChange()
            self.OutputInfoUpdate()
            self.InforBar('选择输入','选择成功！现在可以准备开始计算了。',True)
    
    #本地导入
    def ImportInput(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            data=CaculationFace.read_json_file(file_path)
            Parameterlist = CaculationFace.extract_json_values(data)
            if Parameterlist is None:
                self.InforBar('参数导入', '导入的参数JSON文件格式错误！',False)
            else:
                self.InputjsonPath=file_path
                self.InputjsonInfo=[False,'null','']
                self.LabelChange()
                self.OutputInfoUpdate()
                self.InforBar('导入输入','导入成功！现在可以准备开始计算了。',True)
  
    def DropInput(self):
        title = '确定要丢弃这份输入文件吗?'
        content = """点击按钮将会丢弃输入文件，请确认！"""
        w = MessageBox(title, content, self)
        if w.exec():
            
            self.InputjsonPath=''
            self.InputjsonInfo=[False,'未导入','未导入']
            self.LabelChange()
            self.OutputInfoUpdate()
            self.InforBar('丢弃输入','丢弃成功！',True)

    def BeginCaculation(self):

            # 读取标准JSON文件

            path=os.path.join(self.current_dir,'StandardInput.json')
            data=CaculationFace.read_json_file(path)
            ########################################
            ##########这里是模拟处理输入数据的过程,过程中调用了data。
            ########################################
            del data
            
            outputpath=os.path.join(self.current_dir,'StandardOutput.json')
            newdata=CaculationFace.read_json_file(outputpath)
            #假设计算将data转化为一个新的newdata，上面两行是模拟处理过程
            
            #保存这个临时的结果文件到临时的地方
            file_path=os.path.join(self.current_dir,'TempOutput.json')
            with open(file_path, 'w', encoding='utf-8') as f:
                #注意ensure_ascii=False，否则中文会被编码为\uXXXX格式
                json.dump(newdata, f, indent=4,ensure_ascii=False)

            self.IndeterminateProgressRing.start()
            self.TitleLabel_2.setText('正在计算中...')
            self.timer1 = QTimer()
            self.timer1.setSingleShot(True)
            # 将停止进度环的函数连接到 QTimer 的 timeout 信号
            self.timer1.timeout.connect(self.FinishCaculation)
            # 启动 QTimer，间隔  秒后触发 timeout 信号
            self.timer1.start(2000)  # 5000 毫秒 = 5 秒
    
    def FinishCaculation(self):
        self.IndeterminateProgressRing.stop()
        self.TitleLabel_2.setText('计算完毕！')
        self.OutputjsonInfo=True
        self.LabelChange()
        self.OutputInfoUpdate()
        self.InforBar('计算结果','计算成功！现在处理结果了。',True)

    def DropOutput(self):
        title = '确定要丢弃这份结果吗?'
        content = """点击按钮将会丢弃结果文件，请确认！"""
        w = MessageBox(title, content, self)
        if w.exec():
            self.OutputjsonInfo=False
            self.LabelChange()
            self.OutputInfoUpdate()
            self.InforBar('丢弃结果','丢弃成功！',True)

    def EditOutput(self):      
            w=SelectSaveDialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                self.SubtitleLabel_21.setText(w.mylist[0])
                self.SubtitleLabel_24.setText(w.mylist[1])
                save_folder = os.path.join(self.current_dir, 'OutputJSON')
                self.CaptionLabel.setText(save_folder)
                self.PrimaryPushButton_6.setEnabled(True)
                self.InforBar('信息编辑','信息编辑成功！',True)

    def SaveOutput(self):
        save_folder = self.CaptionLabel.text()
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        #保存在跟目录的OutputJSON文件夹下的名为 参数名_结果ID为id.json
        save_path = os.path.join(save_folder, self.SubtitleLabel_21.text()+'_结果ID为'+self.SubtitleLabel_17.text()+'.json')

        
        #保存计算的信息
        self.mydb.connect()
        if self.SubtitleLabel_10.text()=='null':
           self.SubtitleLabel_10.text()==None 
        field={
            'parameter_id':int(self.SubtitleLabel_10.text()),
            'output_id':int(self.SubtitleLabel_17.text()),
            'output_creat_time':self.SubtitleLabel_19.text(),
            'account_name':self.SubtitleLabel_25.text(),
            'output_name':self.SubtitleLabel_21.text(),
            'output_note':self.SubtitleLabel_24.text(),
            'output_path':save_path
        }
        self.mydb.insert('outputtable',field)
        
        self.PrimaryPushButton_6.setEnabled(False)
        self.CaptionLabel.setText('未输入')
        self.LabelChange()
        self.OutputInfoUpdate()
        #保存到json文件
        path=os.path.join(self.current_dir,'TempOutput.json')
        data=CaculationFace.read_json_file(path)
        # 将更改后的数据保存到新的JSON文件
        with open(save_path, 'w', encoding='utf-8') as f:
            #注意ensure_ascii=False，否则中文会被编码为\uXXXX格式
            json.dump(data, f, indent=4,ensure_ascii=False)
        
        self.InforBar('保存结果','计算保存成功！可以继续进行数据可视化或其他操作了。',True)

    def LabelChange(self):
        #若文件未选中
        if self.InputjsonPath==''and self.InputjsonInfo[0]==False:

            self.PrimaryPushButton.setEnabled(True)
            self.PrimaryPushButton_2.setEnabled(True)
            
            self.IconWidget_9.setIcon(FIF.UNPIN)
            self.TitleLabel_5.setText('未选取任何文件')
            self.PrimaryPushButton_7.setEnabled(False)
            self.SubtitleLabel_5.setText('')
            self.StrongBodyLabel.setText('')
            self.PrimaryPushButton_3.setEnabled(False)
            self.IndeterminateProgressRing.stop()
            self.TitleLabel_2.setText('')
            
            self.IconWidget_12.setIcon(FIF.UNPIN)
            self.TitleLabel_6.setText('')
            self.PrimaryPushButton_8.setEnabled(False)
            self.PrimaryPushButton_4.setEnabled(False)
            self.PrimaryPushButton_6.setEnabled(False)
            
        #若文件已选择
        elif self.InputjsonPath!='' or self.InputjsonInfo[0]:
            self.PrimaryPushButton.setEnabled(False)
            self.PrimaryPushButton_2.setEnabled(False)
            #若文件是数据库导入的
            if self.InputjsonInfo[0]:
                self.PrimaryPushButton.setEnabled(False)
                self.PrimaryPushButton_2.setEnabled(False)

                self.IconWidget_9.setIcon(FIF.COMPLETED)
                self.TitleLabel_5.setText('已选择输入文件!')
                self.PrimaryPushButton_3.setEnabled(True)
                self.PrimaryPushButton_7.setEnabled(True)
                self.SubtitleLabel_5.setText('文件来自数据库')
                self.StrongBodyLabel.setText('参数ID：'+self.InputjsonInfo[1]+'  参数名称：'+self.InputjsonInfo[2])
                
                #若未计算
                if self.OutputjsonInfo==False:
                    self.IndeterminateProgressRing.stop()
                    self.TitleLabel_2.setText('未得到结果！')
                    self.IconWidget_12.setIcon(FIF.UNPIN)
                    self.TitleLabel_6.setText('未得到结果！')
                    self.PrimaryPushButton_8.setEnabled(False)
                    self.PrimaryPushButton_4.setEnabled(False)
                    self.PrimaryPushButton_6.setEnabled(False)
                #若已计算
                elif self.OutputjsonInfo==True:
                    self.PrimaryPushButton_7.setEnabled(False)
                    self.PrimaryPushButton_3.setEnabled(False)
                    self.IndeterminateProgressRing.stop()
                    self.TitleLabel_2.setText('计算完毕！')
                    self.IconWidget_12.setIcon(FIF.COMPLETED)
                    self.TitleLabel_6.setText('已得到结果！')
                    self.PrimaryPushButton_8.setEnabled(True)
                    self.PrimaryPushButton_4.setEnabled(True)
                    self.PrimaryPushButton_6.setEnabled(False)        
            #若文件是本地导入的
            elif not self.InputjsonInfo[0]:
                self.PrimaryPushButton.setEnabled(False)
                self.PrimaryPushButton_2.setEnabled(False)

                self.IconWidget_9.setIcon(FIF.COMPLETED)
                self.TitleLabel_5.setText('已选择输入文件!')
                self.PrimaryPushButton_3.setEnabled(True)
                self.PrimaryPushButton_7.setEnabled(True)
                self.SubtitleLabel_5.setText('文件来自本地，文件路径：')
                self.StrongBodyLabel.setText(self.InputjsonPath)

                #若未计算
                if self.OutputjsonInfo==False:
                    self.IndeterminateProgressRing.stop()
                    self.TitleLabel_2.setText('未得到结果！')
                    self.IconWidget_12.setIcon(FIF.UNPIN)
                    self.TitleLabel_6.setText('未得到结果！')
                    self.PrimaryPushButton_8.setEnabled(False)
                    self.PrimaryPushButton_4.setEnabled(False)
                    self.PrimaryPushButton_6.setEnabled(False)
                #若已计算
                elif self.OutputjsonInfo==True:
                    self.PrimaryPushButton_7.setEnabled(False)
                    self.PrimaryPushButton_3.setEnabled(False)
                    self.IndeterminateProgressRing.stop()
                    self.TitleLabel_2.setText('计算完毕！')
                    self.IconWidget_12.setIcon(FIF.COMPLETED)
                    self.TitleLabel_6.setText('已得到结果！')
                    self.PrimaryPushButton_8.setEnabled(True)
                    self.PrimaryPushButton_4.setEnabled(True)
                    self.PrimaryPushButton_6.setEnabled(False)
 
    def OutputInfoUpdate(self):
        self.mydb.connect()
        lasttime=self.mydb.selectmax("usertable","lastlogin_time")
        condition={"lastlogin_time":lasttime[0]}
        result1=self.mydb.select("usertable",["account_name"],condition)
    #当前登录用户
        self.SubtitleLabel_25.setText(result1[0][0])
    #参数的id
        self.SubtitleLabel_10.setText(self.InputjsonInfo[1])
    #参数的名称
        self.SubtitleLabel_15.setText(self.InputjsonInfo[2])
    #此次计算的ID
        # 查找最大的 id 并加一
        result3=self.mydb.selectmax("outputtable","output_id")
        if result3[0]!=None:
                self.SubtitleLabel_17.setText(str(int(result3[0])+1))
        else:
                self.SubtitleLabel_17.setText('1')

        
        self.mydb.close()
        self.SubtitleLabel_21.setText('未输入')
        self.SubtitleLabel_24.setText('未输入')
            
    def InforBar(self,title,content,issuccess):
          if issuccess:
            InfoBar.success(
                title=title,
                content=content,
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=2000,
                parent=self
                )
          else:
            InfoBar.error(
                title=title,
                content=content,
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=2000,
                parent=self
                )
    def Showtime(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # 更新日期和时间的间隔为1秒
        self.update_datetime()  # 初始化日期和时间显示          
    def update_datetime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        display_text = current_date.toString('yyyy-MM-dd') + ' ' + current_time.toString('hh:mm:ss')
        self.SubtitleLabel_19.setText(display_text)
    @staticmethod      
    def read_json_file(path=str):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    @staticmethod
    def extract_json_values(data=list):
        all_values = []
        for param_group in data.values():
            for param in param_group:
                if 'value' in param:
                    value_str = str(param['value'])
                    all_values.append(value_str)
                else:
                    return None
        return all_values    

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
