# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameInfo1.ui'
#
# Created: Tue Sep 16 20:35:21 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GameInfo1(object):
    def setupUi(self, GameInfo1):
        GameInfo1.setObjectName(_fromUtf8("GameInfo1"))
        GameInfo1.resize(222, 241)
        self.label_25 = QtGui.QLabel(GameInfo1)
        self.label_25.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.layoutWidget = QtGui.QWidget(GameInfo1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_7.addWidget(self.label)
        self.RoundNumberLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.RoundNumberLineEdit.setReadOnly(True)
        self.RoundNumberLineEdit.setObjectName(_fromUtf8("RoundNumberLineEdit"))
        self.horizontalLayout_7.addWidget(self.RoundNumberLineEdit)
        self.layoutWidget_2 = QtGui.QWidget(GameInfo1)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 60, 201, 164))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.RoundTimeLineEdit1 = QtGui.QLineEdit(self.layoutWidget_2)
        self.RoundTimeLineEdit1.setReadOnly(True)
        self.RoundTimeLineEdit1.setObjectName(_fromUtf8("RoundTimeLineEdit1"))
        self.horizontalLayout.addWidget(self.RoundTimeLineEdit1)
        self.RoundTimeLineEdit2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.RoundTimeLineEdit2.setReadOnly(True)
        self.RoundTimeLineEdit2.setObjectName(_fromUtf8("RoundTimeLineEdit2"))
        self.horizontalLayout.addWidget(self.RoundTimeLineEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_8 = QtGui.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.SourceNumberLineEdit1 = QtGui.QLineEdit(self.layoutWidget_2)
        self.SourceNumberLineEdit1.setReadOnly(True)
        self.SourceNumberLineEdit1.setObjectName(_fromUtf8("SourceNumberLineEdit1"))
        self.horizontalLayout_2.addWidget(self.SourceNumberLineEdit1)
        self.SourceNumberLineEdit2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.SourceNumberLineEdit2.setObjectName(_fromUtf8("SourceNumberLineEdit2"))
        self.horizontalLayout_2.addWidget(self.SourceNumberLineEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.BaseLifeLineEdit1 = QtGui.QLineEdit(self.layoutWidget_2)
        self.BaseLifeLineEdit1.setReadOnly(True)
        self.BaseLifeLineEdit1.setObjectName(_fromUtf8("BaseLifeLineEdit1"))
        self.horizontalLayout_3.addWidget(self.BaseLifeLineEdit1)
        self.BaseLifeLineEdit2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.BaseLifeLineEdit2.setObjectName(_fromUtf8("BaseLifeLineEdit2"))
        self.horizontalLayout_3.addWidget(self.BaseLifeLineEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.PlaneNumberLineEdit1 = QtGui.QLineEdit(self.layoutWidget_2)
        self.PlaneNumberLineEdit1.setReadOnly(True)
        self.PlaneNumberLineEdit1.setObjectName(_fromUtf8("PlaneNumberLineEdit1"))
        self.horizontalLayout_4.addWidget(self.PlaneNumberLineEdit1)
        self.PlaneNumberLineEdit2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.PlaneNumberLineEdit2.setObjectName(_fromUtf8("PlaneNumberLineEdit2"))
        self.horizontalLayout_4.addWidget(self.PlaneNumberLineEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.ShipNumberLineEdit1 = QtGui.QLineEdit(self.layoutWidget_2)
        self.ShipNumberLineEdit1.setReadOnly(True)
        self.ShipNumberLineEdit1.setObjectName(_fromUtf8("ShipNumberLineEdit1"))
        self.horizontalLayout_5.addWidget(self.ShipNumberLineEdit1)
        self.ShipNumberLineEdit2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.ShipNumberLineEdit2.setReadOnly(True)
        self.ShipNumberLineEdit2.setObjectName(_fromUtf8("ShipNumberLineEdit2"))
        self.horizontalLayout_5.addWidget(self.ShipNumberLineEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.SubmarineNumberLineEdit1 = QtGui.QLineEdit(self.layoutWidget_2)
        self.SubmarineNumberLineEdit1.setObjectName(_fromUtf8("SubmarineNumberLineEdit1"))
        self.horizontalLayout_6.addWidget(self.SubmarineNumberLineEdit1)
        self.SubmarineNumberLineEdit2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.SubmarineNumberLineEdit2.setObjectName(_fromUtf8("SubmarineNumberLineEdit2"))
        self.horizontalLayout_6.addWidget(self.SubmarineNumberLineEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_24 = QtGui.QLabel(GameInfo1)
        self.label_24.setGeometry(QtCore.QRect(90, 40, 54, 12))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label.setBuddy(self.RoundNumberLineEdit)
        self.label_2.setBuddy(self.RoundTimeLineEdit1)
        self.label_8.setBuddy(self.SourceNumberLineEdit1)
        self.label_7.setBuddy(self.BaseLifeLineEdit1)
        self.label_3.setBuddy(self.PlaneNumberLineEdit1)
        self.label_4.setBuddy(self.ShipNumberLineEdit1)
        self.label_5.setBuddy(self.SubmarineNumberLineEdit1)

        self.retranslateUi(GameInfo1)
        QtCore.QMetaObject.connectSlotsByName(GameInfo1)

    def retranslateUi(self, GameInfo1):
        GameInfo1.setWindowTitle(_translate("GameInfo1", "游戏信息", None))
        self.label_25.setText(_translate("GameInfo1", "   2号", None))
        self.label.setText(_translate("GameInfo1", "回合数    ：", None))
        self.label_2.setText(_translate("GameInfo1", "回合用时  ：", None))
        self.label_8.setText(_translate("GameInfo1", "资源数    ：", None))
        self.label_7.setText(_translate("GameInfo1", "基地生命  ：", None))
        self.label_3.setText(_translate("GameInfo1", "空中单位数：", None))
        self.label_4.setText(_translate("GameInfo1", "水面单位数：", None))
        self.label_5.setText(_translate("GameInfo1", "水下单位数：", None))
        self.label_24.setText(_translate("GameInfo1", "   1号", None))
