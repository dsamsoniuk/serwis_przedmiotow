# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main_qt6.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionmain_page = QAction(MainWindow)
        self.actionmain_page.setObjectName(u"actionmain_page")
        self.actionzwykla_tabela = QAction(MainWindow)
        self.actionzwykla_tabela.setObjectName(u"actionzwykla_tabela")
        self.actionmodel_tabela = QAction(MainWindow)
        self.actionmodel_tabela.setObjectName(u"actionmodel_tabela")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 30, 731, 471))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 50, 251, 41))
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 220, 89, 25))
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 120, 113, 25))
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(250, 170, 113, 25))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 130, 67, 17))
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 170, 67, 17))
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 120, 231, 21))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableView = QTableView(self.page_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(80, 90, 581, 291))
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 40, 241, 21))
        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 420, 89, 25))
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(448, 420, 191, 25))
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 40, 261, 17))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuPliki = QMenu(self.menubar)
        self.menuPliki.setObjectName(u"menuPliki")
        self.menuStrony = QMenu(self.menubar)
        self.menuStrony.setObjectName(u"menuStrony")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPliki.menuAction())
        self.menubar.addAction(self.menuStrony.menuAction())
        self.menuStrony.addAction(self.actionmain_page)
        self.menuStrony.addAction(self.actionmodel_tabela)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionmain_page.setText(QCoreApplication.translate("MainWindow", u"strona g\u0142\u00f3wna", None))
        self.actionzwykla_tabela.setText(QCoreApplication.translate("MainWindow", u"zwykla tabela", None))
        self.actionmodel_tabela.setText(QCoreApplication.translate("MainWindow", u"lista produkt\u00f3w", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Panel logowania", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Zaloguj si\u0119", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nie zalogowany", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lista produkt\u00f3w", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"zapisz", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"pobierz dane z serwera", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menuPliki.setTitle(QCoreApplication.translate("MainWindow", u"Pliki", None))
        self.menuStrony.setTitle(QCoreApplication.translate("MainWindow", u"Strony", None))
    # retranslateUi

