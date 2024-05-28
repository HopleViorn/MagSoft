from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPen,QPixmap,QImage
from PyQt5.Qt import Qt
import cv2
import toupcam
import sys,os
import copy

def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class ImgView(QtWidgets.QLabel):
    def __init__(self,parent):
        super(ImgView,self).__init__(parent)
        path=get_resource_path(os.path.join('res','demo2.png'))
        img = cv_imread(path)
        print(path,img.shape)
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


class GraphicCalcThread(QtCore.QThread):
    finish = QtCore.pyqtSignal(object,object)
    def __init__(self,img):
        super().__init__()
        self.img=img

    def __del__(self):
        self.wait()

    def setImg(self,img):
        self.img=img

    def run(self):
        der=variables.get_derivated_img(self.img)
        mag=variables.mag_lut[der].astype(np.uint8)
        img=cv2.applyColorMap(mag,cv2.COLORMAP_JET)
        self.finish.emit(img,der)

import numpy as np
class Canvas(QtWidgets.QGraphicsScene):
    frameUpdate = QtCore.pyqtSignal(object)
    def __init__(self):
        super(Canvas,self).__init__()
        path=get_resource_path(os.path.join('res','demo2.png'))
        img = cv_imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.piximg=QPixmap.fromImage(QImage(img.tobytes(),img.shape[1],img.shape[0],img.shape[1]*3,QtGui.QImage.Format_RGB888))
        img = img[:,:,0]

        self.single_img=img
        self.worker=GraphicCalcThread(copy.deepcopy(self.single_img))
        self.worker.finish.connect(self.callback)
        # self.worker.start()
        self.setImage(img)
        
    def setQImage(self,img: QImage):
        self.piximg=QPixmap.fromImage(img)

    def callback(self,img,der):
        self.setSceneRect(0,0,img.shape[1],img.shape[0])
        self.frameUpdate.emit(der)
        self.img=img
        self.piximg=QPixmap.fromImage(QImage(img.tobytes(),img.shape[1],img.shape[0],img.shape[1]*3,QtGui.QImage.Format_RGB888))
        self.update()
        

    def Update(self):
        self.worker.setImg(self.single_img)
        self.worker.start()

    def setImage(self,img):
        self.single_img=img
        variables.resolution=(img.shape[1],img.shape[0])
        self.Update()

    def drawBackground(self, painter: QPainter, rect: QtCore.QRectF) -> None:
        painter.drawPixmap(0,0,self.piximg)
        return super().drawBackground(painter, rect)
    
    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        return super().mouseMoveEvent(ev)


from items import RectArea,CalibrationRect,VerticalLine,HorizontalLine,CalibrationLine,DynamicRectArea
import variables

class MainViewer(QtWidgets.QGraphicsView):
    
    selectChanged = QtCore.pyqtSignal(object)
    magCaliChanged = QtCore.pyqtSignal()
    drawDone = QtCore.pyqtSignal()
    lengthCaliChanged = QtCore.pyqtSignal()
    initializeChanged = QtCore.pyqtSignal(object)

    def __init__(self,parent):
        super(MainViewer,self).__init__(parent)
        self.scene=Canvas()
        self.setScene(self.scene)
        self.move(0,0)
        self.onDrawing=0
        self.drawingItem=None

        self.color_map=cv2.COLORMAP_JET
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

    def onInitialize(self):
        variables.base_img=copy.deepcopy(self.scene.single_img)
        self.scene.Update()
        self.initializeChanged.emit(np.mean(variables.base_img))

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        ratio=event.angleDelta().y()
        ratio=ratio/1200+1
        self.scale(ratio,ratio)
        return super().wheelEvent(event)
    
    def startDraw(self,drawItem,clearItem=None):
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.onDrawing=1
        self.drawingItem=drawItem

        if clearItem is not None:
            for item in clearItem.itemList():    
                self.scene.removeItem(item)
        
        for item in self.drawingItem.itemList():
            self.scene.addItem(item)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.onDrawing==1:
            pos=self.mapToScene(event.localPos().toPoint())
            if pos.x()>0 and pos.y()>0 and pos.x() <= variables.resolution[0] and pos.y() <= variables.resolution[1]:
                if self.drawingItem.onClick(pos)==0:
                    self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    self.setMouseTracking(False)
                    self.onDrawing=0
                    if isinstance(self.drawingItem,CalibrationLine):
                        self.lengthCaliChanged.emit()
                        
                    if isinstance(self.drawingItem,CalibrationRect):
                        self.magCaliChanged.emit()

                    self.drawingItem=None
                    self.drawDone.emit()
                    self.scene.frameUpdate.emit(variables.get_derivated_img(self.scene.single_img))
        # else:#Select
        #     rect=self.scene.itemAt(self.mapToScene(event.localPos().toPoint()),QtGui.QTransform())
        #     if rect is not None and isinstance(rect,RectArea):
        #         rect=rect.rect()
        #         proc=lambda x: max(int(x),0)
        #         l,r,u,d=(proc(rect.left()),proc(rect.right()),proc(rect.top()),proc(rect.bottom()))
        #         l,r=min(l,r),max(l,r)
        #         u,d=min(u,d),max(u,d)
        #         partial_img=(self.scene.single_img-variables.base_img)[u:d,l:r]
        #         self.selectChanged.emit(partial_img)

        #     elif rect is not None and isinstance(rect,HorizontalLine):
        #         proc=lambda x: max(int(x),0)
        #         l,r,u,d=rect.x0,rect.x1,rect.y0,rect.y0+1
        #         l,r,u,d=proc(l),proc(r),proc(u),proc(d)
        #         l,r=min(l,r),max(l,r)
        #         u,d=min(u,d),max(u,d)
        #         partial_img=(self.scene.single_img-variables.base_img)[u:d,l:r]
        #         self.selectChanged.emit(partial_img)

        #     elif rect is not None and isinstance(rect,VerticalLine):
        #         proc=lambda x: max(int(x),0)
        #         l,r,u,d=rect.x0,rect.x0+1,rect.y0,rect.y1
        #         l,r,u,d=proc(l),proc(r),proc(u),proc(d)
        #         l,r=min(l,r),max(l,r)
        #         u,d=min(u,d),max(u,d)
        #         print(l,r,u,d)
        #         partial_img=(self.scene.single_img-variables.base_img)[u:d,l:r]
        #         self.selectChanged.emit(partial_img)

        #     elif rect is not None and isinstance(rect,CalibrationRect):
        #         l,r,u,d=rect.getRect()
        #         partial_img=(self.scene.single_img-variables.base_img)[u:d,l:r]
        #         avg=np.mean(partial_img)

        #         import main
        #         d, okPressed = QtWidgets.QInputDialog.getDouble(main.main_ui, "Calibration","Magnetic Density (mT):",rect.md, 0, 100000, 2)
        #         if okPressed:
        #             rect.md=d
        #         else: md=rect.md

        #         rect.setText(avg,rect.md)

        #         if rect not in variables.rgb_mt:
        #             variables.rgb_mt.append(rect)
        #         variables.update_mag_lut()

        #         self.scene.Update()
        #         self.magCaliChanged.emit()
        #     else:
        #         pass
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

mux=QtCore.QMutex()

class ProfileCalcThread(QtCore.QThread):
    finish = QtCore.pyqtSignal(object)
    def __init__(self,axis,width,height):
        super().__init__()
        self.profile=np.zeros((1,1)).astype(np.uint8) 
        self.axis=axis
        self.width=width
        self.height=height

    def __del__(self):
        self.wait()

    def setNuclear(self,profile,width,height):
        self.profile=profile
        self.width=width
        self.height=height

    def run(self):
        img=self.profile
        # img=variables.mag_lut[img]
        buffer_ = BytesIO()
        maxplot=np.max(img,self.axis)
        minplot=np.min(img,self.axis)
        avgplot=np.mean(img,self.axis)
        l=len(maxplot)
        xlist=[i*variables.mm_per_pix for i in range(l)]

        mux.lock()
        plt.figure(figsize=(self.width/100,self.height/100))
        plt.subplots_adjust(right=0.8)
        plt.subplots_adjust(bottom=0.3)
        
        l1=plt.plot(xlist,maxplot,label='Maxima')
        l2=plt.plot(xlist,minplot,label='Minima')
        l3=plt.plot(xlist,avgplot,label='Average')
        title=['Horizontal','Vertical'][self.axis]
        plt.title(title+' Profile')

        plt.legend(bbox_to_anchor=(1.02, 0),loc='lower left')

        plt.xlabel('Width (mm)')
        plt.ylabel('Field (mT)')

        plt.savefig(buffer_,format = 'png')
        plt.close()
        mux.unlock()

        buffer_.seek(0)
        dataPIL = PIL.Image.open(buffer_).convert('RGB')
        data = np.asarray(dataPIL)
        buffer_.close()
        self.finish.emit(data)

class ProfileViewer(ImgView):
    def __init__(self,parent,axis=0):
        super(ProfileViewer,self).__init__(parent)
        self.axis=axis

        self.work=ProfileCalcThread(self.axis,self.width(),self.height())
        self.work.finish.connect(self.callback)
        
        self.setProfile(None)

    def setProfile(self,img):
        self.profile=np.zeros((1,1)).astype(np.uint8) if img is None else img
        self.updateProfile()
    
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.updateProfile()
        return super().resizeEvent(a0)

    def callback(self,img):
        self.setImage(img)

    def updateProfile(self):
        if variables.profile_area is not None:
            l,r,u,d=variables.profile_area.getBox()
            if r>l and d>u:
                self.work.setNuclear(self.profile[u:d,l:r],self.width(),self.height())
            else:
                self.work.setNuclear(np.zeros((1,1)).astype(np.uint8),self.width(),self.height())
        else:
            self.work.setNuclear(np.zeros((1,1)).astype(np.uint8),self.width(),self.height())
        if variables.currentTab==self.axis:
            self.work.start()

class MagCaliViewer(ImgView):
    def __init__(self,parent,axis=0):
        super(MagCaliViewer,self).__init__(parent)
        import variables
        self.lis=variables.rgb_mt
        self.updateProfile()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.updateProfile()
        return super().resizeEvent(a0)

    def updateProfile(self):
        nx=[]
        for point in self.lis:
            nx.append((point.avg,point.md))
        nx.sort(key=lambda x:x[0])

        xx,yy=[],[]
        for p in nx:
            xx.append(p[0])
            yy.append(p[1])

        mux.lock()
        plt.figure(figsize=(self.width()/100,self.height()/100))
        l1=plt.plot(xx,yy)

        buffer_ = BytesIO()
        plt.savefig(buffer_,format = 'png')
        plt.close()
        mux.unlock()
        buffer_.seek(0)
        dataPIL = PIL.Image.open(buffer_).convert('RGB')
        data = np.asarray(dataPIL)
        self.setImage(data)
        buffer_.close()

    
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


class LenCaliViewerThread(QtCore.QThread):
    finish = QtCore.pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.width=0
        self.height=0

    def __del__(self):
        self.wait()

    def run(self):
        data=variables.length_cali_array
        if data is None:
            return
        mux.lock()
        plt.figure(figsize=(self.width/100,self.height/100))
        plt.subplots_adjust(left=0.25)
        plt.subplots_adjust(bottom=0.2)
        l1=plt.scatter(data[:,0],data[:,1])
        l2=plt.axline((0,0),(1,variables.mm_per_pix))
        plt.xlabel('Pixels (px)')
        plt.ylabel('Length (mm)')

        buffer_ = BytesIO()
        plt.savefig(buffer_,format = 'png')
        plt.close()
        mux.unlock()
        buffer_.seek(0)
        dataPIL = PIL.Image.open(buffer_).convert('RGB')
        data = np.asarray(dataPIL)
        self.finish.emit(data)
        buffer_.close()

class LenCaliViewer(ImgView):
    def __init__(self,parent,axis=0):
        super(LenCaliViewer,self).__init__(parent)
        self.worker=LenCaliViewerThread()
        self.worker.finish.connect(self.callback)
        
        self.updateProfile()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.updateProfile()
        return super().resizeEvent(a0)

    def updateProfile(self):
        self.worker.width=self.width()
        self.worker.height=self.height()
        self.worker.start()
    def callback(self,img):
        self.setImage(img)

class LengthLabel(QtWidgets.QLabel):
    def __init__(self,parent):
        super(LengthLabel,self).__init__(parent)
        self.UpdateText()

    def UpdateText(self):
        self.setText('1 pix = {:.2f} mm'.format(variables.mm_per_pix))
        self.repaint()

class InitializeLabel(QtWidgets.QLabel):
    def __init__(self,parent):
        super(InitializeLabel,self).__init__(parent)
        # self.UpdateText()

    def UpdateText(self,avg):
        self.setText('Initialized.\n Average: {:.2f}.'.format(avg))
        self.repaint()


class VideoLabel(QtWidgets.QLabel):
    def __init__(self,parent):
        super(VideoLabel,self).__init__(parent)
        self.UpdateText()

    def UpdateText(self):
        self.setText('{}×{} px'.format(variables.resolution[0],variables.resolution[1]))
        self.repaint()

class LengthTable(QtWidgets.QTableView):
    mppChanged=QtCore.pyqtSignal()
    def __init__(self,parent):
        super(LengthTable, self).__init__(parent)
        variables.length_cali_model=QtGui.QStandardItemModel(0,2)

        model = variables.length_cali_model
        model.setHorizontalHeaderLabels(['pixel length','actual length'])

        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.setModel(model)
        self.deleteButton=None
        model.itemChanged.connect(self.dumpData)
        # model.itemSelectionChanged.connect(select)

    def select(self):
        model=variables.length_cali_model
        print(model.currentIndex())

    def dumpData(self):
        model=variables.length_cali_model
        n_row=model.rowCount()
        n_col=model.columnCount()
        data=[]
        for i in range(0,n_row):
            col=[]
            for j in range(0,n_col):
                item=model.item(i,j) 
                if item is None:
                    col.append(0)
                else:
                    try:
                        value=float(model.item(i,j).text())
                    except:
                        value=0
                    col.append(value)
                    item.setText("{:.4f}".format(value))
            data.append(col)
        data=np.array(data)
        variables.length_cali_array=data

        x,y=data[:,0],data[:,1]
        Sxy=np.sum(x*y)
        Sx2=np.sum(x*x)

        if Sx2==0:
            variables.mm_per_pix=1
        else:
            variables.mm_per_pix=Sxy/Sx2

        self.mppChanged.emit()



class CurveTable(QtWidgets.QTableView):
    curveChanged=QtCore.pyqtSignal()
    def __init__(self,parent):
        super(CurveTable, self).__init__(parent)
        variables.mag_cali_model=QtGui.QStandardItemModel(0,2)

        model = variables.mag_cali_model
        model.setHorizontalHeaderLabels(['pixel mag','actual mag'])

        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.setModel(model)
        self.deleteButton=None
        model.itemChanged.connect(self.dumpData)
        # model.itemSelectionChanged.connect(select)

    def select(self):
        model=variables.mag_cali_model
        print(model.currentIndex())
        
    def dumpData(self):
        model=variables.mag_cali_model
        n_row=model.rowCount()
        n_col=model.columnCount()
        data=[]
        for i in range(0,n_row):
            col=[]
            for j in range(0,n_col):
                item=model.item(i,j) 
                if item is None:
                    col.append(0)
                else:
                    try:
                        value=float(model.item(i,j).text())
                    except:
                        value=0
                    col.append(value)
                    item.setText("{:.4f}".format(value))
            data.append(col)
        data=np.array(data)
        variables.mag_cali_array=data

        x,y=data[:,0],data[:,1]
        Sxy=np.sum(x*y)
        Sx2=np.sum(x*x)

        if Sx2==0:
            variables.mm_per_pix=1
        else:
            variables.mm_per_pix=Sxy/Sx2

        self.mppChanged.emit()