# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/mate/ui/views/map/layer/coordinateSystem_config_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CoordinateSystemConfig(object):
    def setupUi(self, CoordinateSystemConfig):
        CoordinateSystemConfig.setObjectName("CoordinateSystemConfig")
        CoordinateSystemConfig.resize(420, 486)
        self.verticalLayout = QtWidgets.QVBoxLayout(CoordinateSystemConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(CoordinateSystemConfig)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 393, 548))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(4, 4, 4, 4)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameCoordinateSystemEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameCoordinateSystemEdit.setObjectName("nameCoordinateSystemEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameCoordinateSystemEdit)
        self.centerLabel = QtWidgets.QLabel(self.groupBox)
        self.centerLabel.setObjectName("centerLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.centerLabel)
        self.centerWidget = QtWidgets.QWidget(self.groupBox)
        self.centerWidget.setObjectName("centerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centerWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_center_x = QtWidgets.QLabel(self.centerWidget)
        self.label_center_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_center_x.setObjectName("label_center_x")
        self.horizontalLayout_2.addWidget(self.label_center_x)
        self.spin_center_x = QtWidgets.QDoubleSpinBox(self.centerWidget)
        self.spin_center_x.setMinimum(-99.99)
        self.spin_center_x.setObjectName("spin_center_x")
        self.horizontalLayout_2.addWidget(self.spin_center_x)
        self.label_center_y = QtWidgets.QLabel(self.centerWidget)
        self.label_center_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_center_y.setObjectName("label_center_y")
        self.horizontalLayout_2.addWidget(self.label_center_y)
        self.spin_center_y = QtWidgets.QDoubleSpinBox(self.centerWidget)
        self.spin_center_y.setMinimum(-99.99)
        self.spin_center_y.setObjectName("spin_center_y")
        self.horizontalLayout_2.addWidget(self.spin_center_y)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.centerWidget)
        self.enabledLabel = QtWidgets.QLabel(self.groupBox)
        self.enabledLabel.setObjectName("enabledLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enabledLabel)
        self.enabledCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.enabledCheckBox.setChecked(True)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enabledCheckBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(4, 4, 4, 4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.dimensionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.dimensionLabel.setObjectName("dimensionLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dimensionLabel)
        self.dimensionWidget = QtWidgets.QWidget(self.groupBox_2)
        self.dimensionWidget.setObjectName("dimensionWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.dimensionWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_height = QtWidgets.QLabel(self.dimensionWidget)
        self.label_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_height.setObjectName("label_height")
        self.horizontalLayout_3.addWidget(self.label_height)
        self.spin_coordinateSystem_height = QtWidgets.QDoubleSpinBox(self.dimensionWidget)
        self.spin_coordinateSystem_height.setObjectName("spin_coordinateSystem_height")
        self.horizontalLayout_3.addWidget(self.spin_coordinateSystem_height)
        self.label_width = QtWidgets.QLabel(self.dimensionWidget)
        self.label_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_width.setObjectName("label_width")
        self.horizontalLayout_3.addWidget(self.label_width)
        self.spin_coordinateSystem_width = QtWidgets.QDoubleSpinBox(self.dimensionWidget)
        self.spin_coordinateSystem_width.setObjectName("spin_coordinateSystem_width")
        self.horizontalLayout_3.addWidget(self.spin_coordinateSystem_width)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dimensionWidget)
        self.bgColorWidget = QtWidgets.QWidget(self.groupBox_2)
        self.bgColorWidget.setObjectName("bgColorWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bgColorWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bgColorLabel = QtWidgets.QLabel(self.bgColorWidget)
        self.bgColorLabel.setObjectName("bgColorLabel")
        self.horizontalLayout_5.addWidget(self.bgColorLabel)
        self.edit_bgColor = QtWidgets.QLineEdit(self.bgColorWidget)
        self.edit_bgColor.setObjectName("edit_bgColor")
        self.horizontalLayout_5.addWidget(self.edit_bgColor)
        self.btn_bgColor = QtWidgets.QPushButton(self.bgColorWidget)
        self.btn_bgColor.setFlat(False)
        self.btn_bgColor.setObjectName("btn_bgColor")
        self.horizontalLayout_5.addWidget(self.btn_bgColor)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.bgColorWidget)
        self.bgAlphaLabel = QtWidgets.QLabel(self.groupBox_2)
        self.bgAlphaLabel.setObjectName("bgAlphaLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bgAlphaLabel)
        self.spin_coordinateSystem_bgAlpha = QtWidgets.QSpinBox(self.groupBox_2)
        self.spin_coordinateSystem_bgAlpha.setMaximum(255)
        self.spin_coordinateSystem_bgAlpha.setObjectName("spin_coordinateSystem_bgAlpha")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_coordinateSystem_bgAlpha)
        self.lineWidthLabel = QtWidgets.QLabel(self.groupBox_2)
        self.lineWidthLabel.setObjectName("lineWidthLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineWidthLabel)
        self.spin_coordinateSystem_lineWidth = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_coordinateSystem_lineWidth.setObjectName("spin_coordinateSystem_lineWidth")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_coordinateSystem_lineWidth)
        self.stepSizeYLabel = QtWidgets.QLabel(self.groupBox_2)
        self.stepSizeYLabel.setObjectName("stepSizeYLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.stepSizeYLabel)
        self.spin_coordinateSystem_stepSizeY = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_coordinateSystem_stepSizeY.setObjectName("spin_coordinateSystem_stepSizeY")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spin_coordinateSystem_stepSizeY)
        self.stepSizeXLabel = QtWidgets.QLabel(self.groupBox_2)
        self.stepSizeXLabel.setObjectName("stepSizeXLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.stepSizeXLabel)
        self.spin_coordinateSystem_stepSizeX = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_coordinateSystem_stepSizeX.setObjectName("spin_coordinateSystem_stepSizeX")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spin_coordinateSystem_stepSizeX)
        self.lineColorWidget = QtWidgets.QWidget(self.groupBox_2)
        self.lineColorWidget.setObjectName("lineColorWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.lineColorWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineColorLabel = QtWidgets.QLabel(self.lineColorWidget)
        self.lineColorLabel.setObjectName("lineColorLabel")
        self.horizontalLayout_4.addWidget(self.lineColorLabel)
        self.edit_lineColor = QtWidgets.QLineEdit(self.lineColorWidget)
        self.edit_lineColor.setObjectName("edit_lineColor")
        self.horizontalLayout_4.addWidget(self.edit_lineColor)
        self.btn_lineColor = QtWidgets.QPushButton(self.lineColorWidget)
        self.btn_lineColor.setFlat(False)
        self.btn_lineColor.setObjectName("btn_lineColor")
        self.horizontalLayout_4.addWidget(self.btn_lineColor)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.lineColorWidget)
        self.polarLabel = QtWidgets.QLabel(self.groupBox_2)
        self.polarLabel.setObjectName("polarLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.polarLabel)
        self.polarCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.polarCheckBox.setChecked(False)
        self.polarCheckBox.setObjectName("polarCheckBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.polarCheckBox)
        self.polarAngleStepSizeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.polarAngleStepSizeLabel.setObjectName("polarAngleStepSizeLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.polarAngleStepSizeLabel)
        self.spin_coordinateSystem_angleStepSize = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_coordinateSystem_angleStepSize.setObjectName("spin_coordinateSystem_angleStepSize")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spin_coordinateSystem_angleStepSize)
        self.radialStepSizeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.radialStepSizeLabel.setObjectName("radialStepSizeLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.radialStepSizeLabel)
        self.spin_coordinateSystem_radialStepSize = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_coordinateSystem_radialStepSize.setObjectName("spin_coordinateSystem_radialStepSize")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spin_coordinateSystem_radialStepSize)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAccept = QtWidgets.QPushButton(CoordinateSystemConfig)
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout.addWidget(self.btnAccept)
        self.btnDiscard = QtWidgets.QPushButton(CoordinateSystemConfig)
        self.btnDiscard.setObjectName("btnDiscard")
        self.horizontalLayout.addWidget(self.btnDiscard)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CoordinateSystemConfig)
        QtCore.QMetaObject.connectSlotsByName(CoordinateSystemConfig)
        CoordinateSystemConfig.setTabOrder(self.nameCoordinateSystemEdit, self.spin_center_x)
        CoordinateSystemConfig.setTabOrder(self.spin_center_x, self.spin_center_y)
        CoordinateSystemConfig.setTabOrder(self.spin_center_y, self.enabledCheckBox)
        CoordinateSystemConfig.setTabOrder(self.enabledCheckBox, self.spin_coordinateSystem_height)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_height, self.spin_coordinateSystem_width)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_width, self.edit_bgColor)
        CoordinateSystemConfig.setTabOrder(self.edit_bgColor, self.spin_coordinateSystem_bgAlpha)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_bgAlpha, self.spin_coordinateSystem_lineWidth)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_lineWidth, self.spin_coordinateSystem_stepSizeX)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_stepSizeX, self.spin_coordinateSystem_stepSizeY)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_stepSizeY, self.edit_lineColor)
        CoordinateSystemConfig.setTabOrder(self.edit_lineColor, self.polarCheckBox)
        CoordinateSystemConfig.setTabOrder(self.polarCheckBox, self.spin_coordinateSystem_angleStepSize)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_angleStepSize, self.spin_coordinateSystem_radialStepSize)
        CoordinateSystemConfig.setTabOrder(self.spin_coordinateSystem_radialStepSize, self.btnAccept)
        CoordinateSystemConfig.setTabOrder(self.btnAccept, self.btnDiscard)
        CoordinateSystemConfig.setTabOrder(self.btnDiscard, self.scrollArea)

    def retranslateUi(self, CoordinateSystemConfig):
        _translate = QtCore.QCoreApplication.translate
        CoordinateSystemConfig.setWindowTitle(_translate("CoordinateSystemConfig", "Form"))
        self.groupBox.setTitle(_translate("CoordinateSystemConfig", "General:"))
        self.nameLabel.setText(_translate("CoordinateSystemConfig", "Name:"))
        self.centerLabel.setText(_translate("CoordinateSystemConfig", "Center:"))
        self.label_center_x.setText(_translate("CoordinateSystemConfig", "X:"))
        self.label_center_y.setText(_translate("CoordinateSystemConfig", "Y:"))
        self.enabledLabel.setText(_translate("CoordinateSystemConfig", "Enabled:"))
        self.groupBox_2.setTitle(_translate("CoordinateSystemConfig", "CoordinateSystem:"))
        self.dimensionLabel.setText(_translate("CoordinateSystemConfig", "Dimension:"))
        self.label_height.setText(_translate("CoordinateSystemConfig", "Height:"))
        self.label_width.setText(_translate("CoordinateSystemConfig", "Width:"))
        self.bgColorLabel.setText(_translate("CoordinateSystemConfig", "backgroundColor:"))
        self.btn_bgColor.setText(_translate("CoordinateSystemConfig", "Pick"))
        self.bgAlphaLabel.setText(_translate("CoordinateSystemConfig", "backgroundAlpha:"))
        self.lineWidthLabel.setText(_translate("CoordinateSystemConfig", "lineWidth:"))
        self.stepSizeYLabel.setText(_translate("CoordinateSystemConfig", "stepSizeY:"))
        self.stepSizeXLabel.setText(_translate("CoordinateSystemConfig", "stepSizeX:"))
        self.lineColorLabel.setText(_translate("CoordinateSystemConfig", "lineColor:"))
        self.btn_lineColor.setText(_translate("CoordinateSystemConfig", "Pick"))
        self.polarLabel.setText(_translate("CoordinateSystemConfig", "polar:"))
        self.polarAngleStepSizeLabel.setText(_translate("CoordinateSystemConfig", "angleStepSize:"))
        self.radialStepSizeLabel.setText(_translate("CoordinateSystemConfig", "radialStepSize:"))
        self.btnAccept.setText(_translate("CoordinateSystemConfig", "Accept"))
        self.btnDiscard.setText(_translate("CoordinateSystemConfig", "Discard"))
