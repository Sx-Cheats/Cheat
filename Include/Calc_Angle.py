
from math import cos,acos,sin,asin,tan,atan,sqrt,pi
class Calc(): 
    def __init__(self) -> None:
        pass 
    def ANGLE(self,_PLAYER:tuple=(0,0,0),_TARGET:tuple=(0,0,0)):
        self.origine = tuple(map(abs,[x[0]-x[1] for x in zip(_TARGET,_PLAYER)]))
        self.hypotenuse = sqrt(self.origine[0]**2+self.origine[2]**2)
        self.X = acos(self.origine[0]/self.hypotenuse)*180/pi
        self.Y =  sin(self.origine[1]/sqrt(self.hypotenuse**2+self.origine[0]**2))*180/pi
        if  _PLAYER[2] <= _TARGET[2]:
                if _PLAYER[0] <= _TARGET[0]:
                 self.X =  180 - self.X
        elif _PLAYER[2] > _TARGET[2]:
             if _PLAYER[0] >= _TARGET[0]:
               self.X = 360 - self.X
             elif  _PLAYER[0] < _TARGET[0]:
                 self.X += 180
        if _PLAYER[1] > _TARGET[1]:
            self.Y = -self.Y
        elif _PLAYER[1] < _TARGET[1] and self.Y <  0:
          self.Y = abs(self.Y)
        return  self.X,self.Y
