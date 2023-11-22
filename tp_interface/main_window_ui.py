# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 641)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Row_01 = QtWidgets.QHBoxLayout()
        self.Row_01.setObjectName("Row_01")
        self.toolTab = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolTab.sizePolicy().hasHeightForWidth())
        self.toolTab.setSizePolicy(sizePolicy)
        self.toolTab.setMinimumSize(QtCore.QSize(430, 0))
        self.toolTab.setMaximumSize(QtCore.QSize(500, 16777215))
        self.toolTab.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.toolTab.setAutoFillBackground(False)
        self.toolTab.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.toolTab.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.toolTab.setDocumentMode(False)
        self.toolTab.setObjectName("toolTab")
        self.YouTubeTab = QtWidgets.QWidget()
        self.YouTubeTab.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YouTubeTab.sizePolicy().hasHeightForWidth())
        self.YouTubeTab.setSizePolicy(sizePolicy)
        self.YouTubeTab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.YouTubeTab.setObjectName("YouTubeTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.YouTubeTab)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Row_02 = QtWidgets.QHBoxLayout()
        self.Row_02.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.Row_02.setContentsMargins(-1, -1, -1, 10)
        self.Row_02.setObjectName("Row_02")
        self.ytUrlLabel = QtWidgets.QLabel(parent=self.YouTubeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytUrlLabel.sizePolicy().hasHeightForWidth())
        self.ytUrlLabel.setSizePolicy(sizePolicy)
        self.ytUrlLabel.setObjectName("ytUrlLabel")
        self.Row_02.addWidget(self.ytUrlLabel)
        self.ytUrlInput = QtWidgets.QLineEdit(parent=self.YouTubeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytUrlInput.sizePolicy().hasHeightForWidth())
        self.ytUrlInput.setSizePolicy(sizePolicy)
        self.ytUrlInput.setObjectName("ytUrlInput")
        self.Row_02.addWidget(self.ytUrlInput)
        self.ytUrlStatusIcon = QtWidgets.QLabel(parent=self.YouTubeTab)
        self.ytUrlStatusIcon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytUrlStatusIcon.sizePolicy().hasHeightForWidth())
        self.ytUrlStatusIcon.setSizePolicy(sizePolicy)
        self.ytUrlStatusIcon.setMinimumSize(QtCore.QSize(18, 18))
        self.ytUrlStatusIcon.setMaximumSize(QtCore.QSize(18, 18))
        self.ytUrlStatusIcon.setText("")
        self.ytUrlStatusIcon.setPixmap(QtGui.QPixmap("ui/../../../../.designer/backup/icons/grey_checkmark.png"))
        self.ytUrlStatusIcon.setScaledContents(False)
        self.ytUrlStatusIcon.setObjectName("ytUrlStatusIcon")
        self.Row_02.addWidget(self.ytUrlStatusIcon)
        self.verticalLayout_2.addLayout(self.Row_02)
        self.ytMetaData = QtWidgets.QGroupBox(parent=self.YouTubeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytMetaData.sizePolicy().hasHeightForWidth())
        self.ytMetaData.setSizePolicy(sizePolicy)
        self.ytMetaData.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ytMetaData.setObjectName("ytMetaData")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ytMetaData)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Grid_01 = QtWidgets.QGridLayout()
        self.Grid_01.setObjectName("Grid_01")
        self.ytTitleInput = QtWidgets.QLineEdit(parent=self.ytMetaData)
        self.ytTitleInput.setObjectName("ytTitleInput")
        self.Grid_01.addWidget(self.ytTitleInput, 0, 1, 1, 1)
        self.ytTitleLabel = QtWidgets.QLabel(parent=self.ytMetaData)
        self.ytTitleLabel.setObjectName("ytTitleLabel")
        self.Grid_01.addWidget(self.ytTitleLabel, 0, 0, 1, 1)
        self.ytArtistInput = QtWidgets.QLineEdit(parent=self.ytMetaData)
        self.ytArtistInput.setObjectName("ytArtistInput")
        self.Grid_01.addWidget(self.ytArtistInput, 1, 1, 1, 1)
        self.ytArtistLabel = QtWidgets.QLabel(parent=self.ytMetaData)
        self.ytArtistLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ytArtistLabel.setObjectName("ytArtistLabel")
        self.Grid_01.addWidget(self.ytArtistLabel, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.Grid_01)
        self.verticalLayout_2.addWidget(self.ytMetaData)
        self.Row_05 = QtWidgets.QHBoxLayout()
        self.Row_05.setObjectName("Row_05")
        self.ytConversionSettings = QtWidgets.QGroupBox(parent=self.YouTubeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytConversionSettings.sizePolicy().hasHeightForWidth())
        self.ytConversionSettings.setSizePolicy(sizePolicy)
        self.ytConversionSettings.setMinimumSize(QtCore.QSize(0, 0))
        self.ytConversionSettings.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ytConversionSettings.setFlat(False)
        self.ytConversionSettings.setCheckable(True)
        self.ytConversionSettings.setObjectName("ytConversionSettings")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ytConversionSettings)
        self.horizontalLayout.setContentsMargins(12, 12, -1, 12)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ytConversionCompressionSettings = QtWidgets.QGroupBox(parent=self.ytConversionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytConversionCompressionSettings.sizePolicy().hasHeightForWidth())
        self.ytConversionCompressionSettings.setSizePolicy(sizePolicy)
        self.ytConversionCompressionSettings.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ytConversionCompressionSettings.setObjectName("ytConversionCompressionSettings")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.ytConversionCompressionSettings)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.ytCompressionRadioOgg = QtWidgets.QRadioButton(parent=self.ytConversionCompressionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytCompressionRadioOgg.sizePolicy().hasHeightForWidth())
        self.ytCompressionRadioOgg.setSizePolicy(sizePolicy)
        self.ytCompressionRadioOgg.setMinimumSize(QtCore.QSize(0, 24))
        self.ytCompressionRadioOgg.setObjectName("ytCompressionRadioOgg")
        self.verticalLayout_12.addWidget(self.ytCompressionRadioOgg)
        self.ytCompressionRadioM4a = QtWidgets.QRadioButton(parent=self.ytConversionCompressionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytCompressionRadioM4a.sizePolicy().hasHeightForWidth())
        self.ytCompressionRadioM4a.setSizePolicy(sizePolicy)
        self.ytCompressionRadioM4a.setMinimumSize(QtCore.QSize(0, 24))
        self.ytCompressionRadioM4a.setChecked(True)
        self.ytCompressionRadioM4a.setObjectName("ytCompressionRadioM4a")
        self.verticalLayout_12.addWidget(self.ytCompressionRadioM4a)
        self.ytCompressionRadioMp4 = QtWidgets.QRadioButton(parent=self.ytConversionCompressionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytCompressionRadioMp4.sizePolicy().hasHeightForWidth())
        self.ytCompressionRadioMp4.setSizePolicy(sizePolicy)
        self.ytCompressionRadioMp4.setMinimumSize(QtCore.QSize(0, 24))
        self.ytCompressionRadioMp4.setObjectName("ytCompressionRadioMp4")
        self.verticalLayout_12.addWidget(self.ytCompressionRadioMp4)
        self.ytCompressionRadioMp3 = QtWidgets.QRadioButton(parent=self.ytConversionCompressionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytCompressionRadioMp3.sizePolicy().hasHeightForWidth())
        self.ytCompressionRadioMp3.setSizePolicy(sizePolicy)
        self.ytCompressionRadioMp3.setMinimumSize(QtCore.QSize(0, 24))
        self.ytCompressionRadioMp3.setObjectName("ytCompressionRadioMp3")
        self.verticalLayout_12.addWidget(self.ytCompressionRadioMp3)
        self.horizontalLayout.addWidget(self.ytConversionCompressionSettings)
        self.ytConversionBitRateSettings = QtWidgets.QGroupBox(parent=self.ytConversionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytConversionBitRateSettings.sizePolicy().hasHeightForWidth())
        self.ytConversionBitRateSettings.setSizePolicy(sizePolicy)
        self.ytConversionBitRateSettings.setObjectName("ytConversionBitRateSettings")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.ytConversionBitRateSettings)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Row_04 = QtWidgets.QHBoxLayout()
        self.Row_04.setObjectName("Row_04")
        self.ytBitRateDial = QtWidgets.QDial(parent=self.ytConversionBitRateSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytBitRateDial.sizePolicy().hasHeightForWidth())
        self.ytBitRateDial.setSizePolicy(sizePolicy)
        self.ytBitRateDial.setMinimumSize(QtCore.QSize(60, 60))
        self.ytBitRateDial.setMaximumSize(QtCore.QSize(60, 60))
        self.ytBitRateDial.setAutoFillBackground(False)
        self.ytBitRateDial.setMinimum(0)
        self.ytBitRateDial.setMaximum(4)
        self.ytBitRateDial.setSingleStep(1)
        self.ytBitRateDial.setPageStep(1)
        self.ytBitRateDial.setProperty("value", 4)
        self.ytBitRateDial.setSliderPosition(4)
        self.ytBitRateDial.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.ytBitRateDial.setInvertedAppearance(False)
        self.ytBitRateDial.setWrapping(False)
        self.ytBitRateDial.setNotchesVisible(True)
        self.ytBitRateDial.setObjectName("ytBitRateDial")
        self.Row_04.addWidget(self.ytBitRateDial)
        self.verticalLayout_8.addLayout(self.Row_04)
        self.ytBitRateLabel = QtWidgets.QLabel(parent=self.ytConversionBitRateSettings)
        self.ytBitRateLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.ytBitRateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ytBitRateLabel.setObjectName("ytBitRateLabel")
        self.verticalLayout_8.addWidget(self.ytBitRateLabel)
        self.horizontalLayout.addWidget(self.ytConversionBitRateSettings)
        self.ytConversionOtherSettings = QtWidgets.QGroupBox(parent=self.ytConversionSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytConversionOtherSettings.sizePolicy().hasHeightForWidth())
        self.ytConversionOtherSettings.setSizePolicy(sizePolicy)
        self.ytConversionOtherSettings.setObjectName("ytConversionOtherSettings")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ytConversionOtherSettings)
        self.verticalLayout_7.setContentsMargins(6, -1, 12, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ytConversionKeepOriginal = QtWidgets.QCheckBox(parent=self.ytConversionOtherSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytConversionKeepOriginal.sizePolicy().hasHeightForWidth())
        self.ytConversionKeepOriginal.setSizePolicy(sizePolicy)
        self.ytConversionKeepOriginal.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.ytConversionKeepOriginal.setChecked(True)
        self.ytConversionKeepOriginal.setObjectName("ytConversionKeepOriginal")
        self.verticalLayout_7.addWidget(self.ytConversionKeepOriginal)
        self.horizontalLayout.addWidget(self.ytConversionOtherSettings)
        self.Row_05.addWidget(self.ytConversionSettings)
        self.verticalLayout_2.addLayout(self.Row_05)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.ytFileSettings = QtWidgets.QGroupBox(parent=self.YouTubeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytFileSettings.sizePolicy().hasHeightForWidth())
        self.ytFileSettings.setSizePolicy(sizePolicy)
        self.ytFileSettings.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ytFileSettings.setObjectName("ytFileSettings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ytFileSettings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Grid_02 = QtWidgets.QGridLayout()
        self.Grid_02.setObjectName("Grid_02")
        self.ytDestinationInput = QtWidgets.QLineEdit(parent=self.ytFileSettings)
        self.ytDestinationInput.setObjectName("ytDestinationInput")
        self.Grid_02.addWidget(self.ytDestinationInput, 0, 1, 1, 1)
        self.ytDestinationLabel = QtWidgets.QLabel(parent=self.ytFileSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytDestinationLabel.sizePolicy().hasHeightForWidth())
        self.ytDestinationLabel.setSizePolicy(sizePolicy)
        self.ytDestinationLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ytDestinationLabel.setObjectName("ytDestinationLabel")
        self.Grid_02.addWidget(self.ytDestinationLabel, 0, 0, 1, 1)
        self.ytDestinationBrowseButton = QtWidgets.QPushButton(parent=self.ytFileSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytDestinationBrowseButton.sizePolicy().hasHeightForWidth())
        self.ytDestinationBrowseButton.setSizePolicy(sizePolicy)
        self.ytDestinationBrowseButton.setObjectName("ytDestinationBrowseButton")
        self.Grid_02.addWidget(self.ytDestinationBrowseButton, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.Grid_02)
        self.verticalLayout_2.addWidget(self.ytFileSettings)
        self.Row_03 = QtWidgets.QHBoxLayout()
        self.Row_03.setObjectName("Row_03")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Row_03.addItem(spacerItem1)
        self.ytDownloadButton = QtWidgets.QPushButton(parent=self.YouTubeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ytDownloadButton.sizePolicy().hasHeightForWidth())
        self.ytDownloadButton.setSizePolicy(sizePolicy)
        self.ytDownloadButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ytDownloadButton.setObjectName("ytDownloadButton")
        self.Row_03.addWidget(self.ytDownloadButton)
        self.verticalLayout_2.addLayout(self.Row_03)
        self.toolTab.addTab(self.YouTubeTab, "")
        self.tabPlaylist = QtWidgets.QWidget()
        self.tabPlaylist.setEnabled(True)
        self.tabPlaylist.setAccessibleName("")
        self.tabPlaylist.setObjectName("tabPlaylist")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabPlaylist)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.tabPlaylist)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.tabPlaylist)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.toolTab.addTab(self.tabPlaylist, "")
        self.Row_01.addWidget(self.toolTab)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Row_01.addItem(spacerItem2)
        self.debugConsole = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.debugConsole.setObjectName("debugConsole")
        self.Row_01.addWidget(self.debugConsole)
        self.Row_01.setStretch(2, 5)
        self.verticalLayout.addLayout(self.Row_01)
        spacerItem3 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.progressBar.setBaseSize(QtCore.QSize(0, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ytUrlInput, self.ytTitleInput)
        MainWindow.setTabOrder(self.ytTitleInput, self.ytArtistInput)
        MainWindow.setTabOrder(self.ytArtistInput, self.debugConsole)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TekPlexor"))
        self.ytUrlLabel.setText(_translate("MainWindow", "URL:"))
        self.ytMetaData.setTitle(_translate("MainWindow", "Metadata"))
        self.ytTitleLabel.setText(_translate("MainWindow", "Title:"))
        self.ytArtistLabel.setText(_translate("MainWindow", "Artist:"))
        self.ytConversionSettings.setTitle(_translate("MainWindow", "Conversion"))
        self.ytConversionCompressionSettings.setTitle(_translate("MainWindow", "Compression"))
        self.ytCompressionRadioOgg.setText(_translate("MainWindow", "  OGG"))
        self.ytCompressionRadioM4a.setText(_translate("MainWindow", "  m4a"))
        self.ytCompressionRadioMp4.setText(_translate("MainWindow", "  mp4"))
        self.ytCompressionRadioMp3.setText(_translate("MainWindow", "  mp3"))
        self.ytConversionBitRateSettings.setTitle(_translate("MainWindow", "Bit Rate"))
        self.ytBitRateLabel.setText(_translate("MainWindow", "320 kbps"))
        self.ytConversionOtherSettings.setTitle(_translate("MainWindow", "Settings"))
        self.ytConversionKeepOriginal.setText(_translate("MainWindow", "Delete webm"))
        self.ytFileSettings.setTitle(_translate("MainWindow", "File Settings"))
        self.ytDestinationLabel.setText(_translate("MainWindow", "Dest:"))
        self.ytDestinationBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.ytDownloadButton.setText(_translate("MainWindow", "Download"))
        self.toolTab.setTabText(self.toolTab.indexOf(self.YouTubeTab), _translate("MainWindow", "Single"))
        self.label.setText(_translate("MainWindow", "Placeholder"))
        self.label_2.setText(_translate("MainWindow", "another one"))
        self.toolTab.setTabText(self.toolTab.indexOf(self.tabPlaylist), _translate("MainWindow", "Playlist"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
