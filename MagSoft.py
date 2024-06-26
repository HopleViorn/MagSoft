import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QGraphicsScene,QGraphicsPixmapItem,QDialog,QMessageBox
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui
import matplotlib.pyplot as plt
import toupcam
import numpy as np

from main_ui import Ui_MainWindow as MainUI
from items import RectArea,LineArea,MeasureLine,MeasureAngle,CalibrationLine,VerticalLine,HorizontalLine,CalibrationRect,DummyRect
import variables

def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

from mag_cali_dialog import Ui_Dialog as MagUI
from length_cali_dialog import Ui_Dialog as lengthUI

class MainUI(QMainWindow, MainUI):
    def __init__(self):
        super(MainUI,self).__init__()
        self.setupUi(self)
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        lengthcali_ui.close()
        magcali_ui.close()

class MagDialog(QDialog, MagUI):
    def __init__(self):
        super(MagDialog,self).__init__()
        self.setupUi(self)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        delete_cali()
        
class LengthDialog(QDialog, lengthUI):
    def __init__(self):
        super(LengthDialog,self).__init__()
        self.setupUi(self)
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        delete_cali()

main_ui=None

def lengthChanged():
    main_ui.horizontalChart.updateProfile()
    main_ui.verticalChart.updateProfile()
    main_ui.length_info.UpdateText()

def magChanged():
    main_ui.horizontalChart.updateProfile()
    main_ui.verticalChart.updateProfile()

def loadCalibrationFile():
    openfile_name = QtWidgets.QFileDialog.getOpenFileName(main_ui,'Select File','.','calibration file (*.mcfg)')
    if openfile_name[0] != '':
        print('load from {}'.format(openfile_name))
        variables.load_from_file(openfile_name[0])
        update_param()
        magcali_ui.mag_info.updateProfile()
        main_ui.calibrationFile.UpdateText()

def saveCalibrationFile():
    savefile_name=QtWidgets.QFileDialog.getSaveFileName(main_ui, "Save File", ".", "calibration file (*.mcfg)")
    if savefile_name[0] != '':
        print('save to {}'.format(savefile_name))
        variables.save_to_file(savefile_name[0])
        main_ui.graphicsView.scene.Update()
        main_ui.calibrationFile.UpdateText()

def loadScreenshot():
    openfile_name = QtWidgets.QFileDialog.getOpenFileName(main_ui,'Select File','.','image file (*.png)')
    if openfile_name[0] != '':
        print('load from {}'.format(openfile_name))
        img=cv_imread(openfile_name[0]).astype(np.float32)
        img = img[:,:,0]+img[:,:,1]+img[:,:,2]
        img = (img/3).astype(np.uint8)
        main_ui.toupcamwidget.closeCamera()
        main_ui.graphicsView.scene.setImage(img)
        import os
        main_ui.captureList.addCapture(img,os.path.basename(openfile_name[0]))

from PyQt5.QtGui import QImage,QPainter,QColor
from PyQt5.QtCore import QRectF
import cv2


def saveScreenshot():
    savefile_name=QtWidgets.QFileDialog.getSaveFileName(main_ui, "Save File", ".", 'image file (*.png)')
    if savefile_name[0] != '':
        print('save to {}'.format(savefile_name))
        # arr = main_ui.graphicsView.scene.getScreenshot()
        arr = main_ui.graphicsView.scene.single_img
        arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGRA)
        cv2.imwrite(savefile_name[0], arr)

def update_param():
    main_ui.graphicsView.scene.Update()
    main_ui.graphicsView.initializeChanged.emit(np.mean(variables.base_img))

def draw_profie(drawType):
    item=drawType()
    main_ui.graphicsView.startDraw(drawItem=item,clearItem=variables.profile_area)
    variables.profile_area=item

def draw_cali_mag():
    item=CalibrationRect()
    main_ui.graphicsView.scene.Update()
    main_ui.graphicsView.scene.frameUpdate.connect(item.setProfile)
    main_ui.graphicsView.startDraw(drawItem=item,clearItem=variables.cali_mag)
    variables.cali_mag=item

def draw_cali_len():
    item=CalibrationLine()
    main_ui.graphicsView.startDraw(drawItem=item,clearItem=variables.cali_len)
    variables.cali_len=item

def delete_profile():
    if variables.profile_area is not None:
        main_ui.graphicsView.clearItem(variables.profile_area)
        variables.profile_area=None

def delete_cali():
    if variables.cali_mag is not None:
        main_ui.graphicsView.clearItem(variables.cali_mag)
        variables.cali_mag=None
    if variables.cali_len is not None:
        main_ui.graphicsView.clearItem(variables.cali_len)
        variables.cali_len=None

def setUpProfileSettings():
    main_ui.autoScale.setChecked(variables.auto_scale)
    main_ui.yMax.setEnabled(not variables.auto_scale)
    main_ui.yMin.setEnabled(not variables.auto_scale)
    main_ui.xMax.setEnabled(not variables.auto_scale)
    main_ui.xMin.setEnabled(not variables.auto_scale)
    def onAutoScaleChanged():
        variables.auto_scale=main_ui.autoScale.isChecked()
        main_ui.verticalChart.updateProfile()
        main_ui.horizontalChart.updateProfile()
        main_ui.yMax.setEnabled(not variables.auto_scale)
        main_ui.yMin.setEnabled(not variables.auto_scale)
        main_ui.xMax.setEnabled(not variables.auto_scale)
        main_ui.xMin.setEnabled(not variables.auto_scale)
        onScaleChanged()

    def onScaleChanged():
        variables.Ymin=main_ui.yMin.value()
        variables.Ymax=main_ui.yMax.value()
        variables.Xmin=main_ui.xMin.value()
        variables.Xmax=main_ui.xMax.value()

        main_ui.verticalChart.updateProfile()
        main_ui.horizontalChart.updateProfile()

    main_ui.autoScale.stateChanged.connect(onAutoScaleChanged)
    main_ui.yMax.valueChanged.connect(onScaleChanged)
    main_ui.yMin.valueChanged.connect(onScaleChanged)
    main_ui.xMax.valueChanged.connect(onScaleChanged)
    main_ui.xMin.valueChanged.connect(onScaleChanged)

    main_ui.showMinMax.setChecked(variables.show_min_max)
    def onShowMinMaxChanged():
        variables.show_min_max=main_ui.showMinMax.isChecked()
        main_ui.verticalChart.updateProfile()
        main_ui.horizontalChart.updateProfile()
    main_ui.showMinMax.stateChanged.connect(onShowMinMaxChanged)

    main_ui.smooth.setChecked(variables.smooth)
    def onSmoothChanged():
        variables.smooth=main_ui.smooth.isChecked()
        main_ui.verticalChart.updateProfile()
        main_ui.horizontalChart.updateProfile()
    main_ui.smooth.stateChanged.connect(onSmoothChanged)

def setUpTrigger():
    main_ui.toupcamwidget.lbl_video=main_ui.graphicsView.scene
    main_ui.toupcamwidget.btn_snap=main_ui.snap
    main_ui.toupcamwidget.btn_snap.clicked.connect(main_ui.toupcamwidget.onBtnSnap)

    main_ui.measure_square.clicked.connect(lambda: draw_profie(RectArea))
    main_ui.vertical_line.clicked.connect(lambda: draw_profie(VerticalLine))
    main_ui.horizontal_line.clicked.connect(lambda: draw_profie(HorizontalLine))

    main_ui.measure_length.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=MeasureLine(),isMeasure=True))
    main_ui.measure_angle.clicked.connect(lambda: main_ui.graphicsView.startDraw(drawItem=MeasureAngle(),isMeasure=True))
    
    lengthcali_ui.calibration_length.clicked.connect(draw_cali_len)
    magcali_ui.calibration_mag.clicked.connect(draw_cali_mag)

    main_ui.graphicsView.scene.frameUpdate.connect(main_ui.horizontalChart.setProfile)
    main_ui.graphicsView.scene.frameUpdate.connect(main_ui.verticalChart.setProfile)
   
    main_ui.graphicsView.magCaliChanged.connect(magChanged)
    main_ui.graphicsView.lengthCaliChanged.connect(lengthChanged)

    main_ui.captureList.selectImg.connect(main_ui.graphicsView.scene.setImage)
    main_ui.captureList.selectImg.connect(main_ui.toupcamwidget.closeCamera)
    main_ui.toupcamwidget.captured.connect(main_ui.captureList.addCapture)

    main_ui.initBtn.clicked.connect(main_ui.graphicsView.onInitialize)

    main_ui.graphicsView.initializeChanged.connect(main_ui.initializeLabel.UpdateText)

    main_ui.loadCalibration.clicked.connect(loadCalibrationFile)
    main_ui.saveCalibration.clicked.connect(saveCalibrationFile)

    main_ui.graphicsView.scene.frameUpdate.connect(main_ui.videoInfo.UpdateText)

    # main_ui.profileTab.currentChanged.connect(variables.setCurrentTab)
    # main_ui.profileTab.currentChanged.connect(main_ui.verticalProfile.updateProfile)
    # main_ui.profileTab.currentChanged.connect(main_ui.horizontalProfile.updateProfile)


    main_ui.setupLength.clicked.connect((lambda: lengthcali_ui.show()))
    main_ui.setupLength.clicked.connect(main_ui.graphicsView.scene.switch_to_grey)
    main_ui.setupLength.clicked.connect(lambda: main_ui.colorCombo.setCurrentIndex(1))
    main_ui.graphicsView.lengthCaliChanged.connect(lambda:lengthcali_ui.show())
    lengthcali_ui.lengthTable.mppChanged.connect(lengthChanged)
    lengthcali_ui.lengthTable.mppChanged.connect(lengthcali_ui.len_info.updateProfile)
    lengthcali_ui.deleteButton.clicked.connect(lengthcali_ui.lengthTable.deleteSelectedRows)
    lengthcali_ui.calibration_length.clicked.connect(lambda:lengthcali_ui.hide())
    
    lengthcali_ui.OK.clicked.connect(lambda:lengthcali_ui.hide())
    lengthcali_ui.OK.clicked.connect(delete_cali)
    lengthcali_ui.OK.clicked.connect(main_ui.graphicsView.scene.switch_to_color)
    lengthcali_ui.OK.clicked.connect(lambda: main_ui.colorCombo.setCurrentIndex(0))

    main_ui.setupMag.clicked.connect((lambda: magcali_ui.show()))
    main_ui.setupMag.clicked.connect(main_ui.graphicsView.scene.switch_to_grey)
    main_ui.setupMag.clicked.connect(lambda: main_ui.colorCombo.setCurrentIndex(1))

    main_ui.graphicsView.magCaliChanged.connect(lambda:magcali_ui.show())
    magcali_ui.magTable.curveChanged.connect(magChanged)
    magcali_ui.magTable.curveChanged.connect(magcali_ui.mag_info.updateProfile)

    magcali_ui.deleteButton.clicked.connect(magcali_ui.magTable.deleteSelectedRows)
    magcali_ui.calibration_mag.clicked.connect(lambda:magcali_ui.hide())
    
    magcali_ui.OK.clicked.connect(lambda:magcali_ui.hide())
    magcali_ui.OK.clicked.connect(delete_cali)
    magcali_ui.OK.clicked.connect(main_ui.graphicsView.scene.switch_to_color)
    magcali_ui.OK.clicked.connect(lambda: main_ui.colorCombo.setCurrentIndex(0))

    main_ui.clearMark.clicked.connect(main_ui.graphicsView.clearAll)
    main_ui.clearProfile.clicked.connect(delete_profile)

    main_ui.graphicsView.scene.resolutionChanged.connect(main_ui.graphicsView.clearAll)
    main_ui.graphicsView.scene.resolutionChanged.connect(delete_profile)
    main_ui.graphicsView.scene.resolutionChanged.connect(delete_cali)

    # main_ui.saveScreenshot.clicked.connect(saveScreenshot)
    main_ui.loadScreenshot.clicked.connect(loadScreenshot)


    main_ui.colorCombo.currentIndexChanged.connect(lambda x: main_ui.graphicsView.scene.switch_to_color() if x==0 else main_ui.graphicsView.scene.switch_to_grey())

    setUpProfileSettings()



if __name__ == '__main__':
    # QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling,True)  
    # QtCore.QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps,True)
    # QtGui.QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough,True)  
    toupcam.Toupcam.GigeEnable(None, None)
    app = QApplication(sys.argv)
    main_ui=MainUI()
    magcali_ui=MagDialog()
    lengthcali_ui=LengthDialog()

    main_ui.length_info.UpdateText()
    main_ui.initializeLabel.UpdateText()
    main_ui.calibrationFile.UpdateText()

    lengthcali_ui.setWindowIcon(main_ui.windowIcon())
    lengthcali_ui.setWindowTitle('Length Calibration')
    magcali_ui.setWindowIcon(main_ui.windowIcon())
    magcali_ui.setWindowTitle('Curve Calibration')

    setUpTrigger()

    main_ui.show()
    
    msgBox = QMessageBox(main_ui)
    msgBox.setWindowTitle('Welcome')
    msgBox.setText('Would you like to load calibration \nbefore you start?')

    loadFromFileButton = msgBox.addButton('Load from file', QMessageBox.ActionRole)
    useDefaultButton = msgBox.addButton('Use default', QMessageBox.ActionRole)
    msgBox.exec_()

    if msgBox.clickedButton() == loadFromFileButton:
        main_ui.loadCalibration.clicked.emit()

    sys.exit(app.exec_())