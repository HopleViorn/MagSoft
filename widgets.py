from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPen,QPixmap,QImage
from PyQt5.Qt import Qt
import cv2
import toupcam
import sys,os

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class ImgView(QtWidgets.QLabel):
    def __init__(self,parent):
        super(ImgView,self).__init__(parent)
        img = cv2.imread(get_resource_path('res/demo2.png'))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.setImage(img)

    def setQImage(self,img: QImage):
        self.piximg=QPixmap.fromImage(img)

    def setImage(self,img):
        self.piximg=QPixmap.fromImage(QImage(img.tobytes(),img.shape[1],img.shape[0],img.shape[1]*3,QtGui.QImage.Format_RGB888))
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.eraseRect(self.rect())
        painter.begin(self)
        painter.drawPixmap(0,0,self.width(),self.height(),self.piximg)

class NativeCanvas(ImgView):
    def __init__(self,parent):
        super(NativeCanvas,self).__init__(parent)
        self.isDrawing=0
        self.lines=None

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.isDrawing==1:
            self.lines=[[ev.localPos().x(),ev.localPos().y()],[0,0]]
            self.isDrawing=2
        elif self.isDrawing==2:
            self.setMouseTracking(False)
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.isDrawing=0
        return super().mousePressEvent(ev)

    def startDraw(self):
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.isDrawing=1

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.isDrawing==2:
            self.lines[1][0]=ev.localPos().x()
            self.lines[1][1]=ev.localPos().y()
            self.update()
        return super().mouseMoveEvent(ev)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.eraseRect(self.rect())
        painter.begin(self)
        
        painter.drawPixmap(0,0,self.width(),self.height(),self.piximg)

        pen = QPen(Qt.white, 2, Qt.DashLine)
        painter.setPen(pen)
        
        if self.lines is not None:
            line=self.lines
            painter.drawLine(line[0][0],line[0][1],line[1][0],line[1][1])

        painter.end()



import numpy as np
class Canvas(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(Canvas,self).__init__()
        img = cv2.imread(get_resource_path('res/demo2.png'))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img=self.convert_to_grey(img)
        self.setImage(img)

    def setQImage(self,img: QImage):
        self.piximg=QPixmap.fromImage(img)

    def setImage(self,img):
        img=cv2.applyColorMap(img[:,:,0],cv2.COLORMAP_JET)
        self.setSceneRect(0,0,img.shape[1],img.shape[0])
        self.img=img
        self.piximg=QPixmap.fromImage(QImage(img.tobytes(),img.shape[1],img.shape[0],img.shape[1]*3,QtGui.QImage.Format_RGB888))
        self.update()

    def drawBackground(self, painter: QPainter, rect: QtCore.QRectF) -> None:
        painter.drawPixmap(0,0,self.piximg)
        return super().drawBackground(painter, rect)
    
    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        return super().mouseMoveEvent(ev)


from items import RectArea,CalibrationRect
import variables

class MainViewer(QtWidgets.QGraphicsView):
    
    selectChanged = QtCore.pyqtSignal(object)

    def __init__(self,parent):
        super(MainViewer,self).__init__(parent)
        self.scene=Canvas()
        self.setScene(self.scene)
        self.move(0,0)
        self.onDrawing=0
        self.drawingItem=None
        self.base_img=0
        self.color_map=cv2.COLORMAP_JET
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse);
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse);

    def onInitialize(self):
        self.base_img=self.scene.img

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        ratio=event.angleDelta().y()
        ratio=ratio/1200+1
        self.scale(ratio,ratio)
        return super().wheelEvent(event)
    
    def startDraw(self,drawItem,addItem=True):
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.onDrawing=1
        self.drawingItem=drawItem
        if addItem:
            for item in self.drawingItem.itemList():
                self.scene.addItem(item)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.onDrawing==1:
            pos=self.mapToScene(event.localPos().toPoint())
            if self.drawingItem.onClick(pos)==0:
                self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                self.setMouseTracking(False)
                self.onDrawing=0
                self.drawingItem=None
        else:#Select
            rect=self.scene.itemAt(self.mapToScene(event.localPos().toPoint()),QtGui.QTransform())
            if rect is not None and isinstance(rect,RectArea):
                rect=rect.rect()
                proc=lambda x: max(int(x),0)
                l,r,u,d=(proc(rect.left()),proc(rect.right()),proc(rect.top()),proc(rect.bottom()))
                l,r=min(l,r),max(l,r)
                u,d=min(u,d),max(u,d)
                partial_img=(self.scene.img-self.base_img)[u:d,l:r,:]
                self.selectChanged.emit(partial_img)
            elif rect is not None and isinstance(rect,CalibrationRect):
                l,r,u,d=rect.getRect()
                partial_img=(self.scene.img-self.base_img)[u:d,l:r,:]
                avg=np.mean(partial_img)

                from main import main_ui
                d, okPressed = QtWidgets.QInputDialog.getDouble(main_ui, "Calibration","Magnetic Density (mT):",rect.md, 0, 100000, 2)
                if okPressed:
                    rect.md=d
                else: md=rect.md

                if rect not in variables.rgb_mt:
                    variables.rgb_mt.append(rect)
                for x in variables.rgb_mt:
                    print(x.md,x.avg)

                rect.setText(avg,rect.md)

                # rect=rect.rect()
                # proc=lambda x: max(int(x),0)
                # l,r,u,d=(proc(rect.left()),proc(rect.right()),proc(rect.top()),proc(rect.bottom()))
                # l,r=min(l,r),max(l,r)
                # u,d=min(u,d),max(u,d)
            else:
                self.selectChanged.emit(None)
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.drawingItem is not None:
            pos=self.mapToScene(event.localPos().toPoint())
            self.drawingItem.onMoving(pos)

        return super().mouseMoveEvent(event)


import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
import PIL

class AnalysisThread(QtCore.QThread):

    finish = QtCore.pyqtSignal(object)

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):
        pass

class ProfileViewer(ImgView):
    def __init__(self,parent,axis=0):
        super(ProfileViewer,self).__init__(parent)
        self.axis=axis
        self.threads=[]
        self.setProfile(None)

    def setProfile(self,img):
        self.profile=np.zeros((1,1,1)) if img is None else img
        self.updateProfile()
    
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.updateProfile()
        return super().resizeEvent(a0)

    def updateProfile(self):
        img=np.mean(self.profile,axis=2)
        plt.figure(figsize=(self.width()/100,self.height()/100))
        maxplot=np.max(img,self.axis)
        minplot=np.min(img,self.axis)
        avgplot=np.mean(img,self.axis)
        l1=plt.plot(maxplot,label='Maxima')
        l2=plt.plot(minplot,label='Minima')
        l3=plt.plot(avgplot,label='Average')
        title=['Horizontal','Vertical'][self.axis]
        plt.title(title+' Profile')

        plt.legend(bbox_to_anchor=(1.02, 0),loc='lower left')

        plt.xlabel('Width')
        plt.ylabel('Field')

        buffer_ = BytesIO()
        plt.savefig(buffer_,format = 'png')
        buffer_.seek(0)
        dataPIL = PIL.Image.open(buffer_).convert('RGB')
        data = np.asarray(dataPIL)
        self.setImage(data)
        buffer_.close()
        plt.close()

class CaptureList(QtWidgets.QListView):

    selectImg = QtCore.pyqtSignal(object)
    
    def __init__(self,parent):
        super(CaptureList,self).__init__(parent)
        self.imgs=[]
        self.names=[]
        self.updateView()
        self.clicked.connect(self.select)
    
    def updateView(self):
        model=QtCore.QStringListModel()
        model.setStringList(self.names)
        self.setModel(model)

    def addCapture(self,img,name):
        self.imgs.append(img)
        self.names.append(name)
        self.updateView()
    
    def select(self,indx):
        self.selectImg.emit(self.imgs[indx.row()])
        # print(indx.row())