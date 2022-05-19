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

from RESOURCES.MESSAGES.HMI.hmi_messages import Messages as HMIMessages


class Ui_MainWindow(object):
    AREA_PICTURE_FOUND_WIDTH = 451
    AREA_PICTURE_FOUND_HEIGHT = 451

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

    def set_root_folder_browser(self, root_folder_browser: QPlainTextEdit):
        self.root_folder_browser = root_folder_browser

    def get_root_folder_browser(self) -> QPlainTextEdit:
        return self.root_folder_browser

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
        main_window.resize(947, 950)
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
        Management of the part dedicated to the "Root Folder" for the Research  
        """
        self.container_root_folder_for_the_research = QFrame(self.central_widget)
        self.container_root_folder_for_the_research.setObjectName(u"container_root_folder_for_the_research")
        self.container_root_folder_for_the_research.setGeometry(QRect(20, 210, 901, 51))
        self.container_root_folder_for_the_research.setStyleSheet(u"background-color: gray;\n"
                                                                  "border-width: 1;\n"
                                                                  "border-radius: 3;\n"
                                                                  "border-style: solid;\n"
                                                                  "border-color: orange;")
        self.container_root_folder_for_the_research.setFrameShape(QFrame.StyledPanel)
        self.container_root_folder_for_the_research.setFrameShadow(QFrame.Raised)
        self.container_root_folder_for_the_research = QFrame(self.central_widget)
        self.container_root_folder_for_the_research.setObjectName(u"container_root_folder_for_the_research")
        self.container_root_folder_for_the_research.setGeometry(QRect(20, 210, 901, 61))
        self.container_root_folder_for_the_research.setStyleSheet(u"QFrame{\n"
                                                                  "	background-color: gray;\n"
                                                                  "	border-width: 1;\n"
                                                                  "	border-radius: 3;\n"
                                                                  "	border-style: solid;\n"
                                                                  "	border-color: orange;\n"
                                                                  "}")
        self.container_root_folder_for_the_research.setFrameShape(QFrame.StyledPanel)
        self.container_root_folder_for_the_research.setFrameShadow(QFrame.Raised)
        # The Root folder Browser
        self.root_folder_browser = QPlainTextEdit(self.container_root_folder_for_the_research)
        self.root_folder_browser.setObjectName(u"root_folder_browser")
        self.root_folder_browser.setGeometry(QRect(20, 10, 801, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.root_folder_browser.setFont(font1)
        self.root_folder_browser.setStyleSheet(u"QPlainTextEdit\n"
                                               "{\n"
                                               "	background-color:white;\n"
                                               "	border-width: 1;\n"
                                               "	border-radius: 3;\n"
                                               "	border-style: solid;\n"
                                               "	border-color: orange;\n"
                                               "}")
        self.root_folder_browser.setReadOnly(True)
        # PRESENTATION_HMI_R003 : By default, the Root Folder for the Research is set to the Root folder of
        # the Disk “C:\”
        self.root_folder_browser.setPlainText("C/:")
        # The Button for the Root folder Browser
        self.button_open_root_folder_browser = QPushButton(self.container_root_folder_for_the_research)
        self.button_open_root_folder_browser.setObjectName(u"button_open_root_folder_browser")
        self.button_open_root_folder_browser.setGeometry(QRect(830, 10, 61, 41))
        self.button_open_root_folder_browser.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_root_folder_browser.setStyleSheet(u"QPushButton\n"
                                                           "{\n"
                                                           "	background-color : orange;\n"
                                                           "}")
        icon2 = QIcon()
        icon2.addFile(u"RESOURCES/Images/root_folder_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_open_root_folder_browser.setIcon(icon2)
        self.button_open_root_folder_browser.setToolTip(QCoreApplication.translate("MainWindow", u"Root folder", None))
        self.button_open_root_folder_browser.setText("")
        # clicking on the Button opening the Root folder Browser means wanting to update the
        # desired Root folder for the Research
        self.button_open_root_folder_browser.clicked.connect(self.update_root_folder)

        """
        Management of the part dedicated to the "Application Business" of the Application
        """
        self.container_application_business = QFrame(self.central_widget)
        self.container_application_business.setObjectName(u"container_application_business")
        self.container_application_business.setGeometry(QRect(0, 280, 941, 621))
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
        self.area_picture_found.setGeometry(
            QRect(40
                  , 70
                  , Ui_MainWindow.AREA_PICTURE_FOUND_WIDTH
                  , Ui_MainWindow.AREA_PICTURE_FOUND_HEIGHT)
        )
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
        main_window.setWindowTitle(QCoreApplication.translate(HMIMessages.HMI_MAIN_WINDOW_TITLE
                                                              , HMIMessages.HMI_MAIN_WINDOW_TITLE
                                                              , None)
                                   )
        self.label_logo.setText("")
        # if QT_CONFIG(tooltip)
        self.button_launch_research.setToolTip(
            QCoreApplication.translate("MainWindow"
                                       , HMIMessages.HMI_BUTTON_LAUNCH_RESEARCH_TOOLTIP
                                       , None)
        )
        # endif // QT_CONFIG(tooltip)
        self.button_launch_research.setText("")
        # if QT_CONFIG(tooltip)
        self.button_refresh_list_research_results.setToolTip(
            QCoreApplication.translate("MainWindow"
                                       , HMIMessages.HMI_BUTTON_REFRESH_RESEARCH_RESULT_TOOLTIP
                                       , None)
        )
        # endif // QT_CONFIG(tooltip)
        self.button_refresh_list_research_results.setText("")
        self.area_picture_found.setText("")

    def update_root_folder(self):
        """
        First, opening the Root folder Browser, then affecting the path of the chosen folder as the new one
        within the text part related to the previous Browser
        :return: None
        """
        root_folder_path = QFileDialog.getExistingDirectory(self.container_root_folder_for_the_research,
                                                            "Select Directory")
        self.get_root_folder_browser().setPlainText(root_folder_path)

    def update_list_research_results_content(self, content: []):
        """
        Updating the content of the List View dedicated to the results of the Research
        :param content: The list of "images' information", information respecting the specific structure :
            <image>{
                    "name": <image_name>,
                    "extension": <image_extension>,
                    "absolute_path": <image_absolute_path>,
            }
        :return: None
        """
        model = QStandardItemModel()
        for images_information in content:
            image_name = images_information["name"]
            image_extension = images_information["extension"]
            image_absolute_path = images_information["absolute_path"]
            item = QStandardItem(image_name
                                 + "."
                                 + image_extension)
            item.setToolTip(image_absolute_path)
            model.appendRow(item)
        self.list_research_results.setModel(model)

    def update_area_picture_found(self, picture_path: str):
        """
        Updating the content of the area dedicated for the presentation of the selected picture among
        those found after the Research process
        :param picture_path: The path of the picture selected
        :return: None
        """
        raw_pixmap = QPixmap(picture_path)
        pixmap_final = raw_pixmap.scaled(Ui_MainWindow.AREA_PICTURE_FOUND_WIDTH
                                         , Ui_MainWindow.AREA_PICTURE_FOUND_HEIGHT
                                         # Keeping the Aspect Ratio normally if  the Picture orientation is "Portrait",
                                         # keeping the Aspect Ration by expanding if the Picture orientation is
                                         # "Landscape"
                                         , (Qt.KeepAspectRatioByExpanding, Qt.KeepAspectRatio)
                                         [(raw_pixmap.width() > raw_pixmap.height())]
                                         )
        self.get_area_picture_found().setPixmap(pixmap_final)

    def show_selected_image(self, index):
        """
        Getting the ToolTip's value of the selected item, representing the Absolute path of the image concerned,
        and then updating the content of the area dedicated for the image found from this Absolute path
        :param index: the index (within the model of the list view dedicated to the results) of the row (item)
        corresponding to the image
        :return: None
        """
        self.update_area_picture_found(
            self.get_list_research_results()
                .model().item(index.row()).toolTip()
        )
