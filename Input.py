from UI_Input import Input_UI
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from qfluentwidgets import InfoBar,InfoBarPosition,MessageBox
from PyQt5.QtCore import QTimer, QTime, QDate

from UI_Input_dialog import (Input_First_1_dialog_UI,Input_First_2_dialog_UI,Input_First_3_dialog_UI,
                             Input_First_4_dialog_UI,Input_Second_1_dialog_UI,Input_Second_2_dialog_UI,
                             Input_Second_3_dialog_UI,Input_Third_1_dialog_UI,Input_Third_2_dialog_UI,
                             Input_Fourth_1_dialog_UI,Input_Fourth_2_dialog_UI,save_dialog_UI)
from qfluentwidgets import MessageBoxBase
from SQLiteClass import SQLite
import json,os


class InputFace(QtWidgets.QWidget, Input_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.mydb = SQLite()
        self.setupUi(self)
        self.initPivot()
        self.stackedWidget.setCurrentWidget(self.page_21) 
        self.initJumpSignals()
        self.initButtonSignal()
        self.Showtime()

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        
    def initJumpSignals(self):
        self.PrimaryPushButton_71.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_22))
        self.PrimaryPushButton_128.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_22))
        self.PrimaryPushButton_18.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        self.PrimaryPushButton_78.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))
        self.PrimaryPushButton_79.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_23))
        self.PrimaryPushButton_73.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))

        self.PrimaryPushButton_82.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_22))
        self.PrimaryPushButton_83.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_24))
        self.PrimaryPushButton_80.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))

        self.PrimaryPushButton_96.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_23))
        self.PrimaryPushButton_97.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_29))
        self.PrimaryPushButton_94.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))

        self.PrimaryPushButton_122.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_24))
        self.PrimaryPushButton_98.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.PrimaryPushButton_124.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))

        self.PrimaryPushButton_127.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_29))
        self.PrimaryPushButton_117.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.PrimaryPushButton_125.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))

        self.PrimaryPushButton_129.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.PrimaryPushButton_130.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_21))
        self.PrimaryPushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_22))
        self.PrimaryPushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_23))
        self.PrimaryPushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_29))
        self.PrimaryPushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        
        self.stackedWidget.currentChanged.connect(self.onStackedWidgetChanged)

    def onStackedWidgetChanged(self):
        current = self.stackedWidget.currentWidget()
        if current == self.page_21:
            self.Pivot.setCurrentItem('PAGE_0')
        elif current == self.page_22:
            self.Pivot.setCurrentItem('PAGE_1')
        elif current == self.page_23:
            self.Pivot.setCurrentItem('PAGE_2')
        elif current == self.page_24:  
            self.Pivot.setCurrentItem('PAGE_3')
        elif current == self.page_29:
            self.Pivot.setCurrentItem('PAGE_4')
        elif current == self.page:
            self.Pivot.setCurrentItem('PAGE_5')
        elif current == self.page_2:
            self.Pivot.setCurrentItem('PAGE_6')

    def initPivot(self):
        
        self.Pivot.addItem(
            routeKey='PAGE_0',
            text='首页',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_21)
        )
        self.Pivot.addItem(
            routeKey='PAGE_1',
            text='参数#1',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_22)
        )
        self.Pivot.addItem(
            routeKey='PAGE_2',
            text='参数#2P1',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_23)
        )
        self.Pivot.addItem(
            routeKey='PAGE_3',
            text='参数#2P2',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_24)
        )
        self.Pivot.addItem(
            routeKey='PAGE_4',
            text='参数#3',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_29)
        )
        self.Pivot.addItem(
            routeKey='PAGE_5',
            text='参数#4',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page)
        )
        self.Pivot.addItem(
            routeKey='PAGE_6',
            text='参数处理',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_2)
        )
           
    def initButtonSignal(self):
        #首页
        self.PrimaryPushButton_72.clicked.connect(lambda:self.ClearParameter(5))
        self.PrimaryPushButton_17.clicked.connect(self.ImportParameter)
        #参数一
        self.PrimaryPushButton_74.clicked.connect(self.First_1)
        self.PrimaryPushButton_75.clicked.connect(self.First_2)       
        self.PrimaryPushButton_76.clicked.connect(self.First_3)
        self.PrimaryPushButton_77.clicked.connect(self.First_4)
        #参数二
        self.PrimaryPushButton_81.clicked.connect(self.Second_1)
        self.PrimaryPushButton_84.clicked.connect(self.Second_2)
        self.PrimaryPushButton_95.clicked.connect(self.Second_3)
        #参数三
        self.PrimaryPushButton_121.clicked.connect(self.Third_1)
        self.PrimaryPushButton_120.clicked.connect(self.Third_2)
        self.SwitchButton.checkedChanged.connect(self.CardWidget_197_enabled)
        #参数四
        self.PrimaryPushButton_126.clicked.connect(self.Fourth_1)
        self.PrimaryPushButton_123.clicked.connect(self.Fourth_2)
        #参数处理
        self.PrimaryPushButton.clicked.connect(lambda:self.CheckParameter(1))
        self.PrimaryPushButton_2.clicked.connect(lambda:self.CheckParameter(2))
        self.PrimaryPushButton_3.clicked.connect(lambda:self.CheckParameter(3))
        self.PrimaryPushButton_4.clicked.connect(lambda:self.CheckParameter(4))

        self.PrimaryPushButton_9.clicked.connect(lambda:self.ClearParameter(1))
        self.PrimaryPushButton_10.clicked.connect(lambda:self.ClearParameter(2))
        self.PrimaryPushButton_11.clicked.connect(lambda:self.ClearParameter(3))
        self.PrimaryPushButton_12.clicked.connect(lambda:self.ClearParameter(4))
        #参数保存
        self.PrimaryPushButton_14.clicked.connect(self.EditInfo)
        self.PrimaryPushButton_13.clicked.connect(self.SaveParameter)
        
    def ClearParameter(self,index):
        #清空参数命名和备注输入框和路径,保存按钮设为不可用
        self.SubtitleLabel_1044.setText('待输入')
        self.SubtitleLabel_1047.setText('待输入')
        self.CaptionLabel.setText('待输入')
        self.PrimaryPushButton_13.setEnabled(False)
        my_list = ['未输入' for _ in range(93)]
        my_list[72]=False
        #参数一
        if index == 1:
            self.ListWriteToLabel(my_list,1)            
            self.InforBar('参数清除', '柴油机输入参数已经清除成功！',True)
        #参数二    
        elif index == 2:
            self.ListWriteToLabel(my_list,2)
            self.InforBar('参数清除', '活塞环组结构参数已经清除成功！',True)
         
        elif index == 3:
            #参数三
            self.ListWriteToLabel(my_list,3)
            self.InforBar('参数清除', '润滑油属性参数已经清除成功！',True)
       
        elif index == 4:
            #参数四
            self.ListWriteToLabel(my_list,4)
            self.InforBar('参数清除', '收敛判定参数已经清除成功！',True)
            
        elif index==5:
            title = '确定要清除参数吗?'
            content = """点击按钮将会清除所有参数输入，请确认！"""
            w = MessageBox(title, content, self)
            if w.exec():            
                for i in range(1, 5):
                    self.ClearParameter(i)
    def CheckParameter(self,index):
        if index == 1:
            #参数一
            mylist=self.LabelReadToList(1)
            if '未输入' in mylist:
                self.InforBar('参数缺失', '请完整输入柴油机输入参数',False)
            else:
                self.InforBar('参数检查', '柴油机输入参数输入正确！',True)

        elif index == 2:
            #参数二    
            mylist=self.LabelReadToList(2)
            if '未输入' in mylist:
                self.InforBar('参数缺失', '请完整输入活塞环组结构参数',False)
            else:
                self.InforBar('参数检查', '活塞环组结构参数输入正确！',True)
        
        elif index == 3:
            #参数三        
            mylist=self.LabelReadToList(3)
            if '未输入' in mylist:
                self.InforBar('参数缺失', '请完整输入润滑油属性参数',False)
            else:
                self.InforBar('参数检查', '润滑油属性参数输入正确！',True)
        elif index == 4:
            #参数四     
            mylist=self.LabelReadToList(4)
            if '未输入' in mylist:
                self.InforBar('参数缺失', '请完整输入收敛判定参数',False)
            else:
                self.InforBar('参数检查', '收敛判定参数输入正确！',True)
    def ImportParameter(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            data=InputFace.read_json_file(file_path)
            Parameterlist = InputFace.extract_json_values(data)
            if Parameterlist is None:
                self.InforBar('参数导入', '导入的参数JSON文件格式错误！',False)
            else:
                self.ListWriteToLabel(Parameterlist,5)
                self.InforBar('参数导入', '参数导入成功！',True)
    def EditInfo(self):
        #弹出参数保存的细节对话框，并修改对应label的值
        w = Save_dialog(self)
        w.setGeometry(self.geometry())
        if w.exec():
            self.SubtitleLabel_1044.setText(w.mylist[0])
            self.SubtitleLabel_1047.setText(w.mylist[1])
            save_folder = os.path.join(self.current_dir, 'InputJSON')
            self.CaptionLabel.setText(save_folder)
            self.PrimaryPushButton_13.setEnabled(True)
    def SaveParameter(self):       
                
                save_folder = self.CaptionLabel.text()

                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)
                #保存在跟目录的InputJSON文件夹下的名为 参数名_参数ID为id.json
                save_path = os.path.join(save_folder, self.SubtitleLabel_1044.text()+'_参数ID为'+self.SubtitleLabel_1038.text()+'.json')
            #连接数据库存输入记录
                self.mydb.connect()
                field={"Parameter_id":self.SubtitleLabel_1038.text(),
                        "account_name":self.SubtitleLabel_1036.text(),
                        "Parameter_creat_time":self.SubtitleLabel_992.text(),
                        "Parameter_name":self.SubtitleLabel_1044.text(),
                        "Parameter_note":self.SubtitleLabel_1047.text(),
                        "Parameter_path":save_path}
                
                self.mydb.insert("parametertable",field)       
                self.mydb.close()
                
            #开始生成json文件
                # 先将参数值存入列表
                valuelist = self.LabelReadToList(5)
                # 读取标准JSON文件
                path=os.path.join(self.current_dir,'StandardInput.json')
                data=InputFace.read_json_file(path)
                
                # 遍历每个参数组
                for param_group in data.values():
                # 遍历参数组中的每个项目
                    for item in param_group:
                # 从替换值列表中取出一个值，并替换当前项目的value值
                        item['value'] = valuelist.pop(0)

            # 将更改后的数据保存到新的JSON文件
                with open(save_path, 'w', encoding='utf-8') as f:
                    #注意ensure_ascii=False，否则中文会被编码为\uXXXX格式
                    json.dump(data, f, indent=4,ensure_ascii=False)
                #更新id提示label
                self.SubtitleLabel_1038.setText(str(int(self.SubtitleLabel_1038.text())+1))
                #清空参数命名和备注输入框和路径,保存按钮设为不可用
                self.SubtitleLabel_1044.setText('待输入')
                self.SubtitleLabel_1047.setText('待输入')
                self.CaptionLabel.setText('待输入')

                self.PrimaryPushButton_13.setEnabled(False)
                #弹出成功提示框
                self.InforBar('参数保存', '参数已保存成功！可以在本地和管理页面查看！',True)         
    def LabelReadToList(self,index):
        mylist=[]
        #参数一
        if index==1:
            mylist.append(self.SubtitleLabel_651.text())
            mylist.append(self.SubtitleLabel_652.text())
            mylist.append(self.SubtitleLabel_653.text())
            mylist.append(self.SubtitleLabel_654.text())
            mylist.append(self.SubtitleLabel_655.text())  
            mylist.append(self.SubtitleLabel_656.text())

            mylist.append(self.SubtitleLabel_660.text())
            mylist.append(self.SubtitleLabel_661.text())
            mylist.append(self.SubtitleLabel_662.text())

            mylist.append(self.SubtitleLabel_667.text())
            mylist.append(self.SubtitleLabel_668.text())
            mylist.append(self.SubtitleLabel_669.text())
            mylist.append(self.SubtitleLabel_670.text())

            mylist.append(self.SubtitleLabel_676.text())
            mylist.append(self.SubtitleLabel_677.text())
            mylist.append(self.SubtitleLabel_678.text())
            mylist.append(self.SubtitleLabel_679.text())
            mylist.append(self.SubtitleLabel_680.text())
        #参数二
        #696-712
        if index==2:      
            mylist.append(self.SubtitleLabel_696.text())
            mylist.append(self.SubtitleLabel_697.text())
            mylist.append(self.SubtitleLabel_698.text())
            mylist.append(self.SubtitleLabel_699.text())
            mylist.append(self.SubtitleLabel_700.text())
            mylist.append(self.SubtitleLabel_701.text())
            mylist.append(self.SubtitleLabel_702.text())
            mylist.append(self.SubtitleLabel_703.text())
            mylist.append(self.SubtitleLabel_704.text())
            mylist.append(self.SubtitleLabel_705.text())
            mylist.append(self.SubtitleLabel_706.text())
            mylist.append(self.SubtitleLabel_707.text())
            mylist.append(self.SubtitleLabel_708.text())
            mylist.append(self.SubtitleLabel_709.text())
            mylist.append(self.SubtitleLabel_710.text())
            mylist.append(self.SubtitleLabel_711.text())
            mylist.append(self.SubtitleLabel_712.text())
            #728-744
            mylist.append(self.SubtitleLabel_728.text())
            mylist.append(self.SubtitleLabel_729.text())
            mylist.append(self.SubtitleLabel_730.text())
            mylist.append(self.SubtitleLabel_731.text())
            mylist.append(self.SubtitleLabel_732.text())
            mylist.append(self.SubtitleLabel_733.text())
            mylist.append(self.SubtitleLabel_734.text())
            mylist.append(self.SubtitleLabel_735.text())
            mylist.append(self.SubtitleLabel_736.text())
            mylist.append(self.SubtitleLabel_737.text())
            mylist.append(self.SubtitleLabel_738.text())
            mylist.append(self.SubtitleLabel_739.text())
            mylist.append(self.SubtitleLabel_740.text())
            mylist.append(self.SubtitleLabel_741.text())
            mylist.append(self.SubtitleLabel_742.text())
            mylist.append(self.SubtitleLabel_743.text())
            mylist.append(self.SubtitleLabel_744.text())
            #820-836
            mylist.append(self.SubtitleLabel_820.text())
            mylist.append(self.SubtitleLabel_821.text())
            mylist.append(self.SubtitleLabel_822.text())
            mylist.append(self.SubtitleLabel_823.text())
            mylist.append(self.SubtitleLabel_824.text())
            mylist.append(self.SubtitleLabel_825.text())

            mylist.append(self.SubtitleLabel_828.text())
            mylist.append(self.SubtitleLabel_829.text())
            mylist.append(self.SubtitleLabel_830.text())
            mylist.append(self.SubtitleLabel_831.text())
            mylist.append(self.SubtitleLabel_832.text())
            mylist.append(self.SubtitleLabel_833.text())
            mylist.append(self.SubtitleLabel_834.text())
            mylist.append(self.SubtitleLabel_835.text())
            mylist.append(self.SubtitleLabel_836.text())
        #参数三
        if index==3:
            mylist.append(self.SubtitleLabel_983.text())
            mylist.append(self.SubtitleLabel_984.text())
            mylist.append(self.SubtitleLabel_985.text())
            mylist.append(self.SubtitleLabel_986.text())
            mylist.append(self.SubtitleLabel_988.text())
            if self.SwitchButton.isChecked():
                mylist.append(True)
            else:
                mylist.append(False)

            mylist.append(self.SubtitleLabel_1137.text())
            mylist.append(self.SubtitleLabel_1138.text())
            mylist.append(self.SubtitleLabel_1139.text())
            mylist.append(self.SubtitleLabel_1140.text())
            mylist.append(self.SubtitleLabel_1141.text())
            mylist.append(self.SubtitleLabel_1142.text())
            mylist.append(self.SubtitleLabel_1143.text())
            mylist.append(self.SubtitleLabel_1144.text())
            mylist.append(self.SubtitleLabel_1145.text())
        #参数四
        if index==4:
            mylist.append(self.SubtitleLabel_1015.text())
            mylist.append(self.SubtitleLabel_1016.text())
            mylist.append(self.SubtitleLabel_1017.text())
            mylist.append(self.SubtitleLabel_1018.text())
            mylist.append(self.SubtitleLabel_1019.text())
            mylist.append(self.SubtitleLabel_1020.text())
            mylist.append(self.SubtitleLabel_1021.text())
            mylist.append(self.SubtitleLabel_1022.text())
            mylist.append(self.SubtitleLabel_1023.text())

            mylist.append(self.SubtitleLabel_991.text())
            mylist.append(self.SubtitleLabel_1014.text())
        if index==5:
            mylist=self.LabelReadToList(1)+self.LabelReadToList(2) \
                +self.LabelReadToList(3)+self.LabelReadToList(4)        
        return mylist
    def ListWriteToLabel(self,Parameterlist,index):
        #参数一
        if index==1:
            self.SubtitleLabel_651.setText(Parameterlist[0])
            self.SubtitleLabel_652.setText(Parameterlist[1])
            self.SubtitleLabel_653.setText(Parameterlist[2])
            self.SubtitleLabel_654.setText(Parameterlist[3])
            self.SubtitleLabel_655.setText(Parameterlist[4])
            self.SubtitleLabel_656.setText(Parameterlist[5])

            self.SubtitleLabel_660.setText(Parameterlist[6])
            self.SubtitleLabel_661.setText(Parameterlist[7])
            self.SubtitleLabel_662.setText(Parameterlist[8])

            self.SubtitleLabel_667.setText(Parameterlist[9])
            self.SubtitleLabel_668.setText(Parameterlist[10])
            self.SubtitleLabel_669.setText(Parameterlist[11])
            self.SubtitleLabel_670.setText(Parameterlist[12])

            self.SubtitleLabel_676.setText(Parameterlist[13])
            self.SubtitleLabel_677.setText(Parameterlist[14])
            self.SubtitleLabel_678.setText(Parameterlist[15])
            self.SubtitleLabel_679.setText(Parameterlist[16])
            self.SubtitleLabel_680.setText(Parameterlist[17])
        if index==2:
            #参数二
            #696-712
            self.SubtitleLabel_696.setText(Parameterlist[18])
            self.SubtitleLabel_697.setText(Parameterlist[19])
            self.SubtitleLabel_698.setText(Parameterlist[20])
            self.SubtitleLabel_699.setText(Parameterlist[21])
            self.SubtitleLabel_700.setText(Parameterlist[22])
            self.SubtitleLabel_701.setText(Parameterlist[23])
            self.SubtitleLabel_702.setText(Parameterlist[24])
            self.SubtitleLabel_703.setText(Parameterlist[25])
            self.SubtitleLabel_704.setText(Parameterlist[26])
            self.SubtitleLabel_705.setText(Parameterlist[27])
            self.SubtitleLabel_706.setText(Parameterlist[28])
            self.SubtitleLabel_707.setText(Parameterlist[29])
            self.SubtitleLabel_708.setText(Parameterlist[30])
            self.SubtitleLabel_709.setText(Parameterlist[31])
            self.SubtitleLabel_710.setText(Parameterlist[32])
            self.SubtitleLabel_711.setText(Parameterlist[33])
            self.SubtitleLabel_712.setText(Parameterlist[34])
            #728-744
            self.SubtitleLabel_728.setText(Parameterlist[35])
            self.SubtitleLabel_729.setText(Parameterlist[36])
            self.SubtitleLabel_730.setText(Parameterlist[37])
            self.SubtitleLabel_731.setText(Parameterlist[38])
            self.SubtitleLabel_732.setText(Parameterlist[39])
            self.SubtitleLabel_733.setText(Parameterlist[40])
            self.SubtitleLabel_734.setText(Parameterlist[41])
            self.SubtitleLabel_735.setText(Parameterlist[42])
            self.SubtitleLabel_736.setText(Parameterlist[43])
            self.SubtitleLabel_737.setText(Parameterlist[44])
            self.SubtitleLabel_738.setText(Parameterlist[45])
            self.SubtitleLabel_739.setText(Parameterlist[46])
            self.SubtitleLabel_740.setText(Parameterlist[47])
            self.SubtitleLabel_741.setText(Parameterlist[48])
            self.SubtitleLabel_742.setText(Parameterlist[49])
            self.SubtitleLabel_743.setText(Parameterlist[50])
            self.SubtitleLabel_744.setText(Parameterlist[51])
            #820-836
            self.SubtitleLabel_820.setText(Parameterlist[52])
            self.SubtitleLabel_821.setText(Parameterlist[53])
            self.SubtitleLabel_822.setText(Parameterlist[54])
            self.SubtitleLabel_823.setText(Parameterlist[55])
            self.SubtitleLabel_824.setText(Parameterlist[56])
            self.SubtitleLabel_825.setText(Parameterlist[57])

            self.SubtitleLabel_828.setText(Parameterlist[58])
            self.SubtitleLabel_829.setText(Parameterlist[59])
            self.SubtitleLabel_830.setText(Parameterlist[60])
            self.SubtitleLabel_831.setText(Parameterlist[61])
            self.SubtitleLabel_832.setText(Parameterlist[62])
            self.SubtitleLabel_833.setText(Parameterlist[63])
            self.SubtitleLabel_834.setText(Parameterlist[64])
            self.SubtitleLabel_835.setText(Parameterlist[65])
            self.SubtitleLabel_836.setText(Parameterlist[66])
        if index==3:
            #参数三
            self.SubtitleLabel_983.setText(Parameterlist[67])
            self.SubtitleLabel_984.setText(Parameterlist[68])
            self.SubtitleLabel_985.setText(Parameterlist[69])
            self.SubtitleLabel_986.setText(Parameterlist[70])
            self.SubtitleLabel_988.setText(Parameterlist[71])
            if Parameterlist[72] == 'True':
                self.SwitchButton.setChecked(True)
            else:
                self.SwitchButton.setChecked(False)

            self.SubtitleLabel_1137.setText(Parameterlist[73])
            self.SubtitleLabel_1138.setText(Parameterlist[74])
            self.SubtitleLabel_1139.setText(Parameterlist[75])
            self.SubtitleLabel_1140.setText(Parameterlist[76])
            self.SubtitleLabel_1141.setText(Parameterlist[77])
            self.SubtitleLabel_1142.setText(Parameterlist[78])
            self.SubtitleLabel_1143.setText(Parameterlist[79])
            self.SubtitleLabel_1144.setText(Parameterlist[80])
            self.SubtitleLabel_1145.setText(Parameterlist[81])
        if index==4:
            #参数四
            self.SubtitleLabel_1015.setText(Parameterlist[82])
            self.SubtitleLabel_1016.setText(Parameterlist[83])
            self.SubtitleLabel_1017.setText(Parameterlist[84])
            self.SubtitleLabel_1018.setText(Parameterlist[85])
            self.SubtitleLabel_1019.setText(Parameterlist[86])
            self.SubtitleLabel_1020.setText(Parameterlist[87])
            self.SubtitleLabel_1021.setText(Parameterlist[88])
            self.SubtitleLabel_1022.setText(Parameterlist[89])
            self.SubtitleLabel_1023.setText(Parameterlist[90])

            self.SubtitleLabel_991.setText(Parameterlist[91])
            self.SubtitleLabel_1014.setText(Parameterlist[92])
        if index==5:
            self.ListWriteToLabel(Parameterlist,1)
            self.ListWriteToLabel(Parameterlist,2)
            self.ListWriteToLabel(Parameterlist,3)   
            self.ListWriteToLabel(Parameterlist,4)

    def First_1(self):
            w=Input_First_1_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                self.SubtitleLabel_651.setText(w.mylist[0])
                self.SubtitleLabel_652.setText(w.mylist[1])
                self.SubtitleLabel_653.setText(w.mylist[2])
                self.SubtitleLabel_654.setText(w.mylist[3])
                self.SubtitleLabel_655.setText(w.mylist[4])
                self.SubtitleLabel_656.setText(w.mylist[5])         
    def First_2(self):
            w = Input_First_2_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                self.SubtitleLabel_660.setText(w.mylist[0])
                self.SubtitleLabel_661.setText(w.mylist[1])
                self.SubtitleLabel_662.setText(w.mylist[2])
    def First_3(self):
            w = Input_First_3_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec(): 
                self.SubtitleLabel_667.setText(w.mylist[0])
                self.SubtitleLabel_668.setText(w.mylist[1])
                self.SubtitleLabel_669.setText(w.mylist[1])
                self.SubtitleLabel_670.setText(w.mylist[1])      
    def First_4(self):
            w = Input_First_4_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                self.SubtitleLabel_676.setText(w.mylist[0])
                self.SubtitleLabel_677.setText(w.mylist[1])
                self.SubtitleLabel_678.setText(w.mylist[2])
                self.SubtitleLabel_679.setText(w.mylist[3])
                self.SubtitleLabel_680.setText(w.mylist[4])
    def Second_1(self):
            w = Input_Second_1_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                #696-712
                self.SubtitleLabel_696.setText(w.mylist[0])
                self.SubtitleLabel_697.setText(w.mylist[1])
                self.SubtitleLabel_698.setText(w.mylist[2])
                self.SubtitleLabel_699.setText(w.mylist[3])
                self.SubtitleLabel_700.setText(w.mylist[4])
                self.SubtitleLabel_701.setText(w.mylist[5])
                self.SubtitleLabel_702.setText(w.mylist[6])
                self.SubtitleLabel_703.setText(w.mylist[7])
                self.SubtitleLabel_704.setText(w.mylist[8])
                self.SubtitleLabel_705.setText(w.mylist[9])
                self.SubtitleLabel_706.setText(w.mylist[10])
                self.SubtitleLabel_707.setText(w.mylist[11])
                self.SubtitleLabel_708.setText(w.mylist[12])
                self.SubtitleLabel_709.setText(w.mylist[13])
                self.SubtitleLabel_710.setText(w.mylist[14])
                self.SubtitleLabel_711.setText(w.mylist[15])
                self.SubtitleLabel_712.setText(w.mylist[16])
    def Second_2(self):
            w = Input_Second_2_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                #728-744
                self.SubtitleLabel_728.setText(w.mylist[0])
                self.SubtitleLabel_729.setText(w.mylist[1])
                self.SubtitleLabel_730.setText(w.mylist[2])
                self.SubtitleLabel_731.setText(w.mylist[3])
                self.SubtitleLabel_732.setText(w.mylist[4])
                self.SubtitleLabel_733.setText(w.mylist[5])
                self.SubtitleLabel_734.setText(w.mylist[6])
                self.SubtitleLabel_735.setText(w.mylist[7])
                self.SubtitleLabel_736.setText(w.mylist[8])
                self.SubtitleLabel_737.setText(w.mylist[9])
                self.SubtitleLabel_738.setText(w.mylist[10])
                self.SubtitleLabel_739.setText(w.mylist[11])
                self.SubtitleLabel_740.setText(w.mylist[12])
                self.SubtitleLabel_741.setText(w.mylist[13])
                self.SubtitleLabel_742.setText(w.mylist[14])
                self.SubtitleLabel_743.setText(w.mylist[15])
                self.SubtitleLabel_744.setText(w.mylist[16])
    def Second_3(self):
            w = Input_Second_3_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                #820-836
                self.SubtitleLabel_820.setText(w.mylist[0])
                self.SubtitleLabel_821.setText(w.mylist[1])
                self.SubtitleLabel_822.setText(w.mylist[2])
                self.SubtitleLabel_823.setText(w.mylist[3])
                self.SubtitleLabel_824.setText(w.mylist[4])
                self.SubtitleLabel_825.setText(w.mylist[5])

                self.SubtitleLabel_828.setText(w.mylist[6])
                self.SubtitleLabel_829.setText(w.mylist[7])
                self.SubtitleLabel_830.setText(w.mylist[8])
                self.SubtitleLabel_831.setText(w.mylist[9])
                self.SubtitleLabel_832.setText(w.mylist[10])
                self.SubtitleLabel_833.setText(w.mylist[11])
                self.SubtitleLabel_834.setText(w.mylist[12])
                self.SubtitleLabel_835.setText(w.mylist[13])
                self.SubtitleLabel_836.setText(w.mylist[14])
    def Third_1(self):
            w = Input_Third_1_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                #983-988
                self.SubtitleLabel_983.setText(w.mylist[0])
                self.SubtitleLabel_984.setText(w.mylist[1])
                self.SubtitleLabel_985.setText(w.mylist[2])
                self.SubtitleLabel_986.setText(w.mylist[3])
                self.SubtitleLabel_988.setText(w.mylist[4])
    def Third_2(self):
            w = Input_Third_2_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                #1137-1145
                self.SubtitleLabel_1137.setText(w.mylist[0])
                self.SubtitleLabel_1138.setText(w.mylist[1])
                self.SubtitleLabel_1139.setText(w.mylist[2])
                self.SubtitleLabel_1140.setText(w.mylist[3])
                self.SubtitleLabel_1141.setText(w.mylist[4])
                self.SubtitleLabel_1142.setText(w.mylist[5])
                self.SubtitleLabel_1143.setText(w.mylist[6])
                self.SubtitleLabel_1144.setText(w.mylist[7])
                self.SubtitleLabel_1145.setText(w.mylist[8])
    def CardWidget_197_enabled(self):
            if self.SwitchButton.isChecked():
                self.TitleLabel_102.setText('固体颗粒参数/含颗粒')
                self.CardWidget_197.setEnabled(True)
            else:
                self.TitleLabel_102.setText('固体颗粒参数/不含颗粒')
                self.CardWidget_197.setEnabled(False)
    def Fourth_1(self):
            w = Input_Fourth_1_dialog(self)
            w.setGeometry(self.geometry())
            if w.exec():
                #1015-1023
                self.SubtitleLabel_1015.setText(w.mylist[0])
                self.SubtitleLabel_1016.setText(w.mylist[1])
                self.SubtitleLabel_1017.setText(w.mylist[2])
                self.SubtitleLabel_1018.setText(w.mylist[3])
                self.SubtitleLabel_1019.setText(w.mylist[4])
                self.SubtitleLabel_1020.setText(w.mylist[5])
                self.SubtitleLabel_1021.setText(w.mylist[6])
                self.SubtitleLabel_1022.setText(w.mylist[7])
                self.SubtitleLabel_1023.setText(w.mylist[8])
    def Fourth_2(self):
        w = Input_Fourth_2_dialog(self)
        w.setGeometry(self.geometry())
        if w.exec():
            self.SubtitleLabel_991.setText(w.mylist[0])
            self.SubtitleLabel_1014.setText(w.mylist[1])
       
    def Showtime(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # 更新日期和时间的间隔为1秒
        self.update_datetime()  # 初始化日期和时间显示          
    def update_datetime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        display_text = current_date.toString('yyyy-MM-dd') + ' ' + current_time.toString('hh:mm:ss')
        self.SubtitleLabel_992.setText(display_text)       
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
        

class Input_First_1_dialog(MessageBoxBase, Input_First_1_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_151)

        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
        self.LineEdit_6.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        p6=self.LineEdit_6.text()
        self.mylist = [p1,p2,p3,p4,p5,p6]
class Input_First_2_dialog(MessageBoxBase, Input_First_2_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_155)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()   
        self.mylist = [p1,p2,p3]
class Input_First_3_dialog(MessageBoxBase, Input_First_3_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_158)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        self.mylist = [p1,p2,p3,p4]
class Input_First_4_dialog(MessageBoxBase, Input_First_4_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_161)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        self.mylist = [p1,p2,p3,p4,p5]
class Input_Second_1_dialog(MessageBoxBase, Input_Second_1_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_165)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
        self.LineEdit_6.textChanged.connect(self.updata_list)
        self.LineEdit_7.textChanged.connect(self.updata_list)
        self.LineEdit_8.textChanged.connect(self.updata_list)
        self.LineEdit_9.textChanged.connect(self.updata_list)
        self.LineEdit_10.textChanged.connect(self.updata_list)
        self.LineEdit_11.textChanged.connect(self.updata_list)
        self.LineEdit_12.textChanged.connect(self.updata_list)
        self.LineEdit_13.textChanged.connect(self.updata_list)
        self.LineEdit_14.textChanged.connect(self.updata_list)
        self.LineEdit_15.textChanged.connect(self.updata_list)
        self.LineEdit_16.textChanged.connect(self.updata_list)
        self.LineEdit_17.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        p6=self.LineEdit_6.text()
        p7=self.LineEdit_7.text()
        p8=self.LineEdit_8.text()
        p9=self.LineEdit_9.text()
        p10=self.LineEdit_10.text()
        p11=self.LineEdit_11.text()
        p12=self.LineEdit_12.text()
        p13=self.LineEdit_13.text()
        p14=self.LineEdit_14.text()
        p15=self.LineEdit_15.text()
        p16=self.LineEdit_16.text()
        p17=self.LineEdit_17.text()
        self.mylist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17]
class Input_Second_2_dialog(MessageBoxBase, Input_Second_2_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_168)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
        self.LineEdit_6.textChanged.connect(self.updata_list)
        self.LineEdit_7.textChanged.connect(self.updata_list)
        self.LineEdit_8.textChanged.connect(self.updata_list)
        self.LineEdit_9.textChanged.connect(self.updata_list)
        self.LineEdit_10.textChanged.connect(self.updata_list)
        self.LineEdit_11.textChanged.connect(self.updata_list)
        self.LineEdit_12.textChanged.connect(self.updata_list)
        self.LineEdit_13.textChanged.connect(self.updata_list)
        self.LineEdit_14.textChanged.connect(self.updata_list)
        self.LineEdit_15.textChanged.connect(self.updata_list)
        self.LineEdit_16.textChanged.connect(self.updata_list)
        self.LineEdit_17.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        p6=self.LineEdit_6.text()
        p7=self.LineEdit_7.text()
        p8=self.LineEdit_8.text()
        p9=self.LineEdit_9.text()
        p10=self.LineEdit_10.text()
        p11=self.LineEdit_11.text()
        p12=self.LineEdit_12.text()
        p13=self.LineEdit_13.text()
        p14=self.LineEdit_14.text()
        p15=self.LineEdit_15.text()
        p16=self.LineEdit_16.text()
        p17=self.LineEdit_17.text()
        self.mylist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17]
class Input_Second_3_dialog(MessageBoxBase, Input_Second_3_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_193)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
        self.LineEdit_6.textChanged.connect(self.updata_list)
        self.LineEdit_7.textChanged.connect(self.updata_list)
        self.LineEdit_8.textChanged.connect(self.updata_list)
        self.LineEdit_9.textChanged.connect(self.updata_list)
        self.LineEdit_10.textChanged.connect(self.updata_list)
        self.LineEdit_11.textChanged.connect(self.updata_list)
        self.LineEdit_12.textChanged.connect(self.updata_list)
        self.LineEdit_13.textChanged.connect(self.updata_list)
        self.LineEdit_14.textChanged.connect(self.updata_list)
        self.LineEdit_15.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        p6=self.LineEdit_6.text()
        p7=self.LineEdit_7.text()
        p8=self.LineEdit_8.text()
        p9=self.LineEdit_9.text()
        p10=self.LineEdit_10.text()
        p11=self.LineEdit_11.text()
        p12=self.LineEdit_12.text()
        p13=self.LineEdit_13.text()
        p14=self.LineEdit_14.text()
        p15=self.LineEdit_15.text()
        self.mylist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]
class Input_Third_1_dialog(MessageBoxBase, Input_Third_1_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_202)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        self.mylist = [p1,p2,p3,p4,p5]
class Input_Third_2_dialog(MessageBoxBase, Input_Third_2_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_197)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
        self.LineEdit_6.textChanged.connect(self.updata_list)
        self.LineEdit_7.textChanged.connect(self.updata_list)
        self.LineEdit_8.textChanged.connect(self.updata_list)
        self.LineEdit_9.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        p6=self.LineEdit_6.text()
        p7=self.LineEdit_7.text()
        p8=self.LineEdit_8.text()
        p9=self.LineEdit_9.text()
        self.mylist = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
class Input_Fourth_1_dialog(MessageBoxBase, Input_Fourth_1_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_212)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)
        self.LineEdit_5.textChanged.connect(self.updata_list)
        self.LineEdit_6.textChanged.connect(self.updata_list)
        self.LineEdit_7.textChanged.connect(self.updata_list)
        self.LineEdit_8.textChanged.connect(self.updata_list)
        self.LineEdit_9.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        p5=self.LineEdit_5.text()
        p6=self.LineEdit_6.text()
        p7=self.LineEdit_7.text()
        p8=self.LineEdit_8.text()
        p9=self.LineEdit_9.text()
        self.mylist = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
class Input_Fourth_2_dialog(MessageBoxBase, Input_Fourth_2_dialog_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_208)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        self.mylist = [p1,p2]
class Save_dialog(MessageBoxBase, save_dialog_UI):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget_223)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        self.mylist = [p1,p2]
