from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window:
    def set_main_window(self, main_window):
        self.main_window = main_window

    def get_main_window(self):
        return self.main_window

    def set_text_area(self, text_area):
        self.text_area = text_area

    def get_text_area(self):
        return self.text_area

    def set_button_add_new_rindra(self, button_add):
        self.button_add_new_rindra = button_add

    def get_button_add_new_rindra(self):
        return self.button_add_new_rindra

    def set_button_show_rindras(self, button_show):
        self.button_show_rindras = button_show

    def get_button_show_rindras(self):
        return self.button_show_rindras

    def __init__(self):
        # application = QApplication(sys.argv)

        # The Main Window
        main_window = QMainWindow()
        main_window.setGeometry(500, 500, 500, 300)
        main_window.setWindowTitle("Rindra Window")
        self.main_window = main_window

        # The text area
        text_area = QtWidgets.QPlainTextEdit(self.get_main_window())
        text_area.setGeometry(100, 25, 275, 125)
        self.text_area = text_area

        # All the needed buttons
        # The button for adding a new "Rindra"
        button_add_new_rindra = QtWidgets.QPushButton(self.get_main_window())
        button_add_new_rindra.setText("Add")
        button_add_new_rindra.setGeometry(200, 200, 75, 25)
        self.button_add_new_rindra = button_add_new_rindra


        # The button for listing all the already stored in DB "Rindras"
        button_show_rindras = QtWidgets.QPushButton(self.get_main_window())
        button_show_rindras.setText("List")
        button_show_rindras.setGeometry(200, 250, 75, 25)
        self.button_show_rindras = button_show_rindras

