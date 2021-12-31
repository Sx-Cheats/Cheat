
import sys,os
from CMD import *
import re
from win32api import GetAsyncKeyState
from COMMAND import _SHELL_
from PyQt5 import QtCore, QtGui, QtWidgets

class InitUI(_SHELL_):

    def __init__(self)->None:
        super(InitUI,self).__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.StartPos = 0
        self.BackGroundMenu = QtWidgets.QFrame()
        self.UI = Ui_EXE()
        self.Print_Color = "(255,234,128"
        self.CurrentLine,self.LINE = None,[]
        self.UI.setupUi(self.BackGroundMenu)
        self.UI.TITLE.setText("ac_client.exe | Assault Cube cheat")
        self.BackGroundMenu.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.BackGroundMenu.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        def New_Line(SHELL_COMMAND :str = "") -> None:
            self.SHELL_COMMAND = SHELL_COMMAND.strip() if SHELL_COMMAND != "" else "Invalid Command"
            COMMAND = re.search("^\w+",self.SHELL_COMMAND)
            if    (COMMAND == None or not COMMAND.group(0).lower() in self._COMMAND_)  and SHELL_COMMAND != "":
                  self.SHELL_COMMAND = f"-'{SHELL_COMMAND}' is not recognized as an internal\nor external command, executable program, or batch file."
                  self._COMMAND_["print"]("(255,0,0",True)
                  return
            elif COMMAND.group(0).lower() in self._COMMAND_ :
                   self._COMMAND_[COMMAND.group(0).lower()]()
                   return
            LINE_COMMAND = QtWidgets.QWidget(self.UI.CONSO_SCROLL_AREA)
            LINE_COMMAND.setMinimumSize(QtCore.QSize(0, 25))
            LINE_COMMAND.setMaximumSize(QtCore.QSize(690, 25))
            LINE_COMMAND.setStyleSheet("background-color: Transparent;\nborder-width:0px")
            LINE_COMMAND.setObjectName("")
            self.UI.verticalLayout_2.addWidget(LINE_COMMAND)
            horizontalLayoutWidget = QtWidgets.QWidget(LINE_COMMAND)
            horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 690, 31))
            horizontalLayoutWidget.setObjectName("")
            HORIZONTAL_LAYOUT = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
            HORIZONTAL_LAYOUT.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
            HORIZONTAL_LAYOUT.setContentsMargins(3, 0, 0, 0)
            HORIZONTAL_LAYOUT.setSpacing(4)
            HORIZONTAL_LAYOUT.setObjectName("")
            FROM_PATH = QtWidgets.QLabel(horizontalLayoutWidget)
            FROM_PATH.setStyleSheet(f"font: 900 9pt 'MS Shell Dlg 2';\ncolor: rgb{self.Print_Color+',0.80)'};\nselection-color: rgb(0, 0, 0);")
            FROM_PATH.setObjectName("FROM_PATH")
            FROM_PATH.setText(os.getenv("USERPROFILE",sys.path[0])+">")
            HORIZONTAL_LAYOUT.addWidget(FROM_PATH)
            CMDLET = QtWidgets.QLineEdit(horizontalLayoutWidget)
            CMDLET.setMaximumSize(QtCore.QSize(711, 16777215))
            CMDLET.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
            CMDLET.setStyleSheet(f"font: 900 9pt 'MS Shell Dlg 2';\ncolor: rgb{self.Print_Color+',0.93)'};\nselection-color: rgb(0, 0, 0);\nselection-background-color:rgb{self.Print_Color+',0.80)'};")
            CMDLET.setMaxLength(32767)
            CMDLET.setFrame(False)
            CMDLET.setCursorPosition(8)
            CMDLET.setDragEnabled(False)
            CMDLET.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
            CMDLET.setObjectName("CMDLET")
            CMDLET.setPlaceholderText("Command...")
            CMDLET.returnPressed.connect(lambda : New_Line(CMDLET.text()))
            CMDLET.setFocus()
            HORIZONTAL_LAYOUT.addWidget(CMDLET)
            self.LINE.append([LINE_COMMAND,CMDLET,FROM_PATH])
            if len(self.LINE) > 1 and self.CurrentLine:
                 self.CurrentLine.setReadOnly(True)
            self.CurrentLine = CMDLET

        def moveFrame(event):
            if(GetAsyncKeyState(0x01) != 0 and self.StartPos != 0):
                self.BackGroundMenu.move(self.BackGroundMenu.pos() + event.globalPos() - self.StartPos)
                self.StartPos = event.globalPos()
                event.accept()
        def StartPos(event):
            if(GetAsyncKeyState(0x01) != 0):
                  self.StartPos = event.globalPos()
        self.BackGroundMenu.mousePressEvent = StartPos    
        self.BackGroundMenu.mouseMoveEvent = moveFrame
        self._New_Line = New_Line
        self.SHELL_COMMAND = """
██████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝
██████╦╝░╚████╔╝░
██╔══██╗░░╚██╔╝░░
██████╦╝░░░██║░░░
╚═════╝░░░░╚═╝░░░

░███████╗██╗░░██╗░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░████████╗░██████╗
██╔██╔══╝╚██╗██╔╝░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
╚██████╗░░╚███╔╝░█████╗██║░░╚═╝███████║█████╗░░███████║░░░██║░░░╚█████╗░
░╚═██╔██╗░██╔██╗░╚════╝██║░░██╗██╔══██║██╔══╝░░██╔══██║░░░██║░░░░╚═══██╗
███████╔╝██╔╝╚██╗░░░░░░╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██████╔╝
╚══════╝░╚═╝░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░"""
        self._COMMAND_["print"]("(251, 177, 55",True) 
        self.UI.NOTICE.mousePressEvent = lambda ev:  self._COMMAND_["help"]() if GetAsyncKeyState(0x01) != 0 else None
        self.UI.BP_MINIMIZE.clicked.connect(lambda : self.BackGroundMenu.showMinimized())


