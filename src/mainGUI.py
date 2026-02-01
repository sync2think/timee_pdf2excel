# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(564, 332)
        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(200, 290, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.gridLayoutWidget = QWidget(dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 40, 521, 66))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelPdf = QLabel(self.gridLayoutWidget)
        self.labelPdf.setObjectName(u"labelPdf")
        self.labelPdf.setMinimumSize(QSize(61, 21))
        self.labelPdf.setMaximumSize(QSize(61, 21))

        self.gridLayout.addWidget(self.labelPdf, 0, 0, 1, 1)

        self.lineEditPdfFile = QLineEdit(self.gridLayoutWidget)
        self.lineEditPdfFile.setObjectName(u"lineEditPdfFile")
        self.lineEditPdfFile.setMinimumSize(QSize(401, 21))
        self.lineEditPdfFile.setMaximumSize(QSize(401, 21))

        self.gridLayout.addWidget(self.lineEditPdfFile, 0, 1, 1, 1)

        self.pushButtonPdfFile = QPushButton(self.gridLayoutWidget)
        self.pushButtonPdfFile.setObjectName(u"pushButtonPdfFile")
        self.pushButtonPdfFile.setMinimumSize(QSize(31, 26))
        self.pushButtonPdfFile.setMaximumSize(QSize(31, 26))

        self.gridLayout.addWidget(self.pushButtonPdfFile, 0, 2, 1, 1)

        self.labelExcel = QLabel(self.gridLayoutWidget)
        self.labelExcel.setObjectName(u"labelExcel")
        self.labelExcel.setMinimumSize(QSize(61, 21))
        self.labelExcel.setMaximumSize(QSize(61, 21))

        self.gridLayout.addWidget(self.labelExcel, 1, 0, 1, 1)

        self.lineEditExcelFile = QLineEdit(self.gridLayoutWidget)
        self.lineEditExcelFile.setObjectName(u"lineEditExcelFile")
        self.lineEditExcelFile.setMinimumSize(QSize(401, 21))
        self.lineEditExcelFile.setMaximumSize(QSize(401, 21))

        self.gridLayout.addWidget(self.lineEditExcelFile, 1, 1, 1, 1)

        self.pushButtonExcelFile = QPushButton(self.gridLayoutWidget)
        self.pushButtonExcelFile.setObjectName(u"pushButtonExcelFile")
        self.pushButtonExcelFile.setMinimumSize(QSize(31, 26))
        self.pushButtonExcelFile.setMaximumSize(QSize(31, 26))

        self.gridLayout.addWidget(self.pushButtonExcelFile, 1, 2, 1, 1)

        self.lineEditLastName = QLineEdit(dialog)
        self.lineEditLastName.setObjectName(u"lineEditLastName")
        self.lineEditLastName.setGeometry(QRect(110, 120, 113, 21))
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 81, 21))
        self.lineEditFirstName = QLineEdit(dialog)
        self.lineEditFirstName.setObjectName(u"lineEditFirstName")
        self.lineEditFirstName.setGeometry(QRect(250, 120, 113, 21))
        self.groupBox = QGroupBox(dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 150, 501, 131))
        self.labelNotice = QLabel(self.groupBox)
        self.labelNotice.setObjectName(u"labelNotice")
        self.labelNotice.setGeometry(QRect(20, 30, 461, 81))
        self.labelNotice.setLineWidth(2)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Time \u6e90\u6cc9\u5fb4\u53ce\u7968\u30a8\u30af\u30bb\u30eb\u5909\u63db", None))
        self.labelPdf.setText(QCoreApplication.translate("dialog", u"pdf \u30d5\u30a1\u30a4\u30eb", None))
        self.pushButtonPdfFile.setText(QCoreApplication.translate("dialog", u"...", None))
        self.labelExcel.setText(QCoreApplication.translate("dialog", u"\u51fa\u529b \u30d5\u30a1\u30a4\u30eb", None))
        self.pushButtonExcelFile.setText(QCoreApplication.translate("dialog", u"...", None))
        self.lineEditLastName.setText(QCoreApplication.translate("dialog", u"\u30e4\u30de\u30c0", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u6c0f\u540d(\u30ab\u30bf\u30ab\u30ca)", None))
        self.lineEditFirstName.setText(QCoreApplication.translate("dialog", u"\u30bf\u30ed\u30a6", None))
        self.groupBox.setTitle(QCoreApplication.translate("dialog", u"\u304a\u77e5\u3089\u305b", None))
        self.labelNotice.setText(QCoreApplication.translate("dialog", u"pdf \u30d5\u30a1\u30a4\u30eb\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002", None))
    # retranslateUi

