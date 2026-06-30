
from PyQt5 import QtCore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from scipy.interpolate import griddata
from matplotlib.ticker import MaxNLocator
import numpy as np
import json,os

#self.xy_1_1至self.xy_7_3分别为曲线图1至曲线图7的三条曲线x、y坐标数据
#self.info_1至self.info_7分别为曲线图1至曲线图7的图例名称、x轴单位、y轴单位
#self.ax1至self.ax7分别为曲线图1至曲线图7的matplotlib.axes.Axes对象，用来调用self.ax.plot()绘制曲线


def create_canvas(self):
#曲线一
        self.figure1,self.ax1=plt.subplots()
        self.figure1.set_tight_layout(True)
        self.canvas1 = FigureCanvas(self.figure1)
        #嵌入到它对应的frame中
        self.canvas1.setParent(self.frame_2) 
        self.canvas1.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar1 = NavigationToolbar(self.canvas1, self.frame)     
        self.toolbar1.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar1.setObjectName("曲线1工具栏")
#曲线二
        self.figure2,self.ax2=plt.subplots()
        self.figure2.set_tight_layout(True)
        self.canvas2 = FigureCanvas(self.figure2)
        #嵌入到它对应的frame中
        self.canvas2.setParent(self.frame_4) 
        self.canvas2.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar2 = NavigationToolbar(self.canvas2, self.frame_3)
        self.toolbar2.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar2.setObjectName("曲线2工具栏")
#曲线三
        self.figure3,self.ax3=plt.subplots()
        self.figure3.set_tight_layout(True)
        self.canvas3 = FigureCanvas(self.figure3)
        #嵌入到它对应的frame中
        self.canvas3.setParent(self.frame_6) 
        self.canvas3.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar3 = NavigationToolbar(self.canvas3, self.frame_5)
        self.toolbar3.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar3.setObjectName("曲线3工具栏")
#曲线四
        self.figure4,self.ax4=plt.subplots()
        self.figure4.set_tight_layout(True)
        self.canvas4 = FigureCanvas(self.figure4)
        #嵌入到它对应的frame中
        self.canvas4.setParent(self.frame_8) 
        self.canvas4.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar4 = NavigationToolbar(self.canvas4, self.frame_7)
        self.toolbar4.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar4.setObjectName("曲线4工具栏")
#曲线五
        self.figure5,self.ax5=plt.subplots()
        self.figure5.set_tight_layout(True)
        self.canvas5 = FigureCanvas(self.figure5)
        #嵌入到它对应的frame中
        self.canvas5.setParent(self.frame_10) 
        self.canvas5.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar5 = NavigationToolbar(self.canvas5, self.frame_9)
        self.toolbar5.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar5.setObjectName("曲线5工具栏")
#曲线六
        self.figure6,self.ax6=plt.subplots()
        self.figure6.set_tight_layout(True)
        self.canvas6 = FigureCanvas(self.figure6)
        #嵌入到它对应的frame中
        self.canvas6.setParent(self.frame_12) 
        self.canvas6.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar6 = NavigationToolbar(self.canvas6, self.frame_11)
        self.toolbar6.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar6.setObjectName("曲线6工具栏")
#曲线七
        self.figure7,self.ax7=plt.subplots()
        self.figure7.set_tight_layout(True)
        self.canvas7 = FigureCanvas(self.figure7)
        #嵌入到它对应的frame中
        self.canvas7.setParent(self.frame_14) 
        self.canvas7.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar7 = NavigationToolbar(self.canvas7, self.frame_13)
        self.toolbar7.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar7.setObjectName("曲线7工具栏")
#极坐标图八
        self.figure8,self.ax8=plt.subplots(subplot_kw=dict(polar=True))
        self.figure8.set_tight_layout(True)
        self.canvas8 = FigureCanvas(self.figure8)
        #嵌入到它对应的frame中
        self.canvas8.setParent(self.frame_16) 
        self.canvas8.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar8 = NavigationToolbar(self.canvas8, self.frame_15)
        self.toolbar8.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar8.setObjectName("极坐标图工具栏")
#场图九
        self.figure9,self.ax9=plt.subplots()
        self.figure9.set_tight_layout(True)
        self.canvas9 = FigureCanvas(self.figure9)
        #嵌入到它对应的frame中
        self.canvas9.setParent(self.frame_18) 
        self.canvas9.setGeometry(QtCore.QRect(0, 0, 1201, 721))
        #创建 Matplotlib 的工具栏，可以直接嵌入frame中
        self.toolbar9 = NavigationToolbar(self.canvas9, self.frame_17)
        self.toolbar9.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.toolbar9.setObjectName("场图工具栏")

def init_data(self,datapath=str):

        #self.xy_1_1至self.xy_7_3分别为曲线图1至曲线图7的三条曲线x、y坐标数据
        #self.info_1至self.info_7分别为曲线图1至曲线图7的图例名称、x轴单位、y轴单位

        with open(datapath, 'r', encoding='utf-8') as f:
            origin_data = json.load(f)
        self.xy_1_1=[]
        self.xy_1_2=[]
        self.xy_1_3=[]

        self.xy_2_1=[]
        self.xy_2_2=[]
        self.xy_2_3=[]

        self.xy_3_1=[]
        self.xy_3_2=[]
        self.xy_3_3=[]

        self.xy_4_1=[]
        self.xy_4_2=[]
        self.xy_4_3=[]

        self.xy_5_1=[]
        self.xy_5_2=[]
        self.xy_5_3=[]

        self.xy_6_1=[]
        self.xy_6_2=[]
        self.xy_6_3=[]

        self.xy_7_1=[]
        self.xy_7_2=[]
        self.xy_7_3=[]

        self.theta=[]
        self.radius=[]
        self.temp=[]

        self.theta2=[]
        self.radius2=[]
        self.force=[]
        if not origin_data.get('活塞环组最小油膜厚度曲线'):
                return False
        else:
                for element in origin_data['活塞环组最小油膜厚度曲线']:
                        self.xy_1_1.append([element['x1'], element['y1']])
                        self.xy_1_2.append([element['x2'], element['y2']])
                        self.xy_1_3.append([element['x3'], element['y3']])
                for element in origin_data['活塞环组油膜承载力曲线']:
                        self.xy_2_1.append([element['x1'], element['y1']])
                        self.xy_2_2.append([element['x2'], element['y2']])
                        self.xy_2_3.append([element['x3'], element['y3']])
                for element in origin_data['活塞环组微凸体承载力曲线']:
                        self.xy_3_1.append([element['x1'], element['y1']])
                        self.xy_3_2.append([element['x2'], element['y2']])
                        self.xy_3_3.append([element['x3'], element['y3']])
                for element in origin_data['活塞环组润滑油膜剪切力曲线']:
                        self.xy_4_1.append([element['x1'], element['y1']])
                        self.xy_4_2.append([element['x2'], element['y2']])
                        self.xy_4_3.append([element['x3'], element['y3']])
                for element in origin_data['活塞环组微凸体摩擦力曲线']:
                        self.xy_5_1.append([element['x1'], element['y1']])
                        self.xy_5_2.append([element['x2'], element['y2']])
                        self.xy_5_3.append([element['x3'], element['y3']])
                for element in origin_data['活塞环组总摩擦力曲线']:
                        self.xy_6_1.append([element['x1'], element['y1']])
                        self.xy_6_2.append([element['x2'], element['y2']])
                        self.xy_6_3.append([element['x3'], element['y3']])
                for element in origin_data['活塞环组瞬时摩擦损失功率曲线']:
                        self.xy_7_1.append([element['x1'], element['y1']])
                        self.xy_7_2.append([element['x2'], element['y2']])
                        self.xy_7_3.append([element['x3'], element['y3']])
                for element in origin_data['温度分布图']:
                        self.theta.append(element['theta'])
                        self.radius.append(element['radius'])
                        self.temp.append(element['temp'])
                for element in origin_data['油膜压力分布图']:
                        self.theta2.append(element['周向坐标(rad)'])
                        self.radius2.append(element['无量纲轴向坐标'])
                        self.force.append(element['油膜压力(MPa)'])
                
                keys_list = list(origin_data.keys())
                self.info_1=['','','']
                self.info_2=['','','']
                self.info_3=['','','']
                self.info_4=['','','']
                self.info_5=['','','']
                self.info_6=['','','']
                self.info_7=['','','']
                self.info_1[0]=keys_list[0]
                self.info_1[1]=origin_data['活塞环组最小油膜厚度曲线'][0]['x_unit']
                self.info_1[2]=origin_data['活塞环组最小油膜厚度曲线'][0]['y_unit']

                self.info_2[0]=keys_list[1]
                self.info_2[1]=origin_data['活塞环组油膜承载力曲线'][0]['x_unit']
                self.info_2[2]=origin_data['活塞环组油膜承载力曲线'][0]['y_unit']

                self.info_3[0]=keys_list[2]
                self.info_3[1]=origin_data['活塞环组微凸体承载力曲线'][0]['x_unit']
                self.info_3[2]=origin_data['活塞环组微凸体承载力曲线'][0]['y_unit']
                
                self.info_4[0]=keys_list[3]
                self.info_4[1]=origin_data['活塞环组润滑油膜剪切力曲线'][0]['x_unit']
                self.info_4[2]=origin_data['活塞环组润滑油膜剪切力曲线'][0]['y_unit']
                
                self.info_5[0]=keys_list[4]
                self.info_5[1]=origin_data['活塞环组微凸体摩擦力曲线'][0]['x_unit']
                self.info_5[2]=origin_data['活塞环组微凸体摩擦力曲线'][0]['y_unit']
                
                self.info_6[0]=keys_list[5]
                self.info_6[1]=origin_data['活塞环组总摩擦力曲线'][0]['x_unit']
                self.info_6[2]=origin_data['活塞环组总摩擦力曲线'][0]['y_unit']

                self.info_7[0]=keys_list[6]
                self.info_7[1]=origin_data['活塞环组瞬时摩擦损失功率曲线'][0]['x_unit']
                self.info_7[2]=origin_data['活塞环组瞬时摩擦损失功率曲线'][0]['y_unit']

                return True

def plot_data(self):
        #曲线一
        self.ax1.clear()
        x_1_1 = [row[0] for row in self.xy_1_1]
        y_1_1 = [row[1] for row in self.xy_1_1]       
        self.ax1.plot(x_1_1, y_1_1, label='第一道活塞环最小油膜厚度')
        x_1_2= [row[0] for row in self.xy_1_2]
        y_1_2= [row[1] for row in self.xy_1_2]
        self.ax1.plot(x_1_2, y_1_2, label='第二道活塞环最小油膜厚度')
        x_1_3= [row[0] for row in self.xy_1_3]
        y_1_3= [row[1] for row in self.xy_1_3]
        self.ax1.plot(x_1_3, y_1_3, label='第三道活塞环最小油膜厚度')
        self.ax1.set_title(self.info_1[0])
        self.ax1.set_xlabel(self.info_1[1])
        self.ax1.set_ylabel(self.info_1[2])  
        self.ax1.legend()
        #曲线二
        self.ax2.clear()
        x_2_1 = [row[0] for row in self.xy_2_1]
        y_2_1 = [row[1] for row in self.xy_2_1]       
        self.ax2.plot(x_2_1, y_2_1, label='第一道活塞环油膜承载力')
        x_2_2= [row[0] for row in self.xy_2_2]
        y_2_2= [row[1] for row in self.xy_2_2]
        self.ax2.plot(x_2_2, y_2_2, label='第二道活塞环油膜承载力')
        x_2_3= [row[0] for row in self.xy_2_3]
        y_2_3= [row[1] for row in self.xy_2_3]
        self.ax2.plot(x_2_3, y_2_3, label='第三道活塞环油膜承载力')
        self.ax2.set_title(self.info_2[0])
        self.ax2.set_xlabel(self.info_2[1])
        self.ax2.set_ylabel(self.info_2[2])  
        self.ax2.legend()
        #曲线三
        self.ax3.clear()
        x_3_1 = [row[0] for row in self.xy_3_1]
        y_3_1 = [row[1] for row in self.xy_3_1]       
        self.ax3.plot(x_3_1, y_3_1, label='第一道活塞环微凸体承载力')
        x_3_2= [row[0] for row in self.xy_3_2]
        y_3_2= [row[1] for row in self.xy_3_2]
        self.ax3.plot(x_3_2, y_3_2, label='第二道活塞环微凸体承载力')
        x_3_3= [row[0] for row in self.xy_3_3]
        y_3_3= [row[1] for row in self.xy_3_3]
        self.ax3.plot(x_3_3, y_3_3, label='第三道活塞环微凸体承载力')
        self.ax3.set_title(self.info_3[0])
        self.ax3.set_xlabel(self.info_3[1])
        self.ax3.set_ylabel(self.info_3[2])  
        self.ax3.legend()
        #曲线四
        self.ax4.clear()
        x_4_1 = [row[0] for row in self.xy_4_1]
        y_4_1 = [row[1] for row in self.xy_4_1]       
        self.ax4.plot(x_4_1, y_4_1, label='第一道活塞环润滑油膜剪切力')
        x_4_2= [row[0] for row in self.xy_4_2]
        y_4_2= [row[1] for row in self.xy_4_2]
        self.ax4.plot(x_4_2, y_4_2, label='第二道活塞环润滑油膜剪切力')
        x_4_3= [row[0] for row in self.xy_4_3]
        y_4_3= [row[1] for row in self.xy_4_3]
        self.ax4.plot(x_4_3, y_4_3, label='第三道活塞环润滑油膜剪切力')
        self.ax4.set_title(self.info_4[0])
        self.ax4.set_xlabel(self.info_4[1])
        self.ax4.set_ylabel(self.info_4[2])  
        self.ax4.legend()
        #曲线五
        self.ax5.clear()
        x_5_1 = [row[0] for row in self.xy_5_1]
        y_5_1 = [row[1] for row in self.xy_5_1]       
        self.ax5.plot(x_5_1, y_5_1, label='第一道活塞环微凸体摩擦力')
        x_5_2= [row[0] for row in self.xy_5_2]
        y_5_2= [row[1] for row in self.xy_5_2]
        self.ax5.plot(x_5_2, y_5_2, label='第二道活塞环微凸体摩擦力')
        x_5_3= [row[0] for row in self.xy_5_3]
        y_5_3= [row[1] for row in self.xy_5_3]
        self.ax5.plot(x_5_3, y_5_3, label='第三道活塞环微凸体摩擦力')
        self.ax5.set_title(self.info_5[0])
        self.ax5.set_xlabel(self.info_5[1])
        self.ax5.set_ylabel(self.info_5[2])  
        self.ax5.legend()
        #曲线六
        self.ax6.clear()
        x_6_1 = [row[0] for row in self.xy_6_1]
        y_6_1 = [row[1] for row in self.xy_6_1]       
        self.ax6.plot(x_6_1, y_6_1, label='第一道活塞环总摩擦力')
        x_6_2= [row[0] for row in self.xy_6_2]
        y_6_2= [row[1] for row in self.xy_6_2]
        self.ax6.plot(x_6_2, y_6_2, label='第二道活塞环总摩擦力')
        x_6_3= [row[0] for row in self.xy_6_3]
        y_6_3= [row[1] for row in self.xy_6_3]
        self.ax6.plot(x_6_3, y_6_3, label='第三道活塞环总摩擦力')
        self.ax6.set_title(self.info_6[0])
        self.ax6.set_xlabel(self.info_6[1])
        self.ax6.set_ylabel(self.info_6[2])  
        self.ax6.legend()
        #曲线七
        self.ax7.clear()
        x_7_1 = [row[0] for row in self.xy_7_1]
        y_7_1 = [row[1] for row in self.xy_7_1]
        self.ax7.plot(x_7_1, y_7_1, label='第一道活塞环瞬时摩擦损失功率')
        x_7_2= [row[0] for row in self.xy_7_2]
        y_7_2= [row[1] for row in self.xy_7_2]
        self.ax7.plot(x_7_2, y_7_2, label='第二道活塞环瞬时摩擦损失功率')
        x_7_3= [row[0] for row in self.xy_7_3]
        y_7_3= [row[1] for row in self.xy_7_3]
        self.ax7.plot(x_7_3, y_7_3, label='第三道活塞环瞬时摩擦损失功率')
        self.ax7.set_title(self.info_7[0])
        self.ax7.set_xlabel(self.info_7[1])
        self.ax7.set_ylabel(self.info_7[2])  
        self.ax7.legend()
        #极坐标图八

        self.ax8.clear()
        # 定义要在雷达图中插值的网格
        theta_grid, radius_grid = np.meshgrid(np.linspace(0, 2*np.pi, 1000), np.linspace(0, max(self.radius), 100))
        # 进行温度数据的插值
        temp_interp = griddata((self.theta, self.radius), self.temp, (theta_grid, radius_grid), method='cubic')
        # 绘制雷达图
        contour=self.ax8.contourf(theta_grid, radius_grid, temp_interp, cmap='jet', levels=100)
        self.ax8.yaxis.set_major_locator(MaxNLocator(3))  # 设置为想要的刻度线数量
        self.figure8.colorbar(contour, ax=self.ax8,label='温度（°C）')
        self.ax8.set_title('温度分布图')
        
        #油膜压力图
        self.ax9.clear()
        # 定义要在雷达图中插值的网格
        theta_grid, radius_grid = np.meshgrid(np.linspace(0, 2*np.pi, 100), np.linspace(0, max(self.radius2), 100))
        # 进行压力数据的插值
        temp_interp = griddata((self.theta2, self.radius2), self.force, (theta_grid, radius_grid), method='cubic')
        # 绘制雷达图
        contour2=self.ax9.contourf(theta_grid, radius_grid, temp_interp, cmap='jet', levels=1000)
        self.ax9.yaxis.set_major_locator(MaxNLocator(3))  # 设置为想要的刻度线数量
        self.ax9.set_title('油膜压力分布图')
        self.ax9.set_xlabel('周向坐标（rad）')
        self.ax9.set_ylabel('无量纲轴向坐标')  
        self.figure9.colorbar(contour2, ax=self.ax9,label='油膜压力（MPa）')
        self.ax9.legend()

def clear_plot(self):
        self.ax1.clear()   
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        self.ax5.clear()
        self.ax6.clear()
        self.ax7.clear()
        self.ax8.clear()
        self.ax9.clear()
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()
        self.canvas4.draw()
        self.canvas5.draw()
        self.canvas6.draw()
        self.canvas7.draw()
        self.canvas8.draw()
        self.canvas9.draw()

def save_figure(self, folder_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        save_dir = os.path.join(current_dir,'Figure', folder_name)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_name = '活塞环组最小油膜厚度曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure1.savefig(file_path)
        file_name = '活塞环组油膜承载力曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure2.savefig(file_path)
        file_name = '活塞环组微凸体承载力曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure3.savefig(file_path)
        file_name = '活塞环组润滑油膜剪切力曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure4.savefig(file_path)
        file_name = '活塞环组微凸体摩擦力曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure5.savefig(file_path)
        file_name = '活塞环组总摩擦力曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure6.savefig(file_path)
        file_name = '活塞环组瞬时摩擦损失功率曲线.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure7.savefig(file_path)
        file_name='温度分布图.png'
        file_path=os.path.join(save_dir, file_name)
        self.figure8.savefig(file_path)
        file_name = '油膜压力分布图.png'
        file_path = os.path.join(save_dir, file_name)
        self.figure9.savefig(file_path)