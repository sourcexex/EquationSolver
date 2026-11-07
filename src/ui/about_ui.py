# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import webbrowser

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QCommandLinkButton, QDialogButtonBox, QGridLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)

developer_bilibili = "https://space.bilibili.com/3461569679722999"
project_github = "https://github.com/sourcexex/EquationSolver"

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(456, 303)
        icon = QIcon()
        icon.addFile(u"src/resources/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_main = QLabel(Dialog)
        self.label_main.setObjectName(u"label_main")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_main.setFont(font)

        self.verticalLayout_2.addWidget(self.label_main)

        self.label_ver = QLabel(Dialog)
        self.label_ver.setObjectName(u"label_ver")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_ver.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_ver)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_developer = QLabel(Dialog)
        self.label_developer.setObjectName(u"label_developer")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_developer.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_developer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.commandLinkButton_github = QCommandLinkButton(Dialog)
        self.commandLinkButton_github.setObjectName(u"commandLinkButton_github")

        self.verticalLayout.addWidget(self.commandLinkButton_github)

        self.commandLinkButton_bilibili = QCommandLinkButton(Dialog)
        self.commandLinkButton_bilibili.setObjectName(u"commandLinkButton_bilibili")

        self.verticalLayout.addWidget(self.commandLinkButton_bilibili)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"logo.ico"))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_main.setText(QCoreApplication.translate("Dialog", u"Equation Solver", None))
        self.label_ver.setText(QCoreApplication.translate("Dialog", u"v 0.1.0", None))
        self.label_developer.setText(QCoreApplication.translate("Dialog", u"\u4f5c\u8005: Sourcex", None))
        self.commandLinkButton_github.setText(QCoreApplication.translate("Dialog", u"GitHub\u94fe\u63a5", None))
        self.commandLinkButton_bilibili.setText(QCoreApplication.translate("Dialog", u"\u4f5c\u8005B\u7ad9", None))
        self.label.setText("")
    # retranslateUi

    

    def commandLinkButton_bilibili_clicked(self):
        webbrowser.open(developer_bilibili)

    def commandLinkButton_github_clicked(self):
        webbrowser.open(project_github)