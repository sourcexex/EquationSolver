# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QRadioButton, QSizePolicy, QStatusBar,
    QTextBrowser, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_solve = QAction(MainWindow)
        self.action_solve.setObjectName(u"action_solve")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_main = QLabel(self.centralwidget)
        self.label_main.setObjectName(u"label_main")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_main.setFont(font)

        self.verticalLayout.addWidget(self.label_main)

        self.groupBox_input = QGroupBox(self.centralwidget)
        self.groupBox_input.setObjectName(u"groupBox_input")
        font1 = QFont()
        font1.setBold(False)
        self.groupBox_input.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_eqn = QLabel(self.groupBox_input)
        self.label_eqn.setObjectName(u"label_eqn")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_eqn.setFont(font2)

        self.gridLayout.addWidget(self.label_eqn, 0, 0, 1, 1)

        self.lineEdit_unknow = QLineEdit(self.groupBox_input)
        self.lineEdit_unknow.setObjectName(u"lineEdit_unknow")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.lineEdit_unknow.setFont(font3)

        self.gridLayout.addWidget(self.lineEdit_unknow, 1, 2, 1, 1)

        self.label_unknow = QLabel(self.groupBox_input)
        self.label_unknow.setObjectName(u"label_unknow")
        self.label_unknow.setFont(font2)

        self.gridLayout.addWidget(self.label_unknow, 1, 0, 1, 2)

        self.lineEdit_eqn = QLineEdit(self.groupBox_input)
        self.lineEdit_eqn.setObjectName(u"lineEdit_eqn")
        self.lineEdit_eqn.setFont(font3)

        self.gridLayout.addWidget(self.lineEdit_eqn, 0, 1, 1, 2)


        self.verticalLayout.addWidget(self.groupBox_input)

        self.groupBox_range = QGroupBox(self.centralwidget)
        self.groupBox_range.setObjectName(u"groupBox_range")
        self.horizontalLayout = QHBoxLayout(self.groupBox_range)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_imaginary = QGroupBox(self.groupBox_range)
        self.groupBox_imaginary.setObjectName(u"groupBox_imaginary")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_imaginary)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_im_false = QRadioButton(self.groupBox_imaginary)
        self.radioButton_im_false.setObjectName(u"radioButton_im_false")
        font4 = QFont()
        font4.setPointSize(10)
        self.radioButton_im_false.setFont(font4)

        self.horizontalLayout_3.addWidget(self.radioButton_im_false)

        self.radioButton_im_true = QRadioButton(self.groupBox_imaginary)
        self.radioButton_im_true.setObjectName(u"radioButton_im_true")
        self.radioButton_im_true.setFont(font4)

        self.horizontalLayout_3.addWidget(self.radioButton_im_true)

        self.radioButton_im_auto = QRadioButton(self.groupBox_imaginary)
        self.radioButton_im_auto.setObjectName(u"radioButton_im_auto")
        self.radioButton_im_auto.setFont(font4)
        self.radioButton_im_auto.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_im_auto)


        self.horizontalLayout.addWidget(self.groupBox_imaginary)

        self.groupBox_negative = QGroupBox(self.groupBox_range)
        self.groupBox_negative.setObjectName(u"groupBox_negative")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_negative)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_ne_false = QRadioButton(self.groupBox_negative)
        self.radioButton_ne_false.setObjectName(u"radioButton_ne_false")
        self.radioButton_ne_false.setFont(font4)

        self.horizontalLayout_2.addWidget(self.radioButton_ne_false)

        self.radioButton_ne_true = QRadioButton(self.groupBox_negative)
        self.radioButton_ne_true.setObjectName(u"radioButton_ne_true")
        self.radioButton_ne_true.setFont(font4)

        self.horizontalLayout_2.addWidget(self.radioButton_ne_true)

        self.radioButton_ne_auto = QRadioButton(self.groupBox_negative)
        self.radioButton_ne_auto.setObjectName(u"radioButton_ne_auto")
        self.radioButton_ne_auto.setFont(font4)
        self.radioButton_ne_auto.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton_ne_auto)


        self.horizontalLayout.addWidget(self.groupBox_negative)

        self.groupBox_fractional = QGroupBox(self.groupBox_range)
        self.groupBox_fractional.setObjectName(u"groupBox_fractional")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_fractional)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_fr_false = QRadioButton(self.groupBox_fractional)
        self.radioButton_fr_false.setObjectName(u"radioButton_fr_false")
        self.radioButton_fr_false.setFont(font4)

        self.horizontalLayout_4.addWidget(self.radioButton_fr_false)

        self.radioButton_fr_true = QRadioButton(self.groupBox_fractional)
        self.radioButton_fr_true.setObjectName(u"radioButton_fr_true")
        self.radioButton_fr_true.setFont(font4)

        self.horizontalLayout_4.addWidget(self.radioButton_fr_true)

        self.radioButton_fr_auto = QRadioButton(self.groupBox_fractional)
        self.radioButton_fr_auto.setObjectName(u"radioButton_fr_auto")
        self.radioButton_fr_auto.setFont(font4)
        self.radioButton_fr_auto.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_fr_auto)


        self.horizontalLayout.addWidget(self.groupBox_fractional)

        self.groupBox_ran = QGroupBox(self.groupBox_range)
        self.groupBox_ran.setObjectName(u"groupBox_ran")
        self.gridLayout_2 = QGridLayout(self.groupBox_ran)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_range = QLineEdit(self.groupBox_ran)
        self.lineEdit_range.setObjectName(u"lineEdit_range")

        self.gridLayout_2.addWidget(self.lineEdit_range, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_ran)


        self.verticalLayout.addWidget(self.groupBox_range)

        self.textBrowser_output = QTextBrowser(self.centralwidget)
        self.textBrowser_output.setObjectName(u"textBrowser_output")
        self.textBrowser_output.setEnabled(False)
        font5 = QFont()
        font5.setPointSize(11)
        self.textBrowser_output.setFont(font5)

        self.verticalLayout.addWidget(self.textBrowser_output)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_file.addAction(self.action_clear)
        self.menu_file.addAction(self.action_solve)
        self.menu_about.addAction(self.action_help)
        self.menu_about.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EquationSolver", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a(&C)", None))
        self.action_solve.setText(QCoreApplication.translate("MainWindow", u"\u6c42\u89e3(S)", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e(&A)", None))
        self.label_main.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u7a0b\u6c42\u89e3\u5668 | Equation Solver", None))
        self.groupBox_input.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u65b9\u7a0b", None))
        self.label_eqn.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u7a0b: ", None))
        self.label_unknow.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5\u6570: ", None))
        self.groupBox_range.setTitle(QCoreApplication.translate("MainWindow", u"\u8303\u56f4", None))
        self.groupBox_imaginary.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9e\u6570/\u865a\u6570", None))
        self.radioButton_im_false.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u6570", None))
        self.radioButton_im_true.setText(QCoreApplication.translate("MainWindow", u"\u865a\u6570", None))
        self.radioButton_im_auto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.groupBox_negative.setTitle(QCoreApplication.translate("MainWindow", u"\u6b63\u6570/\u8d1f\u6570", None))
        self.radioButton_ne_false.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u6570", None))
        self.radioButton_ne_true.setText(QCoreApplication.translate("MainWindow", u"\u8d1f\u6570", None))
        self.radioButton_ne_auto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.groupBox_fractional.setTitle(QCoreApplication.translate("MainWindow", u"\u6574\u6570/\u5c0f\u6570", None))
        self.radioButton_fr_false.setText(QCoreApplication.translate("MainWindow", u"\u6574\u6570", None))
        self.radioButton_fr_true.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u6570", None))
        self.radioButton_fr_auto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.groupBox_ran.setTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e(&A)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

