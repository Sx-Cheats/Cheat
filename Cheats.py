try:
    import sys,subprocess,re,threading
    from time import sleep
    from math import sqrt
    from ctypes import windll
    import os
    sys.path.append(sys.path[0] + r"\Include")
    from Calc_Angle import Calc
    from  MemoryWrite  import ReadWriteMemory
    from __Init_CMD__ import InitUI
except (ImportError or ImportWarning) as Module:
    print(f"Please Install:\n\n-{Module.msg.replace('No module named','')}") 
class CHEATS(InitUI,ReadWriteMemory,Calc):
     def __init__(self) -> None:
        super(CHEATS,self).__init__()
        self._COMMAND_["attach"] = lambda: START()
        self.process = None
        self.CAMMO = ""
        self.BOT_ADRESS = []
        self.MAX_MAGNITUDE = 65
        self.MouseXX = 0
        self.MouseYY = 0
        self.FreezeValue = None
        self.CHEALTH = ""
        self.CGRENADE = ""
        self.CARMOR  = ""
        def CLOSE():
            self._New_Line = None
            if self.process:
              windll.kernel32.CloseHandle(self.process.handle)
            os._exit(0)
        self.UI.BP_EXIT.clicked.connect(lambda:CLOSE())
        def Magnitude(X0:tuple=(0,0,0),X1:tuple = (1,1,1)):
                return sqrt(sum([(x[0]-x[1])**2 for x in list(zip(X1,X0))]))
        def _GET_BOT_():
              if self.BOT_ADRESS.__len__() > 0:
                  for x in self.BOT_ADRESS:
                      self.BOT_ADRESS.remove(x)
              PLAYERS_ONLINE = self.process.read(0x50F500)
              ENNEMY_OBJ_ADRESS = self.process.get_pointer(0x400000 + 0x10F4F4+4)
              return [self.process.get_pointer(ENNEMY_OBJ_ADRESS+(0x4*x)) for x in range(PLAYERS_ONLINE)][1:]
        def START():
            NAME =  subprocess.getoutput("powershell -C (Get-Process ac_client).ProcessName")
            if NAME== "ac_client":
                rwm = ReadWriteMemory()
                self._COMMAND_.pop("attach")
                self.SHELL_COMMAND = "-ac_client.exe has been found"
                self._COMMAND_["print"]("(45, 255, 134",False)
                self.process = rwm.get_process_by_name(NAME)
                self.process.open()
                def WRITE(self,VAR,VALUE,SET = False,ADRESS = 0x0):  
                    if SET and ADRESS != 0:
                        self.process.write(ADRESS,VALUE)
                        self._New_Line()
                        return
                    try:
                        exec(f"self.{VAR} = int({VALUE})")
                    except:
                        exec(f"self.{VAR} = 'NULL'")
                    self._New_Line()
                PLAYER_OBJ_ADRESS = self.process.get_pointer(0x400000 + 0x10F4F4)
                
                def PRINT_ADRESS(self):
                    self.SHELL_COMMAND  = ""
                    
                    if self.BOT_ADRESS.__len__() != self.process.read(0x50F500) or self.BOT_ADRESS.__len__()  == None:
                           
                           self.BOT_ADRESS = _GET_BOT_()
                    print("BOT ADRESS = ", self.BOT_ADRESS)
                    for x in self.BOT_ADRESS:
                        self.SHELL_COMMAND += "\n\n"+str(hex(x)+f" HEALTH = {self.process.read(x+248)}\n") + f"\nX = {self.process.DEC_TO_FLOAT(self.process.read(x+0x38))}\nY = {self.process.DEC_TO_FLOAT(self.process.read(x+0x3C))}\nZ = {self.process.DEC_TO_FLOAT(self.process.read(x+0x34))}" 
                    self.SHELL_COMMAND +=     "\n\n PLAYER ADRESS (X Y Z) :\n" + f"\nX = {self.process.DEC_TO_FLOAT(self.process.read(PLAYER_OBJ_ADRESS+0x34))}\nY = {self.process.DEC_TO_FLOAT(self.process.read(PLAYER_OBJ_ADRESS+0x3C))}\nZ = {self.process.DEC_TO_FLOAT(self.process.read(PLAYER_OBJ_ADRESS+0x38))}" 
                    self._COMMAND_["print"](None,False)
                    sleep(2)
                
                def TP_ALL(self,Team: int = -1):
                        for x in self.BOT_ADRESS:
                            if self.process.read(x+0x32c) != Team:
                                    self.process.write(x+52,self.process.read(PLAYER_OBJ_ADRESS+4)) #X
                                    self.process.write(x+12,self.process.read(PLAYER_OBJ_ADRESS+12)) #Y
                                    self.process.write(x+56,self.process.read(PLAYER_OBJ_ADRESS+8)) #Z
                        self._New_Line()
                self.BOT_ADRESS = _GET_BOT_()
                self.Health_Adress = PLAYER_OBJ_ADRESS + 0xF8 
                self.ARMAS_ADRESS = [PLAYER_OBJ_ADRESS+0x150,PLAYER_OBJ_ADRESS+0x13C,PLAYER_OBJ_ADRESS+0x15C,PLAYER_OBJ_ADRESS+0x148,PLAYER_OBJ_ADRESS+0x14C,PLAYER_OBJ_ADRESS+0x144,PLAYER_OBJ_ADRESS+0x140]
                self.Armor_Adress = PLAYER_OBJ_ADRESS + 0xFC
                self.Grenade_Adress = PLAYER_OBJ_ADRESS + 0x158
                self.MouseX,self.MouseY  = PLAYER_OBJ_ADRESS+0x40,PLAYER_OBJ_ADRESS+0x44
                self.X,self.Y = None,None
                self.AIMBOT = False
                def AimBot():
                    read,MG = self.process.read,1e10
                    while self._New_Line != None:
                        if self.AIMBOT:
                            if self.BOT_ADRESS.__len__() != read(0x50F500) or self.BOT_ADRESS.__len__() == None:
                                self.BOT_ADRESS = _GET_BOT_()
                            if self.BOT_ADRESS == None:return
                            PLAYER_COORD = (self.process.DEC_TO_FLOAT(read(PLAYER_OBJ_ADRESS+0x38)), self.process.DEC_TO_FLOAT(read(PLAYER_OBJ_ADRESS+0x3C)),self.process.DEC_TO_FLOAT(read(PLAYER_OBJ_ADRESS+0x34)))
                            for x in self.BOT_ADRESS:       
                                BOT_COORD = (self.process.DEC_TO_FLOAT(read(x+0x38)), self.process.DEC_TO_FLOAT(read(x+0x3C)),self.process.DEC_TO_FLOAT(read(x+0x34)))
                                MAGNITUDE = [Magnitude(PLAYER_COORD,BOT_COORD),read(x+0xF8)]
                                if   ((MAGNITUDE[1] >= 4294967286) or (MAGNITUDE[1] <= 1)): continue
                                elif self.MAX_MAGNITUDE >= MAGNITUDE[0] <= MG and 1 < MAGNITUDE[1] <= 100:
                                    MG = MAGNITUDE [0]   
                                    self.TARGET = BOT_COORD  
                            self.X,self.Y = self.ANGLE(PLAYER_COORD,self.TARGET)
                            self.X,self.Y,self.MAGNITUDE = self.process.FLOAT_TO_DEC(self.X),self.process.FLOAT_TO_DEC(self.Y),MG
                            MG = 1e10
                def BlockValue():
                    while self._New_Line != None:
                        try:
                            if type(self.CAMMO) == int:
                                 for x in self.ARMAS_ADRESS :
                                        self.process.write(x,self.CAMMO)
                            if type(self.CHEALTH) == int:
                                self.process.write(self.Health_Adress,self.CHEALTH)
                            if type(self.CGRENADE) == int :
                                    self.process.write(self.Grenade_Adress,self.CGRENADE)
                            if  type(self.CARMOR) == int:
                                self.process.write(self.Armor_Adress,self.CARMOR)
                            if  type(self.X) == int and self.AIMBOT and  self.MAGNITUDE <= self.MAX_MAGNITUDE:
                                self.process.write(self.MouseX,self.X)
                                self.process.write(self.MouseY,self.Y)
                        except:
                            self.SHELL_COMMAND = "-An error has occurred, please restart the program"
                            self._COMMAND_["print"]("(255, 0, 0",True)
                            return
                self._COMMAND_["setammo"] = lambda: WRITE(self,"CAMMO",re.sub("^setammo","",self.SHELL_COMMAND)[1:])
                self._COMMAND_["sethealth"] =  lambda: WRITE(self,"CHEALTH",re.sub("^sethealth","",self.SHELL_COMMAND)[1:])
                self._COMMAND_["setgrenade"] =  lambda: WRITE(self,"CGRENADE",re.sub("^setgrenade","",self.SHELL_COMMAND)[1:])
                self._COMMAND_["setarmor"] =  lambda: WRITE(self,"CARMOR",re.sub("^setarmor","",self.SHELL_COMMAND)[1:])
                self._COMMAND_["setarmor"] =  lambda: WRITE(self,"CARMOR",re.sub("^setarmor","",self.SHELL_COMMAND)[1:])
                self._COMMAND_["freeze"] =  lambda: WRITE(self,"",1,True,0x004FF722)
                self._COMMAND_["unfreeze"] =  lambda: WRITE(self,"",0,True,0x004FF722)
                self._COMMAND_["adress"] =  lambda: PRINT_ADRESS(self)
                self._COMMAND_["tpall"] =  lambda: TP_ALL(self,-1)
                self._COMMAND_["exit"] =  lambda: CLOSE()
                self._COMMAND_["tpteam"] =  lambda: TP_ALL(self,0 if self.process.read(PLAYER_OBJ_ADRESS+0x32c) == 1  else 1)
                self._COMMAND_["tpennemy"] =  lambda: TP_ALL(self,self.process.read(PLAYER_OBJ_ADRESS+0x32c))
                self._COMMAND_["aimbot"] =  lambda: WRITE(self,'AIMBOT',not self.AIMBOT,False,0)
                self._COMMAND_["exit"] = lambda: CLOSE()
                threading.Thread(target=BlockValue).start()
                threading.Thread(target=AimBot).start()
            else:
                self.SHELL_COMMAND = "-Error to find ac_client.exe, you can use 'attach' to check again"
                self._COMMAND_["print"]("(251, 0, 0")
        self.BackGroundMenu.show()
        sys.exit(self.app.exec_())
        
#__import__("ctypes").windll.user32.ShowWindow(__import__("ctypes").windll.kernel32.GetConsoleWindow(),0)

CHEATS()


