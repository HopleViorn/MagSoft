# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1694, 890)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-science-class-with-nucleus-and-atoms-revolving-around-it-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainVertical = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainVertical.sizePolicy().hasHeightForWidth())
        self.mainVertical.setSizePolicy(sizePolicy)
        self.mainVertical.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainVertical.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainVertical.setObjectName("mainVertical")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mainVertical)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.mainVertical)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setObjectName("splitter")
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ToolBox = QtWidgets.QTabWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolBox.sizePolicy().hasHeightForWidth())
        self.ToolBox.setSizePolicy(sizePolicy)
        self.ToolBox.setMinimumSize(QtCore.QSize(330, 0))
        self.ToolBox.setObjectName("ToolBox")
        self.DevicePage = QtWidgets.QWidget()
        self.DevicePage.setObjectName("DevicePage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DevicePage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toupcamwidget = ToupCamWidget(self.DevicePage)
        self.toupcamwidget.setObjectName("toupcamwidget")
        self.verticalLayout_5.addWidget(self.toupcamwidget)
        self.ToolBox.addTab(self.DevicePage, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 20, 291, 201))
        self.groupBox_5.setObjectName("groupBox_5")
        self.loadCalibration = QtWidgets.QPushButton(self.groupBox_5)
        self.loadCalibration.setGeometry(QtCore.QRect(20, 30, 251, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-upload-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadCalibration.setIcon(icon1)
        self.loadCalibration.setIconSize(QtCore.QSize(20, 20))
        self.loadCalibration.setCheckable(False)
        self.loadCalibration.setAutoRepeat(False)
        self.loadCalibration.setObjectName("loadCalibration")
        self.saveCalibration = QtWidgets.QPushButton(self.groupBox_5)
        self.saveCalibration.setGeometry(QtCore.QRect(20, 90, 251, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-download-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveCalibration.setIcon(icon2)
        self.saveCalibration.setIconSize(QtCore.QSize(20, 30))
        self.saveCalibration.setObjectName("saveCalibration")
        self.calibrationFile = CalibrationLabel(self.groupBox_5)
        self.calibrationFile.setGeometry(QtCore.QRect(30, 150, 241, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.calibrationFile.sizePolicy().hasHeightForWidth())
        self.calibrationFile.setSizePolicy(sizePolicy)
        self.calibrationFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.calibrationFile.setObjectName("calibrationFile")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 240, 291, 281))
        self.groupBox_6.setObjectName("groupBox_6")
        self.initBtn = QtWidgets.QPushButton(self.groupBox_6)
        self.initBtn.setGeometry(QtCore.QRect(20, 30, 251, 41))
        self.initBtn.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-image-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.initBtn.setIcon(icon3)
        self.initBtn.setIconSize(QtCore.QSize(30, 30))
        self.initBtn.setObjectName("initBtn")
        self.setupLength = QtWidgets.QPushButton(self.groupBox_6)
        self.setupLength.setGeometry(QtCore.QRect(20, 120, 251, 41))
        self.setupLength.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-drafting-compass-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setupLength.setIcon(icon4)
        self.setupLength.setIconSize(QtCore.QSize(30, 30))
        self.setupLength.setObjectName("setupLength")
        self.setupMag = QtWidgets.QPushButton(self.groupBox_6)
        self.setupMag.setGeometry(QtCore.QRect(20, 210, 251, 41))
        self.setupMag.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-line-chart-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setupMag.setIcon(icon5)
        self.setupMag.setIconSize(QtCore.QSize(30, 30))
        self.setupMag.setObjectName("setupMag")
        self.length_info = LengthLabel(self.groupBox_6)
        self.length_info.setGeometry(QtCore.QRect(30, 170, 241, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.length_info.sizePolicy().hasHeightForWidth())
        self.length_info.setSizePolicy(sizePolicy)
        self.length_info.setObjectName("length_info")
        self.initializeLabel = InitializeLabel(self.groupBox_6)
        self.initializeLabel.setEnabled(True)
        self.initializeLabel.setGeometry(QtCore.QRect(30, 80, 241, 31))
        self.initializeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.initializeLabel.setObjectName("initializeLabel")
        self.ToolBox.addTab(self.tab, "")
        self.AnalysisPage = QtWidgets.QWidget()
        self.AnalysisPage.setObjectName("AnalysisPage")
        self.groupBox = QtWidgets.QGroupBox(self.AnalysisPage)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 291, 201))
        self.groupBox.setObjectName("groupBox")
        self.measure_square = QtWidgets.QPushButton(self.groupBox)
        self.measure_square.setGeometry(QtCore.QRect(20, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_square.sizePolicy().hasHeightForWidth())
        self.measure_square.setSizePolicy(sizePolicy)
        self.measure_square.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-square-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_square.setIcon(icon6)
        self.measure_square.setIconSize(QtCore.QSize(50, 50))
        self.measure_square.setObjectName("measure_square")
        self.horizontal_line = QtWidgets.QPushButton(self.groupBox)
        self.horizontal_line.setEnabled(True)
        self.horizontal_line.setGeometry(QtCore.QRect(110, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontal_line.sizePolicy().hasHeightForWidth())
        self.horizontal_line.setSizePolicy(sizePolicy)
        self.horizontal_line.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-line-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontal_line.setIcon(icon7)
        self.horizontal_line.setIconSize(QtCore.QSize(30, 30))
        self.horizontal_line.setObjectName("horizontal_line")
        self.vertical_line = QtWidgets.QPushButton(self.groupBox)
        self.vertical_line.setEnabled(True)
        self.vertical_line.setGeometry(QtCore.QRect(200, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_line.sizePolicy().hasHeightForWidth())
        self.vertical_line.setSizePolicy(sizePolicy)
        self.vertical_line.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-line-97.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vertical_line.setIcon(icon8)
        self.vertical_line.setIconSize(QtCore.QSize(30, 30))
        self.vertical_line.setObjectName("vertical_line")
        self.clearProfile = QtWidgets.QPushButton(self.groupBox)
        self.clearProfile.setGeometry(QtCore.QRect(20, 130, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearProfile.sizePolicy().hasHeightForWidth())
        self.clearProfile.setSizePolicy(sizePolicy)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-erase-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearProfile.setIcon(icon9)
        self.clearProfile.setIconSize(QtCore.QSize(30, 50))
        self.clearProfile.setObjectName("clearProfile")
        self.groupBox_3 = QtWidgets.QGroupBox(self.AnalysisPage)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 240, 291, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.measure_length = QtWidgets.QPushButton(self.groupBox_3)
        self.measure_length.setEnabled(True)
        self.measure_length.setGeometry(QtCore.QRect(20, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_length.sizePolicy().hasHeightForWidth())
        self.measure_length.setSizePolicy(sizePolicy)
        self.measure_length.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-ruler-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_length.setIcon(icon10)
        self.measure_length.setIconSize(QtCore.QSize(30, 30))
        self.measure_length.setObjectName("measure_length")
        self.measure_angle = QtWidgets.QPushButton(self.groupBox_3)
        self.measure_angle.setEnabled(True)
        self.measure_angle.setGeometry(QtCore.QRect(110, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_angle.sizePolicy().hasHeightForWidth())
        self.measure_angle.setSizePolicy(sizePolicy)
        self.measure_angle.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-angle-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_angle.setIcon(icon11)
        self.measure_angle.setIconSize(QtCore.QSize(30, 30))
        self.measure_angle.setObjectName("measure_angle")
        self.clearMark = QtWidgets.QPushButton(self.groupBox_3)
        self.clearMark.setGeometry(QtCore.QRect(20, 130, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearMark.sizePolicy().hasHeightForWidth())
        self.clearMark.setSizePolicy(sizePolicy)
        self.clearMark.setIcon(icon9)
        self.clearMark.setIconSize(QtCore.QSize(30, 50))
        self.clearMark.setObjectName("clearMark")
        self.ToolBox.addTab(self.AnalysisPage, "")
        self.horizontalLayout.addWidget(self.ToolBox)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView = MainViewer(self.frame_7)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_6.addWidget(self.graphicsView)
        self.videoInfo = VideoLabel(self.frame_7)
        self.videoInfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.videoInfo.setObjectName("videoInfo")
        self.verticalLayout_6.addWidget(self.videoInfo)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.snap = QtWidgets.QPushButton(self.groupBox_2)
        self.snap.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snap.sizePolicy().hasHeightForWidth())
        self.snap.setSizePolicy(sizePolicy)
        self.snap.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-camera-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snap.setIcon(icon12)
        self.snap.setIconSize(QtCore.QSize(30, 30))
        self.snap.setAutoDefault(False)
        self.snap.setDefault(False)
        self.snap.setFlat(False)
        self.snap.setObjectName("snap")
        self.verticalLayout_9.addWidget(self.snap)
        self.loadScreenshot = QtWidgets.QPushButton(self.groupBox_2)
        self.loadScreenshot.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadScreenshot.sizePolicy().hasHeightForWidth())
        self.loadScreenshot.setSizePolicy(sizePolicy)
        self.loadScreenshot.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"}")
        self.loadScreenshot.setIcon(icon1)
        self.loadScreenshot.setIconSize(QtCore.QSize(30, 30))
        self.loadScreenshot.setAutoDefault(False)
        self.loadScreenshot.setDefault(False)
        self.loadScreenshot.setFlat(False)
        self.loadScreenshot.setObjectName("loadScreenshot")
        self.verticalLayout_9.addWidget(self.loadScreenshot)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.captureList = CaptureList(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captureList.sizePolicy().hasHeightForWidth())
        self.captureList.setSizePolicy(sizePolicy)
        self.captureList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.captureList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.captureList.setObjectName("captureList")
        self.verticalLayout_9.addWidget(self.captureList)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.colorCombo = QtWidgets.QComboBox(self.groupBox_7)
        self.colorCombo.setObjectName("colorCombo")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-color-wheel-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorCombo.addItem(icon13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-grey-wheel-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorCombo.addItem(icon14, "")
        self.verticalLayout_7.addWidget(self.colorCombo)
        self.verticalLayout_9.addWidget(self.groupBox_7)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setMinimumSize(QtCore.QSize(280, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 251, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.xMax = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.xMax.setMinimum(-99999.0)
        self.xMax.setMaximum(99999.0)
        self.xMax.setProperty("value", 100.0)
        self.xMax.setObjectName("xMax")
        self.gridLayout.addWidget(self.xMax, 3, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.yMax = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.yMax.setMinimum(-99999.0)
        self.yMax.setMaximum(99998.0)
        self.yMax.setProperty("value", 255.0)
        self.yMax.setObjectName("yMax")
        self.gridLayout.addWidget(self.yMax, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.xMin = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.xMin.setMinimum(-99999.0)
        self.xMin.setMaximum(99999.0)
        self.xMin.setObjectName("xMin")
        self.gridLayout.addWidget(self.xMin, 3, 1, 1, 1)
        self.yMin = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.yMin.setMinimum(-99999.0)
        self.yMin.setMaximum(99999.0)
        self.yMin.setProperty("value", -255.0)
        self.yMin.setObjectName("yMin")
        self.gridLayout.addWidget(self.yMin, 2, 1, 1, 1)
        self.autoScale = QtWidgets.QCheckBox(self.groupBox_4)
        self.autoScale.setObjectName("autoScale")
        self.gridLayout.addWidget(self.autoScale, 1, 0, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 170, 251, 111))
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.smooth = QtWidgets.QCheckBox(self.groupBox_8)
        self.smooth.setObjectName("smooth")
        self.gridLayout_2.addWidget(self.smooth, 1, 0, 1, 1)
        self.showMinMax = QtWidgets.QCheckBox(self.groupBox_8)
        self.showMinMax.setObjectName("showMinMax")
        self.gridLayout_2.addWidget(self.showMinMax, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.profileTab = QtWidgets.QTabWidget(self.frame_4)
        self.profileTab.setMinimumSize(QtCore.QSize(0, 300))
        self.profileTab.setObjectName("profileTab")
        self.HorizonTab = QtWidgets.QWidget()
        self.HorizonTab.setObjectName("HorizonTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.HorizonTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalChart = HorizontalChart(self.HorizonTab)
        self.horizontalChart.setObjectName("horizontalChart")
        self.verticalLayout_2.addWidget(self.horizontalChart)
        self.profileTab.addTab(self.HorizonTab, "")
        self.VerticalTab = QtWidgets.QWidget()
        self.VerticalTab.setObjectName("VerticalTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.VerticalTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalChart = VerticalChart(self.VerticalTab)
        self.verticalChart.setObjectName("verticalChart")
        self.verticalLayout_3.addWidget(self.verticalChart)
        self.profileTab.addTab(self.VerticalTab, "")
        self.horizontalLayout_2.addWidget(self.profileTab)
        self.horizontalLayout_5.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.mainVertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionone = QtWidgets.QAction(MainWindow)
        self.actionone.setObjectName("actionone")
        self.actiontwo = QtWidgets.QAction(MainWindow)
        self.actiontwo.setObjectName("actiontwo")
        self.actionNothing_Here = QtWidgets.QAction(MainWindow)
        self.actionNothing_Here.setObjectName("actionNothing_Here")
        self.actionNothing_Here_2 = QtWidgets.QAction(MainWindow)
        self.actionNothing_Here_2.setObjectName("actionNothing_Here_2")

        self.retranslateUi(MainWindow)
        self.ToolBox.setCurrentIndex(1)
        self.profileTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MagSoft"))
        self.ToolBox.setTabText(self.ToolBox.indexOf(self.DevicePage), _translate("MainWindow", "Device"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Calibration Files"))
        self.loadCalibration.setText(_translate("MainWindow", " Load calibration"))
        self.saveCalibration.setText(_translate("MainWindow", " Save calibration"))
        self.calibrationFile.setText(_translate("MainWindow", "default"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Edit Calibration"))
        self.initBtn.setText(_translate("MainWindow", " Background initialize"))
        self.setupLength.setText(_translate("MainWindow", " Length calibration"))
        self.setupMag.setText(_translate("MainWindow", " Curve calibration"))
        self.length_info.setText(_translate("MainWindow", "Length not calibrated"))
        self.initializeLabel.setText(_translate("MainWindow", "Not initialized"))
        self.ToolBox.setTabText(self.ToolBox.indexOf(self.tab), _translate("MainWindow", "Calibration"))
        self.groupBox.setTitle(_translate("MainWindow", "Profile"))
        self.clearProfile.setText(_translate("MainWindow", "  Clear all"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Marks"))
        self.clearMark.setText(_translate("MainWindow", "  Clear All"))
        self.ToolBox.setTabText(self.ToolBox.indexOf(self.AnalysisPage), _translate("MainWindow", "Analysis"))
        self.videoInfo.setText(_translate("MainWindow", "resolution"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Acquire"))
        self.snap.setText(_translate("MainWindow", "  Capture"))
        self.loadScreenshot.setText(_translate("MainWindow", "  Load image"))
        self.label_2.setText(_translate("MainWindow", "Image List"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Pseudo-Color"))
        self.label.setText(_translate("MainWindow", "color map"))
        self.colorCombo.setItemText(0, _translate("MainWindow", "color"))
        self.colorCombo.setItemText(1, _translate("MainWindow", "grey"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Axis"))
        self.label_6.setText(_translate("MainWindow", "to"))
        self.label_5.setText(_translate("MainWindow", "X:"))
        self.label_3.setText(_translate("MainWindow", "Y:"))
        self.label_4.setText(_translate("MainWindow", "to"))
        self.autoScale.setText(_translate("MainWindow", "Autoscale"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Settings"))
        self.smooth.setText(_translate("MainWindow", "Smooth"))
        self.showMinMax.setText(_translate("MainWindow", "Show average min-max"))
        self.profileTab.setTabText(self.profileTab.indexOf(self.HorizonTab), _translate("MainWindow", "Horizontal Profile"))
        self.profileTab.setTabText(self.profileTab.indexOf(self.VerticalTab), _translate("MainWindow", "Vertical Profile"))
        self.actionone.setText(_translate("MainWindow", "one"))
        self.actiontwo.setText(_translate("MainWindow", "two"))
        self.actionNothing_Here.setText(_translate("MainWindow", "Nothing Here"))
        self.actionNothing_Here_2.setText(_translate("MainWindow", "Nothing Here"))
from toupcamdemo import ToupCamWidget
from widgets import CalibrationLabel, CaptureList, HorizontalChart, InitializeLabel, LengthLabel, MainViewer, VerticalChart, VideoLabel
import res_rc
