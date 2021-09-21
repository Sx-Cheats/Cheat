
import re,subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
class _SHELL_():

    def __init__(self) -> None:
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)

        self._COMMAND_ ={
            "cls":lambda : CLS(),
            "print":lambda COLOR = None,_err=False:  PRINT(COLOR,_err),
            "system":lambda: Command_System(),
            "setcolor":lambda: SET_COLOR(),
            "help": lambda:HELP()
        }
        def HELP(): 
          self.SHELL_COMMAND = "\n\n⚫ Use CLS to clear the results in consol\n\n⚫ Use print-Your_Text_Here to print your text in the console\n\n⚫ Use system-command to call  system commands( example: system-date )\n\n⚫ Use setcolor-(r,g,b) to change color in console\n\n⚫ Use exit to exit the console"
          PRINT(None,False)
        def Command_System():
                self.SHELL_COMMAND = "-"+subprocess.getoutput("powershell -Command "+re.sub("^system","",self.SHELL_COMMAND.lower())[1:])
                PRINT(None,False)

        def SET_COLOR():
            try:
                COLOR = eval(re.sub("setcolor","",self.SHELL_COMMAND.strip().lower())[1:])
                if type(COLOR) != tuple or len(COLOR) != 3 or sum(COLOR) > 765 or "-" in str(COLOR) : raise ValueError()
                self.Print_Color = str(COLOR)[:-1]
                for x in self.LINE:
                   for x2 in x:
                        if x2.objectName() != "ERROR_PLAIN_TEXT":
                            if x2.objectName() == "PLAIN_TEXT":
                                  x2.setStyleSheet(f"font: 900 9pt 'MS Shell Dlg 2';\nselection-color: rgb(0, 0, 0);\npadding-top:8px;\ncolor:rgb{self.Print_Color});\nselection-background-color:rgb{self.Print_Color});")
                            elif x2.objectName() == "FROM_PATH":
                                x2.setStyleSheet(f"color: rgb{self.Print_Color+',0.80)'};\n" "background-color: Transparent;\nselection-color: rgb(0, 0, 0);") 
                            else: 
                                x2.setStyleSheet(f"font: 900 9pt 'MS Shell Dlg 2';\ncolor: rgb{self.Print_Color+',0.93)'};\nbackground-color: Transparent;\nselection-color: rgb(0, 0, 0);\nselection-background-color:rgb{self.Print_Color+',0.80)'};")
                self.SHELL_COMMAND = f"-Current Color: {COLOR})"
                PRINT(None,False)
            except:
                self.SHELL_COMMAND = f"-Error to set color !"
                PRINT("(255,0,0",True)

        def PRINT(COLOR,_err):
            if _err: 
                 NAME = "ERROR_PLAIN_TEXT" 
            else:
                 NAME = "PLAIN_TEXT"
            COLOR = self.Print_Color if not COLOR else  COLOR
            plainTextEdit = QtWidgets.QPlainTextEdit(self.UI.CONSO_SCROLL_AREA)
            HEIGHT = max(((QtGui.QFontMetrics(self.font)).size(0,self.SHELL_COMMAND)).height()/1.225 ,25)
            plainTextEdit.setMinimumSize(QtCore.QSize(0, 25+ HEIGHT))
            plainTextEdit.setMaximumSize(QtCore.QSize(695, 25+ HEIGHT))
            plainTextEdit.setFont(self.font)
            plainTextEdit.setStyleSheet(f"font: 900 9pt 'MS Shell Dlg 2';\npadding-top:8px;\ncolor:rgb{COLOR},0.80);\nselection-color: rgb(0, 0, 0);\nselection-background-color:rgb{COLOR});")
            plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            plainTextEdit.setTabChangesFocus(True)
            plainTextEdit.setDocumentTitle("")
            plainTextEdit.setUndoRedoEnabled(True)
            plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
            plainTextEdit.setReadOnly(True)
            plainTextEdit.setPlainText(re.sub("^print","",self.SHELL_COMMAND)[1:]+"\n")
            plainTextEdit.setOverwriteMode(False)
            plainTextEdit.setTabStopWidth(695)
            plainTextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
            plainTextEdit.setMaximumBlockCount(0)
            plainTextEdit.setCenterOnScroll(False)
            plainTextEdit.setPlaceholderText("")
            plainTextEdit.setObjectName(NAME)
            self.LINE.append([plainTextEdit,plainTextEdit])
            self.UI.verticalLayout_2.addWidget(plainTextEdit)
            self._New_Line()
            
        def CLS():
            for x in self.LINE[2:]:
                    x[0].deleteLater()
                    self.LINE.remove(x)
            self.CurrentLine =  self.LINE[len(self.LINE)-1][1]
            self.CurrentLine.setReadOnly(False)
            self.CurrentLine.setText("")
            self.CurrentLine.setFocus()


