#for GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo                                  
from PyQt5.QtWidgets import QFileDialog,QLabel
# from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
#from PyQt5.QtGui import QLabel
import random
import sys


from recognition_module import*


class Ui_MainWindow(object):
    """
    This class to to generate a GUI (graphical user interface)
    """
    def __init__(self):
        """
        initil them three in order to add clothes later.
        """
        self.top = []
        self.bottom = []
        self.shoes = []
        """
        initil them three in order to add clothes later.
        """
        super(Ui_MainWindow, self).__init__()

        self.top = []
        self.bottom = []
        self.shoes = []

    

        
    def ALL_PREDICT(self):
        """
        User click ADD botton to call this function, after getting a path of a photo, this function do prediction by the models and show the result in the GUI.
        """
        _translate = QtCore.QCoreApplication.translate
        files = QFileDialog.getOpenFileNames(None, "Select file", "H:/")

        for file in files[0]:
            sub, info, res_place_holder = single_classification(file)
            
            # if the result is top, then add an item to the "top" list on GUI.
            if sub == "top":
                item = QtWidgets.QListWidgetItem(info)
                self.TOP_LIST.addItem(item)
                self.top.append(res_place_holder)
            # if the result is bottom, then add an item to the "bottom" list on GUI.
            elif sub == "bottom":
                item = QtWidgets.QListWidgetItem(info)
                self.BOTTOM_LIST.addItem(item)
                self.bottom.append(res_place_holder)
            # if the result is shoes, then add an item to the "shoes" list on GUI.
            elif sub == "foot":
                item = QtWidgets.QListWidgetItem(info)
                self.SHOE_LIST.addItem(item)
                self.shoes.append(res_place_holder)
                
    def TOP_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            
            selected_items = self.TOP_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddTopButton, "EDIT","Please Edit This Top:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.TOP_LIST.takeItem(self.TOP_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.TOP_LIST.addItem(item)   
    def TOP_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.TOP_LIST.selectedItems()
            for i in selected_items:
                self.TOP_LIST.takeItem(self.TOP_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.top:
                if(i[-1] == path):
                    self.top.remove(i)
            
    ####          
    def BOTTOM_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.BOTTOM_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddBottomButton, "EDIT","Please Edit This Bottom:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.BOTTOM_LIST.takeItem(self.BOTTOM_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.BOTTOM_LIST.addItem(item)   
    def BOTTOM_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.BOTTOM_LIST.selectedItems()
            for i in selected_items:
                self.BOTTOM_LIST.takeItem(self.BOTTOM_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.bottom:
                if(i[-1] == path):
                    self.bottom.remove(i)
            
           
    def SHOE_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.SHOE_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddShoeButton, "EDIT","Please Edit This Shoes:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.SHOE_LIST.takeItem(self.SHOE_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.SHOE_LIST.addItem(item)   
    def SHOE_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.SHOE_LIST.selectedItems()
            for i in selected_items:
                self.SHOE_LIST.takeItem(self.SHOE_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.shoes:
                if(i[-1] == path):
                    self.shoes.remove(i)
    #################
#for GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo                                  
from PyQt5.QtWidgets import QFileDialog,QLabel
from PyQt5.QtGui import *
#from PyQt5.QtGui import QLabel
import random

from recognition_module import*


class Ui_MainWindow(object):
    """
    This class to to generate a GUI (graphical user interface)
    """
    def __init__(self):
        """
        initil them three in order to add clothes later.
        """
        self.top = []
        self.bottom = []
        self.shoes = []
        
    def ALL_PREDICT(self):
        """
        User click ADD botton to call this function, after getting a path of a photo, this function do prediction by the models and show the result in the GUI.
        """
        _translate = QtCore.QCoreApplication.translate
        files = QFileDialog.getOpenFileNames(None, "Select file", "H:/")

        for file in files[0]:
            sub, info, res_place_holder = single_classification(file)
            
            # if the result is top, then add an item to the "top" list on GUI.
            if sub == "top":
                item = QtWidgets.QListWidgetItem(info)
                self.TOP_LIST.addItem(item)
                self.top.append(res_place_holder)
            # if the result is bottom, then add an item to the "bottom" list on GUI.
            elif sub == "bottom":
                item = QtWidgets.QListWidgetItem(info)
                self.BOTTOM_LIST.addItem(item)
                self.bottom.append(res_place_holder)
            # if the result is shoes, then add an item to the "shoes" list on GUI.
            elif sub == "foot":
                item = QtWidgets.QListWidgetItem(info)
                self.SHOE_LIST.addItem(item)
                self.shoes.append(res_place_holder)
                
    def TOP_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            
            selected_items = self.TOP_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddTopButton, "EDIT","Please Edit This Top:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.TOP_LIST.takeItem(self.TOP_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.TOP_LIST.addItem(item)   
    def TOP_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.TOP_LIST.selectedItems()
            for i in selected_items:
                self.TOP_LIST.takeItem(self.TOP_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.top:
                if(i[-1] == path):
                    self.top.remove(i)
            
    ####          
    def BOTTOM_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.BOTTOM_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddBottomButton, "EDIT","Please Edit This Bottom:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.BOTTOM_LIST.takeItem(self.BOTTOM_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.BOTTOM_LIST.addItem(item)   
    def BOTTOM_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.BOTTOM_LIST.selectedItems()
            for i in selected_items:
                self.BOTTOM_LIST.takeItem(self.BOTTOM_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.bottom:
                if(i[-1] == path):
                    self.bottom.remove(i)
            
           
    def SHOE_LIST_EDIT(self):
            """
            User click EDIT botton to call this function to edit a prediction result.
            """
            selected_items = self.SHOE_LIST.selectedItems()
            text, okPressed = QtWidgets.QInputDialog.getText(self.AddShoeButton, "EDIT","Please Edit This Shoes:", QtWidgets.QLineEdit.Normal, selected_items[0].text())
            for i in selected_items:
                self.SHOE_LIST.takeItem(self.SHOE_LIST.row(i))
            if okPressed and text != '':
                item = QtWidgets.QListWidgetItem(text)
                self.SHOE_LIST.addItem(item)   
    def SHOE_LIST_DEL(self):
            """
            User click DELETE botton to call this function to delete a photo with prediction result.
            """
            selected_items = self.SHOE_LIST.selectedItems()
            for i in selected_items:
                self.SHOE_LIST.takeItem(self.SHOE_LIST.row(i))
            text = selected_items[0].text()
            
            path = text.split(", ")[-1]
            for i in self.shoes:
                if(i[-1] == path):
                    self.shoes.remove(i)
    #################
    def Generate(self):
        toseason = 'spring'  # Define the season here
        for i in range(2):  # Loop three times to generate three recommendations
            top_right_season = [i for i in self.top if i[3] == toseason ]
            if top_right_season != []:
                ad_top = top_right_season[np.random.randint(len(top_right_season))]
            else:
                ad_top = self.top[np.random.randint(len(self.top))]   
            helper_bot = [i for i in self.bottom if i[4] == ad_top[4] ]
            helper_sho = [i for i in self.shoes if i[4] == ad_top[4] ]
            if helper_bot==[]:
                ad_bot = self.bottom[np.random.randint(len(self.bottom))]
            else:
                bot_right_season = [i for i in helper_bot if i[3] == toseason]
                
                if bot_right_season != []:
                    ad_bot = bot_right_season[np.random.randint(len(bot_right_season))]
                else:
                    ad_bot = helper_bot[np.random.randint(len(helper_bot))]   
            if helper_sho==[]:
                ad_sho = self.shoes[np.random.randint(len(self.shoes))]
            else:
                sho_right_season = [i for i in helper_sho if i[3] == toseason]
                
                if sho_right_season != []:
                    ad_sho = sho_right_season[np.random.randint(len(sho_right_season))]
                else:
                    ad_sho = helper_sho[np.random.randint(len(helper_sho))]
                    
            if i == 0:
                self.listWidget_1.setPixmap(QtGui.QPixmap(ad_top[-1]).scaled(341,300))
                self.listWidget_2.setPixmap(QtGui.QPixmap(ad_bot[-1]).scaled(341,300))
                self.listWidget_3.setPixmap(QtGui.QPixmap(ad_sho[-1]).scaled(341,300))
            elif i == 1:
                self.listWidget_4.setPixmap(QtGui.QPixmap(ad_top[-1]).scaled(341,300))
                self.listWidget_5.setPixmap(QtGui.QPixmap(ad_bot[-1]).scaled(341,300))
                self.listWidget_6.setPixmap(QtGui.QPixmap(ad_sho[-1]).scaled(341,300))
            # elif i == 2:
            #     self.listWidget_7.setPixmap(QtGui.QPixmap(ad_top[-1]).scaled(341,300))
            #     self.listWidget_8.setPixmap(QtGui.QPixmap(ad_bot[-1]).scaled(341,300))
            #     self.listWidget_9.setPixmap(QtGui.QPixmap(ad_sho[-1]).scaled(341,300))
    #####################################################################################

    # The below are the appearance settings of the GUI
    
    def setupUi(self, MainWindow):
        """
        Add items into GUI.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))  # Set the label size to match the window
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\Project\PAHIRAN\Artboard 6.png"))  # Set the path to your image file
        self.label.setScaledContents(True)  # Scale the image to fit the label
        self.TOP_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.TOP_LIST.setGeometry(QtCore.QRect(150, 70, 341, 181))
        self.TOP_LIST.setObjectName("TOP_LIST")
        self.AddTopButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddTopButton.setGeometry(QtCore.QRect(150, 250, 171, 41))
        self.AddTopButton.setAutoFillBackground(False)
        self.AddTopButton.setCheckable(False)
        self.AddTopButton.setObjectName("AddTopButton")
        self.DeleteTopButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteTopButton.setGeometry(QtCore.QRect(320, 250, 171, 41))
        self.DeleteTopButton.setCheckable(False)
        self.DeleteTopButton.setChecked(False)
        self.DeleteTopButton.setObjectName("DeleteTopButton")
        self.AddBottomButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddBottomButton.setGeometry(QtCore.QRect(550, 250, 171, 41))
        self.AddBottomButton.setObjectName("AddBottomButton")
        self.BOTTOM_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.BOTTOM_LIST.setGeometry(QtCore.QRect(550, 70, 341, 181))
        self.BOTTOM_LIST.setObjectName("BOTTOM_LIST")
        self.DeleteBottomButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBottomButton.setGeometry(QtCore.QRect(720, 250, 171, 41))
        self.DeleteBottomButton.setObjectName("DeleteBottomButton")
        self.AddShoeButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddShoeButton.setGeometry(QtCore.QRect(950, 250, 171, 41))
        self.AddShoeButton.setObjectName("AddShoeButton")
        self.SHOE_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.SHOE_LIST.setGeometry(QtCore.QRect(950, 70, 341, 181))
        self.SHOE_LIST.setObjectName("SHOE_LIST")
        self.DeleteShoeButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteShoeButton.setGeometry(QtCore.QRect(1120, 250, 171, 41))
        self.DeleteShoeButton.setObjectName("DeleteShoeButton")
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(1450, 925, 431, 81))
        self.GenerateButton.setObjectName("GenerateButton")
        self.HistoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.HistoryButton.setGeometry(QtCore.QRect(1450, 825, 431, 81))
        self.HistoryButton.setObjectName("HistoryButton")
        self.TopLabel = QtWidgets.QLabel(self.centralwidget)
        self.TopLabel.setGeometry(QtCore.QRect(150, 50, 341, 21))
        self.TopLabel.setTextFormat(QtCore.Qt.RichText)
        self.TopLabel.setObjectName("TopLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 50, 341, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 50, 341, 21))
        self.label_2.setObjectName("label_2")
        
        self.listWidget_1 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(150, 370, 341, 300))
        self.listWidget_1.setObjectName("listWidget_1")
        self.listWidget_1.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        self.listWidget_2 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(550, 370, 341, 300))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        self.listWidget_3 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(950, 370, 341, 300))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        self.listWidget_4 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(150, 700, 341, 300))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_4.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        self.listWidget_5 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(550, 700, 341, 300))
        self.listWidget_5.setObjectName("listWidget_5")
        self.listWidget_5.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        self.listWidget_6 = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_6.setGeometry(QtCore.QRect(950, 700, 341, 300))
        self.listWidget_6.setObjectName("listWidget_6")
        self.listWidget_6.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        # self.listWidget_7 = QtWidgets.QLabel(self.centralwidget)
        # self.listWidget_7.setGeometry(QtCore.QRect(150, 1050, 341, 300))
        # self.listWidget_7.setObjectName("listWidget_7")
        # self.listWidget_7.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        # self.listWidget_8 = QtWidgets.QLabel(self.centralwidget)
        # self.listWidget_8.setGeometry(QtCore.QRect(550, 1050, 341, 300))
        # self.listWidget_8.setObjectName("listWidget_8")
        # self.listWidget_8.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        # self.listWidget_9 = QtWidgets.QLabel(self.centralwidget)
        # self.listWidget_9.setGeometry(QtCore.QRect(950, 1050, 341, 300))
        # self.listWidget_9.setObjectName("listWidget_9")
        # self.listWidget_9.setPixmap(QtGui.QPixmap("/Users/pingkefan/Desktop/top_question.png").scaled(281,300))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #####################################################################################
        
        # Establish a connection between buttons and functions
        self.AddTopButton.clicked.connect(self.TOP_LIST_EDIT)
        self.DeleteTopButton.clicked.connect(self.TOP_LIST_DEL)
        
        self.AddBottomButton.clicked.connect(self.BOTTOM_LIST_EDIT)
        self.DeleteBottomButton.clicked.connect(self.BOTTOM_LIST_DEL)
        
        self.AddShoeButton.clicked.connect(self.SHOE_LIST_EDIT)
        self.DeleteShoeButton.clicked.connect(self.SHOE_LIST_DEL)
        self.HistoryButton.clicked.connect(self.ALL_PREDICT)            
        self.GenerateButton.clicked.connect(self.Generate)              
        
        #####################################################################################

    def retranslateUi(self, MainWindow):
        """
        This function translate the item on GUI from what computer can understand to what we can understand. (Gives items names)
        """
        _translate = QtCore.QCoreApplication.translate
        logo_path = 'D:\Project\PAHIRAN\pahiran icons -01.png'
        logo =QIcon(logo_path)
        MainWindow.setWindowIcon(logo)
        
        # # Create a QLabel widget to display the logo
        # logo_label = QLabel(MainWindow)
        # pixmap = QPixmap(logo_path).scaled(175, 175)  # Set the size to 100x100
        # logo_label.setPixmap(pixmap)
        # logo_label.setGeometry(1730, 25, 175, 175)  # Set the position and size of the label
        # logo_label.show()
        
        MainWindow.setWindowTitle(_translate("MainWindow", "PAHIRAN"))
        self.AddTopButton.setText(_translate("MainWindow", "EDIT"))
        self.DeleteTopButton.setText(_translate("MainWindow", "DELETE"))
        self.AddBottomButton.setText(_translate("MainWindow", "EDIT "))
        self.DeleteBottomButton.setText(_translate("MainWindow", "DELETE"))
        self.AddShoeButton.setText(_translate("MainWindow", "EDIT "))
        self.DeleteShoeButton.setText(_translate("MainWindow", "DELETE"))
        self.GenerateButton.setText(_translate("MainWindow", "Generate Today\'s Outfit Recommendation"))
        self.HistoryButton.setText(_translate("MainWindow", "ADD A PHOTO"))
        self.TopLabel.setText(_translate("MainWindow", "TOP"))
        self.label.setText(_translate("MainWindow", "BOTTOM"))
        self.label_2.setText(_translate("MainWindow", "SHOES"))
import sys        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())           

def run_ui():
    

    # This part is to run the GUI we defined above and for some basic settings about the GUI, such as color, style, etc.

    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('fusion'))
    # MainWindow = QtWidgets.QMainWindow()
    # MainWindow.setStyleSheet("color: white;"
    #                          "selection-background-color: peru;"
    #                          "selection-color: white;"
    #                          "background-color: saddlebrown;")
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('fusion'))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet("background-color: aubergine;")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

# Set the button background color to white and text color to black
    ui.GenerateButton.setStyleSheet("background-color: white; color: black;")
    ui.HistoryButton.setStyleSheet("background-color: Turquoise; color: black;")
    ui.TOP_LIST.setStyleSheet("background-color: white; color: black;")
    ui.BOTTOM_LIST.setStyleSheet("background-color: white; color: black;")
    ui.SHOE_LIST.setStyleSheet("background-color: white; color: black;")
    ui.AddTopButton.setStyleSheet("background-color: white; color: black;")
    ui.AddBottomButton.setStyleSheet("background-color: white; color: black;")
    ui.AddShoeButton.setStyleSheet("background-color: white; color: black;")
    ui.DeleteTopButton.setStyleSheet("background-color: white; color: black;")
    ui.DeleteBottomButton.setStyleSheet("background-color: white; color: black;")
    ui.DeleteShoeButton.setStyleSheet("background-color: white; color: black;")
    ui.label.setStyleSheet("background-color: Turquoise; color: black;")
    ui.label_2.setStyleSheet("background-color: Turquoise; color: black;")
    ui.TopLabel.setStyleSheet("background-color: Turquoise; color: black;")
    ui.listWidget_1.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    ui.listWidget_2.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    ui.listWidget_3.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    ui.listWidget_4.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    ui.listWidget_5.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    ui.listWidget_6.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    # ui.listWidget_7.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    # ui.listWidget_8.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    # ui.listWidget_9.setStyleSheet("background-color: rgba(255, 255, 255, 50);")
    MainWindow.show()
    sys.exit(app.exec_())