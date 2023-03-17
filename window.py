# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_table2sql(object):
    def setupUi(self, table2sql):
        if not table2sql.objectName():
            table2sql.setObjectName(u"table2sql")
        table2sql.resize(564, 468)
        self.verticalLayout_5 = QVBoxLayout(table2sql)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(table2sql)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(table2sql)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(table2sql)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.plainTextEdit = QPlainTextEdit(table2sql)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_3.addWidget(self.plainTextEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(table2sql)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.plainTextEdit_2 = QPlainTextEdit(table2sql)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout_2.addWidget(self.plainTextEdit_2)

        self.label_4 = QLabel(table2sql)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openPushButton = QPushButton(table2sql)
        self.openPushButton.setObjectName(u"openPushButton")

        self.verticalLayout.addWidget(self.openPushButton)

        self.postPushButton = QPushButton(table2sql)
        self.postPushButton.setObjectName(u"postPushButton")

        self.verticalLayout.addWidget(self.postPushButton)

        self.sqlPostPushButton = QPushButton(table2sql)
        self.sqlPostPushButton.setObjectName(u"sqlPostPushButton")

        self.verticalLayout.addWidget(self.sqlPostPushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.retranslateUi(table2sql)

        QMetaObject.connectSlotsByName(table2sql)
    # setupUi

    def retranslateUi(self, table2sql):
        table2sql.setWindowTitle(QCoreApplication.translate("table2sql", u"Form", None))
        self.label.setText(QCoreApplication.translate("table2sql", u"\u8bf7\u8f93\u5165\u5173\u7cfb\u540d(\u9ed8\u8ba4\u4e3arelation)\uff1a", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("table2sql", u"relation", None))
        self.label_3.setText(QCoreApplication.translate("table2sql", u"\u6570\u636e", None))
        self.plainTextEdit.setPlainText("")
        self.label_2.setText(QCoreApplication.translate("table2sql", u"\u6a21\u5f0f", None))
        self.label_4.setText(QCoreApplication.translate("table2sql", u"\u8bf7\u6ce8\u610f\uff1a\u56fe\u7247\u5c3d\u91cf\u4e0d\u5305\u542b\u8868\u9898", None))
        self.openPushButton.setText(QCoreApplication.translate("table2sql", u"open", None))
        self.postPushButton.setText(QCoreApplication.translate("table2sql", u"post", None))
        self.sqlPostPushButton.setText(QCoreApplication.translate("table2sql", u"sql", None))
    # retranslateUi

