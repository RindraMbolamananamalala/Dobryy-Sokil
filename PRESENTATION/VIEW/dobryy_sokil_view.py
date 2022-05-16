# -*- coding: utf-8 -*-

"""
dobryy_sokil_view.py: The dedicated class file for the "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from enum import Enum

from PRESENTATION.HMI.dobryy_sokil_HMI import Ui_MainWindow


class DobryySokilViewWidgetEventId(Enum):
    """
    The Enum dedicated to the representation of the couple (Widget, Event) with a unique Id
    """
    BUTTON_LAUNCH_RESEARCH_CLICKED = 1
    BUTTON_REFRESH_LIST_RESEARCH_RESULTS_CLICKED = 2
    TYPING_ON_INPUT_TEXT_TO_RESEARCH = 3


class DobryySokilView:
    def set_dobryy_sokil_hmi(self, dobryy_sokil_hmi: Ui_MainWindow):
        self.dobryy_sokil_hmi = dobryy_sokil_hmi

    def get_dobryy_sokil_hmi(self):
        return self.dobryy_sokil_hmi

    def __init__(self, window: Ui_MainWindow):
        self.set_dobryy_sokil_hmi(window)
        self.manage_event(DobryySokilViewWidgetEventId.TYPING_ON_INPUT_TEXT_TO_RESEARCH, self.PRESENTATION_HMI_R001)
        # at the start, disabling the Button that launches the Research
        self.PRESENTATION_HMI_R001()

    def manage_event(self, widget_event_id, event):
        """
        :param widget_event_id: The id representing the concerned couple (widget, external event)
        :param event: The internal event to be connected to the Widget after the corresponding external event
        """
        if widget_event_id == DobryySokilViewWidgetEventId.BUTTON_LAUNCH_RESEARCH_CLICKED:
            # the Button for the launch of the Research has been clicked
            self.get_dobryy_sokil_hmi().get_button_launch_research().clicked.connect(event)
        elif widget_event_id == DobryySokilViewWidgetEventId.BUTTON_REFRESH_LIST_RESEARCH_RESULTS_CLICKED:
            # the Button for the Refresh process of the Research results list has been clicked
            self.get_dobryy_sokil_hmi().get_button_refresh_list_research_results().clicked.connect(event)
        elif widget_event_id == DobryySokilViewWidgetEventId.TYPING_ON_INPUT_TEXT_TO_RESEARCH:
            # User is typing on the Input Text dedicated for the Research
            # Rule PRESENTATION_HMI_R001 must be respected
            self.get_dobryy_sokil_hmi().get_input_text_to_research().textChanged.connect(self.PRESENTATION_HMI_R001)
        else:
            # no match found for the couple (widget, event) represented by the Id : widget_event_id
            print('An internal error was occurred!')

    """
    THE SPECIFIC RULES TO APPLY TO THE HMI PART
    """

    def PRESENTATION_HMI_R001(self):
        """
        If the content of the Input Text for the research is empty, the Button for the launch of the Research must be disabled.
        """
        if self.get_dobryy_sokil_hmi().get_input_text_to_research().toPlainText() is None \
                or len(self.get_dobryy_sokil_hmi().get_input_text_to_research().toPlainText()) < 1:
            self.get_dobryy_sokil_hmi().get_button_launch_research().setDisabled(True)
        else:
            self.get_dobryy_sokil_hmi().get_button_launch_research().setDisabled(False)

    def show_image(self, picture_path: str):
        """
        Showing a picture on the Area Picture found part
        :param picture_path: The path of the Picture to show
        :return: None
        """
        self.get_dobryy_sokil_hmi().update_area_picture_found(picture_path)
