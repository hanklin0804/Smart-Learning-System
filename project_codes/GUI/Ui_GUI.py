# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\AhJayzZ\Desktop\NTUST Assignment\Project\Smart-Learning-System\project_codes\GUI\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SmartLearningSystemGUI(object):
    def setupUi(self, SmartLearningSystemGUI):
        SmartLearningSystemGUI.setObjectName("SmartLearningSystemGUI")
        SmartLearningSystemGUI.resize(1238, 807)
        font = QtGui.QFont()
        font.setPointSize(10)
        SmartLearningSystemGUI.setFont(font)
        self.result_label = QtWidgets.QLabel(SmartLearningSystemGUI)
        self.result_label.setGeometry(QtCore.QRect(880, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.warning_label = QtWidgets.QLabel(SmartLearningSystemGUI)
        self.warning_label.setGeometry(QtCore.QRect(420, 720, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.warning_label.setFont(font)
        self.warning_label.setAutoFillBackground(False)
        self.warning_label.setObjectName("warning_label")
        self.confirm_btn = QtWidgets.QPushButton(SmartLearningSystemGUI)
        self.confirm_btn.setGeometry(QtCore.QRect(880, 660, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setObjectName("confirm_btn")
        self.revise_btn = QtWidgets.QPushButton(SmartLearningSystemGUI)
        self.revise_btn.setGeometry(QtCore.QRect(880, 710, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.revise_btn.setFont(font)
        self.revise_btn.setObjectName("revise_btn")
        self.tableWidget = QtWidgets.QTableWidget(SmartLearningSystemGUI)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 871, 691))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.camera_label = QtWidgets.QLabel(SmartLearningSystemGUI)
        self.camera_label.setGeometry(QtCore.QRect(0, 10, 871, 691))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.camera_label.setFont(font)
        self.camera_label.setScaledContents(False)
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_label.setObjectName("camera_label")
        self.result_list = QtWidgets.QListWidget(SmartLearningSystemGUI)
        self.result_list.setGeometry(QtCore.QRect(880, 40, 351, 561))
        self.result_list.setObjectName("result_list")
        self.revise_textbox = QtWidgets.QLineEdit(SmartLearningSystemGUI)
        self.revise_textbox.setGeometry(QtCore.QRect(880, 610, 351, 41))
        self.revise_textbox.setObjectName("revise_textbox")
        self.camera_selector = QtWidgets.QComboBox(SmartLearningSystemGUI)
        self.camera_selector.setGeometry(QtCore.QRect(100, 730, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.camera_selector.setFont(font)
        self.camera_selector.setEditable(False)
        self.camera_selector.setCurrentText("")
        self.camera_selector.setPlaceholderText("")
        self.camera_selector.setObjectName("camera_selector")
        self.camera_select_label = QtWidgets.QLabel(SmartLearningSystemGUI)
        self.camera_select_label.setGeometry(QtCore.QRect(10, 730, 81, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(20)
        self.camera_select_label.setFont(font)
        self.camera_select_label.setObjectName("camera_select_label")
        self.clear_btn = QtWidgets.QPushButton(SmartLearningSystemGUI)
        self.clear_btn.setGeometry(QtCore.QRect(880, 760, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")

        self.retranslateUi(SmartLearningSystemGUI)
        self.camera_selector.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(SmartLearningSystemGUI)

    def retranslateUi(self, SmartLearningSystemGUI):
        _translate = QtCore.QCoreApplication.translate
        SmartLearningSystemGUI.setWindowTitle(_translate("SmartLearningSystemGUI", "Dialog"))
        self.result_label.setText(_translate("SmartLearningSystemGUI", "辨識結果:"))
        self.warning_label.setText(_translate("SmartLearningSystemGUI", "Warning:光線不足"))
        self.confirm_btn.setText(_translate("SmartLearningSystemGUI", "新增至資料庫"))
        self.revise_btn.setText(_translate("SmartLearningSystemGUI", "修正"))
        self.camera_label.setText(_translate("SmartLearningSystemGUI", "ThisLabelWillBeChangedToVideoFrame"))
        self.camera_select_label.setText(_translate("SmartLearningSystemGUI", "鏡頭:"))
        self.clear_btn.setText(_translate("SmartLearningSystemGUI", "清除"))