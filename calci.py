# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from math import *
  
import sys
  
  
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Calculator")
  
        # setting geometry
        self.setGeometry(100, 100, 360, 600)
  
        # calling method
        self.UiComponents()
        
        self.setStyleSheet('background-color:#2C394B;color:#F8485E')
        # showing all the widgets
        
        
        self.history = open('history.txt','a+')
        self.cur = 0
        self.hi = -2
        
        self.show()
        #self.his()
    
    
        
    def his(self):
        
        history = open('history.txt','r+')
        historyList = QComboBox(self)
        #historyList.setFixedHeight(45)
        historyList.setStyleSheet(
            'background-color:#334756;color:#F8485E;selection-background-color:#334756;selection-color:#00FFFF;')
        #historyList.setModel(model)
        history.seek(0)
        list = history.readlines()
        list.reverse()
        for x in range(0,len(list),2):
            historyList.addItem('{}{}'.format(list[x+1],list[x]))
        historyList.setGeometry(80, 500, 200, 60)
        historyList.activated[str].connect(self.style_choice)
        history.close()
  
        # method for widgets
    def UiComponents(self):
  
        # creating a label
        self.label = QLabel(self)
  
        # setting geometry to the label
        self.label.setGeometry(5, 5, 350, 70)
  
        # creating label multi line
        self.label.setWordWrap(True)
  
        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid #FF4C29;"
                                 "background : white;"
                                 "}")
  
        # setting alignment to the label
        self.label.setAlignment(Qt.AlignRight)
  
        # setting font
        self.label.setFont(QFont('Arial', 15))
  
  
        # adding number button to the screen
        # creating a push button
        push1 = QPushButton("1", self)
  
        # setting geometry
        push1.setGeometry(5, 150, 80, 40)
  
        # creating a push button
        push2 = QPushButton("2", self)
  
        # setting geometry
        push2.setGeometry(95, 150, 80, 40)
  
        # creating a push button
        push3 = QPushButton("3", self)
  
        # setting geometry
        push3.setGeometry(185, 150, 80, 40)
  
        # creating a push button
        push4 = QPushButton("4", self)
  
        # setting geometry
        push4.setGeometry(5, 200, 80, 40)
  
        # creating a push button
        push5 = QPushButton("5", self)
  
        # setting geometry
        push5.setGeometry(95, 200, 80, 40)
  
        # creating a push button
        push6 = QPushButton("5", self)
  
        # setting geometry
        push6.setGeometry(185, 200, 80, 40)
  
        # creating a push button
        push7 = QPushButton("7", self)
  
        # setting geometry
        push7.setGeometry(5, 250, 80, 40)
  
        # creating a push button
        push8 = QPushButton("8", self)
  
        # setting geometry
        push8.setGeometry(95, 250, 80, 40)
  
        # creating a push button
        push9 = QPushButton("9", self)
  
        # setting geometry
        push9.setGeometry(185, 250, 80, 40)
  
        # creating a push button
        push0 = QPushButton("0", self)
  
        # setting geometry
        push0.setGeometry(5, 300, 80, 40)
  
        # adding operator push button
        # creating push button
        push_equal = QPushButton("=", self)
  
        # setting geometry
        push_equal.setGeometry(275, 300, 80, 40)
  
        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)
  
        # creating push button
        push_plus = QPushButton("+", self)
  
        # setting geometry
        push_plus.setGeometry(275, 250, 80, 40)
  
        # creating push button
        push_minus = QPushButton("-", self)
  
        # setting geometry
        push_minus.setGeometry(275, 200, 80, 40)
  
        # creating push button
        push_mul = QPushButton("*", self)
  
        # setting geometry
        push_mul.setGeometry(275, 150, 80, 40)
  
        # creating push button
        push_div = QPushButton("/", self)
  
        # setting geometry
        push_div.setGeometry(185, 300, 80, 40)
  
        # creating push button
        push_point = QPushButton(".", self)
  
        # setting geometry
        push_point.setGeometry(95, 300, 80, 40)
  
  
        # clear button
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 200, 40)
  
        # del one character button
        push_del = QPushButton("Del", self) #changes
        push_del.setGeometry(210, 100, 145, 40)
        
        
        ## new ones
        
        
        push_pi = QPushButton("Pi", self)
        push_pi.setGeometry(5, 350, 80, 40)
        
        push_sqrt = QPushButton("√", self)
        push_sqrt.setGeometry(95, 350, 80, 40)
        
        push_sinh = QPushButton("sinh", self)
        push_sinh.setGeometry(185, 350, 80, 40)
        
        push_cosh = QPushButton("cosh", self)
        push_cosh.setGeometry(275, 350, 80, 40)
        
        push_tanh = QPushButton("tanh", self)
        push_tanh.setGeometry(5, 400, 80, 40)
        
        push_log10 = QPushButton("log10", self)
        push_log10.setGeometry(95, 400, 80, 40)
        
        '''push_pi = QPushButton("pi", self)
        push_pi.setGeometry(185, 400, 80, 40)'''
        
        push_pow = QPushButton("power", self)
        push_pow.setGeometry(185, 400, 80, 40)
        
        push_tan = QPushButton("tan", self)
        push_tan.setGeometry(275, 400, 80, 40)
        
        push_cos = QPushButton("cos", self)
        push_cos.setGeometry(5, 450, 80, 40)
        
        push_sin = QPushButton("sin", self)
        push_sin.setGeometry(95, 450, 80, 40)
        
        push_op = QPushButton("(", self)
        push_op.setGeometry(185, 450, 80, 40)
        
        push_cl = QPushButton(")", self)
        push_cl.setGeometry(275, 450, 80, 40)
        
        #added history
        #model= QStandardItemModel(0,1)
        
            
        self.his()

        #generalLayout.addWidget(historyList)
        
        
        
  
        # adding action to each of the button
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)
  
        # new
        
        push_pi.clicked.connect(self.action_pi)
        push_sqrt.clicked.connect(self.action_sqrt)
        push_sinh.clicked.connect(self.action_sinh)
        push_cosh.clicked.connect(self.action_cosh)
        push_tanh.clicked.connect(self.action_tanh)
        push_log10.clicked.connect(self.action_log10)
        push_pow.clicked.connect(self.action_pow)
        push_tan.clicked.connect(self.action_tan)
        push_cos.clicked.connect(self.action_cos)
        push_sin.clicked.connect(self.action_sin)
        push_op.clicked.connect(self.action_op)
        push_cl.clicked.connect(self.action_cl)
        
        
    def action_pi(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " pi ")
        
    def action_sqrt(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " sqrt( ")
    
    def action_sinh(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " sinh( ")
        
    def action_cosh(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " cosh( ")
        
    def action_tanh(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " tanh( ")
        
    def action_log10(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " log10( ")
    
    def action_pow(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " pow( ")
        
    def action_cos(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " cos( ")
        
    def action_tan(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " tan( ")
        
    def action_sin(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " sin( ")
        
    def action_op(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " ( ")
    
    def action_cl(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " ) ")
        
        
        
    def style_choice(self, text='hey'):
        self.label.setText(text.split('=')[0])
  
    def action_equal(self):
  
        # get the label text
        equation = self.label.text()
  
        try:
            # getting the ans
            
            
            ans = eval(equation, {'sqrt': sqrt, 'pow': pow, "fact": factorial,
                                  "exp": exp, "sin": sin, "cos": cos, "tan": tan,
                                  "ln": log, "e": e, "pi": pi, "mod": fmod, "abs": fabs,
                                  'log10': log10, "sinh": sinh, "cosh": cosh, "tanh": tanh,
                                  }, {})
  
            # setting text to the label
            self.label.setText(str(ans))
            
            answer = str(ans)
  
        except:
            # setting text to the label
            self.label.setText("Wrong Input")
            answer =  'WRONG INPUT'
        finally:
            self.history.seek(0,2)
            self.history.write('{}\n= {}\n'.format(equation,answer))
  
    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")
  
    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")
  
    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")
  
    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")
  
    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")
  
    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")
  
    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")
  
    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")
  
    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")
  
    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")
  
    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")
  
    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")
  
    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")
  
    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")
  
    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")
  
    def action_clear(self):
        # clearing the label text
        self.label.setText("")
  
    def action_del(self):
        # clearing a single digit
        
        
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])  #√
        
    def keyPressEvent(self, e):
        self.history.seek(0)# doesnt work when app is in background
        if e.key() == Qt.Key_H:
            if self.cur == QCursor().pos():
                self.hi -=2
            else:
                self.hi = -2
            try:
                self.label.setText(self.history.readlines()[self.hi])
            except:
                self.label.setText('No History')
            finally:
                self.history.seek(0)
                self.cur = QCursor().pos()
        elif e.key() == Qt.Key_J:
            if self.hi<-2:
                self.hi +=2
                try:
                    self.label.setText(self.history.readlines()[self.hi])
                    self.history.seek(0)
                except:
                    self.label.setText('No History')
            elif self.hi>=-2:
                self.hi +=2
                self.label.setText('')
                
        
    def close_conn(self):
        self.history.close()
        
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())

window.close_conn()