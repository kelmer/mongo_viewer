# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created: Fri Oct 12 19:06:54 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditHost = QtGui.QLineEdit(self.centralwidget)
        self.lineEditHost.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditHost.setMaximumSize(QtCore.QSize(190, 16777215))
        self.lineEditHost.setObjectName(_fromUtf8("lineEditHost"))
        self.horizontalLayout_2.addWidget(self.lineEditHost)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditPort = QtGui.QLineEdit(self.centralwidget)
        self.lineEditPort.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.horizontalLayout_2.addWidget(self.lineEditPort)
        self.pushButtonConnect = QtGui.QPushButton(self.centralwidget)
        self.pushButtonConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonConnect.setObjectName(_fromUtf8("pushButtonConnect"))
        self.horizontalLayout_2.addWidget(self.pushButtonConnect)
        spacerItem = QtGui.QSpacerItem(288, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidgetMain = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidgetMain.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.treeWidgetMain.setFont(font)
        self.treeWidgetMain.setColumnCount(1)
        self.treeWidgetMain.setObjectName(_fromUtf8("treeWidgetMain"))
        self.treeWidgetMain.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidgetMain.header().setVisible(True)
        self.horizontalLayout.addWidget(self.treeWidgetMain)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEditQueries = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEditQueries.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.plainTextEditQueries.setFont(font)
        self.plainTextEditQueries.setObjectName(_fromUtf8("plainTextEditQueries"))
        self.verticalLayout.addWidget(self.plainTextEditQueries)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_table = QtGui.QWidget()
        self.tab_table.setObjectName(_fromUtf8("tab_table"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_table)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableWidgetMain = QtGui.QTableWidget(self.tab_table)
        self.tableWidgetMain.setObjectName(_fromUtf8("tableWidgetMain"))
        self.tableWidgetMain.setColumnCount(0)
        self.tableWidgetMain.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidgetMain)
        self.tabWidget.addTab(self.tab_table, _fromUtf8(""))
        self.tab_text = QtGui.QWidget()
        self.tab_text.setObjectName(_fromUtf8("tab_text"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_text)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.textEditMain = QtGui.QTextEdit(self.tab_text)
        self.textEditMain.setObjectName(_fromUtf8("textEditMain"))
        self.horizontalLayout_5.addWidget(self.textEditMain)
        self.tabWidget.addTab(self.tab_text, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Database = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/Misc-New-Database-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Database.setIcon(icon)
        self.actionNew_Database.setText(QtGui.QApplication.translate("MainWindow", "New Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Database.setToolTip(QtGui.QApplication.translate("MainWindow", "Create a new database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Database.setObjectName(_fromUtf8("actionNew_Database"))
        self.toolBar.addAction(self.actionNew_Database)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.treeWidgetMain.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_table), QtGui.QApplication.translate("MainWindow", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_text), QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
