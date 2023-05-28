# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVR_Configrator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from lxml import etree as ET
import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1088, 834)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1081, 831))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.dio_tab = QWidget()
        self.dio_tab.setObjectName(u"dio_tab")
        self.tabWidget_2 = QTabWidget(self.dio_tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 1071, 791))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.tabWidget_2.setFont(font1)
        self.portA_tab = QWidget()
        self.portA_tab.setObjectName(u"portA_tab")
        self.groupBox = QGroupBox(self.portA_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 30, 471, 171))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox.setFont(font2)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN0_INPUT_radioButton_ = QRadioButton(self.groupBox_3)
        self.PORTA_PIN0_INPUT_radioButton_.setObjectName(u"PORTA_PIN0_INPUT_radioButton_")
        self.PORTA_PIN0_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN0_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN0_OUTPUT_radioButton_ = QRadioButton(self.groupBox_3)
        self.PORTA_PIN0_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN0_OUTPUT_radioButton_")
        self.PORTA_PIN0_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN0_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_4)
        self.PORTA_PIN0_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN0_IN_PULL_UP_radioButton_")
        self.PORTA_PIN0_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN0_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN0_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_4)
        self.PORTA_PIN0_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN0_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN0_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN0_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_5)
        self.PORTA_PIN0_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN0_OUT_HIGH_radioButton_")
        self.PORTA_PIN0_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN0_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN0_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_5)
        self.PORTA_PIN0_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN0_OUT_LOW_radioButton_")
        self.PORTA_PIN0_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_6 = QGroupBox(self.portA_tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 210, 471, 171))
        self.groupBox_6.setFont(font2)
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN2_INPUT_radioButton_ = QRadioButton(self.groupBox_7)
        self.PORTA_PIN2_INPUT_radioButton_.setObjectName(u"PORTA_PIN2_INPUT_radioButton_")
        self.PORTA_PIN2_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN2_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN2_OUTPUT_radioButton_ = QRadioButton(self.groupBox_7)
        self.PORTA_PIN2_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN2_OUTPUT_radioButton_")
        self.PORTA_PIN2_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.PORTA_PIN2_OUTPUT_radioButton_.setChecked(False)
        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN2_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_8)
        self.PORTA_PIN2_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN2_IN_PULL_UP_radioButton_")
        self.PORTA_PIN2_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN2_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN2_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_8)
        self.PORTA_PIN2_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN2_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN2_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_9 = QGroupBox(self.groupBox_6)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setEnabled(False)
        self.groupBox_9.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN2_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_9)
        self.PORTA_PIN2_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN2_OUT_HIGH_radioButton_")
        self.PORTA_PIN2_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN2_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN2_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_9)
        self.PORTA_PIN2_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN2_OUT_LOW_radioButton_")
        self.PORTA_PIN2_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_10 = QGroupBox(self.portA_tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(20, 390, 471, 171))
        self.groupBox_10.setFont(font2)
        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN4_INPUT_radioButton_ = QRadioButton(self.groupBox_11)
        self.PORTA_PIN4_INPUT_radioButton_.setObjectName(u"PORTA_PIN4_INPUT_radioButton_")
        self.PORTA_PIN4_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN4_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN4_OUTPUT_radioButton_ = QRadioButton(self.groupBox_11)
        self.PORTA_PIN4_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN4_OUTPUT_radioButton_")
        self.PORTA_PIN4_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_12 = QGroupBox(self.groupBox_10)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN4_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_12)
        self.PORTA_PIN4_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN4_IN_PULL_UP_radioButton_")
        self.PORTA_PIN4_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN4_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN4_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_12)
        self.PORTA_PIN4_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN4_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN4_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_13 = QGroupBox(self.groupBox_10)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setEnabled(False)
        self.groupBox_13.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN4_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_13)
        self.PORTA_PIN4_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN4_OUT_HIGH_radioButton_")
        self.PORTA_PIN4_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN4_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN4_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_13)
        self.PORTA_PIN4_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN4_OUT_LOW_radioButton_")
        self.PORTA_PIN4_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_14 = QGroupBox(self.portA_tab)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(20, 570, 471, 171))
        self.groupBox_14.setFont(font2)
        self.groupBox_15 = QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN6_INPUT_radioButton_ = QRadioButton(self.groupBox_15)
        self.PORTA_PIN6_INPUT_radioButton_.setObjectName(u"PORTA_PIN6_INPUT_radioButton_")
        self.PORTA_PIN6_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN6_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN6_OUTPUT_radioButton_ = QRadioButton(self.groupBox_15)
        self.PORTA_PIN6_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN6_OUTPUT_radioButton_")
        self.PORTA_PIN6_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN6_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_16)
        self.PORTA_PIN6_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN6_IN_PULL_UP_radioButton_")
        self.PORTA_PIN6_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN6_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN6_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_16)
        self.PORTA_PIN6_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN6_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN6_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_17 = QGroupBox(self.groupBox_14)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setEnabled(False)
        self.groupBox_17.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN6_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_17)
        self.PORTA_PIN6_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN6_OUT_HIGH_radioButton_")
        self.PORTA_PIN6_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN6_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN6_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_17)
        self.PORTA_PIN6_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN6_OUT_LOW_radioButton_")
        self.PORTA_PIN6_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_2 = QGroupBox(self.portA_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(530, 30, 471, 171))
        self.groupBox_2.setFont(font2)
        self.groupBox_18 = QGroupBox(self.groupBox_2)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN1_INPUT_radioButton_ = QRadioButton(self.groupBox_18)
        self.PORTA_PIN1_INPUT_radioButton_.setObjectName(u"PORTA_PIN1_INPUT_radioButton_")
        self.PORTA_PIN1_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN1_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN1_OUTPUT_radioButton_ = QRadioButton(self.groupBox_18)
        self.PORTA_PIN1_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN1_OUTPUT_radioButton_")
        self.PORTA_PIN1_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_19 = QGroupBox(self.groupBox_2)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN1_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_19)
        self.PORTA_PIN1_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN1_IN_PULL_UP_radioButton_")
        self.PORTA_PIN1_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN1_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN1_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_19)
        self.PORTA_PIN1_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN1_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN1_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_20 = QGroupBox(self.groupBox_2)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setEnabled(False)
        self.groupBox_20.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN1_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_20)
        self.PORTA_PIN1_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN1_OUT_HIGH_radioButton_")
        self.PORTA_PIN1_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN1_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN1_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_20)
        self.PORTA_PIN1_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN1_OUT_LOW_radioButton_")
        self.PORTA_PIN1_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_41 = QGroupBox(self.portA_tab)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setGeometry(QRect(530, 210, 471, 171))
        self.groupBox_41.setFont(font2)
        self.groupBox_42 = QGroupBox(self.groupBox_41)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.groupBox_42.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN3_INPUT_radioButton_ = QRadioButton(self.groupBox_42)
        self.PORTA_PIN3_INPUT_radioButton_.setObjectName(u"PORTA_PIN3_INPUT_radioButton_")
        self.PORTA_PIN3_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN3_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN3_OUTPUT_radioButton_ = QRadioButton(self.groupBox_42)
        self.PORTA_PIN3_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN3_OUTPUT_radioButton_")
        self.PORTA_PIN3_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_43 = QGroupBox(self.groupBox_41)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN3_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_43)
        self.PORTA_PIN3_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN3_IN_PULL_UP_radioButton_")
        self.PORTA_PIN3_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN3_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN3_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_43)
        self.PORTA_PIN3_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN3_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN3_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_44 = QGroupBox(self.groupBox_41)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setEnabled(False)
        self.groupBox_44.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN3_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_44)
        self.PORTA_PIN3_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN3_OUT_HIGH_radioButton_")
        self.PORTA_PIN3_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN3_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN3_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_44)
        self.PORTA_PIN3_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN3_OUT_LOW_radioButton_")
        self.PORTA_PIN3_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_45 = QGroupBox(self.portA_tab)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.groupBox_45.setGeometry(QRect(530, 390, 471, 171))
        self.groupBox_45.setFont(font2)
        self.groupBox_46 = QGroupBox(self.groupBox_45)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.groupBox_46.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN5_INPUT_radioButton_ = QRadioButton(self.groupBox_46)
        self.PORTA_PIN5_INPUT_radioButton_.setObjectName(u"PORTA_PIN5_INPUT_radioButton_")
        self.PORTA_PIN5_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN5_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN5_OUTPUT_radioButton_ = QRadioButton(self.groupBox_46)
        self.PORTA_PIN5_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN5_OUTPUT_radioButton_")
        self.PORTA_PIN5_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_47 = QGroupBox(self.groupBox_45)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.groupBox_47.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN5_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_47)
        self.PORTA_PIN5_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN5_IN_PULL_UP_radioButton_")
        self.PORTA_PIN5_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN5_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN5_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_47)
        self.PORTA_PIN5_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN5_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN5_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_48 = QGroupBox(self.groupBox_45)
        self.groupBox_48.setObjectName(u"groupBox_48")
        self.groupBox_48.setEnabled(False)
        self.groupBox_48.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN5_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_48)
        self.PORTA_PIN5_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN5_OUT_HIGH_radioButton_")
        self.PORTA_PIN5_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN5_OUT_HIGH_radioButton_.setChecked(True)
        self.PORTA_PIN5_OUT_LOW_radioButton_ = QRadioButton(self.groupBox_48)
        self.PORTA_PIN5_OUT_LOW_radioButton_.setObjectName(u"PORTA_PIN5_OUT_LOW_radioButton_")
        self.PORTA_PIN5_OUT_LOW_radioButton_.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_49 = QGroupBox(self.portA_tab)
        self.groupBox_49.setObjectName(u"groupBox_49")
        self.groupBox_49.setGeometry(QRect(530, 570, 471, 171))
        self.groupBox_49.setFont(font2)
        self.groupBox_50 = QGroupBox(self.groupBox_49)
        self.groupBox_50.setObjectName(u"groupBox_50")
        self.groupBox_50.setGeometry(QRect(10, 30, 141, 131))
        self.PORTA_PIN7_INPUT_radioButton_ = QRadioButton(self.groupBox_50)
        self.PORTA_PIN7_INPUT_radioButton_.setObjectName(u"PORTA_PIN7_INPUT_radioButton_")
        self.PORTA_PIN7_INPUT_radioButton_.setGeometry(QRect(10, 40, 95, 20))
        self.PORTA_PIN7_INPUT_radioButton_.setChecked(True)
        self.PORTA_PIN7_OUTPUT_radioButton_ = QRadioButton(self.groupBox_50)
        self.PORTA_PIN7_OUTPUT_radioButton_.setObjectName(u"PORTA_PIN7_OUTPUT_radioButton_")
        self.PORTA_PIN7_OUTPUT_radioButton_.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_51 = QGroupBox(self.groupBox_49)
        self.groupBox_51.setObjectName(u"groupBox_51")
        self.groupBox_51.setGeometry(QRect(170, 20, 281, 61))
        self.PORTA_PIN7_IN_PULL_UP_radioButton_ = QRadioButton(self.groupBox_51)
        self.PORTA_PIN7_IN_PULL_UP_radioButton_.setObjectName(u"PORTA_PIN7_IN_PULL_UP_radioButton_")
        self.PORTA_PIN7_IN_PULL_UP_radioButton_.setGeometry(QRect(10, 30, 95, 20))
        self.PORTA_PIN7_IN_PULL_UP_radioButton_.setChecked(True)
        self.PORTA_PIN7_IN_PULL_DOWN_radioButton_ = QRadioButton(self.groupBox_51)
        self.PORTA_PIN7_IN_PULL_DOWN_radioButton_.setObjectName(u"PORTA_PIN7_IN_PULL_DOWN_radioButton_")
        self.PORTA_PIN7_IN_PULL_DOWN_radioButton_.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_52 = QGroupBox(self.groupBox_49)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setEnabled(False)
        self.groupBox_52.setGeometry(QRect(170, 90, 281, 71))
        self.PORTA_PIN7_OUT_HIGH_radioButton_ = QRadioButton(self.groupBox_52)
        self.PORTA_PIN7_OUT_HIGH_radioButton_.setObjectName(u"PORTA_PIN7_OUT_HIGH_radioButton_")
        self.PORTA_PIN7_OUT_HIGH_radioButton_.setGeometry(QRect(10, 30, 111, 20))
        self.PORTA_PIN7_OUT_HIGH_radioButton_.setChecked(True)
        self.radioButton_78 = QRadioButton(self.groupBox_52)
        self.radioButton_78.setObjectName(u"radioButton_78")
        self.radioButton_78.setGeometry(QRect(140, 30, 95, 20))
        self.tabWidget_2.addTab(self.portA_tab, "")
        self.portB_tab = QWidget()
        self.portB_tab.setObjectName(u"portB_tab")
        self.groupBox_113 = QGroupBox(self.portB_tab)
        self.groupBox_113.setObjectName(u"groupBox_113")
        self.groupBox_113.setGeometry(QRect(530, 210, 471, 171))
        self.groupBox_113.setFont(font2)
        self.groupBox_114 = QGroupBox(self.groupBox_113)
        self.groupBox_114.setObjectName(u"groupBox_114")
        self.groupBox_114.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN3_INPUT_radioButton_1 = QRadioButton(self.groupBox_114)
        self.PORTB_PIN3_INPUT_radioButton_1.setObjectName(u"PORTB_PIN3_INPUT_radioButton_1")
        self.PORTB_PIN3_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN3_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN3_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_114)
        self.PORTB_PIN3_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN3_OUTPUT_radioButton_1")
        self.PORTB_PIN3_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_115 = QGroupBox(self.groupBox_113)
        self.groupBox_115.setObjectName(u"groupBox_115")
        self.groupBox_115.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN3_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_115)
        self.PORTB_PIN3_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN3_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN3_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN3_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN3_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_115)
        self.PORTB_PIN3_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN3_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN3_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_116 = QGroupBox(self.groupBox_113)
        self.groupBox_116.setObjectName(u"groupBox_116")
        self.groupBox_116.setEnabled(False)
        self.groupBox_116.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN3_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_116)
        self.PORTB_PIN3_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN3_OUT_HIGH_radioButton_1")
        self.PORTB_PIN3_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN3_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN3_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_116)
        self.PORTB_PIN3_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN3_OUT_LOW_radioButton_1")
        self.PORTB_PIN3_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_105 = QGroupBox(self.portB_tab)
        self.groupBox_105.setObjectName(u"groupBox_105")
        self.groupBox_105.setGeometry(QRect(530, 30, 471, 171))
        self.groupBox_105.setFont(font2)
        self.groupBox_106 = QGroupBox(self.groupBox_105)
        self.groupBox_106.setObjectName(u"groupBox_106")
        self.groupBox_106.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN1_INPUT_radioButton_1 = QRadioButton(self.groupBox_106)
        self.PORTB_PIN1_INPUT_radioButton_1.setObjectName(u"PORTB_PIN1_INPUT_radioButton_1")
        self.PORTB_PIN1_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN1_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN1_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_106)
        self.PORTB_PIN1_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN1_OUTPUT_radioButton_1")
        self.PORTB_PIN1_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_107 = QGroupBox(self.groupBox_105)
        self.groupBox_107.setObjectName(u"groupBox_107")
        self.groupBox_107.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN1_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_107)
        self.PORTB_PIN1_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN1_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN1_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN1_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN1_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_107)
        self.PORTB_PIN1_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN1_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN1_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_108 = QGroupBox(self.groupBox_105)
        self.groupBox_108.setObjectName(u"groupBox_108")
        self.groupBox_108.setEnabled(False)
        self.groupBox_108.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN1_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_108)
        self.PORTB_PIN1_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN1_OUT_HIGH_radioButton_1")
        self.PORTB_PIN1_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN1_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN1_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_108)
        self.PORTB_PIN1_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN1_OUT_LOW_radioButton_1")
        self.PORTB_PIN1_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_97 = QGroupBox(self.portB_tab)
        self.groupBox_97.setObjectName(u"groupBox_97")
        self.groupBox_97.setGeometry(QRect(20, 210, 471, 171))
        self.groupBox_97.setFont(font2)
        self.groupBox_98 = QGroupBox(self.groupBox_97)
        self.groupBox_98.setObjectName(u"groupBox_98")
        self.groupBox_98.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN2_INPUT_radioButton_1 = QRadioButton(self.groupBox_98)
        self.PORTB_PIN2_INPUT_radioButton_1.setObjectName(u"PORTB_PIN2_INPUT_radioButton_1")
        self.PORTB_PIN2_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN2_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN2_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_98)
        self.PORTB_PIN2_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN2_OUTPUT_radioButton_1")
        self.PORTB_PIN2_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.PORTB_PIN2_OUTPUT_radioButton_1.setChecked(False)
        self.groupBox_99 = QGroupBox(self.groupBox_97)
        self.groupBox_99.setObjectName(u"groupBox_99")
        self.groupBox_99.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN2_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_99)
        self.PORTB_PIN2_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN2_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN2_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN2_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN2_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_99)
        self.PORTB_PIN2_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN2_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN2_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_100 = QGroupBox(self.groupBox_97)
        self.groupBox_100.setObjectName(u"groupBox_100")
        self.groupBox_100.setEnabled(False)
        self.groupBox_100.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN2_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_100)
        self.PORTB_PIN2_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN2_OUT_HIGH_radioButton_1")
        self.PORTB_PIN2_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN2_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN2_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_100)
        self.PORTB_PIN2_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN2_OUT_LOW_radioButton_1")
        self.PORTB_PIN2_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_101 = QGroupBox(self.portB_tab)
        self.groupBox_101.setObjectName(u"groupBox_101")
        self.groupBox_101.setGeometry(QRect(530, 390, 471, 171))
        self.groupBox_101.setFont(font2)
        self.groupBox_102 = QGroupBox(self.groupBox_101)
        self.groupBox_102.setObjectName(u"groupBox_102")
        self.groupBox_102.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN5_INPUT_radioButton_1 = QRadioButton(self.groupBox_102)
        self.PORTB_PIN5_INPUT_radioButton_1.setObjectName(u"PORTB_PIN5_INPUT_radioButton_1")
        self.PORTB_PIN5_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN5_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN5_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_102)
        self.PORTB_PIN5_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN5_OUTPUT_radioButton_1")
        self.PORTB_PIN5_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_103 = QGroupBox(self.groupBox_101)
        self.groupBox_103.setObjectName(u"groupBox_103")
        self.groupBox_103.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN5_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_103)
        self.PORTB_PIN5_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN5_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN5_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN5_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN5_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_103)
        self.PORTB_PIN5_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN5_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN5_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_104 = QGroupBox(self.groupBox_101)
        self.groupBox_104.setObjectName(u"groupBox_104")
        self.groupBox_104.setEnabled(False)
        self.groupBox_104.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN5_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_104)
        self.PORTB_PIN5_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN5_OUT_HIGH_radioButton_1")
        self.PORTB_PIN5_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN5_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN5_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_104)
        self.PORTB_PIN5_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN5_OUT_LOW_radioButton_1")
        self.PORTB_PIN5_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_89 = QGroupBox(self.portB_tab)
        self.groupBox_89.setObjectName(u"groupBox_89")
        self.groupBox_89.setGeometry(QRect(20, 390, 471, 171))
        self.groupBox_89.setFont(font2)
        self.groupBox_90 = QGroupBox(self.groupBox_89)
        self.groupBox_90.setObjectName(u"groupBox_90")
        self.groupBox_90.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN4_INPUT_radioButton_1 = QRadioButton(self.groupBox_90)
        self.PORTB_PIN4_INPUT_radioButton_1.setObjectName(u"PORTB_PIN4_INPUT_radioButton_1")
        self.PORTB_PIN4_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN4_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN4_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_90)
        self.PORTB_PIN4_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN4_OUTPUT_radioButton_1")
        self.PORTB_PIN4_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_91 = QGroupBox(self.groupBox_89)
        self.groupBox_91.setObjectName(u"groupBox_91")
        self.groupBox_91.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN4_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_91)
        self.PORTB_PIN4_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN4_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN4_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN4_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN4_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_91)
        self.PORTB_PIN4_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN4_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN4_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_92 = QGroupBox(self.groupBox_89)
        self.groupBox_92.setObjectName(u"groupBox_92")
        self.groupBox_92.setEnabled(False)
        self.groupBox_92.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN4_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_92)
        self.PORTB_PIN4_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN4_OUT_HIGH_radioButton_1")
        self.PORTB_PIN4_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN4_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN4_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_92)
        self.PORTB_PIN4_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN4_OUT_LOW_radioButton_1")
        self.PORTB_PIN4_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_85 = QGroupBox(self.portB_tab)
        self.groupBox_85.setObjectName(u"groupBox_85")
        self.groupBox_85.setGeometry(QRect(530, 570, 471, 171))
        self.groupBox_85.setFont(font2)
        self.groupBox_86 = QGroupBox(self.groupBox_85)
        self.groupBox_86.setObjectName(u"groupBox_86")
        self.groupBox_86.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN7_INPUT_radioButton_1 = QRadioButton(self.groupBox_86)
        self.PORTB_PIN7_INPUT_radioButton_1.setObjectName(u"PORTB_PIN7_INPUT_radioButton_1")
        self.PORTB_PIN7_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN7_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN7_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_86)
        self.PORTB_PIN7_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN7_OUTPUT_radioButton_1")
        self.PORTB_PIN7_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_87 = QGroupBox(self.groupBox_85)
        self.groupBox_87.setObjectName(u"groupBox_87")
        self.groupBox_87.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN7_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_87)
        self.PORTB_PIN7_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN7_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN7_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN7_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN7_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_87)
        self.PORTB_PIN7_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN7_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN7_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_88 = QGroupBox(self.groupBox_85)
        self.groupBox_88.setObjectName(u"groupBox_88")
        self.groupBox_88.setEnabled(False)
        self.groupBox_88.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN7_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_88)
        self.PORTB_PIN7_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN7_OUT_HIGH_radioButton_1")
        self.PORTB_PIN7_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN7_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN7_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_88)
        self.PORTB_PIN7_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN7_OUT_LOW_radioButton_1")
        self.PORTB_PIN7_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_109 = QGroupBox(self.portB_tab)
        self.groupBox_109.setObjectName(u"groupBox_109")
        self.groupBox_109.setGeometry(QRect(20, 570, 471, 171))
        self.groupBox_109.setFont(font2)
        self.groupBox_110 = QGroupBox(self.groupBox_109)
        self.groupBox_110.setObjectName(u"groupBox_110")
        self.groupBox_110.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN6_INPUT_radioButton_1 = QRadioButton(self.groupBox_110)
        self.PORTB_PIN6_INPUT_radioButton_1.setObjectName(u"PORTB_PIN6_INPUT_radioButton_1")
        self.PORTB_PIN6_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN6_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN6_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_110)
        self.PORTB_PIN6_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN6_OUTPUT_radioButton_1")
        self.PORTB_PIN6_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_111 = QGroupBox(self.groupBox_109)
        self.groupBox_111.setObjectName(u"groupBox_111")
        self.groupBox_111.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN6_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_111)
        self.PORTB_PIN6_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN6_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN6_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN6_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN6_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_111)
        self.PORTB_PIN6_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN6_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN6_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_112 = QGroupBox(self.groupBox_109)
        self.groupBox_112.setObjectName(u"groupBox_112")
        self.groupBox_112.setEnabled(False)
        self.groupBox_112.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN6_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_112)
        self.PORTB_PIN6_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN6_OUT_HIGH_radioButton_1")
        self.PORTB_PIN6_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN6_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN6_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_112)
        self.PORTB_PIN6_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN6_OUT_LOW_radioButton_1")
        self.PORTB_PIN6_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_93 = QGroupBox(self.portB_tab)
        self.groupBox_93.setObjectName(u"groupBox_93")
        self.groupBox_93.setGeometry(QRect(20, 30, 471, 171))
        self.groupBox_93.setFont(font2)
        self.groupBox_94 = QGroupBox(self.groupBox_93)
        self.groupBox_94.setObjectName(u"groupBox_94")
        self.groupBox_94.setGeometry(QRect(10, 30, 141, 131))
        self.PORTB_PIN0_INPUT_radioButton_1 = QRadioButton(self.groupBox_94)
        self.PORTB_PIN0_INPUT_radioButton_1.setObjectName(u"PORTB_PIN0_INPUT_radioButton_1")
        self.PORTB_PIN0_INPUT_radioButton_1.setGeometry(QRect(10, 40, 95, 20))
        self.PORTB_PIN0_INPUT_radioButton_1.setChecked(True)
        self.PORTB_PIN0_OUTPUT_radioButton_1 = QRadioButton(self.groupBox_94)
        self.PORTB_PIN0_OUTPUT_radioButton_1.setObjectName(u"PORTB_PIN0_OUTPUT_radioButton_1")
        self.PORTB_PIN0_OUTPUT_radioButton_1.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_95 = QGroupBox(self.groupBox_93)
        self.groupBox_95.setObjectName(u"groupBox_95")
        self.groupBox_95.setGeometry(QRect(170, 20, 281, 61))
        self.PORTB_PIN0_IN_PULL_UP_radioButton_1 = QRadioButton(self.groupBox_95)
        self.PORTB_PIN0_IN_PULL_UP_radioButton_1.setObjectName(u"PORTB_PIN0_IN_PULL_UP_radioButton_1")
        self.PORTB_PIN0_IN_PULL_UP_radioButton_1.setGeometry(QRect(10, 30, 95, 20))
        self.PORTB_PIN0_IN_PULL_UP_radioButton_1.setChecked(True)
        self.PORTB_PIN0_IN_PULL_DOWN_radioButton_1 = QRadioButton(self.groupBox_95)
        self.PORTB_PIN0_IN_PULL_DOWN_radioButton_1.setObjectName(u"PORTB_PIN0_IN_PULL_DOWN_radioButton_1")
        self.PORTB_PIN0_IN_PULL_DOWN_radioButton_1.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_96 = QGroupBox(self.groupBox_93)
        self.groupBox_96.setObjectName(u"groupBox_96")
        self.groupBox_96.setEnabled(False)
        self.groupBox_96.setGeometry(QRect(170, 90, 281, 71))
        self.PORTB_PIN0_OUT_HIGH_radioButton_1 = QRadioButton(self.groupBox_96)
        self.PORTB_PIN0_OUT_HIGH_radioButton_1.setObjectName(u"PORTB_PIN0_OUT_HIGH_radioButton_1")
        self.PORTB_PIN0_OUT_HIGH_radioButton_1.setGeometry(QRect(10, 30, 111, 20))
        self.PORTB_PIN0_OUT_HIGH_radioButton_1.setChecked(True)
        self.PORTB_PIN0_OUT_LOW_radioButton_1 = QRadioButton(self.groupBox_96)
        self.PORTB_PIN0_OUT_LOW_radioButton_1.setObjectName(u"PORTB_PIN0_OUT_LOW_radioButton_1")
        self.PORTB_PIN0_OUT_LOW_radioButton_1.setGeometry(QRect(140, 30, 95, 20))
        self.tabWidget_2.addTab(self.portB_tab, "")
        self.portC_tab = QWidget()
        self.portC_tab.setObjectName(u"portC_tab")
        self.groupBox_225 = QGroupBox(self.portC_tab)
        self.groupBox_225.setObjectName(u"groupBox_225")
        self.groupBox_225.setGeometry(QRect(530, 210, 471, 171))
        self.groupBox_225.setFont(font2)
        self.groupBox_226 = QGroupBox(self.groupBox_225)
        self.groupBox_226.setObjectName(u"groupBox_226")
        self.groupBox_226.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN3_INPUT_radioButton_2 = QRadioButton(self.groupBox_226)
        self.PORTC_PIN3_INPUT_radioButton_2.setObjectName(u"PORTC_PIN3_INPUT_radioButton_2")
        self.PORTC_PIN3_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN3_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN3_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_226)
        self.PORTC_PIN3_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN3_OUTPUT_radioButton_2")
        self.PORTC_PIN3_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_227 = QGroupBox(self.groupBox_225)
        self.groupBox_227.setObjectName(u"groupBox_227")
        self.groupBox_227.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN3_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_227)
        self.PORTC_PIN3_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN3_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN3_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN3_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN3_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_227)
        self.PORTC_PIN3_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN3_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN3_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_228 = QGroupBox(self.groupBox_225)
        self.groupBox_228.setObjectName(u"groupBox_228")
        self.groupBox_228.setEnabled(False)
        self.groupBox_228.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN3_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_228)
        self.PORTC_PIN3_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN3_OUT_HIGH_radioButton_2")
        self.PORTC_PIN3_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN3_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN3_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_228)
        self.PORTC_PIN3_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN3_OUT_LOW_radioButton_2")
        self.PORTC_PIN3_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_205 = QGroupBox(self.portC_tab)
        self.groupBox_205.setObjectName(u"groupBox_205")
        self.groupBox_205.setGeometry(QRect(20, 30, 471, 171))
        self.groupBox_205.setFont(font2)
        self.groupBox_206 = QGroupBox(self.groupBox_205)
        self.groupBox_206.setObjectName(u"groupBox_206")
        self.groupBox_206.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN0_INPUT_radioButton_2 = QRadioButton(self.groupBox_206)
        self.PORTC_PIN0_INPUT_radioButton_2.setObjectName(u"PORTC_PIN0_INPUT_radioButton_2")
        self.PORTC_PIN0_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN0_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN0_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_206)
        self.PORTC_PIN0_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN0_OUTPUT_radioButton_2")
        self.PORTC_PIN0_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_207 = QGroupBox(self.groupBox_205)
        self.groupBox_207.setObjectName(u"groupBox_207")
        self.groupBox_207.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN0_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_207)
        self.PORTC_PIN0_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN0_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN0_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN0_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN0_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_207)
        self.PORTC_PIN0_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN0_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN0_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_208 = QGroupBox(self.groupBox_205)
        self.groupBox_208.setObjectName(u"groupBox_208")
        self.groupBox_208.setEnabled(False)
        self.groupBox_208.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN0_OUT_HIGH_radioButton = QRadioButton(self.groupBox_208)
        self.PORTC_PIN0_OUT_HIGH_radioButton.setObjectName(u"PORTC_PIN0_OUT_HIGH_radioButton")
        self.PORTC_PIN0_OUT_HIGH_radioButton.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN0_OUT_HIGH_radioButton.setChecked(True)
        self.PORTC_PIN0_OUT_LOW_radioButton = QRadioButton(self.groupBox_208)
        self.PORTC_PIN0_OUT_LOW_radioButton.setObjectName(u"PORTC_PIN0_OUT_LOW_radioButton")
        self.PORTC_PIN0_OUT_LOW_radioButton.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_117 = QGroupBox(self.portC_tab)
        self.groupBox_117.setObjectName(u"groupBox_117")
        self.groupBox_117.setGeometry(QRect(530, 570, 471, 171))
        self.groupBox_117.setFont(font2)
        self.groupBox_121 = QGroupBox(self.groupBox_117)
        self.groupBox_121.setObjectName(u"groupBox_121")
        self.groupBox_121.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN7_INPUT_radioButton_2 = QRadioButton(self.groupBox_121)
        self.PORTC_PIN7_INPUT_radioButton_2.setObjectName(u"PORTC_PIN7_INPUT_radioButton_2")
        self.PORTC_PIN7_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN7_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN7_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_121)
        self.PORTC_PIN7_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN7_OUTPUT_radioButton_2")
        self.PORTC_PIN7_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_125 = QGroupBox(self.groupBox_117)
        self.groupBox_125.setObjectName(u"groupBox_125")
        self.groupBox_125.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN7_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_125)
        self.PORTC_PIN7_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN7_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN7_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN7_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN7_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_125)
        self.PORTC_PIN7_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN7_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN7_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_129 = QGroupBox(self.groupBox_117)
        self.groupBox_129.setObjectName(u"groupBox_129")
        self.groupBox_129.setEnabled(False)
        self.groupBox_129.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN7_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_129)
        self.PORTC_PIN7_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN7_OUT_HIGH_radioButton_2")
        self.PORTC_PIN7_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN7_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN7_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_129)
        self.PORTC_PIN7_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN7_OUT_LOW_radioButton_2")
        self.PORTC_PIN7_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_213 = QGroupBox(self.portC_tab)
        self.groupBox_213.setObjectName(u"groupBox_213")
        self.groupBox_213.setGeometry(QRect(530, 390, 471, 171))
        self.groupBox_213.setFont(font2)
        self.groupBox_214 = QGroupBox(self.groupBox_213)
        self.groupBox_214.setObjectName(u"groupBox_214")
        self.groupBox_214.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN5_INPUT_radioButton_2 = QRadioButton(self.groupBox_214)
        self.PORTC_PIN5_INPUT_radioButton_2.setObjectName(u"PORTC_PIN5_INPUT_radioButton_2")
        self.PORTC_PIN5_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN5_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN5_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_214)
        self.PORTC_PIN5_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN5_OUTPUT_radioButton_2")
        self.PORTC_PIN5_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_215 = QGroupBox(self.groupBox_213)
        self.groupBox_215.setObjectName(u"groupBox_215")
        self.groupBox_215.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN5_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_215)
        self.PORTC_PIN5_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN5_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN5_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN5_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN5_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_215)
        self.PORTC_PIN5_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN5_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN5_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_216 = QGroupBox(self.groupBox_213)
        self.groupBox_216.setObjectName(u"groupBox_216")
        self.groupBox_216.setEnabled(False)
        self.groupBox_216.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN5_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_216)
        self.PORTC_PIN5_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN5_OUT_HIGH_radioButton_2")
        self.PORTC_PIN5_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN5_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN5_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_216)
        self.PORTC_PIN5_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN5_OUT_LOW_radioButton_2")
        self.PORTC_PIN5_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_209 = QGroupBox(self.portC_tab)
        self.groupBox_209.setObjectName(u"groupBox_209")
        self.groupBox_209.setGeometry(QRect(20, 210, 471, 171))
        self.groupBox_209.setFont(font2)
        self.groupBox_210 = QGroupBox(self.groupBox_209)
        self.groupBox_210.setObjectName(u"groupBox_210")
        self.groupBox_210.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN2_INPUT_radioButton_2 = QRadioButton(self.groupBox_210)
        self.PORTC_PIN2_INPUT_radioButton_2.setObjectName(u"PORTC_PIN2_INPUT_radioButton_2")
        self.PORTC_PIN2_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN2_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN2_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_210)
        self.PORTC_PIN2_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN2_OUTPUT_radioButton_2")
        self.PORTC_PIN2_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.PORTC_PIN2_OUTPUT_radioButton_2.setChecked(False)
        self.groupBox_211 = QGroupBox(self.groupBox_209)
        self.groupBox_211.setObjectName(u"groupBox_211")
        self.groupBox_211.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN2_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_211)
        self.PORTC_PIN2_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN2_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN2_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN2_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN2_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_211)
        self.PORTC_PIN2_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN2_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN2_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_212 = QGroupBox(self.groupBox_209)
        self.groupBox_212.setObjectName(u"groupBox_212")
        self.groupBox_212.setEnabled(False)
        self.groupBox_212.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN2_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_212)
        self.PORTC_PIN2_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN2_OUT_HIGH_radioButton_2")
        self.PORTC_PIN2_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN2_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN2_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_212)
        self.PORTC_PIN2_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN2_OUT_LOW_radioButton_2")
        self.PORTC_PIN2_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_133 = QGroupBox(self.portC_tab)
        self.groupBox_133.setObjectName(u"groupBox_133")
        self.groupBox_133.setGeometry(QRect(20, 390, 471, 171))
        self.groupBox_133.setFont(font2)
        self.groupBox_137 = QGroupBox(self.groupBox_133)
        self.groupBox_137.setObjectName(u"groupBox_137")
        self.groupBox_137.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN4_INPUT_radioButton_2 = QRadioButton(self.groupBox_137)
        self.PORTC_PIN4_INPUT_radioButton_2.setObjectName(u"PORTC_PIN4_INPUT_radioButton_2")
        self.PORTC_PIN4_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN4_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN4_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_137)
        self.PORTC_PIN4_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN4_OUTPUT_radioButton_2")
        self.PORTC_PIN4_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_141 = QGroupBox(self.groupBox_133)
        self.groupBox_141.setObjectName(u"groupBox_141")
        self.groupBox_141.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN4_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_141)
        self.PORTC_PIN4_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN4_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN4_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN4_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN4_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_141)
        self.PORTC_PIN4_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN4_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN4_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_145 = QGroupBox(self.groupBox_133)
        self.groupBox_145.setObjectName(u"groupBox_145")
        self.groupBox_145.setEnabled(False)
        self.groupBox_145.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN4_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_145)
        self.PORTC_PIN4_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN4_OUT_HIGH_radioButton_2")
        self.PORTC_PIN4_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN4_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN4_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_145)
        self.PORTC_PIN4_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN4_OUT_LOW_radioButton_2")
        self.PORTC_PIN4_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_221 = QGroupBox(self.portC_tab)
        self.groupBox_221.setObjectName(u"groupBox_221")
        self.groupBox_221.setGeometry(QRect(20, 570, 471, 171))
        self.groupBox_221.setFont(font2)
        self.groupBox_222 = QGroupBox(self.groupBox_221)
        self.groupBox_222.setObjectName(u"groupBox_222")
        self.groupBox_222.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN6_INPUT_radioButton_2 = QRadioButton(self.groupBox_222)
        self.PORTC_PIN6_INPUT_radioButton_2.setObjectName(u"PORTC_PIN6_INPUT_radioButton_2")
        self.PORTC_PIN6_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN6_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN6_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_222)
        self.PORTC_PIN6_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN6_OUTPUT_radioButton_2")
        self.PORTC_PIN6_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_223 = QGroupBox(self.groupBox_221)
        self.groupBox_223.setObjectName(u"groupBox_223")
        self.groupBox_223.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN6_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_223)
        self.PORTC_PIN6_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN6_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN6_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN6_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN6_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_223)
        self.PORTC_PIN6_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN6_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN6_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_224 = QGroupBox(self.groupBox_221)
        self.groupBox_224.setObjectName(u"groupBox_224")
        self.groupBox_224.setEnabled(False)
        self.groupBox_224.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN6_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_224)
        self.PORTC_PIN6_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN6_OUT_HIGH_radioButton_2")
        self.PORTC_PIN6_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN6_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN6_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_224)
        self.PORTC_PIN6_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN6_OUT_LOW_radioButton_2")
        self.PORTC_PIN6_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_217 = QGroupBox(self.portC_tab)
        self.groupBox_217.setObjectName(u"groupBox_217")
        self.groupBox_217.setGeometry(QRect(530, 30, 471, 171))
        self.groupBox_217.setFont(font2)
        self.groupBox_218 = QGroupBox(self.groupBox_217)
        self.groupBox_218.setObjectName(u"groupBox_218")
        self.groupBox_218.setGeometry(QRect(10, 30, 141, 131))
        self.PORTC_PIN1_INPUT_radioButton_2 = QRadioButton(self.groupBox_218)
        self.PORTC_PIN1_INPUT_radioButton_2.setObjectName(u"PORTC_PIN1_INPUT_radioButton_2")
        self.PORTC_PIN1_INPUT_radioButton_2.setGeometry(QRect(10, 40, 95, 20))
        self.PORTC_PIN1_INPUT_radioButton_2.setChecked(True)
        self.PORTC_PIN1_OUTPUT_radioButton_2 = QRadioButton(self.groupBox_218)
        self.PORTC_PIN1_OUTPUT_radioButton_2.setObjectName(u"PORTC_PIN1_OUTPUT_radioButton_2")
        self.PORTC_PIN1_OUTPUT_radioButton_2.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_219 = QGroupBox(self.groupBox_217)
        self.groupBox_219.setObjectName(u"groupBox_219")
        self.groupBox_219.setGeometry(QRect(170, 20, 281, 61))
        self.PORTC_PIN1_IN_PULL_UP_radioButton_2 = QRadioButton(self.groupBox_219)
        self.PORTC_PIN1_IN_PULL_UP_radioButton_2.setObjectName(u"PORTC_PIN1_IN_PULL_UP_radioButton_2")
        self.PORTC_PIN1_IN_PULL_UP_radioButton_2.setGeometry(QRect(10, 30, 95, 20))
        self.PORTC_PIN1_IN_PULL_UP_radioButton_2.setChecked(True)
        self.PORTC_PIN1_IN_PULL_DOWN_radioButton_2 = QRadioButton(self.groupBox_219)
        self.PORTC_PIN1_IN_PULL_DOWN_radioButton_2.setObjectName(u"PORTC_PIN1_IN_PULL_DOWN_radioButton_2")
        self.PORTC_PIN1_IN_PULL_DOWN_radioButton_2.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_220 = QGroupBox(self.groupBox_217)
        self.groupBox_220.setObjectName(u"groupBox_220")
        self.groupBox_220.setEnabled(False)
        self.groupBox_220.setGeometry(QRect(170, 90, 281, 71))
        self.PORTC_PIN1_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_220)
        self.PORTC_PIN1_OUT_HIGH_radioButton_2.setObjectName(u"PORTC_PIN1_OUT_HIGH_radioButton_2")
        self.PORTC_PIN1_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTC_PIN1_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTC_PIN1_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_220)
        self.PORTC_PIN1_OUT_LOW_radioButton_2.setObjectName(u"PORTC_PIN1_OUT_LOW_radioButton_2")
        self.PORTC_PIN1_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.tabWidget_2.addTab(self.portC_tab, "")
        self.portD_tab = QWidget()
        self.portD_tab.setObjectName(u"portD_tab")
        self.groupBox_229 = QGroupBox(self.portD_tab)
        self.groupBox_229.setObjectName(u"groupBox_229")
        self.groupBox_229.setGeometry(QRect(20, 30, 471, 171))
        self.groupBox_229.setFont(font2)
        self.groupBox_230 = QGroupBox(self.groupBox_229)
        self.groupBox_230.setObjectName(u"groupBox_230")
        self.groupBox_230.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN0_INPUT_radioButton_3 = QRadioButton(self.groupBox_230)
        self.PORTD_PIN0_INPUT_radioButton_3.setObjectName(u"PORTD_PIN0_INPUT_radioButton_3")
        self.PORTD_PIN0_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN0_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN0_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_230)
        self.PORTD_PIN0_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN0_OUTPUT_radioButton_3")
        self.PORTD_PIN0_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_231 = QGroupBox(self.groupBox_229)
        self.groupBox_231.setObjectName(u"groupBox_231")
        self.groupBox_231.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN0_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_231)
        self.PORTD_PIN0_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN0_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN0_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN0_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN0_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_231)
        self.PORTD_PIN0_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN0_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN0_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_232 = QGroupBox(self.groupBox_229)
        self.groupBox_232.setObjectName(u"groupBox_232")
        self.groupBox_232.setEnabled(False)
        self.groupBox_232.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN0_OUT_HIGH_radioButton_2 = QRadioButton(self.groupBox_232)
        self.PORTD_PIN0_OUT_HIGH_radioButton_2.setObjectName(u"PORTD_PIN0_OUT_HIGH_radioButton_2")
        self.PORTD_PIN0_OUT_HIGH_radioButton_2.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN0_OUT_HIGH_radioButton_2.setChecked(True)
        self.PORTD_PIN0_OUT_LOW_radioButton_2 = QRadioButton(self.groupBox_232)
        self.PORTD_PIN0_OUT_LOW_radioButton_2.setObjectName(u"PORTD_PIN0_OUT_LOW_radioButton_2")
        self.PORTD_PIN0_OUT_LOW_radioButton_2.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_149 = QGroupBox(self.portD_tab)
        self.groupBox_149.setObjectName(u"groupBox_149")
        self.groupBox_149.setGeometry(QRect(530, 570, 471, 171))
        self.groupBox_149.setFont(font2)
        self.groupBox_153 = QGroupBox(self.groupBox_149)
        self.groupBox_153.setObjectName(u"groupBox_153")
        self.groupBox_153.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN7_INPUT_radioButton_3 = QRadioButton(self.groupBox_153)
        self.PORTD_PIN7_INPUT_radioButton_3.setObjectName(u"PORTD_PIN7_INPUT_radioButton_3")
        self.PORTD_PIN7_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN7_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN7_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_153)
        self.PORTD_PIN7_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN7_OUTPUT_radioButton_3")
        self.PORTD_PIN7_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_157 = QGroupBox(self.groupBox_149)
        self.groupBox_157.setObjectName(u"groupBox_157")
        self.groupBox_157.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN7_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_157)
        self.PORTD_PIN7_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN7_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN7_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN7_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN7_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_157)
        self.PORTD_PIN7_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN7_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN7_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_161 = QGroupBox(self.groupBox_149)
        self.groupBox_161.setObjectName(u"groupBox_161")
        self.groupBox_161.setEnabled(False)
        self.groupBox_161.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN7_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_161)
        self.PORTD_PIN7_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN7_OUT_HIGH_radioButton_3")
        self.PORTD_PIN7_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN7_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN7_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_161)
        self.PORTD_PIN7_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN7_OUT_LOW_radioButton_3")
        self.PORTD_PIN7_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_233 = QGroupBox(self.portD_tab)
        self.groupBox_233.setObjectName(u"groupBox_233")
        self.groupBox_233.setGeometry(QRect(530, 390, 471, 171))
        self.groupBox_233.setFont(font2)
        self.groupBox_234 = QGroupBox(self.groupBox_233)
        self.groupBox_234.setObjectName(u"groupBox_234")
        self.groupBox_234.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN5_INPUT_radioButton_3 = QRadioButton(self.groupBox_234)
        self.PORTD_PIN5_INPUT_radioButton_3.setObjectName(u"PORTD_PIN5_INPUT_radioButton_3")
        self.PORTD_PIN5_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN5_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN5_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_234)
        self.PORTD_PIN5_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN5_OUTPUT_radioButton_3")
        self.PORTD_PIN5_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_235 = QGroupBox(self.groupBox_233)
        self.groupBox_235.setObjectName(u"groupBox_235")
        self.groupBox_235.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN5_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_235)
        self.PORTD_PIN5_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN5_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN5_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN5_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN5_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_235)
        self.PORTD_PIN5_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN5_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN5_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_236 = QGroupBox(self.groupBox_233)
        self.groupBox_236.setObjectName(u"groupBox_236")
        self.groupBox_236.setEnabled(False)
        self.groupBox_236.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN5_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_236)
        self.PORTD_PIN5_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN5_OUT_HIGH_radioButton_3")
        self.PORTD_PIN5_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN5_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN5_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_236)
        self.PORTD_PIN5_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN5_OUT_LOW_radioButton_3")
        self.PORTD_PIN5_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_237 = QGroupBox(self.portD_tab)
        self.groupBox_237.setObjectName(u"groupBox_237")
        self.groupBox_237.setGeometry(QRect(20, 210, 471, 171))
        self.groupBox_237.setFont(font2)
        self.groupBox_238 = QGroupBox(self.groupBox_237)
        self.groupBox_238.setObjectName(u"groupBox_238")
        self.groupBox_238.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN2_INPUT_radioButton_3 = QRadioButton(self.groupBox_238)
        self.PORTD_PIN2_INPUT_radioButton_3.setObjectName(u"PORTD_PIN2_INPUT_radioButton_3")
        self.PORTD_PIN2_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN2_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN2_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_238)
        self.PORTD_PIN2_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN2_OUTPUT_radioButton_3")
        self.PORTD_PIN2_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.PORTD_PIN2_OUTPUT_radioButton_3.setChecked(False)
        self.groupBox_239 = QGroupBox(self.groupBox_237)
        self.groupBox_239.setObjectName(u"groupBox_239")
        self.groupBox_239.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN2_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_239)
        self.PORTD_PIN2_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN2_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN2_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN2_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN2_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_239)
        self.PORTD_PIN2_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN2_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN2_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_240 = QGroupBox(self.groupBox_237)
        self.groupBox_240.setObjectName(u"groupBox_240")
        self.groupBox_240.setEnabled(False)
        self.groupBox_240.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN2_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_240)
        self.PORTD_PIN2_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN2_OUT_HIGH_radioButton_3")
        self.PORTD_PIN2_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN2_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN2_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_240)
        self.PORTD_PIN2_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN2_OUT_LOW_radioButton_3")
        self.PORTD_PIN2_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_165 = QGroupBox(self.portD_tab)
        self.groupBox_165.setObjectName(u"groupBox_165")
        self.groupBox_165.setGeometry(QRect(20, 390, 471, 171))
        self.groupBox_165.setFont(font2)
        self.groupBox_169 = QGroupBox(self.groupBox_165)
        self.groupBox_169.setObjectName(u"groupBox_169")
        self.groupBox_169.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN4_INPUT_radioButton_3 = QRadioButton(self.groupBox_169)
        self.PORTD_PIN4_INPUT_radioButton_3.setObjectName(u"PORTD_PIN4_INPUT_radioButton_3")
        self.PORTD_PIN4_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN4_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN4_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_169)
        self.PORTD_PIN4_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN4_OUTPUT_radioButton_3")
        self.PORTD_PIN4_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_173 = QGroupBox(self.groupBox_165)
        self.groupBox_173.setObjectName(u"groupBox_173")
        self.groupBox_173.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN4_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_173)
        self.PORTD_PIN4_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN4_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN4_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN4_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN4_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_173)
        self.PORTD_PIN4_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN4_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN4_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_177 = QGroupBox(self.groupBox_165)
        self.groupBox_177.setObjectName(u"groupBox_177")
        self.groupBox_177.setEnabled(False)
        self.groupBox_177.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN4_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_177)
        self.PORTD_PIN4_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN4_OUT_HIGH_radioButton_3")
        self.PORTD_PIN4_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN4_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN4_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_177)
        self.PORTD_PIN4_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN4_OUT_LOW_radioButton_3")
        self.PORTD_PIN4_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_241 = QGroupBox(self.portD_tab)
        self.groupBox_241.setObjectName(u"groupBox_241")
        self.groupBox_241.setGeometry(QRect(20, 570, 471, 171))
        self.groupBox_241.setFont(font2)
        self.groupBox_242 = QGroupBox(self.groupBox_241)
        self.groupBox_242.setObjectName(u"groupBox_242")
        self.groupBox_242.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN6_INPUT_radioButton_3 = QRadioButton(self.groupBox_242)
        self.PORTD_PIN6_INPUT_radioButton_3.setObjectName(u"PORTD_PIN6_INPUT_radioButton_3")
        self.PORTD_PIN6_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN6_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN6_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_242)
        self.PORTD_PIN6_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN6_OUTPUT_radioButton_3")
        self.PORTD_PIN6_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_243 = QGroupBox(self.groupBox_241)
        self.groupBox_243.setObjectName(u"groupBox_243")
        self.groupBox_243.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN6_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_243)
        self.PORTD_PIN6_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN6_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN6_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN6_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN6_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_243)
        self.PORTD_PIN6_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN6_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN6_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_244 = QGroupBox(self.groupBox_241)
        self.groupBox_244.setObjectName(u"groupBox_244")
        self.groupBox_244.setEnabled(False)
        self.groupBox_244.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN6_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_244)
        self.PORTD_PIN6_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN6_OUT_HIGH_radioButton_3")
        self.PORTD_PIN6_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN6_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN6_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_244)
        self.PORTD_PIN6_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN6_OUT_LOW_radioButton_3")
        self.PORTD_PIN6_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_245 = QGroupBox(self.portD_tab)
        self.groupBox_245.setObjectName(u"groupBox_245")
        self.groupBox_245.setGeometry(QRect(530, 30, 471, 171))
        self.groupBox_245.setFont(font2)
        self.groupBox_246 = QGroupBox(self.groupBox_245)
        self.groupBox_246.setObjectName(u"groupBox_246")
        self.groupBox_246.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN1_INPUT_radioButton_3 = QRadioButton(self.groupBox_246)
        self.PORTD_PIN1_INPUT_radioButton_3.setObjectName(u"PORTD_PIN1_INPUT_radioButton_3")
        self.PORTD_PIN1_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN1_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN1_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_246)
        self.PORTD_PIN1_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN1_OUTPUT_radioButton_3")
        self.PORTD_PIN1_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_247 = QGroupBox(self.groupBox_245)
        self.groupBox_247.setObjectName(u"groupBox_247")
        self.groupBox_247.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN1_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_247)
        self.PORTD_PIN1_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN1_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN1_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN1_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN1_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_247)
        self.PORTD_PIN1_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN1_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN1_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_248 = QGroupBox(self.groupBox_245)
        self.groupBox_248.setObjectName(u"groupBox_248")
        self.groupBox_248.setEnabled(False)
        self.groupBox_248.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN1_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_248)
        self.PORTD_PIN1_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN1_OUT_HIGH_radioButton_3")
        self.PORTD_PIN1_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN1_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN1_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_248)
        self.PORTD_PIN1_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN1_OUT_LOW_radioButton_3")
        self.PORTD_PIN1_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.groupBox_249 = QGroupBox(self.portD_tab)
        self.groupBox_249.setObjectName(u"groupBox_249")
        self.groupBox_249.setGeometry(QRect(530, 210, 471, 171))
        self.groupBox_249.setFont(font2)
        self.groupBox_250 = QGroupBox(self.groupBox_249)
        self.groupBox_250.setObjectName(u"groupBox_250")
        self.groupBox_250.setGeometry(QRect(10, 30, 141, 131))
        self.PORTD_PIN3_INPUT_radioButton_3 = QRadioButton(self.groupBox_250)
        self.PORTD_PIN3_INPUT_radioButton_3.setObjectName(u"PORTD_PIN3_INPUT_radioButton_3")
        self.PORTD_PIN3_INPUT_radioButton_3.setGeometry(QRect(10, 40, 95, 20))
        self.PORTD_PIN3_INPUT_radioButton_3.setChecked(True)
        self.PORTD_PIN3_OUTPUT_radioButton_3 = QRadioButton(self.groupBox_250)
        self.PORTD_PIN3_OUTPUT_radioButton_3.setObjectName(u"PORTD_PIN3_OUTPUT_radioButton_3")
        self.PORTD_PIN3_OUTPUT_radioButton_3.setGeometry(QRect(10, 80, 95, 20))
        self.groupBox_251 = QGroupBox(self.groupBox_249)
        self.groupBox_251.setObjectName(u"groupBox_251")
        self.groupBox_251.setGeometry(QRect(170, 20, 281, 61))
        self.PORTD_PIN3_IN_PULL_UP_radioButton_3 = QRadioButton(self.groupBox_251)
        self.PORTD_PIN3_IN_PULL_UP_radioButton_3.setObjectName(u"PORTD_PIN3_IN_PULL_UP_radioButton_3")
        self.PORTD_PIN3_IN_PULL_UP_radioButton_3.setGeometry(QRect(10, 30, 95, 20))
        self.PORTD_PIN3_IN_PULL_UP_radioButton_3.setChecked(True)
        self.PORTD_PIN3_IN_PULL_DOWN_radioButton_3 = QRadioButton(self.groupBox_251)
        self.PORTD_PIN3_IN_PULL_DOWN_radioButton_3.setObjectName(u"PORTD_PIN3_IN_PULL_DOWN_radioButton_3")
        self.PORTD_PIN3_IN_PULL_DOWN_radioButton_3.setGeometry(QRect(140, 30, 141, 20))
        self.groupBox_252 = QGroupBox(self.groupBox_249)
        self.groupBox_252.setObjectName(u"groupBox_252")
        self.groupBox_252.setEnabled(False)
        self.groupBox_252.setGeometry(QRect(170, 90, 281, 71))
        self.PORTD_PIN3_OUT_HIGH_radioButton_3 = QRadioButton(self.groupBox_252)
        self.PORTD_PIN3_OUT_HIGH_radioButton_3.setObjectName(u"PORTD_PIN3_OUT_HIGH_radioButton_3")
        self.PORTD_PIN3_OUT_HIGH_radioButton_3.setGeometry(QRect(10, 30, 111, 20))
        self.PORTD_PIN3_OUT_HIGH_radioButton_3.setChecked(True)
        self.PORTD_PIN3_OUT_LOW_radioButton_3 = QRadioButton(self.groupBox_252)
        self.PORTD_PIN3_OUT_LOW_radioButton_3.setObjectName(u"PORTD_PIN3_OUT_LOW_radioButton_3")
        self.PORTD_PIN3_OUT_LOW_radioButton_3.setGeometry(QRect(140, 30, 95, 20))
        self.tabWidget_2.addTab(self.portD_tab, "")
        self.generate_tab = QWidget()
        self.generate_tab.setObjectName(u"generate_tab")
        self.path_text = QPlainTextEdit(self.generate_tab)
        self.path_text.setObjectName(u"path_text")
        self.path_text.setGeometry(QRect(90, 100, 891, 51))
        self.label = QLabel(self.generate_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 101, 41))
        self.generate_PB = QPushButton(self.generate_tab)
        self.generate_PB.setObjectName(u"generate_PB")
        self.generate_PB.setGeometry(QRect(610, 220, 171, 61))
        # self.save_PB = QPushButton(self.generate_tab)
        # self.save_PB.setObjectName(u"save_PB")
        # self.save_PB.setGeometry(QRect(140, 220, 171, 61))
        self.load_PB = QPushButton(self.generate_tab)
        self.load_PB.setObjectName(u"load_PB")
        self.load_PB.setGeometry(QRect(370, 220, 171, 61))
        self.tabWidget_2.addTab(self.generate_tab, "")
        self.tabWidget.addTab(self.dio_tab, "")
        self.timer_tab = QWidget()
        self.timer_tab.setObjectName(u"timer_tab")
        self.tabWidget.addTab(self.timer_tab, "")

        self.retranslateUi(Form)
        self.PORTD_PIN0_INPUT_radioButton_3.toggled.connect(self.groupBox_231.setEnabled)
        self.PORTD_PIN0_INPUT_radioButton_3.toggled.connect(self.groupBox_232.setDisabled)
        self.PORTD_PIN0_OUTPUT_radioButton_3.toggled.connect(self.groupBox_231.setDisabled)
        self.PORTD_PIN0_OUTPUT_radioButton_3.toggled.connect(self.groupBox_232.setEnabled)
        self.PORTD_PIN1_INPUT_radioButton_3.toggled.connect(self.groupBox_247.setEnabled)
        self.PORTD_PIN1_INPUT_radioButton_3.toggled.connect(self.groupBox_248.setDisabled)
        self.PORTD_PIN1_OUTPUT_radioButton_3.toggled.connect(self.groupBox_247.setDisabled)
        self.PORTD_PIN1_OUTPUT_radioButton_3.toggled.connect(self.groupBox_248.setEnabled)
        self.PORTD_PIN2_INPUT_radioButton_3.toggled.connect(self.groupBox_239.setEnabled)
        self.PORTD_PIN2_INPUT_radioButton_3.toggled.connect(self.groupBox_240.setDisabled)
        self.PORTD_PIN2_OUTPUT_radioButton_3.toggled.connect(self.groupBox_239.setDisabled)
        self.PORTD_PIN2_OUTPUT_radioButton_3.toggled.connect(self.groupBox_240.setEnabled)
        self.PORTD_PIN3_INPUT_radioButton_3.toggled.connect(self.groupBox_251.setEnabled)
        self.PORTD_PIN3_INPUT_radioButton_3.toggled.connect(self.groupBox_252.setDisabled)
        self.PORTD_PIN3_OUTPUT_radioButton_3.toggled.connect(self.groupBox_251.setDisabled)
        self.PORTD_PIN3_OUTPUT_radioButton_3.toggled.connect(self.groupBox_252.setEnabled)
        self.PORTD_PIN4_INPUT_radioButton_3.toggled.connect(self.groupBox_173.setEnabled)
        self.PORTD_PIN4_INPUT_radioButton_3.toggled.connect(self.groupBox_177.setDisabled)
        self.PORTD_PIN4_OUTPUT_radioButton_3.toggled.connect(self.groupBox_173.setDisabled)
        self.PORTD_PIN4_OUTPUT_radioButton_3.toggled.connect(self.groupBox_177.setEnabled)
        self.PORTD_PIN5_INPUT_radioButton_3.toggled.connect(self.groupBox_235.setEnabled)
        self.PORTD_PIN5_INPUT_radioButton_3.toggled.connect(self.groupBox_236.setDisabled)
        self.PORTD_PIN5_OUTPUT_radioButton_3.toggled.connect(self.groupBox_235.setDisabled)
        self.PORTD_PIN5_OUTPUT_radioButton_3.toggled.connect(self.groupBox_236.setEnabled)
        self.PORTD_PIN6_INPUT_radioButton_3.toggled.connect(self.groupBox_243.setEnabled)
        self.PORTD_PIN6_INPUT_radioButton_3.toggled.connect(self.groupBox_244.setDisabled)
        self.PORTC_PIN5_INPUT_radioButton_2.toggled.connect(self.groupBox_216.setDisabled)
        self.PORTA_PIN0_INPUT_radioButton_.toggled.connect(self.groupBox_4.setEnabled)
        self.PORTA_PIN7_INPUT_radioButton_.toggled.connect(self.groupBox_52.setDisabled)
        self.PORTB_PIN2_INPUT_radioButton_1.toggled.connect(self.groupBox_99.setEnabled)
        self.PORTC_PIN6_OUTPUT_radioButton_2.toggled.connect(self.groupBox_223.setDisabled)
        self.PORTB_PIN5_OUTPUT_radioButton_1.toggled.connect(self.groupBox_104.setEnabled)
        self.PORTB_PIN6_OUTPUT_radioButton_1.toggled.connect(self.groupBox_112.setEnabled)
        self.PORTA_PIN0_INPUT_radioButton_.toggled.connect(self.groupBox_5.setDisabled)
        self.PORTC_PIN2_OUTPUT_radioButton_2.toggled.connect(self.groupBox_212.setEnabled)
        self.PORTB_PIN3_OUTPUT_radioButton_1.toggled.connect(self.groupBox_116.setEnabled)
        self.PORTC_PIN4_INPUT_radioButton_2.toggled.connect(self.groupBox_141.setEnabled)
        self.PORTC_PIN4_OUTPUT_radioButton_2.toggled.connect(self.groupBox_145.setEnabled)
        self.PORTC_PIN2_OUTPUT_radioButton_2.toggled.connect(self.groupBox_211.setDisabled)
        self.PORTA_PIN0_OUTPUT_radioButton_.toggled.connect(self.groupBox_4.setDisabled)
        self.PORTA_PIN6_INPUT_radioButton_.toggled.connect(self.groupBox_16.setEnabled)
        self.PORTA_PIN6_INPUT_radioButton_.toggled.connect(self.groupBox_17.setDisabled)
        self.PORTC_PIN7_OUTPUT_radioButton_2.toggled.connect(self.groupBox_129.setEnabled)
        self.PORTA_PIN1_OUTPUT_radioButton_.toggled.connect(self.groupBox_20.setEnabled)
        self.PORTB_PIN1_OUTPUT_radioButton_1.toggled.connect(self.groupBox_107.setDisabled)
        self.PORTA_PIN7_OUTPUT_radioButton_.toggled.connect(self.groupBox_52.setEnabled)
        self.PORTA_PIN5_OUTPUT_radioButton_.toggled.connect(self.groupBox_48.setEnabled)
        self.PORTB_PIN6_OUTPUT_radioButton_1.toggled.connect(self.groupBox_111.setDisabled)
        self.PORTA_PIN5_INPUT_radioButton_.toggled.connect(self.groupBox_47.setEnabled)
        self.PORTB_PIN3_OUTPUT_radioButton_1.toggled.connect(self.groupBox_115.setDisabled)
        self.PORTA_PIN4_OUTPUT_radioButton_.toggled.connect(self.groupBox_12.setDisabled)
        self.PORTB_PIN0_INPUT_radioButton_1.toggled.connect(self.groupBox_96.setDisabled)
        self.PORTC_PIN1_OUTPUT_radioButton_2.toggled.connect(self.groupBox_219.setDisabled)
        self.PORTB_PIN4_INPUT_radioButton_1.toggled.connect(self.groupBox_91.setEnabled)
        self.PORTC_PIN0_OUTPUT_radioButton_2.toggled.connect(self.groupBox_207.setDisabled)
        self.PORTC_PIN5_OUTPUT_radioButton_2.toggled.connect(self.groupBox_216.setEnabled)
        self.PORTC_PIN7_INPUT_radioButton_2.toggled.connect(self.groupBox_125.setEnabled)
        self.PORTB_PIN3_INPUT_radioButton_1.toggled.connect(self.groupBox_116.setDisabled)
        self.PORTC_PIN3_OUTPUT_radioButton_2.toggled.connect(self.groupBox_227.setDisabled)
        self.PORTB_PIN5_INPUT_radioButton_1.toggled.connect(self.groupBox_103.setEnabled)
        self.PORTC_PIN3_OUTPUT_radioButton_2.toggled.connect(self.groupBox_228.setEnabled)
        self.PORTA_PIN5_OUTPUT_radioButton_.toggled.connect(self.groupBox_47.setDisabled)
        self.PORTC_PIN6_INPUT_radioButton_2.toggled.connect(self.groupBox_224.setDisabled)
        self.PORTA_PIN0_OUTPUT_radioButton_.toggled.connect(self.groupBox_5.setEnabled)
        self.PORTC_PIN5_OUTPUT_radioButton_2.toggled.connect(self.groupBox_215.setDisabled)
        self.PORTB_PIN1_OUTPUT_radioButton_1.toggled.connect(self.groupBox_108.setEnabled)
        self.PORTC_PIN1_INPUT_radioButton_2.toggled.connect(self.groupBox_219.setEnabled)
        self.PORTC_PIN6_OUTPUT_radioButton_2.toggled.connect(self.groupBox_224.setEnabled)
        self.PORTB_PIN4_OUTPUT_radioButton_1.toggled.connect(self.groupBox_91.setDisabled)
        self.PORTA_PIN1_INPUT_radioButton_.toggled.connect(self.groupBox_19.setEnabled)
        self.PORTB_PIN0_OUTPUT_radioButton_1.toggled.connect(self.groupBox_95.setDisabled)
        self.PORTB_PIN7_INPUT_radioButton_1.toggled.connect(self.groupBox_88.setDisabled)
        self.PORTC_PIN0_INPUT_radioButton_2.toggled.connect(self.groupBox_208.setDisabled)
        self.PORTA_PIN7_INPUT_radioButton_.toggled.connect(self.groupBox_51.setEnabled)
        self.PORTA_PIN3_INPUT_radioButton_.toggled.connect(self.groupBox_43.setEnabled)
        self.PORTB_PIN0_OUTPUT_radioButton_1.toggled.connect(self.groupBox_96.setEnabled)
        self.PORTA_PIN7_OUTPUT_radioButton_.toggled.connect(self.groupBox_51.setDisabled)
        self.PORTB_PIN6_INPUT_radioButton_1.toggled.connect(self.groupBox_111.setEnabled)
        self.PORTB_PIN5_INPUT_radioButton_1.toggled.connect(self.groupBox_104.setDisabled)
        self.PORTA_PIN6_OUTPUT_radioButton_.toggled.connect(self.groupBox_16.setDisabled)
        self.PORTB_PIN2_OUTPUT_radioButton_1.toggled.connect(self.groupBox_99.setDisabled)
        self.PORTB_PIN1_INPUT_radioButton_1.toggled.connect(self.groupBox_107.setEnabled)
        self.PORTA_PIN3_OUTPUT_radioButton_.toggled.connect(self.groupBox_44.setEnabled)
        self.PORTB_PIN2_OUTPUT_radioButton_1.toggled.connect(self.groupBox_100.setEnabled)
        self.PORTC_PIN4_OUTPUT_radioButton_2.toggled.connect(self.groupBox_141.setDisabled)
        self.PORTB_PIN7_INPUT_radioButton_1.toggled.connect(self.groupBox_87.setEnabled)
        self.PORTA_PIN2_INPUT_radioButton_.toggled.connect(self.groupBox_9.setDisabled)
        self.PORTC_PIN1_OUTPUT_radioButton_2.toggled.connect(self.groupBox_220.setEnabled)
        self.PORTA_PIN3_INPUT_radioButton_.toggled.connect(self.groupBox_44.setDisabled)
        self.PORTB_PIN7_OUTPUT_radioButton_1.toggled.connect(self.groupBox_87.setDisabled)
        self.PORTA_PIN5_INPUT_radioButton_.toggled.connect(self.groupBox_48.setDisabled)
        self.PORTC_PIN7_INPUT_radioButton_2.toggled.connect(self.groupBox_129.setDisabled)
        self.PORTC_PIN4_INPUT_radioButton_2.toggled.connect(self.groupBox_145.setDisabled)
        self.PORTA_PIN4_INPUT_radioButton_.toggled.connect(self.groupBox_13.setDisabled)
        self.PORTB_PIN1_INPUT_radioButton_1.toggled.connect(self.groupBox_108.setDisabled)
        self.PORTC_PIN6_INPUT_radioButton_2.toggled.connect(self.groupBox_223.setEnabled)
        self.PORTC_PIN5_INPUT_radioButton_2.toggled.connect(self.groupBox_215.setEnabled)
        self.PORTC_PIN2_INPUT_radioButton_2.toggled.connect(self.groupBox_211.setEnabled)
        self.PORTB_PIN6_INPUT_radioButton_1.toggled.connect(self.groupBox_112.setDisabled)
        self.PORTB_PIN4_OUTPUT_radioButton_1.toggled.connect(self.groupBox_92.setEnabled)
        self.PORTC_PIN0_INPUT_radioButton_2.toggled.connect(self.groupBox_207.setEnabled)
        self.PORTA_PIN2_OUTPUT_radioButton_.toggled.connect(self.groupBox_9.setEnabled)
        self.PORTC_PIN0_OUTPUT_radioButton_2.toggled.connect(self.groupBox_208.setEnabled)
        self.PORTA_PIN2_INPUT_radioButton_.toggled.connect(self.groupBox_8.setEnabled)
        self.PORTA_PIN4_INPUT_radioButton_.toggled.connect(self.groupBox_12.setEnabled)
        self.PORTC_PIN1_INPUT_radioButton_2.toggled.connect(self.groupBox_220.setDisabled)
        self.PORTB_PIN5_OUTPUT_radioButton_1.toggled.connect(self.groupBox_103.setDisabled)
        self.PORTA_PIN1_INPUT_radioButton_.toggled.connect(self.groupBox_20.setDisabled)
        self.PORTA_PIN4_OUTPUT_radioButton_.toggled.connect(self.groupBox_13.setEnabled)
        self.PORTA_PIN2_OUTPUT_radioButton_.toggled.connect(self.groupBox_8.setDisabled)
        self.PORTB_PIN7_OUTPUT_radioButton_1.toggled.connect(self.groupBox_88.setEnabled)
        self.PORTA_PIN1_OUTPUT_radioButton_.toggled.connect(self.groupBox_19.setDisabled)
        self.PORTB_PIN2_INPUT_radioButton_1.toggled.connect(self.groupBox_100.setDisabled)
        self.PORTC_PIN3_INPUT_radioButton_2.toggled.connect(self.groupBox_228.setDisabled)
        self.PORTB_PIN0_INPUT_radioButton_1.toggled.connect(self.groupBox_95.setEnabled)
        self.PORTA_PIN6_OUTPUT_radioButton_.toggled.connect(self.groupBox_17.setEnabled)
        self.PORTC_PIN7_OUTPUT_radioButton_2.toggled.connect(self.groupBox_125.setDisabled)
        self.PORTB_PIN4_INPUT_radioButton_1.toggled.connect(self.groupBox_92.setDisabled)
        self.PORTA_PIN3_OUTPUT_radioButton_.toggled.connect(self.groupBox_43.setDisabled)
        self.PORTB_PIN3_INPUT_radioButton_1.toggled.connect(self.groupBox_115.setEnabled)
        self.PORTC_PIN3_INPUT_radioButton_2.toggled.connect(self.groupBox_227.setEnabled)
        self.PORTC_PIN2_INPUT_radioButton_2.toggled.connect(self.groupBox_212.setDisabled)
        self.PORTD_PIN6_OUTPUT_radioButton_3.toggled.connect(self.groupBox_243.setDisabled)
        self.PORTD_PIN6_OUTPUT_radioButton_3.toggled.connect(self.groupBox_244.setEnabled)
        self.PORTD_PIN7_INPUT_radioButton_3.toggled.connect(self.groupBox_157.setEnabled)
        self.PORTD_PIN7_INPUT_radioButton_3.toggled.connect(self.groupBox_161.setDisabled)
        self.PORTD_PIN7_OUTPUT_radioButton_3.toggled.connect(self.groupBox_157.setDisabled)
        self.PORTD_PIN7_OUTPUT_radioButton_3.toggled.connect(self.groupBox_161.setEnabled)
        self.generate_PB.clicked.connect(self.file_generation)
        self.load_PB.clicked.connect(self.file_load)
        # self.save_PB.clicked.connect(self.file_save)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN0_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN0_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN0_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN0_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN0_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN0_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN2_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN2_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN2_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN2_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN2_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN2_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN4_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN4_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN4_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN4_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN4_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN4_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN6_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN6_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN6_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN6_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN6_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN6_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN1_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN1_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN1_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN1_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN1_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN1_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN3_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN3_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN3_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN3_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN3_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN3_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.groupBox_46.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN5_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN5_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_47.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN5_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN5_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_48.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN5_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTA_PIN5_OUT_LOW_radioButton_.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_49.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.groupBox_50.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTA_PIN7_INPUT_radioButton_.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTA_PIN7_OUTPUT_radioButton_.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_51.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTA_PIN7_IN_PULL_UP_radioButton_.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTA_PIN7_IN_PULL_DOWN_radioButton_.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_52.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTA_PIN7_OUT_HIGH_radioButton_.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.radioButton_78.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.portA_tab),
                                    QCoreApplication.translate("Form", u"PORTA", None))
        self.groupBox_113.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.groupBox_114.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN3_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN3_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_115.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN3_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN3_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_116.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN3_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN3_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_105.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.groupBox_106.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN1_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN1_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_107.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN1_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN1_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_108.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN1_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN1_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_97.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.groupBox_98.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN2_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN2_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_99.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN2_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN2_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_100.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN2_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN2_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_101.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.groupBox_102.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN5_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN5_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_103.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN5_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN5_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_104.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN5_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN5_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_89.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.groupBox_90.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN4_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN4_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_91.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN4_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN4_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_92.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN4_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN4_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_85.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.groupBox_86.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN7_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN7_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_87.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN7_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN7_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_88.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN7_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN7_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_109.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.groupBox_110.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN6_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN6_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_111.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN6_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN6_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_112.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN6_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN6_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_93.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.groupBox_94.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTB_PIN0_INPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTB_PIN0_OUTPUT_radioButton_1.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_95.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTB_PIN0_IN_PULL_UP_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTB_PIN0_IN_PULL_DOWN_radioButton_1.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_96.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTB_PIN0_OUT_HIGH_radioButton_1.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTB_PIN0_OUT_LOW_radioButton_1.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.portB_tab),
                                    QCoreApplication.translate("Form", u"PORTB", None))
        self.groupBox_225.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.groupBox_226.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN3_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN3_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_227.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN3_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN3_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_228.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN3_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN3_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_205.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.groupBox_206.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN0_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN0_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_207.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN0_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN0_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_208.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN0_OUT_HIGH_radioButton.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN0_OUT_LOW_radioButton.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_117.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.groupBox_121.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN7_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN7_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_125.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN7_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN7_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_129.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN7_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN7_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_213.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.groupBox_214.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN5_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN5_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_215.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN5_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN5_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_216.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN5_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN5_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_209.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.groupBox_210.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN2_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN2_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_211.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN2_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN2_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_212.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN2_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN2_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_133.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.groupBox_137.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN4_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN4_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_141.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN4_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN4_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_145.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN4_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN4_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_221.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.groupBox_222.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN6_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN6_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_223.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN6_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN6_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_224.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN6_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN6_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_217.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.groupBox_218.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTC_PIN1_INPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTC_PIN1_OUTPUT_radioButton_2.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_219.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTC_PIN1_IN_PULL_UP_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTC_PIN1_IN_PULL_DOWN_radioButton_2.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_220.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTC_PIN1_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTC_PIN1_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.portC_tab),
                                    QCoreApplication.translate("Form", u"PORTC", None))
        self.groupBox_229.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.groupBox_230.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN0_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN0_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_231.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN0_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN0_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_232.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN0_OUT_HIGH_radioButton_2.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN0_OUT_LOW_radioButton_2.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_149.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.groupBox_153.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN7_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN7_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_157.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN7_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN7_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_161.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN7_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN7_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_233.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.groupBox_234.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN5_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN5_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_235.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN5_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN5_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_236.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN5_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN5_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_237.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.groupBox_238.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN2_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN2_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_239.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN2_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN2_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_240.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN2_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN2_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_165.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.groupBox_169.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN4_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN4_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_173.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN4_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN4_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_177.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN4_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN4_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_241.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.groupBox_242.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN6_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN6_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_243.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN6_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN6_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_244.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN6_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN6_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_245.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.groupBox_246.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN1_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN1_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_247.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN1_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN1_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_248.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN1_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN1_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.groupBox_249.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.groupBox_250.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.PORTD_PIN3_INPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"INPUT", None))
        self.PORTD_PIN3_OUTPUT_radioButton_3.setText(QCoreApplication.translate("Form", u"OUTPUT", None))
        self.groupBox_251.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PORTD_PIN3_IN_PULL_UP_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL UP", None))
        self.PORTD_PIN3_IN_PULL_DOWN_radioButton_3.setText(QCoreApplication.translate("Form", u"PULL DOWN", None))
        self.groupBox_252.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.PORTD_PIN3_OUT_HIGH_radioButton_3.setText(QCoreApplication.translate("Form", u"HIGH", None))
        self.PORTD_PIN3_OUT_LOW_radioButton_3.setText(QCoreApplication.translate("Form", u"LOW", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.portD_tab),
                                    QCoreApplication.translate("Form", u"PORTD", None))
        self.label.setText(QCoreApplication.translate("Form", u"PATH", None))
        self.generate_PB.setText(QCoreApplication.translate("Form", u"GENERATE", None))
        # self.save_PB.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.load_PB.setText(QCoreApplication.translate("Form", u"LOAD", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.generate_tab),
                                    QCoreApplication.translate("Form", u"GENERATE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dio_tab),
                                  QCoreApplication.translate("Form", u"DIO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.timer_tab),
                                  QCoreApplication.translate("Form", u"TIMER", None))

    # retranslateUi
    def file_save(self):
        DIO = ET.Element("DIO_Cfg")
        PORTA = ET.Element("PORTA")
        PORTA_PIN0 = ET.Element("PIN0")
        PORTA_PIN1 = ET.Element("PIN1")
        PORTA_PIN2 = ET.Element("PIN2")
        PORTA_PIN3 = ET.Element("PIN3")
        PORTA_PIN4 = ET.Element("PIN4")
        PORTA_PIN5 = ET.Element("PIN5")
        PORTA_PIN6 = ET.Element("PIN6")
        PORTA_PIN7 = ET.Element("PIN7")

        PORTA_PIN0_DIR = ET.Element("DIR")
        PORTA_PIN0_CFG = ET.Element("CFG")

        PORTA_PIN1_DIR = ET.Element("DIR")
        PORTA_PIN1_CFG = ET.Element("CFG")

        PORTA_PIN2_DIR = ET.Element("DIR")
        PORTA_PIN2_CFG = ET.Element("CFG")

        PORTA_PIN3_DIR = ET.Element("DIR")
        PORTA_PIN3_CFG = ET.Element("CFG")

        PORTA_PIN4_DIR = ET.Element("DIR")
        PORTA_PIN4_CFG = ET.Element("CFG")

        PORTA_PIN5_DIR = ET.Element("DIR")
        PORTA_PIN5_CFG = ET.Element("CFG")

        PORTA_PIN6_DIR = ET.Element("DIR")
        PORTA_PIN6_CFG = ET.Element("CFG")

        PORTA_PIN7_DIR = ET.Element("DIR")
        PORTA_PIN7_CFG = ET.Element("CFG")

        # PortA
        if self.PORTA_PIN0_OUTPUT_radioButton_.isChecked():
            PORTA_PIN0_DIR.text = "OUTPUT"
            if self.PORTA_PIN0_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN0_CFG.text = "HIGH"
            else:
                PORTA_PIN0_CFG.text = "LOW"
        else:
            PORTA_PIN0_DIR.text = "INPUT"
            if self.PORTA_PIN0_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN0_CFG.text = "PULL_UP"
            else:
                PORTA_PIN0_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN1_OUTPUT_radioButton_.isChecked():
            PORTA_PIN1_DIR.text = "OUTPUT"
            if self.PORTA_PIN1_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN1_CFG.text = "HIGH"
            else:
                PORTA_PIN1_CFG.text = "LOW"
        else:
            PORTA_PIN1_DIR.text = "INPUT"
            if self.PORTA_PIN1_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN1_CFG.text = "PULL_UP"
            else:
                PORTA_PIN1_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN2_OUTPUT_radioButton_.isChecked():
            PORTA_PIN2_DIR.text = "OUTPUT"
            if self.PORTA_PIN2_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN2_CFG.text = "HIGH"
            else:
                PORTA_PIN2_CFG.text = "LOW"
        else:
            PORTA_PIN2_DIR.text = "INPUT"
            if self.PORTA_PIN2_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN2_CFG.text = "PULL_UP"
            else:
                PORTA_PIN2_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN3_OUTPUT_radioButton_.isChecked():
            PORTA_PIN3_DIR.text = "OUTPUT"
            if self.PORTA_PIN3_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN3_CFG.text = "HIGH"
            else:
                PORTA_PIN3_CFG.text = "LOW"
        else:
            PORTA_PIN3_DIR.text = "INPUT"
            if self.PORTA_PIN3_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN3_CFG.text = "PULL_UP"
            else:
                PORTA_PIN3_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN4_OUTPUT_radioButton_.isChecked():
            PORTA_PIN4_DIR.text = "OUTPUT"
            if self.PORTA_PIN4_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN4_CFG.text = "HIGH"
            else:
                PORTA_PIN4_CFG.text = "LOW"
        else:
            PORTA_PIN4_DIR.text = "INPUT"
            if self.PORTA_PIN4_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN4_CFG.text = "PULL_UP"
            else:
                PORTA_PIN4_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN5_OUTPUT_radioButton_.isChecked():
            PORTA_PIN5_DIR.text = "OUTPUT"
            if self.PORTA_PIN5_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN5_CFG.text = "HIGH"
            else:
                PORTA_PIN5_CFG.text = "LOW"
        else:
            PORTA_PIN5_DIR.text = "INPUT"
            if self.PORTA_PIN5_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN5_CFG.text = "PULL_UP"
            else:
                PORTA_PIN5_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN6_OUTPUT_radioButton_.isChecked():
            PORTA_PIN6_DIR.text = "OUTPUT"
            if self.PORTA_PIN6_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN6_CFG.text = "HIGH"
            else:
                PORTA_PIN6_CFG.text = "LOW"
        else:
            PORTA_PIN6_DIR.text = "INPUT"
            if self.PORTA_PIN6_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN6_CFG.text = "PULL_UP"
            else:
                PORTA_PIN6_CFG.text = "HIGH_IMP"

        if self.PORTA_PIN7_OUTPUT_radioButton_.isChecked():
            PORTA_PIN7_DIR.text = "OUTPUT"
            if self.PORTA_PIN7_OUT_HIGH_radioButton_.isChecked():
                PORTA_PIN7_CFG.text = "HIGH"
            else:
                PORTA_PIN7_CFG.text = "LOW"
        else:
            PORTA_PIN7_DIR.text = "INPUT"
            if self.PORTA_PIN7_IN_PULL_UP_radioButton_.isChecked():
                PORTA_PIN7_CFG.text = "PULL_UP"
            else:
                PORTA_PIN7_CFG.text = "HIGH_IMP"

        DIO.append(PORTA)
        PORTA.append(PORTA_PIN0)
        PORTA_PIN0.append(PORTA_PIN0_DIR)
        PORTA_PIN0.append(PORTA_PIN0_CFG)
        PORTA.append(PORTA_PIN1)
        PORTA_PIN1.append(PORTA_PIN1_DIR)
        PORTA_PIN1.append(PORTA_PIN1_CFG)
        PORTA.append(PORTA_PIN2)
        PORTA_PIN2.append(PORTA_PIN2_DIR)
        PORTA_PIN2.append(PORTA_PIN2_CFG)
        PORTA.append(PORTA_PIN3)
        PORTA_PIN3.append(PORTA_PIN3_DIR)
        PORTA_PIN3.append(PORTA_PIN3_CFG)
        PORTA.append(PORTA_PIN4)
        PORTA_PIN4.append(PORTA_PIN4_DIR)
        PORTA_PIN4.append(PORTA_PIN4_CFG)
        PORTA.append(PORTA_PIN5)
        PORTA_PIN5.append(PORTA_PIN5_DIR)
        PORTA_PIN5.append(PORTA_PIN5_CFG)
        PORTA.append(PORTA_PIN6)
        PORTA_PIN6.append(PORTA_PIN6_DIR)
        PORTA_PIN6.append(PORTA_PIN6_CFG)
        PORTA.append(PORTA_PIN7)
        PORTA_PIN7.append(PORTA_PIN7_DIR)
        PORTA_PIN7.append(PORTA_PIN7_CFG)

        ################################################################################################################
        ################################################################################################################

        PORTB = ET.Element("PORTB")
        PORTB_PIN0 = ET.Element("PIN0")
        PORTB_PIN1 = ET.Element("PIN1")
        PORTB_PIN2 = ET.Element("PIN2")
        PORTB_PIN3 = ET.Element("PIN3")
        PORTB_PIN4 = ET.Element("PIN4")
        PORTB_PIN5 = ET.Element("PIN5")
        PORTB_PIN6 = ET.Element("PIN6")
        PORTB_PIN7 = ET.Element("PIN7")

        PORTB_PIN0_DIR = ET.Element("DIR")
        PORTB_PIN0_CFG = ET.Element("CFG")

        PORTB_PIN1_DIR = ET.Element("DIR")
        PORTB_PIN1_CFG = ET.Element("CFG")

        PORTB_PIN2_DIR = ET.Element("DIR")
        PORTB_PIN2_CFG = ET.Element("CFG")

        PORTB_PIN3_DIR = ET.Element("DIR")
        PORTB_PIN3_CFG = ET.Element("CFG")

        PORTB_PIN4_DIR = ET.Element("DIR")
        PORTB_PIN4_CFG = ET.Element("CFG")

        PORTB_PIN5_DIR = ET.Element("DIR")
        PORTB_PIN5_CFG = ET.Element("CFG")

        PORTB_PIN6_DIR = ET.Element("DIR")
        PORTB_PIN6_CFG = ET.Element("CFG")

        PORTB_PIN7_DIR = ET.Element("DIR")
        PORTB_PIN7_CFG = ET.Element("CFG")

        # PORTB
        if self.PORTB_PIN0_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN0_DIR.text = "OUTPUT"
            if self.PORTB_PIN0_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN0_CFG.text = "HIGH"
            else:
                PORTB_PIN0_CFG.text = "LOW"
        else:
            PORTB_PIN0_DIR.text = "INPUT"
            if self.PORTB_PIN0_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN0_CFG.text = "PULL_UP"
            else:
                PORTB_PIN0_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN1_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN1_DIR.text = "OUTPUT"
            if self.PORTB_PIN1_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN1_CFG.text = "HIGH"
            else:
                PORTB_PIN1_CFG.text = "LOW"
        else:
            PORTB_PIN1_DIR.text = "INPUT"
            if self.PORTB_PIN1_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN1_CFG.text = "PULL_UP"
            else:
                PORTB_PIN1_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN2_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN2_DIR.text = "OUTPUT"
            if self.PORTB_PIN2_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN2_CFG.text = "HIGH"
            else:
                PORTB_PIN2_CFG.text = "LOW"
        else:
            PORTB_PIN2_DIR.text = "INPUT"
            if self.PORTB_PIN2_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN2_CFG.text = "PULL_UP"
            else:
                PORTB_PIN2_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN3_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN3_DIR.text = "OUTPUT"
            if self.PORTB_PIN3_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN3_CFG.text = "HIGH"
            else:
                PORTB_PIN3_CFG.text = "LOW"
        else:
            PORTB_PIN3_DIR.text = "INPUT"
            if self.PORTB_PIN3_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN3_CFG.text = "PULL_UP"
            else:
                PORTB_PIN3_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN4_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN4_DIR.text = "OUTPUT"
            if self.PORTB_PIN4_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN4_CFG.text = "HIGH"
            else:
                PORTB_PIN4_CFG.text = "LOW"
        else:
            PORTB_PIN4_DIR.text = "INPUT"
            if self.PORTB_PIN4_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN4_CFG.text = "PULL_UP"
            else:
                PORTB_PIN4_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN5_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN5_DIR.text = "OUTPUT"
            if self.PORTB_PIN5_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN5_CFG.text = "HIGH"
            else:
                PORTB_PIN5_CFG.text = "LOW"
        else:
            PORTB_PIN5_DIR.text = "INPUT"
            if self.PORTB_PIN5_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN5_CFG.text = "PULL_UP"
            else:
                PORTB_PIN5_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN6_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN6_DIR.text = "OUTPUT"
            if self.PORTB_PIN6_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN6_CFG.text = "HIGH"
            else:
                PORTB_PIN6_CFG.text = "LOW"
        else:
            PORTB_PIN6_DIR.text = "INPUT"
            if self.PORTB_PIN6_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN6_CFG.text = "PULL_UP"
            else:
                PORTB_PIN6_CFG.text = "HIGH_IMP"

        if self.PORTB_PIN7_OUTPUT_radioButton_1.isChecked():
            PORTB_PIN7_DIR.text = "OUTPUT"
            if self.PORTB_PIN7_OUT_HIGH_radioButton_1.isChecked():
                PORTB_PIN7_CFG.text = "HIGH"
            else:
                PORTB_PIN7_CFG.text = "LOW"
        else:
            PORTB_PIN7_DIR.text = "INPUT"
            if self.PORTB_PIN7_IN_PULL_UP_radioButton_1.isChecked():
                PORTB_PIN7_CFG.text = "PULL_UP"
            else:
                PORTB_PIN7_CFG.text = "HIGH_IMP"

        DIO.append(PORTB)
        PORTB.append(PORTB_PIN0)
        PORTB_PIN0.append(PORTB_PIN0_DIR)
        PORTB_PIN0.append(PORTB_PIN0_CFG)
        PORTB.append(PORTB_PIN1)
        PORTB_PIN1.append(PORTB_PIN1_DIR)
        PORTB_PIN1.append(PORTB_PIN1_CFG)
        PORTB.append(PORTB_PIN2)
        PORTB_PIN2.append(PORTB_PIN2_DIR)
        PORTB_PIN2.append(PORTB_PIN2_CFG)
        PORTB.append(PORTB_PIN3)
        PORTB_PIN3.append(PORTB_PIN3_DIR)
        PORTB_PIN3.append(PORTB_PIN3_CFG)
        PORTB.append(PORTB_PIN4)
        PORTB_PIN4.append(PORTB_PIN4_DIR)
        PORTB_PIN4.append(PORTB_PIN4_CFG)
        PORTB.append(PORTB_PIN5)
        PORTB_PIN5.append(PORTB_PIN5_DIR)
        PORTB_PIN5.append(PORTB_PIN5_CFG)
        PORTB.append(PORTB_PIN6)
        PORTB_PIN6.append(PORTB_PIN6_DIR)
        PORTB_PIN6.append(PORTB_PIN6_CFG)
        PORTB.append(PORTB_PIN7)
        PORTB_PIN7.append(PORTB_PIN7_DIR)
        PORTB_PIN7.append(PORTB_PIN7_CFG)

        ################################################################################################################
        ################################################################################################################

        PORTC = ET.Element("PORTC")
        PORTC_PIN0 = ET.Element("PIN0")
        PORTC_PIN1 = ET.Element("PIN1")
        PORTC_PIN2 = ET.Element("PIN2")
        PORTC_PIN3 = ET.Element("PIN3")
        PORTC_PIN4 = ET.Element("PIN4")
        PORTC_PIN5 = ET.Element("PIN5")
        PORTC_PIN6 = ET.Element("PIN6")
        PORTC_PIN7 = ET.Element("PIN7")

        PORTC_PIN0_DIR = ET.Element("DIR")
        PORTC_PIN0_CFG = ET.Element("CFG")

        PORTC_PIN1_DIR = ET.Element("DIR")
        PORTC_PIN1_CFG = ET.Element("CFG")

        PORTC_PIN2_DIR = ET.Element("DIR")
        PORTC_PIN2_CFG = ET.Element("CFG")

        PORTC_PIN3_DIR = ET.Element("DIR")
        PORTC_PIN3_CFG = ET.Element("CFG")

        PORTC_PIN4_DIR = ET.Element("DIR")
        PORTC_PIN4_CFG = ET.Element("CFG")

        PORTC_PIN5_DIR = ET.Element("DIR")
        PORTC_PIN5_CFG = ET.Element("CFG")

        PORTC_PIN6_DIR = ET.Element("DIR")
        PORTC_PIN6_CFG = ET.Element("CFG")

        PORTC_PIN7_DIR = ET.Element("DIR")
        PORTC_PIN7_CFG = ET.Element("CFG")

        # PORTC
        if self.PORTC_PIN0_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN0_DIR.text = "OUTPUT"
            if self.PORTC_PIN0_OUT_HIGH_radioButton.isChecked():
                PORTC_PIN0_CFG.text = "HIGH"
            else:
                PORTC_PIN0_CFG.text = "LOW"
        else:
            PORTC_PIN0_DIR.text = "INPUT"
            if self.PORTC_PIN0_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN0_CFG.text = "PULL_UP"
            else:
                PORTC_PIN0_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN1_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN1_DIR.text = "OUTPUT"
            if self.PORTC_PIN1_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN1_CFG.text = "HIGH"
            else:
                PORTC_PIN1_CFG.text = "LOW"
        else:
            PORTC_PIN1_DIR.text = "INPUT"
            if self.PORTC_PIN1_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN1_CFG.text = "PULL_UP"
            else:
                PORTC_PIN1_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN2_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN2_DIR.text = "OUTPUT"
            if self.PORTC_PIN2_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN2_CFG.text = "HIGH"
            else:
                PORTC_PIN2_CFG.text = "LOW"
        else:
            PORTC_PIN2_DIR.text = "INPUT"
            if self.PORTC_PIN2_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN2_CFG.text = "PULL_UP"
            else:
                PORTC_PIN2_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN3_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN3_DIR.text = "OUTPUT"
            if self.PORTC_PIN3_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN3_CFG.text = "HIGH"
            else:
                PORTC_PIN3_CFG.text = "LOW"
        else:
            PORTC_PIN3_DIR.text = "INPUT"
            if self.PORTC_PIN3_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN3_CFG.text = "PULL_UP"
            else:
                PORTC_PIN3_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN4_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN4_DIR.text = "OUTPUT"
            if self.PORTC_PIN4_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN4_CFG.text = "HIGH"
            else:
                PORTC_PIN4_CFG.text = "LOW"
        else:
            PORTC_PIN4_DIR.text = "INPUT"
            if self.PORTC_PIN4_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN4_CFG.text = "PULL_UP"
            else:
                PORTC_PIN4_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN5_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN5_DIR.text = "OUTPUT"
            if self.PORTC_PIN5_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN5_CFG.text = "HIGH"
            else:
                PORTC_PIN5_CFG.text = "LOW"
        else:
            PORTC_PIN5_DIR.text = "INPUT"
            if self.PORTC_PIN5_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN5_CFG.text = "PULL_UP"
            else:
                PORTC_PIN5_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN6_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN6_DIR.text = "OUTPUT"
            if self.PORTC_PIN6_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN6_CFG.text = "HIGH"
            else:
                PORTC_PIN6_CFG.text = "LOW"
        else:
            PORTC_PIN6_DIR.text = "INPUT"
            if self.PORTC_PIN6_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN6_CFG.text = "PULL_UP"
            else:
                PORTC_PIN6_CFG.text = "HIGH_IMP"

        if self.PORTC_PIN7_OUTPUT_radioButton_2.isChecked():
            PORTC_PIN7_DIR.text = "OUTPUT"
            if self.PORTC_PIN7_OUT_HIGH_radioButton_2.isChecked():
                PORTC_PIN7_CFG.text = "HIGH"
            else:
                PORTC_PIN7_CFG.text = "LOW"
        else:
            PORTC_PIN7_DIR.text = "INPUT"
            if self.PORTC_PIN7_IN_PULL_UP_radioButton_2.isChecked():
                PORTC_PIN7_CFG.text = "PULL_UP"
            else:
                PORTC_PIN7_CFG.text = "HIGH_IMP"

        DIO.append(PORTC)
        PORTC.append(PORTC_PIN0)
        PORTC_PIN0.append(PORTC_PIN0_DIR)
        PORTC_PIN0.append(PORTC_PIN0_CFG)
        PORTC.append(PORTC_PIN1)
        PORTC_PIN1.append(PORTC_PIN1_DIR)
        PORTC_PIN1.append(PORTC_PIN1_CFG)
        PORTC.append(PORTC_PIN2)
        PORTC_PIN2.append(PORTC_PIN2_DIR)
        PORTC_PIN2.append(PORTC_PIN2_CFG)
        PORTC.append(PORTC_PIN3)
        PORTC_PIN3.append(PORTC_PIN3_DIR)
        PORTC_PIN3.append(PORTC_PIN3_CFG)
        PORTC.append(PORTC_PIN4)
        PORTC_PIN4.append(PORTC_PIN4_DIR)
        PORTC_PIN4.append(PORTC_PIN4_CFG)
        PORTC.append(PORTC_PIN5)
        PORTC_PIN5.append(PORTC_PIN5_DIR)
        PORTC_PIN5.append(PORTC_PIN5_CFG)
        PORTC.append(PORTC_PIN6)
        PORTC_PIN6.append(PORTC_PIN6_DIR)
        PORTC_PIN6.append(PORTC_PIN6_CFG)
        PORTC.append(PORTC_PIN7)
        PORTC_PIN7.append(PORTC_PIN7_DIR)
        PORTC_PIN7.append(PORTC_PIN7_CFG)

        ################################################################################################################
        ################################################################################################################

        PORTD = ET.Element("PORTD")
        PORTD_PIN0 = ET.Element("PIN0")
        PORTD_PIN1 = ET.Element("PIN1")
        PORTD_PIN2 = ET.Element("PIN2")
        PORTD_PIN3 = ET.Element("PIN3")
        PORTD_PIN4 = ET.Element("PIN4")
        PORTD_PIN5 = ET.Element("PIN5")
        PORTD_PIN6 = ET.Element("PIN6")
        PORTD_PIN7 = ET.Element("PIN7")

        PORTD_PIN0_DIR = ET.Element("DIR")
        PORTD_PIN0_CFG = ET.Element("CFG")

        PORTD_PIN1_DIR = ET.Element("DIR")
        PORTD_PIN1_CFG = ET.Element("CFG")

        PORTD_PIN2_DIR = ET.Element("DIR")
        PORTD_PIN2_CFG = ET.Element("CFG")

        PORTD_PIN3_DIR = ET.Element("DIR")
        PORTD_PIN3_CFG = ET.Element("CFG")

        PORTD_PIN4_DIR = ET.Element("DIR")
        PORTD_PIN4_CFG = ET.Element("CFG")

        PORTD_PIN5_DIR = ET.Element("DIR")
        PORTD_PIN5_CFG = ET.Element("CFG")

        PORTD_PIN6_DIR = ET.Element("DIR")
        PORTD_PIN6_CFG = ET.Element("CFG")

        PORTD_PIN7_DIR = ET.Element("DIR")
        PORTD_PIN7_CFG = ET.Element("CFG")

        # PORTD
        if self.PORTD_PIN0_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN0_DIR.text = "OUTPUT"
            if self.PORTD_PIN0_OUT_HIGH_radioButton_2.isChecked():
                PORTD_PIN0_CFG.text = "HIGH"
            else:
                PORTD_PIN0_CFG.text = "LOW"
        else:
            PORTD_PIN0_DIR.text = "INPUT"
            if self.PORTD_PIN0_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN0_CFG.text = "PULL_UP"
            else:
                PORTD_PIN0_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN1_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN1_DIR.text = "OUTPUT"
            if self.PORTD_PIN1_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN1_CFG.text = "HIGH"
            else:
                PORTD_PIN1_CFG.text = "LOW"
        else:
            PORTD_PIN1_DIR.text = "INPUT"
            if self.PORTD_PIN1_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN1_CFG.text = "PULL_UP"
            else:
                PORTD_PIN1_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN2_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN2_DIR.text = "OUTPUT"
            if self.PORTD_PIN2_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN2_CFG.text = "HIGH"
            else:
                PORTD_PIN2_CFG.text = "LOW"
        else:
            PORTD_PIN2_DIR.text = "INPUT"
            if self.PORTD_PIN2_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN2_CFG.text = "PULL_UP"
            else:
                PORTD_PIN2_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN3_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN3_DIR.text = "OUTPUT"
            if self.PORTD_PIN3_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN3_CFG.text = "HIGH"
            else:
                PORTD_PIN3_CFG.text = "LOW"
        else:
            PORTD_PIN3_DIR.text = "INPUT"
            if self.PORTD_PIN3_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN3_CFG.text = "PULL_UP"
            else:
                PORTD_PIN3_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN4_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN4_DIR.text = "OUTPUT"
            if self.PORTD_PIN4_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN4_CFG.text = "HIGH"
            else:
                PORTD_PIN4_CFG.text = "LOW"
        else:
            PORTD_PIN4_DIR.text = "INPUT"
            if self.PORTD_PIN4_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN4_CFG.text = "PULL_UP"
            else:
                PORTD_PIN4_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN5_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN5_DIR.text = "OUTPUT"
            if self.PORTD_PIN5_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN5_CFG.text = "HIGH"
            else:
                PORTD_PIN5_CFG.text = "LOW"
        else:
            PORTD_PIN5_DIR.text = "INPUT"
            if self.PORTD_PIN5_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN5_CFG.text = "PULL_UP"
            else:
                PORTD_PIN5_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN6_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN6_DIR.text = "OUTPUT"
            if self.PORTD_PIN6_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN6_CFG.text = "HIGH"
            else:
                PORTD_PIN6_CFG.text = "LOW"
        else:
            PORTD_PIN6_DIR.text = "INPUT"
            if self.PORTD_PIN6_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN6_CFG.text = "PULL_UP"
            else:
                PORTD_PIN6_CFG.text = "HIGH_IMP"

        if self.PORTD_PIN7_OUTPUT_radioButton_3.isChecked():
            PORTD_PIN7_DIR.text = "OUTPUT"
            if self.PORTD_PIN7_OUT_HIGH_radioButton_3.isChecked():
                PORTD_PIN7_CFG.text = "HIGH"
            else:
                PORTD_PIN7_CFG.text = "LOW"
        else:
            PORTD_PIN7_DIR.text = "INPUT"
            if self.PORTD_PIN7_IN_PULL_UP_radioButton_3.isChecked():
                PORTD_PIN7_CFG.text = "PULL_UP"
            else:
                PORTD_PIN7_CFG.text = "HIGH_IMP"

        DIO.append(PORTD)
        PORTD.append(PORTD_PIN0)
        PORTD_PIN0.append(PORTD_PIN0_DIR)
        PORTD_PIN0.append(PORTD_PIN0_CFG)
        PORTD.append(PORTD_PIN1)
        PORTD_PIN1.append(PORTD_PIN1_DIR)
        PORTD_PIN1.append(PORTD_PIN1_CFG)
        PORTD.append(PORTD_PIN2)
        PORTD_PIN2.append(PORTD_PIN2_DIR)
        PORTD_PIN2.append(PORTD_PIN2_CFG)
        PORTD.append(PORTD_PIN3)
        PORTD_PIN3.append(PORTD_PIN3_DIR)
        PORTD_PIN3.append(PORTD_PIN3_CFG)
        PORTD.append(PORTD_PIN4)
        PORTD_PIN4.append(PORTD_PIN4_DIR)
        PORTD_PIN4.append(PORTD_PIN4_CFG)
        PORTD.append(PORTD_PIN5)
        PORTD_PIN5.append(PORTD_PIN5_DIR)
        PORTD_PIN5.append(PORTD_PIN5_CFG)
        PORTD.append(PORTD_PIN6)
        PORTD_PIN6.append(PORTD_PIN6_DIR)
        PORTD_PIN6.append(PORTD_PIN6_CFG)
        PORTD.append(PORTD_PIN7)
        PORTD_PIN7.append(PORTD_PIN7_DIR)
        PORTD_PIN7.append(PORTD_PIN7_CFG)
        output_path = self.path_text.toPlainText() + r'/DIO_Cfg.xml'
        File_Handler2 = open(output_path, 'w')
        File_Handler2.write(ET.tostring(DIO, pretty_print=True).decode())
        File_Handler2.close()

    def file_generation(self):
        output_path = self.path_text.toPlainText() + r'/DIO_Cfg.h'
        if not bool(self.path_text.toPlainText()):
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Critical)
            msg1.setText("Error!!! Empty Path")
            msg1.setInformativeText("Please Enter Valid Path")
            msg1.setWindowTitle("AVR CONFIGURATOR")
            msg1.setMinimumHeight(600)
            msg1.setSizeIncrement(1, 1)
            msg1.setSizeGripEnabled(True)
            msg1.exec_()
        elif not bool(os.path.exists(self.path_text.toPlainText())):
            msg4 = QMessageBox()
            msg4.setIcon(QMessageBox.Critical)
            msg4.setText("Error!!!PATH Not Found")
            msg4.setInformativeText("Please Enter Valid Path")
            msg4.setWindowTitle("AVR CONFIGURATOR")
            msg4.resize(250, 150)
            msg4.setSizeIncrement(1, 1)
            msg4.setSizeGripEnabled(True)
            msg4.exec_()
        else:
            file_handler = open(output_path, 'w')
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("/*                           AVR CONFIGURATOR                              */\n")
            file_handler.write("/*          Author: MOAZ OMAR                                              */\n")
            file_handler.write("/*          EMBEDDED SOFTWARE ENGINEER @ ITI-INTAKE 43                     */\n")
            file_handler.write("/*          %s  %s                                     */\n" % ("DATE:", dt_string))
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("\n")
            file_handler.write("\n")
            file_handler.write("\n")
            file_handler.write("\n")
            file_handler.write("#ifndef_DIO_CFG_H\n")
            file_handler.write("#define_DIO_CFG_H\n")
            file_handler.write("\n")
            file_handler.write("\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("/* PORTA                                                                   */\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("\n")
            file_handler.write("\n")

            if self.PORTA_PIN0_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN0_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN0_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN0_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN0_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN0_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTA_PIN1_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN1_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN1_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN1_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN1_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN1_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTA_PIN2_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN2_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN2_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN2_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN2_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN2_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTA_PIN3_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN3_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN3_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN3_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN3_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN3_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################

            if self.PORTA_PIN4_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN4_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN4_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN4_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN4_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN4_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTA_PIN5_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN5_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN5_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN5_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN5_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN5_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTA_PIN6_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN6_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN6_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN6_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN6_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN6_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTA_PIN7_OUTPUT_radioButton_.isChecked():
                if self.PORTA_PIN7_OUT_HIGH_radioButton_.isChecked():
                    file_handler.write("#define DIO_PORTA_PIN7_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTA_PIN7_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTA_PIN7_IN_PULL_UP_radioButton_.isChecked():
                    file_handler.write('#define DIO_PORTA_PIN7_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTA_PIN7_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')

            file_handler.write("\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("/* PORTB                                                                   */\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("\n")
            if self.PORTB_PIN0_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN0_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN0_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN0_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN0_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN0_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTB_PIN1_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN1_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN1_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN1_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN1_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN1_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTB_PIN2_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN2_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN2_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN2_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN2_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN2_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTB_PIN3_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN3_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN3_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN3_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN3_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN3_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################

            if self.PORTB_PIN4_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN4_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN4_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN4_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN4_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN4_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTB_PIN5_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN5_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN5_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN5_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN5_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN5_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTB_PIN6_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN6_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN6_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN6_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN6_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN6_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTB_PIN7_OUTPUT_radioButton_1.isChecked():
                if self.PORTB_PIN7_OUT_HIGH_radioButton_1.isChecked():
                    file_handler.write("#define DIO_PORTB_PIN7_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTB_PIN7_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTB_PIN7_IN_PULL_UP_radioButton_1.isChecked():
                    file_handler.write('#define DIO_PORTB_PIN7_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTB_PIN7_MODE    DIO_INPUT_HIGH_IMPEDANCE\n')
            file_handler.write("\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("/* PORTC                                                                   */\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("\n")
            if self.PORTC_PIN0_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN0_OUT_HIGH_radioButton.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN0_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN0_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN0_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN0_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTC_PIN1_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN1_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN1_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN1_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN1_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN1_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTC_PIN2_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN2_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN2_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN2_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN2_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN2_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTC_PIN3_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN3_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN3_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN3_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN3_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN3_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################

            if self.PORTC_PIN4_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN4_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN4_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN4_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN4_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN4_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTC_PIN5_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN5_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN5_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN5_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN5_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN5_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTC_PIN6_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN6_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN6_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN6_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN6_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN6_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTC_PIN7_OUTPUT_radioButton_2.isChecked():
                if self.PORTC_PIN7_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTC_PIN7_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTC_PIN7_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTC_PIN7_IN_PULL_UP_radioButton_2.isChecked():
                    file_handler.write('#define DIO_PORTC_PIN7_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTC_PIN7_MODE    DIO_INPUT_HIGH_IMPEDANCE\n')
            file_handler.write("\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("/* PORTD                                                                   */\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("\n")

            if self.PORTD_PIN0_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN0_OUT_HIGH_radioButton_2.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN0_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN0_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN0_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN0_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTD_PIN1_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN1_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN1_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN1_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN1_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN1_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTD_PIN2_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN2_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN2_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN2_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN2_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN2_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTD_PIN3_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN3_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN3_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN3_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN3_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN3_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################

            if self.PORTD_PIN4_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN4_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN4_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN4_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN4_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN4_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTD_PIN5_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN5_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN5_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN5_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN5_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN5_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTD_PIN6_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN6_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN6_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN6_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN6_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN6_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
            ################################################################################################################
            if self.PORTD_PIN7_OUTPUT_radioButton_3.isChecked():
                if self.PORTD_PIN7_OUT_HIGH_radioButton_3.isChecked():
                    file_handler.write("#define DIO_PORTD_PIN7_MODE     DIO_OUTPUT_HIGH\n")
                else:
                    file_handler.write("#define DIO_PORTD_PIN7_MODE     DIO_OUTPUT_LOW\n")
            else:
                if self.PORTD_PIN7_IN_PULL_UP_radioButton_3.isChecked():
                    file_handler.write('#define DIO_PORTD_PIN7_MODE     DIO_INPUT_PULL_UP\n')
                else:
                    file_handler.write('#define DIO_PORTD_PIN7_MODE    DIO_INPUT_HIGH_IMPEDANCE\n')
            file_handler.write("\n")
            file_handler.write("\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("/*             END OF CONFIGURATION XD                                     */\n")
            file_handler.write("/***************************************************************************/\n")
            file_handler.write("\n")
            file_handler.write("\n")
            file_handler.write("#endef _DIO_CFG_H\n")
            file_handler.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Configuration Generated Successfully")
            msg.setWindowTitle("AVR CONFIGURATOR")
            msg.exec_()
            self.file_save()

    def file_load(self):
        output_path = self.path_text.toPlainText() + r'/DIO_Cfg.xml'
        if not bool(self.path_text.toPlainText()):
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Critical)
            msg1.setText("Error!!! Empty Path")
            msg1.setInformativeText("Please Enter Valid Path")
            msg1.setWindowTitle("AVR CONFIGURATOR")
            msg1.resize(250, 150)
            msg1.setSizeIncrement(1, 1)
            msg1.setSizeGripEnabled(True)
            msg1.exec_()
        elif not bool(os.path.exists(output_path)):
            msg4 = QMessageBox()
            msg4.setIcon(QMessageBox.Critical)
            msg4.setText("Error!!!PATH Not Found")
            msg4.setInformativeText("Please Enter Valid Path")
            msg4.setWindowTitle("AVR CONFIGURATOR")
            msg4.resize(250, 150)
            msg4.setSizeIncrement(1, 1)
            msg4.setSizeGripEnabled(True)
            msg4.exec_()
        elif not bool(os.path.isfile(output_path)):
            msg3 = QMessageBox()
            msg3.setIcon(QMessageBox.Critical)
            msg3.setText("Error!!!File Not Found")
            msg3.setInformativeText("Please Enter Valid Path")
            msg3.setWindowTitle("AVR CONFIGURATOR")
            msg3.resize(250, 150)
            msg3.setSizeIncrement(1, 1)
            msg3.setSizeGripEnabled(True)
            msg3.exec_()

        else:
            tree = ET.parse(output_path)
            DIO = tree.getroot()
            port = DIO.find('PORTA')
            pin = port.find('PIN0')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN0_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_5.setEnabled(True)
                self.groupBox_4.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN0_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN0_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN0_INPUT_radioButton_.setChecked(True)
                self.groupBox_5.setDisabled(True)
                self.groupBox_4.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN0_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN0_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN1')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN1_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_20.setEnabled(True)
                self.groupBox_19.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN1_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN1_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN1_INPUT_radioButton_.setChecked(True)
                self.groupBox_20.setDisabled(True)
                self.groupBox_19.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN1_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN1_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN2')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN2_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_9.setEnabled(True)
                self.groupBox_8.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN2_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN2_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN2_INPUT_radioButton_.setChecked(True)
                self.groupBox_9.setDisabled(True)
                self.groupBox_8.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN2_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN2_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN3')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN3_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_44.setEnabled(True)
                self.groupBox_43.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN3_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN3_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN3_INPUT_radioButton_.setChecked(True)
                self.groupBox_44.setDisabled(True)
                self.groupBox_43.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN3_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN3_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN4')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN4_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_13.setEnabled(True)
                self.groupBox_12.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN4_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN4_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN4_INPUT_radioButton_.setChecked(True)
                self.groupBox_13.setDisabled(True)
                self.groupBox_12.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN4_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN4_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN5')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN5_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_48.setEnabled(True)
                self.groupBox_47.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN5_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN5_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN5_INPUT_radioButton_.setChecked(True)
                self.groupBox_48.setDisabled(True)
                self.groupBox_47.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN5_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN5_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN6')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN6_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_17.setEnabled(True)
                self.groupBox_16.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN6_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN6_OUT_LOW_radioButton_.setChecked(True)
            else:
                self.PORTA_PIN6_INPUT_radioButton_.setChecked(True)
                self.groupBox_17.setDisabled(True)
                self.groupBox_16.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN6_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN6_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTA')
            pin = port.find('PIN7')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTA_PIN7_OUTPUT_radioButton_.setChecked(True)
                self.groupBox_52.setEnabled(True)
                self.groupBox_51.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTA_PIN7_OUT_HIGH_radioButton_.setChecked(True)
                else:
                    self.radioButton_78.setChecked(True)
            else:
                self.PORTA_PIN7_INPUT_radioButton_.setChecked(True)
                self.groupBox_52.setDisabled(True)
                self.groupBox_51.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTA_PIN7_IN_PULL_UP_radioButton_.setChecked(True)
                else:
                    self.PORTA_PIN7_IN_PULL_DOWN_radioButton_.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN0')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN0_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_96.setEnabled(True)
                self.groupBox_95.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN0_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN0_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN0_INPUT_radioButton_1.setChecked(True)
                self.groupBox_96.setDisabled(True)
                self.groupBox_95.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN0_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN0_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN1')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN1_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_108.setEnabled(True)
                self.groupBox_107.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN1_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN1_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN1_INPUT_radioButton_1.setChecked(True)
                self.groupBox_108.setDisabled(True)
                self.groupBox_107.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN1_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN1_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN2')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN2_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_100.setEnabled(True)
                self.groupBox_99.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN2_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN2_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN2_INPUT_radioButton_1.setChecked(True)
                self.groupBox_100.setDisabled(True)
                self.groupBox_99.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN2_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN2_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN3')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN3_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_116.setEnabled(True)
                self.groupBox_115.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN3_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN3_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN3_INPUT_radioButton_1.setChecked(True)
                self.groupBox_116.setDisabled(True)
                self.groupBox_115.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN3_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN3_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN4')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN4_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_92.setEnabled(True)
                self.groupBox_91.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN4_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN4_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN4_INPUT_radioButton_1.setChecked(True)
                self.groupBox_92.setDisabled(True)
                self.groupBox_91.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN4_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN4_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN5')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN5_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_104.setEnabled(True)
                self.groupBox_103.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN5_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN5_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN5_INPUT_radioButton_1.setChecked(True)
                self.groupBox_104.setDisabled(True)
                self.groupBox_103.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN5_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN5_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN6')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN6_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_112.setEnabled(True)
                self.groupBox_111.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN6_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN6_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN6_INPUT_radioButton_1.setChecked(True)
                self.groupBox_112.setDisabled(True)
                self.groupBox_111.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN6_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN6_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTB')
            pin = port.find('PIN7')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTB_PIN7_OUTPUT_radioButton_1.setChecked(True)
                self.groupBox_88.setEnabled(True)
                self.groupBox_87.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTB_PIN7_OUT_HIGH_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN7_OUT_LOW_radioButton_1.setChecked(True)
            else:
                self.PORTB_PIN7_INPUT_radioButton_1.setChecked(True)
                self.groupBox_88.setDisabled(True)
                self.groupBox_87.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTB_PIN7_IN_PULL_UP_radioButton_1.setChecked(True)
                else:
                    self.PORTB_PIN7_IN_PULL_DOWN_radioButton_1.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN0')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN0_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_208.setEnabled(True)
                self.groupBox_207.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN0_OUT_HIGH_radioButton.setChecked(True)
                else:
                    self.PORTC_PIN0_OUT_LOW_radioButton.setChecked(True)
            else:
                self.PORTC_PIN0_INPUT_radioButton_2.setChecked(True)
                self.groupBox_208.setDisabled(True)
                self.groupBox_207.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN0_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN0_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN1')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN1_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_220.setEnabled(True)
                self.groupBox_219.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN1_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN1_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN1_INPUT_radioButton_2.setChecked(True)
                self.groupBox_220.setDisabled(True)
                self.groupBox_219.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN1_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN1_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN2')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN2_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_212.setEnabled(True)
                self.groupBox_211.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN2_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN2_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN2_INPUT_radioButton_2.setChecked(True)
                self.groupBox_212.setDisabled(True)
                self.groupBox_211.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN2_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN2_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN3')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN3_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_228.setEnabled(True)
                self.groupBox_227.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN3_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN3_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN3_INPUT_radioButton_2.setChecked(True)
                self.groupBox_228.setDisabled(True)
                self.groupBox_227.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN3_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN3_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN4')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN4_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_145.setEnabled(True)
                self.groupBox_141.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN4_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN4_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN4_INPUT_radioButton_2.setChecked(True)
                self.groupBox_145.setDisabled(True)
                self.groupBox_141.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN4_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN4_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN5')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN5_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_216.setEnabled(True)
                self.groupBox_215.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN5_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN5_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN5_INPUT_radioButton_2.setChecked(True)
                self.groupBox_216.setDisabled(True)
                self.groupBox_215.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN5_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN5_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN6')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN6_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_224.setEnabled(True)
                self.groupBox_223.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN6_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN6_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN6_INPUT_radioButton_2.setChecked(True)
                self.groupBox_224.setDisabled(True)
                self.groupBox_223.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN6_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN6_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTC')
            pin = port.find('PIN7')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTC_PIN7_OUTPUT_radioButton_2.setChecked(True)
                self.groupBox_129.setEnabled(True)
                self.groupBox_125.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTC_PIN7_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN7_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTC_PIN7_INPUT_radioButton_2.setChecked(True)
                self.groupBox_129.setDisabled(True)
                self.groupBox_125.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTC_PIN7_IN_PULL_UP_radioButton_2.setChecked(True)
                else:
                    self.PORTC_PIN7_IN_PULL_DOWN_radioButton_2.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN0')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN0_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_232.setEnabled(True)
                self.groupBox_231.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN0_OUT_HIGH_radioButton_2.setChecked(True)
                else:
                    self.PORTD_PIN0_OUT_LOW_radioButton_2.setChecked(True)
            else:
                self.PORTD_PIN0_INPUT_radioButton_3.setChecked(True)
                self.groupBox_232.setDisabled(True)
                self.groupBox_231.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN0_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN0_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN1')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN1_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_248.setEnabled(True)
                self.groupBox_247.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN1_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN1_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN1_INPUT_radioButton_3.setChecked(True)
                self.groupBox_248.setDisabled(True)
                self.groupBox_247.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN1_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN1_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN2')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN2_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_240.setEnabled(True)
                self.groupBox_239.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN2_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN2_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN2_INPUT_radioButton_3.setChecked(True)
                self.groupBox_240.setDisabled(True)
                self.groupBox_239.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN2_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN2_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN3')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN3_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_252.setEnabled(True)
                self.groupBox_251.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN3_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN3_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN3_INPUT_radioButton_3.setChecked(True)
                self.groupBox_252.setDisabled(True)
                self.groupBox_251.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN3_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN3_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN4')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN4_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_177.setEnabled(True)
                self.groupBox_173.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN4_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN4_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN4_INPUT_radioButton_3.setChecked(True)
                self.groupBox_177.setDisabled(True)
                self.groupBox_173.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN4_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN4_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN5')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN5_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_236.setEnabled(True)
                self.groupBox_235.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN5_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN5_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN5_INPUT_radioButton_3.setChecked(True)
                self.groupBox_236.setDisabled(True)
                self.groupBox_235.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN5_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN5_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN6')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN6_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_244.setEnabled(True)
                self.groupBox_243.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN6_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN6_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN6_INPUT_radioButton_3.setChecked(True)
                self.groupBox_244.setDisabled(True)
                self.groupBox_243.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN6_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN6_IN_PULL_DOWN_radioButton_3.setChecked(True)

            port = DIO.find('PORTD')
            pin = port.find('PIN7')
            direction = pin.find('DIR').text
            cfg = pin.find('CFG').text
            if direction == "OUTPUT":
                self.PORTD_PIN7_OUTPUT_radioButton_3.setChecked(True)
                self.groupBox_161.setEnabled(True)
                self.groupBox_157.setDisabled(True)
                if cfg == "HIGH":
                    self.PORTD_PIN7_OUT_HIGH_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN7_OUT_LOW_radioButton_3.setChecked(True)
            else:
                self.PORTD_PIN7_INPUT_radioButton_3.setChecked(True)
                self.groupBox_161.setDisabled(True)
                self.groupBox_157.setEnabled(True)
                if cfg == "PULL_UP":
                    self.PORTD_PIN7_IN_PULL_UP_radioButton_3.setChecked(True)
                else:
                    self.PORTD_PIN7_IN_PULL_DOWN_radioButton_3.setChecked(True)

            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setText("Configuration Loaded Successfully")
            msg2.setWindowTitle("AVR CONFIGURATOR")
            msg2.exec_()


app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
