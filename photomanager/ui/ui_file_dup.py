# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_dup.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgFileDup(object):
    def setupUi(self, DlgFileDup):
        DlgFileDup.setObjectName("DlgFileDup")
        DlgFileDup.setEnabled(True)
        DlgFileDup.resize(1021, 854)
        self.verticalLayoutWidget = QtWidgets.QWidget(DlgFileDup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblImage.setText("")
        self.lblImage.setObjectName("lblImage")
        self.verticalLayout.addWidget(self.lblImage)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(DlgFileDup)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(640, 0, 381, 791))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstDupFiles = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.lstDupFiles.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lstDupFiles.setObjectName("lstDupFiles")
        self.verticalLayout_2.addWidget(self.lstDupFiles)
        self.btnCancel = QtWidgets.QDialogButtonBox(DlgFileDup)
        self.btnCancel.setGeometry(QtCore.QRect(920, 810, 75, 23))
        self.btnCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.btnCancel.setCenterButtons(False)
        self.btnCancel.setObjectName("btnCancel")
        self.btnPrev = QtWidgets.QPushButton(DlgFileDup)
        self.btnPrev.setGeometry(QtCore.QRect(10, 810, 75, 23))
        self.btnPrev.setObjectName("btnPrev")
        self.btnNext = QtWidgets.QPushButton(DlgFileDup)
        self.btnNext.setGeometry(QtCore.QRect(110, 810, 75, 23))
        self.btnNext.setObjectName("btnNext")
        self.btnDelete = QtWidgets.QPushButton(DlgFileDup)
        self.btnDelete.setGeometry(QtCore.QRect(700, 810, 75, 23))
        self.btnDelete.setObjectName("btnDelete")

        self.retranslateUi(DlgFileDup)
        self.btnNext.clicked.connect(DlgFileDup.btnNext_click)
        self.btnPrev.clicked.connect(DlgFileDup.btnPrev_click)
        self.lstDupFiles.itemSelectionChanged.connect(DlgFileDup.lstDupFiles_itemSelectChanged)
        self.btnDelete.clicked.connect(DlgFileDup.btnDelete_click)
        QtCore.QMetaObject.connectSlotsByName(DlgFileDup)

    def retranslateUi(self, DlgFileDup):
        _translate = QtCore.QCoreApplication.translate
        DlgFileDup.setWindowTitle(_translate("DlgFileDup", "Remove Duplicate"))
        self.btnPrev.setText(_translate("DlgFileDup", "Previous"))
        self.btnNext.setText(_translate("DlgFileDup", "Next"))
        self.btnDelete.setText(_translate("DlgFileDup", "Delete"))
