from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QFileDialog

# from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie,QColor
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
import sys
import boto3

class MyWindows(QMainWindow):
    def __init__(self):
        super(MyWindows,self).__init__()
        self.setGeometry(0,0,3000,3000)
        self.setWindowTitle("MAT")
        self.setStyleSheet("background-color: black;")
        self.UI()
    def UI(self):
        label = QLabel(self)
        label.setAlignment(Qt.AlignCenter)
        label.setMinimumSize(1000, 1000)
            # Load the GIF using QMovie
        movie = QMovie("bg.gif")

            # Set the QLabel's background pixmap to the GIF's frames
        label.setMovie(movie)
        movie.start()

            # Set the central widget of the main window to the QLabel
        self.setCentralWidget(label)

        self.label=QtWidgets.QLabel(self)
        self.label.setText('Enter')
        self.label.move(850,900)
        self.label.setStyleSheet('font-size: 30px;'
                                  'color : white;')

        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("INPUT")
        self.b1.clicked.connect(self.click1)
        self.b1.setGeometry(1200,340,200,60)
        self.b1.setStyleSheet('''
                QPushButton {
                    border-radius: 5px;
                    background-color: #FFD95A;
                    color: black;
                    font-size: 20px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background-color: #FEFF86;
                }
                QPushButton:pressed {
                    background-color: #FEFF86;
                }
                ''')
        
        
        self.b2=QtWidgets.QPushButton(self)
        self.b2.setText("ANALYSIS")
        self.b2.clicked.connect(self.click2)

        self.b2.setGeometry(1200,500,200,60)
        self.b2.setStyleSheet('''
                QPushButton {
                    border-radius: 5px;
                    background-color: #F99B7D;
                    color: black;
                    font-size: 20px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background-color:  #F6C391;
                }
                QPushButton:pressed {
                    background-color: #F6C391;
                }
                ''')
    
        self.b3=QtWidgets.QPushButton(self)
        self.b3.setText("RESULT")
        self.b3.clicked.connect(self.click3)
        self.b3.setGeometry(1200,660,200,60)
        self.b3.setStyleSheet('''
                QPushButton {
                    border-radius: 5px;
                    background-color: #4CAF50;
                    color: black;
                    font-size: 20px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background-color: #3e8e41;
                }
                QPushButton:pressed {
                    background-color: #2e6223;
                }
                ''')

    def click1(self):
        self.label.setText("INPUT IS TAKEN")
        self.update()
        self.insertFile()
    def click2(self):
        self.label.setText("ANALYSING")
        self.update() 
    def click3(self):
        self.label.setText("RESULT")
        self.update()
    def update(self):
        self.label.adjustSize()
    def insertFile(self):
       
        # Open a file dialog box to allow the user to select a file
        global file_path,file_name
        file_dialog = QFileDialog(self)
        # set the accept mode to accept any file type
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)

        # show the dialog
        if file_dialog.exec_() == QFileDialog.Accepted:
            # get the selected file path
            file_path = file_dialog.selectedFiles()[0]
            file_name= file_path.split("/")[-1]
            self.aws(file_path,file_name)
    
    def aws(self,file_path,file_name):
         aws_access_key_id = 'AKIA25KEWWDMZSEDZ7GJ'
         aws_secret_access_key = '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'

         s3 = boto3.client('s3', aws_access_key_id = 'AKIA25KEWWDMZSEDZ7GJ',aws_secret_access_key = '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')
         response = s3.list_buckets()
         buckets = [bucket['Name'] for bucket in response['Buckets']]
         print("Bucket List: ", buckets)

         bucket_name = buckets[0]
         # print(file_path)
         file_path1=file_path
         file_name1=file_name
         
         with open(file_path1, 'rb') as f:
            s3.put_object(Bucket=bucket_name, Key=file_name1, Body=f)

                


def windows():
    app=QApplication(sys.argv)
    win=MyWindows()

    win.show()
    sys.exit(app.exec_())
windows()


