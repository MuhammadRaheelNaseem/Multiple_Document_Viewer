from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    # initialize count
    count = 0
    def __init__(self):
        super().__init__()
        #set title for main windows
        self.setWindowTitle("Multiple Document Interface")
        #create container area
        self.wn = QMdiArea()
        #set central widget with mdi container
        self.setCentralWidget(self.wn)
        #create menubar
        bar = self.menuBar()
        #create file menu on menubar
        file = bar.addMenu("File")
        #create new menu
        newAction = QAction("New",self)
        file.addAction(newAction)
        #connect trigger action for new menu
        newAction.triggered.connect(self.new_subwindow)
        #add title menu
        tiledAction = QAction("Tile",self)
        file.addAction(tiledAction)
        #connect triggered action for tiled menu
        tiledAction.triggered.connect(self.tiled_window)
        
    def new_subwindow(self):
        #increament count
        MainWindow.count+=1
        #create sub window
        sub_window = QMdiSubWindow()
        #set textedit widget on subwindow
        sub_window.setWidget(QTextEdit())
        #set title for sub window
        sub_window.setWindowTitle("Sub Window"+str(MainWindow.count))
        #add sub window on container area
        self.wn.addSubWindow(sub_window)
        #show sub window
        sub_window.show()
    
    def tiled_window(self):
        #expand all created subwindow
        #to fill up the mdi container
        self.wn.tileSubWindows()
        
app = QApplication(sys.argv)
wn = MainWindow()
wn.show()
app.exec()
