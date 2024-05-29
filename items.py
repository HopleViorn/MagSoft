
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPen,QPixmap,QImage
from PyQt5.Qt import Qt
import numpy as np
import variables

class DynamicRectArea(QtWidgets.QGraphicsRectItem):
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        super(RectArea,self).__init__(x0,y0,x1,y1)
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1
        self.setPen(QPen(Qt.white, 2, Qt.DashLine))
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setVisible(False)
        self.state=0
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setRect(self.x0,self.y0,0,0)
            self.setVisible(True)
            return 1
        if self.state==1:
            return 0

    def itemList(self):
        return [self]

    def onMoving(self,pos):
        x1,y1=pos.x(),pos.y()
        w,h=abs(x1-self.x0),abs(y1-self.y0)
        self.setRect(min(self.x0,x1),min(self.y0,y1),w,h)

class RectArea(QtWidgets.QGraphicsRectItem):
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        super(RectArea,self).__init__(x0,y0,x1,y1)
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1
        self.setPen(QPen(Qt.blue, variables.get_line_width(), Qt.DashLine))
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setVisible(False)
        self.state=0
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setRect(self.x0,self.y0,0,0)
            self.setVisible(True)
            return 1
        if self.state==1:
            return 0

    def itemList(self):
        return [self]

    def onMoving(self,pos):
        x1,y1=pos.x(),pos.y()
        self.x1,self.y1=x1,y1
        w,h=abs(x1-self.x0),abs(y1-self.y0)
        self.setRect(min(self.x0,x1),min(self.y0,y1),w,h)

    def getBox(self):
        f=lambda x:max(int(x),0)
        return f(min(self.x0,self.x1)),f(max(self.x0,self.x1)),f(min(self.y0,self.y1)),f(max(self.y0,self.y1))

class LineArea(QtWidgets.QGraphicsLineItem):
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        super(LineArea,self).__init__(x0,y0,x1,y1)
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1
        self.setPen(QPen(Qt.blue, variables.get_line_width(), Qt.DashLine))
        self.setVisible(False)
        self.state=0
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setLine(self.x0,self.y0,self.x0,self.y0)
            self.setVisible(True)
            return 1
        if self.state==1:
            return 0

    def itemList(self):
        return [self]

    def onMoving(self,pos):
        x1,y1=pos.x(),pos.y()
        self.setLine(self.x0,self.y0,x1,y1)

    
class HorizontalLine(QtWidgets.QGraphicsLineItem):
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        super(HorizontalLine,self).__init__(x0,y0,x1,y1)
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1
        self.setPen(QPen(Qt.blue, variables.get_line_width(), Qt.DashLine))
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setVisible(False)
        self.state=0
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setLine(self.x0,self.y0,self.x0,self.y0)
            self.setVisible(True)
            return 1
        if self.state==1:
            return 0

    def itemList(self):
        return [self]

    def onMoving(self,pos):
        self.x1,self.y1=pos.x(),pos.y()
        self.y0=self.y1
        self.setLine(self.x0,self.y0,self.x1,self.y1)

    def getBox(self):
        f=lambda x:max(int(x),0)
        return f(min(self.x0,self.x1)),f(max(self.x0,self.x1)),f(min(self.y0,self.y0+1)),f(max(self.y0,self.y0+1))


class VerticalLine(QtWidgets.QGraphicsLineItem):
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        super(VerticalLine,self).__init__(x0,y0,x1,y1)
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1
        self.setPen(QPen(Qt.blue, variables.get_line_width(), Qt.DashLine))
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setVisible(False)
        self.state=0
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setLine(self.x0,self.y0,self.x0,self.y0)
            self.setVisible(True)
            return 1
        if self.state==1:
            return 0

    def itemList(self):
        return [self]

    def onMoving(self,pos):
        self.x1,self.y1=pos.x(),pos.y()
        self.x0=self.x1
        self.setLine(self.x0,self.y0,self.x1,self.y1)
    def getBox(self):
        f=lambda x:max(int(x),0)
        return f(min(self.x0,self.x0+1)),f(max(self.x0,self.x0+1)),f(min(self.y0,self.y1)),f(max(self.y0,self.y1))

class MeasureLine():
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1

        self.width=10 #pix

        self.mainLine=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.secLine0=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.secLine1=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.text=QtWidgets.QGraphicsTextItem('length:{}'.format(0))
        self.text.setDefaultTextColor(Qt.white)
        font = QtGui.QFont()
        font.setPointSize(variables.get_font_width())
        self.text.setFont(font)
        
        self.mainLine.setPen(QPen(Qt.white, variables.get_line_width(), Qt.DashLine))
        self.secLine0.setPen(QPen(Qt.white, variables.get_line_width(), Qt.DashLine))
        self.secLine1.setPen(QPen(Qt.white, variables.get_line_width(), Qt.DashLine))

        self.items=[self.mainLine,self.secLine0,self.secLine1,self.text]
        for item in self.items:
            item.setVisible(False)

        self.setSegment(x0,y0,x1,y1)
        self.state=0

    def setSegment(self,x0,y0,x1,y1):
        self.mainLine.setLine(x0,y0,x1,y1)
        dv=np.array([y0-y1,x1-x0])
        
        self.text.setPos(x1,y1)
        self.text.setPlainText('{:.3f} mm\n{:.3f} px'.format(np.linalg.norm(dv)*variables.mm_per_pix,np.linalg.norm(dv)))

        dv=dv/np.linalg.norm(dv)*self.width

        self.secLine0.setLine(x0-dv[0],y0-dv[1],x0+dv[0],y0+dv[1])
        self.secLine1.setLine(x1-dv[0],y1-dv[1],x1+dv[0],y1+dv[1])
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setSegment(self.x0,self.y0,self.x0,self.y0)
            for item in self.items:
                item.setVisible(True)
            return 1
        if self.state==1:
            return 0

    def itemList(self):
        return self.items

    def onMoving(self,pos):
        x1,y1=pos.x(),pos.y()
        self.setSegment(self.x0,self.y0,x1,y1)

class CalibrationLine():
    def __init__(self,x0=0,y0=0,x1=0,y1=0):
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1

        self.width=25 #pix


        self.mainLine=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.secLine0=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.secLine1=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.text=QtWidgets.QGraphicsTextItem('length:{}'.format(0))

        self.text.setDefaultTextColor(Qt.red)
        font = QtGui.QFont()
        font.setPointSize(variables.get_font_width())
        self.text.setFont(font)

        self.mainLine.setPen(QPen(Qt.red, variables.get_line_width(), Qt.DashLine))
        self.secLine0.setPen(QPen(Qt.red, variables.get_line_width(), Qt.DashLine))
        self.secLine1.setPen(QPen(Qt.red, variables.get_line_width(), Qt.DashLine))

        self.items=[self.mainLine,self.secLine0,self.secLine1,self.text]
        for item in self.items:
            item.setVisible(False)

        self.setSegment(x0,y0,x1,y1)
        self.state=0

    def init(self):
        for item in self.items:
            item.setVisible(False)

        self.setSegment(0,0,0,0)
        self.state=0

    def setSegment(self,x0,y0,x1,y1):
        self.mainLine.setLine(x0,y0,x1,y1)

        dv=np.array([y0-y1,x1-x0])
        self.text.setPos(x1,y1)
        
        self.text.setPlainText('{:.3f} px'.format(np.linalg.norm(dv)))

        if np.linalg.norm(dv)>0:
            dv=dv/np.linalg.norm(dv)*self.width

        self.secLine0.setLine(x0-dv[0],y0-dv[1],x0+dv[0],y0+dv[1])
        self.secLine1.setLine(x1-dv[0],y1-dv[1],x1+dv[0],y1+dv[1])
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setSegment(self.x0,self.y0,self.x0,self.y0)
            for item in self.items:
                item.setVisible(True)
            return 1
        if self.state==1:
            self.x1,self.y1=pos.x(),pos.y()
            l=np.linalg.norm(np.array([self.y0-self.y1,self.x1-self.x0]))
            # variables.mm_per_pix=self.getDouble()/l
            variables.add_length_point(l,self.getDouble())
            # self.text.setPlainText('{:.3f} mm\n{:.3f} px'.format(l*variables.mm_per_pix,l))
            return 0

    def getDouble(self):
        from main import main_ui
        d, okPressed = QtWidgets.QInputDialog.getDouble(main_ui, "Calibration","Actual Length(mm):", 0, 0, 100000, 2)
        if okPressed:
            return d

    def itemList(self):
        return self.items

    def onMoving(self,pos):
        self.x1,self.y1=pos.x(),pos.y()
        self.setSegment(self.x0,self.y0,self.x1,self.y1)


class AverageThread(QtCore.QThread):
    finish = QtCore.pyqtSignal(object,object)
    def __init__(self,img):
        super().__init__()
        self.img=img

    def __del__(self):
        self.wait()

    def setImg(self,img):
        self.img=img

    def run(self):
        self.finish.emit(img,np.mean(img))

class CalibrationRect(QtWidgets.QGraphicsRectItem):
    def __init__(self,x0=0,y0=0,x1=0,y1=0,md=0,avg=0):
        super(CalibrationRect,self).__init__(x0,y0,x1,y1)
        self.x0,self.y0,self.x1,self.y1=x0,y0,x1,y1

        self.setPen(QPen(Qt.red, variables.get_line_width(), Qt.SolidLine))

        self.text=QtWidgets.QGraphicsTextItem('Average:')
        self.text.setPos(max(self.x0,self.x1),min(self.y0,self.y1))
        self.text.setDefaultTextColor(Qt.red)

        font = QtGui.QFont()
        font.setPointSize(variables.get_font_width())
        self.text.setFont(font)
        
        self.profile=np.zeros((1,1))
        self.avg=0

        self.items=[self,self.text]
        for item in self.items:
            item.setVisible(False)
        self.state=0
        
    def init(self):
        for item in self.items:
            item.setVisible(False)
        self.setSegment(0,0,0,0)
        self.state=0

    def setProfile(self,img):
        self.profile=img
        self.setSegment(self.x0,self.y0,self.x1,self.y1)

    def getRect(self):
        l,r=min(self.x0,self.x1),max(self.x0,self.x1)
        u,d=min(self.y0,self.y1),max(self.y0,self.y1)
        return int(l),int(r),int(u),int(d)
        
    def setSegment(self,x0,y0,x1,y1):
        l,r,u,d=self.getRect()
        if r>l and d>u:
            partial=self.profile[u:d,l:r]
        else:
            partial=np.zeros((1,1))

        w,h=abs(x1-x0),abs(y1-y0)
        self.text.setPos(x1,y1)
        self.avg=np.mean(partial)
        self.text.setPlainText('Average: {:.4f} px'.format(self.avg))
        self.setRect(min(x0,x1),min(y0,y1),w,h)
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.state=1
            self.setSegment(self.x0,self.y0,self.x0,self.y0)
            for item in self.items:
                item.setVisible(True)
            return 1
        if self.state==1:
            self.x1=pos.x()
            self.y1=pos.y()
            variables.add_mag_point(self.avg,self.getDouble())
            return 0

    def getDouble(self):
        from main import main_ui
        d, okPressed = QtWidgets.QInputDialog.getDouble(main_ui, "Calibration","Magfield Strength (mT):", 0, 0, 100000, 2)
        if okPressed:
            return d
    
    def itemList(self):
        return self.items

    def onMoving(self,pos):
        x1,y1=pos.x(),pos.y()
        self.x1,self.y1=x1,y1
        self.setSegment(self.x0,self.y0,x1,y1)


        
class DummyRect():
    def __init__(self,md=0,avg=0):
        self.md=md
        self.avg=avg


class MeasureAngle():
    def __init__(self):
        self.x0,self.y0=0,0
        self.x1,self.y1=0,0
        self.x2,self.y1=0,0
        
        self.line0=QtWidgets.QGraphicsLineItem(0,0,0,0)
        self.line1=QtWidgets.QGraphicsLineItem(0,0,0,0)

        self.line0.setPen(QPen(Qt.white, variables.get_line_width(), Qt.DashLine))
        self.line1.setPen(QPen(Qt.white, variables.get_line_width(), Qt.DashLine))

        self.text=QtWidgets.QGraphicsTextItem('angle')
        self.text.setDefaultTextColor(Qt.white)
        font = QtGui.QFont()
        font.setPointSize(variables.get_font_width())
        self.text.setFont(font)

        self.items=[self.line0,self.line1,self.text]
        for item in self.items:
            item.setVisible(False)

        self.state=0
    
    def onClick(self,pos):
        if self.state==0:
            self.x0=pos.x()
            self.y0=pos.y()
            self.line0.setLine(self.x0,self.y0,self.x0,self.y0)
            self.line0.setVisible(True)
            self.state=1
            return 1
        if self.state==1:
            self.x1=pos.x()
            self.y1=pos.y()
            self.line1.setLine(self.x1,self.y1,self.x1,self.y1)
            self.line1.setVisible(True)
            self.state=2
            return 2
        if self.state==2:
            self.x2=pos.x()
            self.y2=pos.y()
            self.text.setVisible(True)
            self.text.setPos(self.x1,self.y1)

            v0=np.array([self.x1-self.x0,self.y1-self.y0])
            v1=-np.array([self.x2-self.x1,self.y2-self.y1])
            import math
            self.text.setPlainText('{:.2f}°'.format(math.acos(np.dot(v1,v0)/(np.linalg.norm(v0)*np.linalg.norm(v1)))/np.pi*180))
            return 0

    def itemList(self):
        return self.items

    def onMoving(self,pos):
        if self.state==1:
            self.line0.setLine(self.x0,self.y0,pos.x(),pos.y())
        elif self.state==2:
            self.line1.setLine(self.x1,self.y1,pos.x(),pos.y())