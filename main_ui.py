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
        MainWindow.resize(1534, 966)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.ToolBox.setMinimumSize(QtCore.QSize(280, 0))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 30, 211, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-color-wheel-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.ToolBox.addTab(self.tab, "")
        self.AnalysisPage = QtWidgets.QWidget()
        self.AnalysisPage.setObjectName("AnalysisPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.AnalysisPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.AnalysisPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 340))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.measure_square = QtWidgets.QPushButton(self.groupBox)
        self.measure_square.setGeometry(QtCore.QRect(30, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_square.sizePolicy().hasHeightForWidth())
        self.measure_square.setSizePolicy(sizePolicy)
        self.measure_square.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-square-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_square.setIcon(icon2)
        self.measure_square.setIconSize(QtCore.QSize(50, 50))
        self.measure_square.setObjectName("measure_square")
        self.vertical_line = QtWidgets.QPushButton(self.groupBox)
        self.vertical_line.setEnabled(True)
        self.vertical_line.setGeometry(QtCore.QRect(30, 130, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_line.sizePolicy().hasHeightForWidth())
        self.vertical_line.setSizePolicy(sizePolicy)
        self.vertical_line.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-line-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vertical_line.setIcon(icon3)
        self.vertical_line.setIconSize(QtCore.QSize(30, 30))
        self.vertical_line.setObjectName("vertical_line")
        self.horizontal_line = QtWidgets.QPushButton(self.groupBox)
        self.horizontal_line.setEnabled(True)
        self.horizontal_line.setGeometry(QtCore.QRect(30, 220, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontal_line.sizePolicy().hasHeightForWidth())
        self.horizontal_line.setSizePolicy(sizePolicy)
        self.horizontal_line.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-line-97.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontal_line.setIcon(icon4)
        self.horizontal_line.setIconSize(QtCore.QSize(30, 30))
        self.horizontal_line.setObjectName("horizontal_line")
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.measure_length = QtWidgets.QPushButton(self.groupBox_3)
        self.measure_length.setEnabled(True)
        self.measure_length.setGeometry(QtCore.QRect(30, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_length.sizePolicy().hasHeightForWidth())
        self.measure_length.setSizePolicy(sizePolicy)
        self.measure_length.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-ruler-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_length.setIcon(icon5)
        self.measure_length.setIconSize(QtCore.QSize(30, 30))
        self.measure_length.setObjectName("measure_length")
        self.measure_angle = QtWidgets.QPushButton(self.groupBox_3)
        self.measure_angle.setEnabled(True)
        self.measure_angle.setGeometry(QtCore.QRect(30, 130, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_angle.sizePolicy().hasHeightForWidth())
        self.measure_angle.setSizePolicy(sizePolicy)
        self.measure_angle.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-angle-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_angle.setIcon(icon6)
        self.measure_angle.setIconSize(QtCore.QSize(30, 30))
        self.measure_angle.setObjectName("measure_angle")
        self.measure_29 = QtWidgets.QPushButton(self.groupBox_3)
        self.measure_29.setEnabled(False)
        self.measure_29.setGeometry(QtCore.QRect(30, 220, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_29.sizePolicy().hasHeightForWidth())
        self.measure_29.setSizePolicy(sizePolicy)
        self.measure_29.setText("")
        self.measure_29.setIconSize(QtCore.QSize(50, 50))
        self.measure_29.setObjectName("measure_29")
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.AnalysisPage)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.calibration_length = QtWidgets.QPushButton(self.frame)
        self.calibration_length.setGeometry(QtCore.QRect(20, 10, 221, 41))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-drafting-compass-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibration_length.setIcon(icon7)
        self.calibration_length.setIconSize(QtCore.QSize(30, 30))
        self.calibration_length.setObjectName("calibration_length")
        self.calibration_magfiled = QtWidgets.QPushButton(self.frame)
        self.calibration_magfiled.setGeometry(QtCore.QRect(20, 60, 221, 41))
        self.calibration_magfiled.setIcon(icon7)
        self.calibration_magfiled.setIconSize(QtCore.QSize(30, 30))
        self.calibration_magfiled.setObjectName("calibration_magfiled")
        self.verticalLayout_7.addWidget(self.frame)
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
        self.resolution = QtWidgets.QLabel(self.frame_7)
        self.resolution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resolution.setObjectName("resolution")
        self.verticalLayout_6.addWidget(self.resolution)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.snap = QtWidgets.QPushButton(self.groupBox_2)
        self.snap.setEnabled(False)
        self.snap.setGeometry(QtCore.QRect(20, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snap.sizePolicy().hasHeightForWidth())
        self.snap.setSizePolicy(sizePolicy)
        self.snap.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-camera-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snap.setIcon(icon8)
        self.snap.setIconSize(QtCore.QSize(50, 50))
        self.snap.setAutoDefault(False)
        self.snap.setDefault(False)
        self.snap.setFlat(False)
        self.snap.setObjectName("snap")
        self.measure_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.measure_18.setEnabled(False)
        self.measure_18.setGeometry(QtCore.QRect(100, 40, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_18.sizePolicy().hasHeightForWidth())
        self.measure_18.setSizePolicy(sizePolicy)
        self.measure_18.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-movie-camera-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_18.setIcon(icon9)
        self.measure_18.setIconSize(QtCore.QSize(50, 50))
        self.measure_18.setObjectName("measure_18")
        self.initBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.initBtn.setGeometry(QtCore.QRect(20, 120, 141, 41))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-analysis-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.initBtn.setIcon(icon10)
        self.initBtn.setIconSize(QtCore.QSize(30, 30))
        self.initBtn.setObjectName("initBtn")
        self.initialized = QtWidgets.QLabel(self.groupBox_2)
        self.initialized.setEnabled(True)
        self.initialized.setGeometry(QtCore.QRect(20, 170, 141, 21))
        self.initialized.setAlignment(QtCore.Qt.AlignCenter)
        self.initialized.setObjectName("initialized")
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.captureList = CaptureList(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captureList.sizePolicy().hasHeightForWidth())
        self.captureList.setSizePolicy(sizePolicy)
        self.captureList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.captureList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.captureList.setObjectName("captureList")
        self.verticalLayout_4.addWidget(self.captureList)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
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
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 251, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.HorizonTab = QtWidgets.QWidget()
        self.HorizonTab.setObjectName("HorizonTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.HorizonTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalProfile = ProfileViewer(self.HorizonTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalProfile.sizePolicy().hasHeightForWidth())
        self.horizontalProfile.setSizePolicy(sizePolicy)
        self.horizontalProfile.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalProfile.setMouseTracking(False)
        self.horizontalProfile.setObjectName("horizontalProfile")
        self.verticalLayout_2.addWidget(self.horizontalProfile)
        self.tabWidget.addTab(self.HorizonTab, "")
        self.VerticalTab = QtWidgets.QWidget()
        self.VerticalTab.setObjectName("VerticalTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.VerticalTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalProfile = ProfileViewer(self.VerticalTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalProfile.sizePolicy().hasHeightForWidth())
        self.verticalProfile.setSizePolicy(sizePolicy)
        self.verticalProfile.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalProfile.setMouseTracking(False)
        self.verticalProfile.setObjectName("verticalProfile")
        self.verticalLayout_3.addWidget(self.verticalProfile)
        self.tabWidget.addTab(self.VerticalTab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_5.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.mainVertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1534, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionone = QtWidgets.QAction(MainWindow)
        self.actionone.setObjectName("actionone")
        self.actiontwo = QtWidgets.QAction(MainWindow)
        self.actiontwo.setObjectName("actiontwo")
        self.actionNothing_Here = QtWidgets.QAction(MainWindow)
        self.actionNothing_Here.setObjectName("actionNothing_Here")
        self.actionNothing_Here_2 = QtWidgets.QAction(MainWindow)
        self.actionNothing_Here_2.setObjectName("actionNothing_Here_2")
        self.menuFIle.addAction(self.actionNothing_Here)
        self.menuFIle.addAction(self.actionNothing_Here_2)
        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.ToolBox.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MagSoft"))
        self.ToolBox.setTabText(self.ToolBox.indexOf(self.DevicePage), _translate("MainWindow", "Device"))
        self.pushButton_3.setText(_translate("MainWindow", "Spectrum"))
        self.ToolBox.setTabText(self.ToolBox.indexOf(self.tab), _translate("MainWindow", "Options"))
        self.groupBox.setTitle(_translate("MainWindow", "Profile"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Measure"))
        self.calibration_length.setText(_translate("MainWindow", " Length  Calibration"))
        self.calibration_magfiled.setText(_translate("MainWindow", " Magnetic Field Calibration"))
        self.ToolBox.setTabText(self.ToolBox.indexOf(self.AnalysisPage), _translate("MainWindow", "Analysis"))
        self.resolution.setText(_translate("MainWindow", "resolution"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Acquire"))
        self.initBtn.setText(_translate("MainWindow", "Initialize"))
        self.initialized.setText(_translate("MainWindow", "Initialized"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Info"))
        self.horizontalProfile.setText(_translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HorizonTab), _translate("MainWindow", "Horizontal Profile"))
        self.verticalProfile.setText(_translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VerticalTab), _translate("MainWindow", "Vertical Profile"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionone.setText(_translate("MainWindow", "one"))
        self.actiontwo.setText(_translate("MainWindow", "two"))
        self.actionNothing_Here.setText(_translate("MainWindow", "Nothing Here"))
        self.actionNothing_Here_2.setText(_translate("MainWindow", "Nothing Here"))
from toupcamdemo import ToupCamWidget
from widgets import CaptureList, MainViewer, ProfileViewer
import res_rc
