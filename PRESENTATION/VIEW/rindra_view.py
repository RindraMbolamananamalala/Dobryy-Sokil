from enum import Enum

from PRESENTATION.HMI.Window import Window


class ViewWidgetsId(Enum):
    BUTTON_ADD_NEW_RINDRA = 1
    BUTTON_LIST = 2


class Rindra_View:

    def set_window(self, window):
        self.window = window

    def get_window(self):
        return self.window

    def __init__(self, window):
        self.set_window(window)

    def manage_event(self, widget_id, event):
        if widget_id == ViewWidgetsId.BUTTON_ADD_NEW_RINDRA:
            self.get_window().get_button_add_new_rindra().clicked.connect(event)
        elif widget_id == ViewWidgetsId.BUTTON_LIST:
            self.get_window().get_button_show_rindras().clicked.connect(event)
        else:
            print('An internal error was occurred!')

    def get_user_input_text(self):
        return self.get_window().get_text_area().toPlainText()

    def update_text_to_show_to_user(self, text):
        self.get_window().get_text_area().setPlainText(text)



