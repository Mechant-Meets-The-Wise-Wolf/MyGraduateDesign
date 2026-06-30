from UI_Input_dialog import (Input_First_1_dialog_UI,Input_First_2_dialog_UI,Input_First_3_dialog_UI,
                             Input_First_4_dialog_UI,Input_Second_1_dialog_UI,Input_Second_2_dialog_UI,
                             Input_Second_3_dialog_UI,Input_Third_1_dialog_UI,Input_Third_2_dialog_UI,
                             Input_Fourth_1_dialog_UI,Input_Fourth_2_dialog_UI,save_dialog_UI)
from qfluentwidgets import MessageBoxBase

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