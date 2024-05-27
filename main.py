import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui
import matplotlib.pyplot as plt
import toupcam
import numpy as np

from main_ui import Ui_MainWindow as MainUI
from items import RectArea,LineArea,MeasureLine,MeasureAngle,CalibrationLine,VerticalLine,HorizontalLine,CalibrationRect,DummyRect
import variables

from mag_cali_dialog import Ui_Dialog

class MainUI(QMainWindow, MainUI):
    def __init__(self):
        super(MainUI,self).__init__()
        self.setupUi(self)

class MagDialog(QWidget, Ui_Dialog):
    def __init__(self):
        super(MagDialog,self).__init__()
        self.setupUi(self)

main_ui=None

def lengthChanged():
    main_ui.horizontalProfile.updateProfile()
    main_ui.verticalProfile.updateProfile()

def loadCalibrationFile():
    openfile_name = QtWidgets.QFileDialog.getOpenFileName(main_ui,'Select File','.','calibration file (*.mcfg)')
    if openfile_name[0] != '':
        print('load from {}'.format(openfile_name))
        variables.load_from_file(openfile_name[0])
        update_param()

def saveCalibrationFile():
    savefile_name=QtWidgets.QFileDialog.getSaveFileName(main_ui, "Save File", ".", "calibration file (*.mcfg)")
    if savefile_name[0] != '':
        print('save to {}'.format(savefile_name))
        variables.save_to_file(savefile_name[0])
        main_ui.graphicsView.scene.Update()

def update_param():
    main_ui.graphicsView.scene.Update()
    main_ui.graphicsView.initializeChanged.emit(np.mean(variables.base_img))

def draw_profie(drawType):
    item=drawType()
    main_ui.graphicsView.startDraw(drawItem=item,clearItem=variables.profile_area)
    variables.profile_area=item

def setUpTrigger():
    main_ui.toupcamwidget.lbl_video=main_ui.graphicsView.scene
    main_ui.toupcamwidget.btn_snap=main_ui.snap
    main_ui.toupcamwidget.btn_snap.clicked.connect(main_ui.toupcamwidget.onBtnSnap)

    main_ui.measure_square.clicked.connect(lambda: draw_profie(RectArea))
    main_ui.vertical_line.clicked.connect(lambda: draw_profie(VerticalLine))
    main_ui.horizontal_line.clicked.connect(lambda: draw_profie(HorizontalLine))

    main_ui.measure_length.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=MeasureLine()))
    main_ui.measure_angle.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=MeasureAngle()))
    main_ui.calibration_length.clicked.connect(lambda: (cali_len.init(),main_ui.graphicsView.startDraw(drawItem=cali_len)))
    main_ui.calibration_magfiled.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=CalibrationRect()))

    main_ui.horizontalProfile.axis=0
    main_ui.horizontalProfile.work.axis=0
    main_ui.verticalProfile.axis=1
    main_ui.verticalProfile.work.axis=1

    # main_ui.graphicsView.selectChanged.connect(main_ui.horizontalProfile.setProfile)
    # main_ui.graphicsView.selectChanged.connect(main_ui.verticalProfile.setProfile)
    main_ui.graphicsView.scene.frameUpdate.connect(main_ui.verticalProfile.setProfile)
    main_ui.graphicsView.scene.frameUpdate.connect(main_ui.horizontalProfile.setProfile)



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

    main_ui.loadCalibration.clicked.connect(loadCalibrationFile)
    main_ui.saveCalibration.clicked.connect(saveCalibrationFile)

    main_ui.graphicsView.scene.frameUpdate.connect(main_ui.videoInfo.UpdateText)

if __name__ == '__main__':

    variables.rgb_mt.append(DummyRect(avg=0,md=0))
    variables.rgb_mt.append(DummyRect(avg=256,md=999))

    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling,True)  
    QtCore.QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps,True)
    QtGui.QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough,True)  
    toupcam.Toupcam.GigeEnable(None, None)
    app = QApplication(sys.argv)
    main_ui=MainUI()
    # test=MagDialog()

    cali_len=CalibrationLine()

    setUpTrigger()
    
    main_ui.show()
    # test.show()


    
    sys.exit(app.exec_())