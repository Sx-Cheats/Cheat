
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_EXE(object):
    def setupUi(self, EXE):
        EXE.setObjectName("EXE")
        EXE.resize(730, 446)
        EXE.setStyleSheet("color: rgb(255, 255, 255);")
        self.Background = QtWidgets.QWidget(EXE)
        self.Background.setGeometry(QtCore.QRect(10, 40, 711, 401))
        self.Background.setStyleSheet("#Background\n"
"{\n"
"background-color: rgb(17, 5, 11);\n"
"border-style:solid;\n"
"\n"
"  border-color: rgb(255, 255, 255,0.1);\n"
"border-bottom-width:3px;\n"
"border-top-width:0px;\n"
"border-left-width:0px;\n"
"border-right-width:0px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
".QScrollBar:vertical {\n"
"width: 9px;\n"
" border-left: 2px solid grey;\n"
" background: rgb(106, 9, 84 );\n"
"     margin: -2px 0 -2px 0;\n"
"\n"
"}\n"
"\n"
".QScrollBar::handle:vertical {\n"
"     background: rgb(55, 53, 55);\n"
"\n"
"\n"
" }\n"
"\n"
"/*  add-line & sub-line is arrow */\n"
".QScrollBar::add-line:vertical {\n"
" border-left: 2px solid grey;\n"
"}\n"
"\n"
".QScrollBar::sub-line:vertical {\n"
" border-left: 2px solid grey;\n"
" }\n"
"\n"
"\n"
"QScrollBar::add-page:vertical ,QScrollBar::sub-page:vertical{       \n"
"    background-color: rgb(30, 30, 30 );\n"
"}\n"
"")
        self.Background.setObjectName("Background")
        self.CONSOL_OBJ = QtWidgets.QScrollArea(self.Background)
        self.CONSOL_OBJ.setGeometry(QtCore.QRect(0, 0, 711, 401))
        self.CONSOL_OBJ.setStyleSheet("\n"
"border-style:solid;\n"
"background-color: rgb(16, 5, 10);\n"
"  border-color: rgb(255, 255, 255,0.1);\n"
"border-width:4px;\n"
"border-top-width:0px;\n"
"border-left-width:0px;\n"
"border-right-width:0px;\n"
"")
        self.CONSOL_OBJ.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.CONSOL_OBJ.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CONSOL_OBJ.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CONSOL_OBJ.setWidgetResizable(True)
        self.CONSOL_OBJ.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CONSOL_OBJ.setObjectName("CONSOL_OBJ")
        self.CONSO_SCROLL_AREA = QtWidgets.QWidget()
        self.CONSO_SCROLL_AREA.setGeometry(QtCore.QRect(0, 0, 700, 400))
        self.CONSO_SCROLL_AREA.setStyleSheet("border-bottom-width:0px;")
        self.CONSO_SCROLL_AREA.setObjectName("CONSO_SCROLL_AREA")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CONSO_SCROLL_AREA)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(5, 15, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.CONSOL_OBJ.setWidget(self.CONSO_SCROLL_AREA)
        self.TOP = QtWidgets.QFrame(EXE)
        self.TOP.setGeometry(QtCore.QRect(10, 14, 711, 26))
        self.TOP.setStyleSheet("background-color: rgb(19,7,8);\n"
"\n"
"\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"\n"
"border-style:solid;\n"
"border-bottom-width:2px;\n"
"border-color: rgb(146, 4, 4 );\n"
"font: 900 9pt 'MS Shell Dlg 2';\n"
"\n"
"\n"
"\n"
"")
        self.TOP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TOP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TOP.setObjectName("TOP")
        self.BP_EXIT = QtWidgets.QPushButton(self.TOP)
        self.BP_EXIT.setGeometry(QtCore.QRect(690, 9, 10, 10))
        self.BP_EXIT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BP_EXIT.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-style:solid;\n"
"border-radius:4px")
        self.BP_EXIT.setText("")
        self.BP_EXIT.setObjectName("BP_EXIT")
        self.BP_MINIMIZE = QtWidgets.QPushButton(self.TOP)
        self.BP_MINIMIZE.setGeometry(QtCore.QRect(670, 9, 10, 10))
        self.BP_MINIMIZE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BP_MINIMIZE.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-style:solid;\n"
"border-radius:4px")
        self.BP_MINIMIZE.setText("")
        self.BP_MINIMIZE.setObjectName("BP_MINIMIZE")
        self.TITLE = QtWidgets.QLabel(self.TOP)
        self.TITLE.setGeometry(QtCore.QRect(10, 0, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE.setFont(font)
        self.TITLE.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: Transparent;\n"
"border-width:0px;")
        self.TITLE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TITLE.setObjectName("TITLE")
        self.NOTICE = QtWidgets.QLabel(self.TOP)
        self.NOTICE.setGeometry(QtCore.QRect(395, 2, 271, 20))
        self.NOTICE.setText("Use Help to see which commands is valid")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.NOTICE.setFont(font)
        self.NOTICE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NOTICE.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-bottom-width:0px;")
        self.NOTICE.setObjectName("NOTICE")

