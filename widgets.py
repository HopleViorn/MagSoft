from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPen,QPixmap,QImage,QColor
from PyQt5.QtChart import QChartView,QChart,QLineSeries,QValueAxis
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRectF,QPointF
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
        img=np.zeros((1,1))
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
        self.maglut=True

    def __del__(self):
        self.wait()

    def setImg(self,img):
        self.img=img

    def run(self):
        der=variables.get_derivated_img(self.img)
        amax=variables.mag_lut.max()
        amin=variables.mag_lut.min()
        if self.maglut:
            mag=variables.mag_lut[der]
            mag=(mag-amin)/(amax-amin)*255
            mag=mag.astype(np.uint8)
        else:
            mag=der
        img=cv2.applyColorMap(mag,variables.color_map)
        
        self.finish.emit(img,der)

import numpy as np
class Canvas(QtWidgets.QGraphicsScene):
    frameUpdate = QtCore.pyqtSignal(object)
    resolutionChanged = QtCore.pyqtSignal(object)
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
        self.setImage(img)

    def switch_to_grey(self):
        variables.color_map=cv2.COLORMAP_BONE
        self.worker.maglut=False
        self.Update()

    def switch_to_color(self):
        variables.color_map=cv2.COLORMAP_JET
        self.worker.maglut=True
        self.Update()

        
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
        this_resolution=(img.shape[1],img.shape[0])

        if variables.resolution != this_resolution:
            self.resolutionChanged.emit(this_resolution)
        variables.resolution=this_resolution

        self.Update()

    def getScreenshot(self):
        scene=self
        scene_rect = scene.sceneRect()
        image = QImage(int(scene_rect.width()), int(scene_rect.height()), QImage.Format_ARGB32)
        image.fill(QColor(255, 255, 255, 0))  # 设置背景透明
        painter = QPainter(image)
        scene.render(painter, target=QRectF(image.rect()), source=scene_rect)
        painter.end()
        buffer = image.bits()
        buffer.setsize(image.byteCount())
        arr = np.array(buffer).reshape((image.height(), image.width(), 4))
        return arr
        

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
        self.measureItems=[]

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

    def clearItem(self,clearItem):
        for item in clearItem.itemList():    
            self.scene.removeItem(item)

    def clearAll(self):
        for ss in self.measureItems:
            for item in ss.itemList():    
                self.scene.removeItem(item)
        self.measureItems.clear()

    
    def startDraw(self,drawItem,clearItem=None,isMeasure=False):
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.onDrawing=1
        self.drawingItem=drawItem

        if isMeasure:
            self.measureItems.append(drawItem)

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
        img=variables.mag_lut[img]
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
                self.work.setNuclear(self.profile[u:min(d,self.profile.shape[0]),l:min(r,self.profile.shape[1])],self.width(),self.height())
            else:
                self.work.setNuclear(np.zeros((1,1)).astype(np.uint8),self.width(),self.height())
        else:
            self.work.setNuclear(np.zeros((1,1)).astype(np.uint8),self.width(),self.height())
        if variables.currentTab==self.axis:
            self.work.start()

class MagCaliViewerThread(QtCore.QThread):
    finish = QtCore.pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.width=0
        self.height=0

    def __del__(self):
        self.wait()

    def run(self):
        data=variables.mag_cali_array
        if data is None:
            return
        
        mux.lock()
        plt.figure(figsize=(self.width/100,self.height/100))
        plt.subplots_adjust(left=0.25)
        plt.subplots_adjust(bottom=0.2)
        x=np.hstack((0,data[:,0],256))
        y=np.hstack((0,data[:,1],256))
        l1=plt.plot(x,y)
        plt.xlabel('grayscale ')
        plt.ylabel('density  (mT)')

        buffer_ = BytesIO()
        plt.savefig(buffer_,format = 'png')
        plt.close()
        mux.unlock()
        
        buffer_.seek(0)
        dataPIL = PIL.Image.open(buffer_).convert('RGB')
        data = np.asarray(dataPIL)
        self.finish.emit(data)
        buffer_.close()

class MagCaliViewer(ImgView):
    def __init__(self,parent,axis=0):
        super(MagCaliViewer,self).__init__(parent)
        self.worker=MagCaliViewerThread()
        self.worker.finish.connect(self.callback)

        self.updateProfile()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.updateProfile()
        return super().resizeEvent(a0)

    def callback(self,img):
        self.setImage(img)

    def updateProfile(self):
        self.worker.width=self.width()
        self.worker.height=self.height()
        self.worker.start()

    
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
        plt.xlabel('pixel length (px)')
        plt.ylabel('actual length (mm)')

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
        self.UpdateText()

    def UpdateText(self):
        self.setText('Background Average: {:.2f}.'.format(np.mean(variables.base_img)))
        self.repaint()

class CalibrationLabel(QtWidgets.QLabel):
    def __init__(self,parent):
        super(CalibrationLabel,self).__init__(parent)
        self.UpdateText()

    def UpdateText(self):
        self.setText('{}'.format(variables.current_file_name))
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
        variables.len_recovery(np.zeros((0,2)))
        model = variables.length_cali_model

        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.setModel(model)
        model.itemChanged.connect(self.dumpData)

    def deleteSelectedRows(self):
        model=variables.length_cali_model
        selected_indexes = self.selectionModel().selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "No row selected!")
            return
        for index in sorted(selected_indexes, key=lambda x: x.row(), reverse=True):
            model.removeRow(index.row())
        self.dumpData()

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
        if len(data)==0:
            data=np.zeros((0,2))
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
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        variables.mag_recovery(np.zeros((0,2)))
        model = variables.mag_cali_model

        self.setModel(model)
        model.itemChanged.connect(self.dumpData)

    def deleteSelectedRows(self):
        model=variables.mag_cali_model
        selected_indexes = self.selectionModel().selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "No row selected!")
            return
        for index in sorted(selected_indexes, key=lambda x: x.row(), reverse=True):
            model.removeRow(index.row())
        self.dumpData()

    def updateModel(self):
        self.setModel(variables.mag_cali_model)

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
        if len(data)==0:
            data=np.zeros((0,2))
        indx=np.argsort(data[:,0])
        data=data[indx]
        variables.mag_cali_array=data

        temp=[]

        temp.append((0,0))
        for i in range(data.shape[0]):
            temp.append((data[i,0],data[i,1]))
        temp.append((256,256))

        j=0
        l=len(temp)
        variables.mag_lut=np.array([i for i in range(0,256)])
        for i in range(256):
            if j+1<l and temp[j+1][0] <= i:
                j+=1
            x0,x1=temp[j][0],temp[j+1][0]
            if abs(x1-x0)<0.001:
                continue
            y0,y1=temp[j][1],temp[j+1][1]

            point=(i-x0)*(y1-y0)/(x1-x0)+y0
            variables.mag_lut[i]=point

        self.curveChanged.emit()

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
        img=variables.mag_lut[img]
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

class SeriesThread(QtCore.QThread):
    finish = QtCore.pyqtSignal(object)
    def __init__(self,axis):
        super().__init__()
        self.profile=np.zeros((1,1)).astype(np.uint8)
        self.axis=axis

    def setProfile(self,profile):
        self.profile=profile

    def __del__(self):
        self.wait()
    
    def run(self):
        img=self.profile
        img=variables.mag_lut[img]
        w=img.shape[1-self.axis]

        mean=np.mean(img,axis=self.axis)
        maxi=np.max(img,axis=self.axis)
        minn=np.min(img,axis=self.axis)
        if len(mean) > 21 and variables.smooth is True:
            mean=scipy.signal.savgol_filter(mean,21,2) 
            maxi=scipy.signal.savgol_filter(maxi,21,2)
            minn=scipy.signal.savgol_filter(minn,21,2)
        maxima=np.max(mean)
        maxpos=np.argmax(mean)*variables.mm_per_pix
        minima=np.min(mean)
        minpos=np.argmin(mean)*variables.mm_per_pix
        minima=np.min(mean)
        self.finish.emit((mean,maxi,minn,maxima,maxpos,minima,minpos,w))

import scipy

class ProfileChart(QChartView):
    scaleChanged = QtCore.pyqtSignal(object)
    def new_line(self,name):
        series=QLineSeries()
        series.setName(name)
        self.chart.addSeries(series)
        mark=QtWidgets.QGraphicsTextItem(self.chart)
        mark.setDefaultTextColor(series.color())
        return series,mark

    def __init__(self, parent=None):
        super(ProfileChart, self).__init__(parent)
        self.chart = QChart()               # 创建 chart
        self.chart.legend().setAlignment(Qt.AlignRight)
        self.chart.setTitle(["Horizontal Profile","Vertical Profile"][self.axis])
        self.setChart(self.chart)

        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.profile=np.zeros((1,1)).astype(np.uint8)
        self.xlim=0

        self.series0,self.mark0=self.new_line('Average')
        self.series1,self.mark1=self.new_line('Maxima')
        self.series2,self.mark2=self.new_line('Minima')

        axisX = QValueAxis()      # x轴
        axisX.setTitleText("Width (mm)")
        axisY = QValueAxis()      # y轴
        axisY.setTitleText("Field (mT)")    # 轴标题
        self.chart.setAxisX(axisX, self.series0)    # 为序列series0设置坐标轴
        self.chart.setAxisY(axisY, self.series0)
        self.chart.setAxisX(axisX, self.series1)    # 为序列series0设置坐标轴
        self.chart.setAxisY(axisY, self.series1)
        self.chart.setAxisX(axisX, self.series2)    # 为序列series0设置坐标轴
        self.chart.setAxisY(axisY, self.series2)

        blackPen=self.chart.axisY().linePen()
        blackPen.setColor(QColor(255,0,0))

        self.verticalLine = QtWidgets.QGraphicsLineItem(self.chart)
        self.verticalLine.setPen(self.chart.axisY().linePen())

        self.maximaLine = QtWidgets.QGraphicsLineItem(self.chart)
        self.maximaLine.setPen(blackPen)

        self.maximaMark=QtWidgets.QGraphicsTextItem(self.chart)
        self.maximaMark.setDefaultTextColor(QColor(255,0,0))

        self.minimaLine = QtWidgets.QGraphicsLineItem(self.chart)
        self.minimaLine.setPen(blackPen)

        self.minimaMark=QtWidgets.QGraphicsTextItem(self.chart)
        self.minimaMark.setDefaultTextColor(QColor(255,0,0))
        
        self.scene().addItem(self.verticalLine)
        self.scene().addItem(self.maximaLine)
        self.scene().addItem(self.minimaLine)

        self.setMouseTracking(True)

        self.worker=SeriesThread(self.axis)
        self.worker.finish.connect(self.callback)

    def setProfile(self,img):
        self.profile=np.zeros((1,1)).astype(np.uint8) if img is None else img
        self.updateProfile()

    def callback(self,res):
        mean,maxi,minn,maxima,maxpos,minima,minpos,w=res
        if variables.auto_scale:
            self.chart.axisX().setRange(0,w)
            self.chart.axisY().setRange(np.min(variables.mag_lut),np.max(variables.mag_lut))
            variables.Xmin=0
            variables.Xmax=w
            variables.Ymin=np.min(variables.mag_lut)
            variables.Ymax=np.max(variables.mag_lut)
            self.scaleChanged.emit((variables.Xmin,variables.Xmax,variables.Ymin,variables.Ymax))
        else:
            self.chart.axisX().setRange(variables.Xmin,variables.Xmax)
            self.chart.axisY().setRange(variables.Ymin,variables.Ymax)

        self.series0.replace([QPointF(i*variables.mm_per_pix,mean[i]) for i in range(0,len(mean))])
        self.series1.replace([QPointF(i*variables.mm_per_pix,maxi[i]) for i in range(0,len(maxi))])
        self.series2.replace([QPointF(i*variables.mm_per_pix,minn[i]) for i in range(0,len(minn))])

        self.maximaMark.setPlainText('MAX : {:.2f}'.format(maxima))
        self.minimaMark.setPlainText('MIN : {:.2f}'.format(minima))

        maximaPoint=self.chart.mapToPosition(QPointF(maxpos,maxima))
        minimaPoint=self.chart.mapToPosition(QPointF(minpos,minima))
        self.maximaMark.setPos(maximaPoint)
        self.minimaMark.setPos(minimaPoint)
    
    def updateProfile(self):
        if variables.profile_area is not None:
            l,r,u,d=variables.profile_area.getBox()
            l=min(l,self.profile.shape[1])
            r=min(r,self.profile.shape[1])
            u=min(u,self.profile.shape[0])
            d=min(d,self.profile.shape[0])
        else:
            l,r,u,d=1,0,1,0
            
        if r>l and d>u:
            img=self.profile[u:d,l:r]
        else:
            img=np.zeros((1,1)).astype(np.uint8)
        self.worker.setProfile(img)
        self.worker.start()
            
        
        # self.maximaLine.setLine(self.chart.plotArea().left(), maximaPoint.y(), self.chart.plotArea().right(),maximaPoint.y())
        # self.minimaLine.setLine(self.chart.plotArea().left(), minimaPoint.y(), self.chart.plotArea().right(),minimaPoint.y())
        

        if isinstance(variables.profile_area, RectArea):
            self.series1.show()
            self.series2.show()
            self.mark1.show()
            self.mark2.show()
        else:
            self.series1.hide()
            self.series2.hide()
            self.mark1.hide()
            self.mark2.hide()
        
        if variables.show_min_max is True:
            self.minimaMark.show()
            self.maximaMark.show()
        else:
            self.minimaMark.hide()
            self.maximaMark.hide()

    def mouseMoveEvent(self, event):
        pos = event.localPos()
        chart_value = self.chart.mapToValue(QPointF(pos))
        x_value = chart_value.x()
        if x_value < 0 or x_value > self.chart.axisX().max():
            return

        point0 = QPointF(x_value, self.series0.at(x_value).y())
        point1 = QPointF(x_value, self.series1.at(x_value).y())
        point2 = QPointF(x_value, self.series2.at(x_value).y())

        back0=self.chart.mapToPosition(QPointF(point0))
        back1=self.chart.mapToPosition(QPointF(point1))
        back2=self.chart.mapToPosition(QPointF(point2))
        self.verticalLine.setLine(back0.x(), self.chart.plotArea().top(), back0.x(), self.chart.plotArea().bottom())

        self.mark0.setPos(back0)
        self.mark1.setPos(back1)
        self.mark2.setPos(back2)
        self.mark0.setPlainText('{:.2f}'.format(point0.y()))
        self.mark1.setPlainText('{:.2f}'.format(point1.y()))
        self.mark2.setPlainText('{:.2f}'.format(point2.y()))

        super(ProfileChart, self).mouseMoveEvent(event)

class HorizontalChart(ProfileChart):
    def __init__(self, parent=None):
        self.axis=0
        super(HorizontalChart, self).__init__(parent)

class VerticalChart(ProfileChart):
    def __init__(self, parent=None):
        self.axis=1
        super(VerticalChart, self).__init__(parent)