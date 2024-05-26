import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui
import matplotlib.pyplot as plt
import toupcam

from main_ui import Ui_MainWindow as MainUI
from items import RectArea,LineArea,MeasureLine,MeasureAngle,CalibrationLine,VerticalLine,HorizontalLine,CalibrationRect,DummyRect
import variables

class MainUI(QMainWindow, MainUI):
    def __init__(self):
        super(MainUI,self).__init__()
        self.setupUi(self)

main_ui=None

def lengthChanged():
    main_ui.horizontalProfile.updateProfile()
    main_ui.verticalProfile.updateProfile()

def setUpTrigger():
    main_ui.toupcamwidget.lbl_video=main_ui.graphicsView.scene
    main_ui.toupcamwidget.btn_snap=main_ui.snap
    main_ui.toupcamwidget.btn_snap.clicked.connect(main_ui.toupcamwidget.onBtnSnap)

    main_ui.measure_square.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=RectArea()))
    main_ui.vertical_line.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=VerticalLine()))
    main_ui.horizontal_line.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=HorizontalLine()))
    main_ui.measure_length.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=MeasureLine()))
    main_ui.measure_angle.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=MeasureAngle()))
    main_ui.calibration_length.clicked.connect(lambda: (cali_len.init(),main_ui.graphicsView.startDraw(drawItem=cali_len)))
    main_ui.calibration_magfiled.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=CalibrationRect()))

    main_ui.horizontalProfile.axis=0
    main_ui.horizontalProfile.work.axis=0
    main_ui.verticalProfile.axis=1
    main_ui.verticalProfile.work.axis=1

    main_ui.graphicsView.selectChanged.connect(main_ui.horizontalProfile.setProfile)
    main_ui.graphicsView.selectChanged.connect(main_ui.verticalProfile.setProfile)

    main_ui.graphicsView.magCaliChanged.connect(main_ui.mag_info.updateProfile)

    main_ui.graphicsView.magCaliChanged.connect(main_ui.horizontalProfile.updateProfile)
    main_ui.graphicsView.magCaliChanged.connect(main_ui.verticalProfile.updateProfile)

    main_ui.graphicsView.lengthCaliChanged.connect(main_ui.horizontalProfile.updateProfile)
    main_ui.graphicsView.lengthCaliChanged.connect(main_ui.verticalProfile.updateProfile)

    main_ui.graphicsView.lengthCaliChanged.connect(main_ui.length_info.UpdateText)

    main_ui.captureList.selectImg.connect(main_ui.graphicsView.scene.setImage)
    main_ui.toupcamwidget.captured.connect(main_ui.captureList.addCapture)

    main_ui.initBtn.clicked.connect(main_ui.graphicsView.onInitialize)

    main_ui.graphicsView.initializeChanged.connect(main_ui.initializeLabel.UpdateText)

    # main_ui.graphicsView.scene.frameUpdate.connect(main_ui.horizontalProfile.updateProfile)
    # main_ui.graphicsView.scene.frameUpdate.connect(main_ui.verticalProfile.updateProfile)


# sys._excepthook = sys.excepthook 
# def exception_hook(exctype, value, traceback):
#     print(exctype, value, traceback)
#     sys._excepthook(exctype, value, traceback) 
#     sys.exit(1) 
# sys.excepthook = exception_hook 

if __name__ == '__main__':

    variables.rgb_mt.append(DummyRect(avg=0,md=0))
    variables.rgb_mt.append(DummyRect(avg=256,md=999))

    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling,True)  
    QtCore.QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps,True)
    QtGui.QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough,True)  
    toupcam.Toupcam.GigeEnable(None, None)
    app = QApplication(sys.argv)
    main_ui=MainUI()

    cali_len=CalibrationLine()

    setUpTrigger()
    
    main_ui.show()
    
    sys.exit(app.exec_())