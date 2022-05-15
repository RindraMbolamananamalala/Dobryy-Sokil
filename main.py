# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PRESENTATION.HMI.Window import Window
from PRESENTATION.VIEW.dobryy_sokil_view import DobryySokilView
from PRESENTATION.CONTROLLER.dobrry_sokil_controller import DobrrySokilController

from PRESENTATION.HMI.dobryy_sokil_HMI import Ui_MainWindow

from PySide2.QtWidgets import *
from PyQt5.QtWidgets import QApplication
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    application = QApplication(sys.argv)

    # window = Window()
    # view = Rindra_View(window)
    # controller = RindraController(view)
    #
    # controller.get_rindra_view().get_window().get_main_window().show()

    main_window = QMainWindow()
    window = Ui_MainWindow(main_window)
    view = DobryySokilView(window)
    controller = DobrrySokilController(view)
    controller.get_dobryy_sokil_view().get_dobryy_sokil_hmi().get_main_window().show()

    sys.exit(application.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
