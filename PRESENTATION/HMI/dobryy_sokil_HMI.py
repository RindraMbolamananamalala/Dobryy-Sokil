# -*- coding: utf-8 -*-

"""dobryy_sokil_HMI.py: The dedicated class file for the graphical definition of the Main Window of the Добрий Сокіл
project's Human-Machine Interface
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

################################################################################
## Created with: Qt User Interface Compiler version 5.15.2
################################################################################


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):

    def set_main_window(self, main_window: QMainWindow):
        self.main_window = main_window

    def get_main_window(self) -> QMainWindow:
        return self.main_window

    def set_input_text_to_research(self, input_text_to_research):
        self.input_text_to_research = input_text_to_research

    def get_input_text_to_research(self) -> QPlainTextEdit:
        return self.input_text_to_research

    def set_button_launch_research(self, button_launch_research):
        self.button_launch_research = button_launch_research

    def get_button_launch_research(self):
        return self.button_launch_research

    def set_button_refresh_list_research_results(self, button_refresh_list_research_results):
        self.button_refresh_list_research_results = button_refresh_list_research_results

    def get_button_refresh_list_research_results(self):
        return self.button_refresh_list_research_results

    def set_list_research_results(self, list_research_results: QListView):
        self.list_research_results = list_research_results

    def get_list_research_results(self) -> QListView:
        return self.list_research_results

    def set_area_picture_found(self, area_picture_found):
        self.area_picture_found = area_picture_found

    def get_area_picture_found(self):
        return self.area_picture_found

    def __init__(self, main_window):
        """
        Setting up the UI
        :param main_window: a blank main window to be assigned to the set of settings
        """

        """
        Basics configurations (Part I)
        """
        if not main_window.objectName():
            main_window.setObjectName(u"Добрий Сокіл")
        main_window.resize(947, 838)
        self.set_main_window(main_window)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"centralwidget")

        """
        Management of the part dedicated to the "Identity" of the Application
        """
        self.container_application_identity = QFrame(self.central_widget)
        self.container_application_identity.setObjectName(u"container_application_identity")
        self.container_application_identity.setGeometry(QRect(0, 0, 941, 161))
        self.container_application_identity.setMouseTracking(False)
        self.container_application_identity.setAutoFillBackground(False)
        self.container_application_identity.setStyleSheet(u"background-color:none;\n"
                                                          "")
        self.container_application_identity.setFrameShape(QFrame.StyledPanel)
        self.container_application_identity.setFrameShadow(QFrame.Raised)
        self.label_logo = QLabel(self.container_application_identity)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(310, -70, 881, 301))
        self.label_logo.setPixmap(
            QPixmap(u"RESOURCES/Images/\u0414\u043e\u0431\u0440\u044b\u0439_\u0421\u043e\u043a\u043e\u043b_LOGO.JPG"))

        """
        Management of the part dedicated to the "Application Business" of the Application
        """
        self.container_application_business = QFrame(self.central_widget)
        self.container_application_business.setObjectName(u"container_application_business")
        self.container_application_business.setGeometry(QRect(0, 170, 941, 621))
        self.container_application_business.setFrameShape(QFrame.StyledPanel)
        self.container_application_business.setFrameShadow(QFrame.Raised)
        # The "research" part
        self.container_research = QFrame(self.container_application_business)
        self.container_research.setObjectName(u"container_research")
        self.container_research.setGeometry(QRect(20, 10, 371, 621))
        self.container_research.setStyleSheet(u"QFrame\n"
                                              "{\n"
                                              "	background-color:gray;\n"
                                              "	border-width: 1;\n"
                                              "	border-radius: 3;\n"
                                              "	border-style: solid;\n"
                                              "	border-color: orange;\n"
                                              "}")
        self.container_research.setFrameShape(QFrame.StyledPanel)
        self.container_research.setFrameShadow(QFrame.Raised)
        self.input_text_to_research = QPlainTextEdit(self.container_research)
        self.input_text_to_research.setObjectName(u"input_text_to_research")
        self.input_text_to_research.setGeometry(QRect(40, 20, 261, 41))
        self.input_text_to_research.setStyleSheet(u"background-color:white;\n"
                                                  "border-width: 1;\n"
                                                  "border-radius: 3;\n"
                                                  "border-style: solid;\n"
                                                  "border-color: orange;\n"
                                                  "")
        self.button_launch_research = QPushButton(self.container_research)
        self.button_launch_research.setObjectName(u"button_launch_research")
        self.button_launch_research.setGeometry(QRect(310, 20, 41, 41))
        self.button_launch_research.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_launch_research.setStyleSheet(u"QPushButton\n"
                                                  "{\n"
                                                  "	background-color : orange;\n"
                                                  "}")
        icon = QIcon()
        icon.addFile(u"RESOURCES/Images/launch_search_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_launch_research.setIcon(icon)
        self.scrollArea = QScrollArea(self.container_research)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(40, 70, 311, 511))
        self.scrollArea.setStyleSheet(u"QScrollArea\n"
                                      "{\n"
                                      "	background-color:none;\n"
                                      "	border-width: 1;\n"
                                      "	border-radius: 3;\n"
                                      "	border-style: solid;\n"
                                      "	border-color: orange;\n"
                                      "}")
        self.scrollArea.setWidgetResizable(True)
        # The "research's results" part
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 309, 509))
        self.button_refresh_list_research_results = QPushButton(self.scrollAreaWidgetContents)
        self.button_refresh_list_research_results.setObjectName(u"button_refresh_list_research_results")
        self.button_refresh_list_research_results.setGeometry(QRect(10, 30, 31, 31))
        self.button_refresh_list_research_results.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_refresh_list_research_results.setAutoFillBackground(False)
        self.button_refresh_list_research_results.setStyleSheet(u"QPushButton\n"
                                                                "{\n"
                                                                "	background-color:orange;\n"
                                                                "}")
        icon1 = QIcon()
        icon1.addFile(u"RESOURCES/Images/refresh_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_refresh_list_research_results.setIcon(icon1)
        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(50, 10, 251, 491))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 249, 489))
        self.list_research_results = QListView(self.scrollAreaWidgetContents_2)
        self.list_research_results.setObjectName(u"list_research_results")
        self.list_research_results.setGeometry(QRect(0, 0, 251, 491))
        self.list_research_results.setStyleSheet(u"QListView\n"
                                                 "{\n"
                                                 "background-color:white;\n"
                                                 "border-width: 1;\n"
                                                 "border-radius: 3;\n"
                                                 "border-style: solid;\n"
                                                 "border-color: white;\n"
                                                 "}")
        self.list_research_results.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.list_research_results.setItemAlignment(Qt.AlignLeading)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.input_text_to_research.raise_()
        self.button_launch_research.raise_()
        # The "Image Result" part
        self.container_image_result = QFrame(self.container_application_business)
        self.container_image_result.setObjectName(u"container_image_result")
        self.container_image_result.setGeometry(QRect(400, 10, 521, 611))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(128, 128, 128, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush2)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush2)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
        # endif
        self.container_image_result.setPalette(palette)
        self.container_image_result.setAutoFillBackground(False)
        self.container_image_result.setStyleSheet(u"background-color: gray;\n"
                                                  "border-width: 1;\n"
                                                  "border-radius: 3;\n"
                                                  "border-style: solid;\n"
                                                  "border-color: orange;")
        self.container_image_result.setFrameShape(QFrame.StyledPanel)
        self.container_image_result.setFrameShadow(QFrame.Raised)
        self.area_picture_found = QLabel(self.container_image_result)
        self.area_picture_found.setObjectName(u"area_picture_found")
        self.area_picture_found.setGeometry(QRect(40, 70, 451, 451))
        self.area_picture_found.setPixmap(QPixmap(u"RESOURCES/Images/no_element_found.JPG"))

        """
        Basics configurations (Part II)
        """
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 26))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        """
        Re-translating  the UI
        :param main_window: The main window to be retranslated
        """
        main_window.setWindowTitle(QCoreApplication.translate("Добрий Сокіл"
                                                              , u"Добрий Сокіл"
                                                              , None)
                                   )
        self.label_logo.setText("")
        # if QT_CONFIG(tooltip)
        self.button_launch_research.setToolTip(QCoreApplication.translate("MainWindow"
                                                                          , u"Go!"
                                                                          , None)
                                               )
        # endif // QT_CONFIG(tooltip)
        self.button_launch_research.setText("")
        # if QT_CONFIG(tooltip)
        self.button_refresh_list_research_results.setToolTip(QCoreApplication.translate("MainWindow"
                                                                                        , u"Refresh"
                                                                                        , None)
                                                             )
        # endif // QT_CONFIG(tooltip)
        self.button_refresh_list_research_results.setText("")
        self.area_picture_found.setText("")

    def update_list_research_results_content(self, content : str):
        model = QStandardItemModel()
        item = QStandardItem(content)
        model.appendRow(item)
        self.list_research_results.setModel(model)