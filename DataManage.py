from UI_DataManage import DataManage_UI,ManageDialog_UI
from SQLiteClass import SQLite
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import QTimer,Qt
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QWidget,QTableWidgetItem,QCompleter,QFileDialog
from qfluentwidgets import FluentIcon as FIF,InfoBar,InfoBarPosition,MessageBox,MessageBoxBase
import os,sqlite3,shutil

class DataManageFace(QWidget,DataManage_UI):

    def __init__(self,parent=None):
        super(DataManageFace,self).__init__(parent)
        self.setupUi(self)
        self.mydb=SQLite()
        self.current_dir=os.path.dirname(os.path.realpath(__file__))
        #isSearching,SearchField,SearchText
        self.SearchInfo1=[False,'','']
        self.SearchInfo2=[False,'','']
        self.SearchInfo3=[False,'','']
        self.SearchInfo4=[False,'','']
        self.SearchInfo5=[False,'','']

        self.InitPivot()
        self.InitTable()
        self.InitComboBoxAndCompleter()
        self.InitButtonSignal()

    def InitTable(self):
        def InitTableStyle(TableWidget,ColumnCount,RowCount,HeaderLabels):
            #设置表格样式
            TableWidget.setBorderVisible(True)
            TableWidget.setBorderRadius(8)
            TableWidget.verticalHeader().hide()
            TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            #重要，设置列数和行数，设置列宽以及表头
            TableWidget.setColumnCount(ColumnCount)
            TableWidget.setRowCount(RowCount)
            TableWidget.setHorizontalHeaderLabels(HeaderLabels)
            
            #设置行宽
            for i in range(RowCount):
                TableWidget.setRowHeight(i, 33)
            #设置列宽
            for i in range(ColumnCount):
                width=1080/ColumnCount
                TableWidget.setColumnWidth(i, width)
        #参数表
        ColumnCount=6
        RowCount=110
        HeaderLabels=['参数ID','参数名称','参数备注','用户名','参数创建时间','存放路径']
        InitTableStyle(TableWidget=self.TableWidget,ColumnCount=ColumnCount,RowCount=RowCount,HeaderLabels=HeaderLabels)
        
        #输出表
        ColumnCount=7
        RowCount=110
        HeaderLabels=['参数ID','计算结果ID','计算结果名称','计算结果备注','用户名','计算结果创建时间','存放路径']
        InitTableStyle(TableWidget=self.TableWidget_2,ColumnCount=ColumnCount,RowCount=RowCount,HeaderLabels=HeaderLabels)
        
        #可视化表
        ColumnCount=7
        RowCount=110
        HeaderLabels=['计算结果ID','可视化ID','可视化名称','可视化备注','用户名','可视化创建时间','存放路径']
        InitTableStyle(TableWidget=self.TableWidget_3,ColumnCount=ColumnCount,RowCount=RowCount,HeaderLabels=HeaderLabels)
        
        #完整分析组
        ColumnCount=7
        RowCount=110
        HeaderLabels=['完整分析组ID','完整分析组名称','参数ID','计算结果ID','可视化ID','存放状态','存放路径']
        InitTableStyle(TableWidget=self.TableWidget_4,ColumnCount=ColumnCount,RowCount=RowCount,HeaderLabels=HeaderLabels)
        
        #用户管理
        ColumnCount=3
        RowCount=110
        HeaderLabels=['用户名','创建时间','最后登录时间']
        InitTableStyle(TableWidget=self.TableWidget_5,ColumnCount=ColumnCount,RowCount=RowCount,HeaderLabels=HeaderLabels)
        #初始化数据
        self.InitTableData(0)
     
    #初始化表格的数据，显示所有数据，除了切换界面，点击清空按钮也会触发。          
    def InitTableData(self, which_table):
        def set_table_contents(table_widget, result):
            table_widget.clearContents()
            for i, row in enumerate(result):
                for j, data in enumerate(row):
                    table_widget.setItem(i, j, QTableWidgetItem(str(data)))

        self.mydb.connect()

        if which_table == 0:
            for i in range(1, 6):
                self.InitTableData(i)
        elif which_table == 1:
            result=self.mydb.select("parametertable")
            set_table_contents(self.TableWidget, result)
        elif which_table == 2:
            result=self.mydb.select("outputtable")
            set_table_contents(self.TableWidget_2, result)
        elif which_table == 3:
            result=self.mydb.select("visualizationtable")
            set_table_contents(self.TableWidget_3, result)
        elif which_table == 4:
            result=self.mydb.select("grouptable")
            set_table_contents(self.TableWidget_4, result)
        elif which_table == 5:
            field=['account_name','create_time','lastlogin_time']
            result=self.mydb.select("usertable",field)
            set_table_contents(self.TableWidget_5, result)
        self.mydb.close()     
        self.SearchInfo = [False, '', '']
        self.LabelandPivotChange()

    def RefreshTable(self):
        current = self.stackedWidget.currentWidget()
        page_mapping = {
            self.page: (1, '参数输入表'),
            self.page_2: (2, '计算结果表'),
            self.page_3: (3, '结果可视化表'),
            self.page_4: (4, '完整分析组表'),
            self.page_5: (5, '用户管理表')
        }
        
        if current in page_mapping:
            page_num, table_name = page_mapping[current]
            self.InitTableData(page_num)
            self.InforBar('刷新列表', f'{table_name}刷新成功', True)
            setattr(self, f'SearchInfo{page_num}', [False, '', ''])
            self.LabelandPivotChange()    

    def InitComboBoxAndCompleter(self):
        #根据当前页的不同，设定不同的下拉框内容
        self.mydb.connect()
        current = self.stackedWidget.currentWidget()
        self.ComboBox.clear()
        all_data=[]  
        if current == self.page:       
            self.ComboBox.addItems(['参数ID','参数名称','参数备注','用户名','参数创建时间','存放路径'])                   
            result=self.mydb.select("parametertable")              
        elif current == self.page_2:
            self.ComboBox.addItems(['参数ID','计算结果ID','计算结果名称','计算结果备注','用户名','计算结果创建时间','存放路径'])
            result=self.mydb.select("outputtable")
        elif current == self.page_3:
            self.ComboBox.addItems(['计算结果ID','可视化ID','可视化名称','可视化备注','用户名','可视化创建时间','存放路径'])
            result=self.mydb.select("visualizationtable")
        elif current == self.page_4:
            self.ComboBox.addItems(['完整分析组ID','完整分析组名称','参数ID','计算结果ID','可视化ID','存放路径'])
            result=self.mydb.select("grouptable")
        elif current == self.page_5:
            self.ComboBox.addItems(['用户名','创建时间','最后登录时间'])
            fidld=['account_name','create_time','lastlogin_time']
            result=self.mydb.select("usertable",fidld)
        self.mydb.close()
        #获取所有数据
        all_data=[str(item) for sublist in result for item in sublist]
 
        self.completer=QCompleter(all_data,self.SearchLineEdit)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setMaxVisibleItems(8)

        self.ComboBox.setCurrentIndex(-1)
        self.SearchLineEdit.setCompleter(self.completer)
        self.SearchLineEdit.setEnabled(False)

    def SearchButtonChange(self):
        self.SearchLineEdit.setEnabled(False)
        if self.ComboBox.currentIndex()>=0:
            self.SearchLineEdit.setEnabled(True)

    def SearchElement(self):      
        
        def Search(current_table,field,text):
            self.mydb.connect()
            result=self.mydb.selectlike(current_table,field,text)
            self.mydb.close()
            return result
        
        def ShowOnTable(table_widget,result):
            table_widget.clearContents()
            for i, row in enumerate(result):
                for j, data in enumerate(row):
                    table_widget.setItem(i, j, QTableWidgetItem(str(data)))
        which_table={
            1: "parametertable",
            2: "outputtable",
            3: "visualizationtable",
            4: "grouptable",
            5: "usertable"
        }
        table_1 = {
            0: "parameter_id",
            1: "parameter_name",
            2: "parameter_note",
            3: "account_name",
            4: "create_time",
            5: "parameter_path"
        }
        table_2 = {
            0: "parameter_id",
            1: "output_id",
            2: "output_name",
            3: "output_note",
            4: "account_name",
            5: "create_time",
            6: "output_path"
        }
        table_3 = {
            0: "output_id",
            1: "visualization_id",
            2: "visualization_name",
            3: "visualization_note",
            4: "account_name",
            5: "create_time",
            6: "visualization_path"
        }
        table_4 = {
            0: "group_id",
            1: "group_name",
            2: "parameter_id",
            3: "output_id",
            4: "visualization_id",
            5: "group_path"
        }
        table_5 = {
            0: "account_name",
            1: "create_time",
            2: "lastlogin_time"
        }
        if self.stackedWidget.currentWidget() == self.page:
            tablewidget=self.TableWidget
            current_table = which_table.get(1, None)
            field = table_1.get(self.ComboBox.currentIndex(), None)
        elif self.stackedWidget.currentWidget() == self.page_2:
            tablewidget=self.TableWidget_2
            current_table = which_table.get(2, None)
            field = table_2.get(self.ComboBox.currentIndex(), None)
        elif self.stackedWidget.currentWidget() == self.page_3:
            tablewidget=self.TableWidget_3
            current_table = which_table.get(3, None)
            field = table_3.get(self.ComboBox.currentIndex(), None)
        elif self.stackedWidget.currentWidget() == self.page_4:
            tablewidget=self.TableWidget_4
            current_table = which_table.get(4, None)
            field = table_4.get(self.ComboBox.currentIndex(), None)
        elif self.stackedWidget.currentWidget() == self.page_5:
            tablewidget=self.TableWidget_5
            current_table = which_table.get(5, None)
            field = table_5.get(self.ComboBox.currentIndex(), None)
        text = self.SearchLineEdit.text()
        if text == '':
            self.InforBar('搜索', '请输入搜索内容',False)
            return
        else:
            result=Search(current_table,field,text)
            if not result:
                self.InforBar('搜索', '没有找到相关数据',False)
            else:             
                self.InforBar('搜索', '搜索成功!请查看表格！',True)
            ShowOnTable(tablewidget,result)

            if self.stackedWidget.currentWidget() == self.page:
                self.SearchInfo1=[True,field,text]
            elif self.stackedWidget.currentWidget() == self.page_2:
                self.SearchInfo2=[True,field,text]
            elif self.stackedWidget.currentWidget() == self.page_3:
                self.SearchInfo3=[True,field,text]
            elif self.stackedWidget.currentWidget() == self.page_4:
                self.SearchInfo4=[True,field,text]
            elif self.stackedWidget.currentWidget() == self.page_5:
                self.SearchInfo5=[True,field,text]

            self.LabelandPivotChange()
 
    def EditElement(self):
        def edit_row(self, selected_row, table_widget, table_name,field, id_column,path_column ,rename_prefix):
            #如果已经选中了一行
            if selected_row >= 0:
                #如果该行有id
                if table_widget.item(selected_row, id_column):
                    w = ManageDialog(self)
                    w.setGeometry(self.geometry())
                    textlist = [rename_prefix + '名称', rename_prefix + '备注']
                    w.changelabel(2, textlist)
                    if w.exec():
                        old_path = table_widget.item(selected_row, path_column).text()
                        if os.path.exists(old_path):
                            new_path = os.path.join(rootpath, 'InputJSON', w.mylist[0] + '_ID为' + table_widget.item(selected_row, id_column).text() + '.json')
                            os.rename(old_path, new_path)
                            conn, cursor = self.MysqlConnect()
                            sql = f"UPDATE {table_name} SET {field}_name=?, {field}_note=?, {field}_path=? WHERE {field}_id=?"
                            val = (w.mylist[0], w.mylist[1], new_path, int(table_widget.item(selected_row, id_column).text()))
                            cursor.execute(sql, val)
                            self.InforBar('修改数据', '数据修改成功', True)
                            timer = QTimer()
                            timer.singleShot(500, lambda: self.InitTableData(0))
                            conn.commit()
                            conn.close()
                else:
                    self.InforBar('修改数据', '请先选择要修改的记录', False)
            else:
                self.InforBar('修改数据', '请先选择要修改的记录', False)

        rootpath = os.path.dirname(__file__)
        current = self.stackedWidget.currentWidget()
        selected_row = None
        table_widget = None
        table_name = None
        field = None
        id_column = None
        path_column = None
        rename_prefix = None

        if current == self.page:
            table_widget = self.TableWidget
            table_name = "parametertable"
            field="parameter"
            id_column = 0
            path_column = 5
            rename_prefix = '参数'
        elif current == self.page_2:
            table_widget = self.TableWidget_2
            table_name = "outputtable"
            field="output"
            id_column = 1
            path_column = 6
            rename_prefix = '计算结果'
        elif current == self.page_3:
            table_widget = self.TableWidget_3
            table_name = "visualizationtable"
            field="visualization"
            id_column = 1
            path_column = 6
            rename_prefix = '可视化'
        elif current == self.page_4:
            table_widget = self.TableWidget_4
            table_name = "grouptable"
            field="group"
            id_column = 0
            path_column = 5
            rename_prefix = '完整分析组'
        elif current == self.page_5:
            table_widget = self.TableWidget_5
            table_name = "usertable"
            field="user"
            id_column = 0
            rename_prefix = '用户'
        
        selected_row = table_widget.currentRow()
        edit_row(self, selected_row, table_widget, table_name, field,id_column,path_column, rename_prefix)
                             
    def DeleteElement(self):
        def delete_row( table_widget, table_name,id, id_column, row_index,path_column):
            conn, cursor = self.MysqlConnect()
            if row_index >= 0:
                if table_widget==self.TableWidget_5:
                    id_data = table_widget.item(row_index, id_column).text()
                else:
                    id_data = int(table_widget.item(row_index, id_column).text())
  
                sql = f"DELETE FROM {table_name} WHERE {id} = ?"
                cursor.execute(sql, (id_data,))
                conn.commit()
                conn.close()
                #删除文件
                if table_widget!=self.TableWidget_5:

                    path=os.path.abspath(table_widget.item(row_index, path_column).text())
                    if os.path.isfile(path):
                        # 如果是文件，直接删除
                        os.remove(path)
                    elif os.path.isdir(path):
                        # 如果是文件夹，删除空文件夹
                        shutil.rmtree(path)
                self.InforBar('删除数据', '数据删除成功', True)
                timer = QTimer()
                timer.singleShot(500, lambda: self.InitTableData(0))
                return True
            else:
                self.InforBar('删除数据', '请先选择要删除的记录', False)
                conn.close()
                return False
            
        # 定义一个字典，存储表名、表格对象和对应的游标
        table_cursor_map = {
            self.page: (self.TableWidget, "parametertable","parameter_id",0,5),
            self.page_2: (self.TableWidget_2, "outputtable","output_id",1,6),
            self.page_3: (self.TableWidget_3, "visualizationtable","visualization_id",1,6),
            self.page_4: (self.TableWidget_4, "grouptable","group_id",0,6),
            self.page_5: (self.TableWidget_5, "usertable","account_name",0,0)
        }

        current = self.stackedWidget.currentWidget()
        selected_row = None
        table_widget = None
        table_name = None
        id = None
        id_column=None
        path_column=None

        if current in table_cursor_map:
            table_widget,table_name,id,id_column,path_column = table_cursor_map[current]
            selected_row = table_widget.currentRow()

        delete_row( table_widget, table_name, id, id_column=id_column, row_index=selected_row,path_column=path_column)
                
    def OpenElement(self):
        selected_row = None
        file_path = None
        if self.stackedWidget.currentWidget() == self.page:
            selected_row = self.TableWidget.currentRow()
        elif self.stackedWidget.currentWidget() == self.page_2:
            selected_row = self.TableWidget_2.currentRow()
        elif self.stackedWidget.currentWidget() == self.page_3:
            selected_row = self.TableWidget_3.currentRow()
        elif self.stackedWidget.currentWidget() == self.page_4:
            selected_row = self.TableWidget_4.currentRow()

        if selected_row is not None and selected_row >= 0:
            if self.stackedWidget.currentWidget() == self.page:
                table_widget = self.TableWidget
                column_index = 5
            elif self.stackedWidget.currentWidget() == self.page_2:
                table_widget = self.TableWidget_2
                column_index = 6
            elif self.stackedWidget.currentWidget() == self.page_3:
                table_widget = self.TableWidget_3
                column_index = 6
            elif self.stackedWidget.currentWidget() == self.page_4:
                table_widget = self.TableWidget_4
                column_index = 6
            if table_widget.item(selected_row, 0):
                file_path = table_widget.item(selected_row, column_index).text()
            else:
                self.InforBar('打开文件', '请先选择要打开的文件', False)

        if file_path and os.path.exists(file_path):
            if table_widget == self.TableWidget_4 or table_widget == self.TableWidget_3:
                os.startfile(file_path)
            else:
                folder_path = os.path.dirname(file_path)
                os.startfile(folder_path)
            self.InforBar('打开文件', '文件夹打开成功', True)
        else:
            self.InforBar('打开文件', '请先选择要打开的文件', False)
    def ExportElement(self):
        selected_row = None
        file_path = None
        if self.stackedWidget.currentWidget() == self.page:
            selected_row = self.TableWidget.currentRow()
        elif self.stackedWidget.currentWidget() == self.page_2:
            selected_row = self.TableWidget_2.currentRow()
        elif self.stackedWidget.currentWidget() == self.page_3:
            selected_row = self.TableWidget_3.currentRow()
        elif self.stackedWidget.currentWidget() == self.page_4:
            selected_row = self.TableWidget_4.currentRow()

        if selected_row is not None and selected_row >= 0:
            if self.stackedWidget.currentWidget() == self.page:
                table_widget = self.TableWidget
                column_index = 5
            elif self.stackedWidget.currentWidget() == self.page_2:
                table_widget = self.TableWidget_2
                column_index = 6
            elif self.stackedWidget.currentWidget() == self.page_3:
                table_widget = self.TableWidget_3
                column_index = 6
            elif self.stackedWidget.currentWidget() == self.page_4:
                table_widget = self.TableWidget_4
                column_index = 6

            if table_widget.item(selected_row, 0):
                file_path = table_widget.item(selected_row, column_index).text()
            else:
                self.InforBar('导出文件', '请先选择要导出的文件', False)

        if file_path and os.path.exists(file_path):
            options = QFileDialog.Options()
            directory = QFileDialog.getExistingDirectory(self, "选择导出文件路径", "", QFileDialog.ShowDirsOnly)
            if directory:  # 检查用户是否选择了一个目录
                if os.path.isfile(file_path):
                    # 如果是文件，直接复制
                    file_name = os.path.basename(file_path)
                    export_path = os.path.join(directory, file_name)
                    shutil.copy(file_path, export_path)
                    self.InforBar('导出文件', '文件导出成功', True)
                elif os.path.isdir(file_path):
                    # 如果是目录，复制整个目录
                    folder_name = os.path.basename(file_path)
                    export_path = os.path.join(directory, folder_name)
                    # 如果目标文件夹已存在，删除旧文件夹
                    if os.path.exists(export_path):
                        shutil.rmtree(export_path)
                    shutil.copytree(file_path, export_path)
                    self.InforBar('导出文件', '文件夹导出成功', True)
                #打开目录
                os.startfile(directory)
            else:
                self.InforBar('导出文件', '没有选择导出路径', False)
        else:
            self.InforBar('导出文件', '请先选择要导出的文件', False)
          
            
    def InitButtonSignal(self):
        #pivot
        self.stackedWidget.currentChanged.connect(self.LabelandPivotChange)
        self.stackedWidget.currentChanged.connect(self.InitComboBoxAndCompleter)
        self.SearchLineEdit.searchButton.clicked.connect(self.SearchElement)
        self.PrimaryPushButton.clicked.connect(self.RefreshTable)
        self.PrimaryPushButton_2.clicked.connect(self.EditElement)
        self.PrimaryPushButton_3.clicked.connect(self.DeleteElement)
        self.PrimaryPushButton_4.clicked.connect(self.OpenElement)
        self.PrimaryPushButton_6.clicked.connect(self.ExportElement)
        self.ComboBox.currentIndexChanged.connect(self.SearchButtonChange)

    def InitPivot(self):
        
        self.Pivot.addItem(
            routeKey='page',
            text='参数输入管理',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page),
            icon=FIF.LABEL
        )
        self.Pivot.addItem(
            routeKey='page_2',
            text='计算结果管理',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_2),
            icon=FIF.DEVELOPER_TOOLS
        )
        self.Pivot.addItem(
            routeKey='page_3',
            text='结果可视化管理',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_3),
            icon=FIF.UNIT
        )    
        self.Pivot.addItem(
            routeKey='page_4',
            text='完整分析组管理',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_4),
            icon=FIF.IOT
        )
        self.Pivot.addItem(
            routeKey='page_5',
            text='用户管理',
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.page_5),
            icon=FIF.PEOPLE
        )
        self.stackedWidget.setCurrentWidget(self.page)
        self.Pivot.setCurrentItem('page')
    def LabelandPivotChange(self):
        current = self.stackedWidget.currentWidget()
        self.PrimaryPushButton_2.setEnabled(True)
        self.PrimaryPushButton_4.setEnabled(True)
        self.PrimaryPushButton_6.setEnabled(True)

        
        if current == self.page:
            self.Pivot.setCurrentItem('page')
            
            if self.SearchInfo1[0]:
                self.IconWidget_6.setIcon(FIF.SEARCH)
                self.SubtitleLabel_8.setText('搜索字段:'+self.SearchInfo1[1]+';搜索内容:'+self.SearchInfo1[2])     
            else:      
                self.IconWidget_6.setIcon(FIF.LABEL)
                self.SubtitleLabel_8.setText('参数输入表：完整展示当前所有参数输入记录')
        elif current == self.page_2:
            self.Pivot.setCurrentItem('page_2')
            if self.SearchInfo2[0]:
                self.IconWidget_6.setIcon(FIF.SEARCH)
                self.SubtitleLabel_8.setText('搜索字段:'+self.SearchInfo2[1]+';搜索内容:'+self.SearchInfo2[2])
            else:      
                self.IconWidget_6.setIcon(FIF.DEVELOPER_TOOLS)
                self.SubtitleLabel_8.setText('计算结果表：完整展示当前所有计算结果记录')
        elif current == self.page_3:
            self.Pivot.setCurrentItem('page_3')
            if self.SearchInfo3[0]:
                self.SubtitleLabel_8.setText('搜索字段:'+self.SearchInfo3[1]+';搜索内容:'+self.SearchInfo3[2])
                self.IconWidget_6.setIcon(FIF.SEARCH)     
            else:    
                self.IconWidget_6.setIcon(FIF.UNIT)
                self.SubtitleLabel_8.setText('结果可视化表：完整展示当前所有结果可视化记录')
        elif current == self.page_4:
            self.Pivot.setCurrentItem('page_4')

            if self.SearchInfo4[0]:
                self.SubtitleLabel_8.setText('搜索字段:'+self.SearchInfo4[1]+';搜索内容:'+self.SearchInfo4[2])
                self.IconWidget_6.setIcon(FIF.SEARCH)
            else:    
                self.IconWidget_6.setIcon(FIF.IOT)
                self.SubtitleLabel_8.setText('完整分析组：经过完整的 参数输入-计算结果-结果可视化 分析流程的一组数据。')
        elif current == self.page_5:
            self.Pivot.setCurrentItem('page_5')
            self.PrimaryPushButton_2.setEnabled(False)
            self.PrimaryPushButton_4.setEnabled(False)
            self.PrimaryPushButton_6.setEnabled(False)
            self.mydb.connect()
            time=self.mydb.selectmax("usertable", "lastlogin_time")
            condition={"lastlogin_time":time[0]}
            fields=["permission"]
            ismanage=self.mydb.select("usertable", fields, condition)
            self.mydb.close()
            if ismanage == '1':
                self.PrimaryPushButton.setEnabled(False)
                self.PrimaryPushButton_3.setEnabled(False)
            elif ismanage == '0':
                self.PrimaryPushButton.setEnabled(True)
                self.PrimaryPushButton_3.setEnabled(True)
            if self.SearchInfo5[0]:
                self.SubtitleLabel_8.setText('搜索字段:'+self.SearchInfo5[1]+';搜索内容:'+self.SearchInfo5[2])
                self.IconWidget_6.setIcon(FIF.SEARCH)
            else:    
                self.IconWidget_6.setIcon(FIF.PEOPLE)
                self.SubtitleLabel_8.setText('用户表：展示当前所有用户信息')
    def MysqlConnect(self):
        #连接数据库存输入记录
            path=os.path.join(self.current_dir,'Database.db')
            conn = sqlite3.connect(database=path)
            cursor = conn.cursor()
            return conn,cursor  
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
            

class ManageDialog(MessageBoxBase,ManageDialog_UI):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.viewLayout.addWidget(self.CardWidget)
        self.updata_list()
        self.LineEdit.textChanged.connect(self.updata_list)
        self.LineEdit_2.textChanged.connect(self.updata_list)
        self.LineEdit_3.textChanged.connect(self.updata_list)
        self.LineEdit_4.textChanged.connect(self.updata_list)

    def changelabel(self,index,textlist):
        if index==2:
            
            self.CardWidget.setGeometry(QtCore.QRect(10, 10, 401, 121))
            self.CardWidget.setMinimumSize(QtCore.QSize(401, 121))
            self.SubtitleLabel.setText(textlist[0])
            self.SubtitleLabel_2.setText(textlist[1])
            self.SubtitleLabel_3.setVisible(False)
            self.SubtitleLabel_4.setVisible(False)
            self.LineEdit_3.setVisible(False)
            self.LineEdit_4.setVisible(False)
        if index==3:
            
            self.CardWidget.setGeometry(QtCore.QRect(10, 10, 401, 171))
            self.CardWidget.setMinimumSize(QtCore.QSize(401, 171))
            self.SubtitleLabel.setText(textlist[0])
            self.SubtitleLabel_2.setText(textlist[1])
            self.SubtitleLabel_3.setText(textlist[2])
            self.SubtitleLabel_4.setVisible(False)
            self.LineEdit_4.setVisible(False)
        if index==4:
           
            self.CardWidget.setGeometry(QtCore.QRect(10, 10, 401, 221))
            self.CardWidget.setMinimumSize(QtCore.QSize(401, 221))
            self.SubtitleLabel.setText(textlist[0])
            self.SubtitleLabel_2.setText(textlist[1])
            self.SubtitleLabel_3.setText(textlist[2])
            self.SubtitleLabel_4.setText(textlist[3])
    def updata_list(self):
        p1=self.LineEdit.text()
        p2=self.LineEdit_2.text()
        p3=self.LineEdit_3.text()
        p4=self.LineEdit_4.text()
        self.mylist = [p1,p2,p3,p4]