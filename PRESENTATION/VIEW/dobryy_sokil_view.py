# -*- coding: utf-8 -*-

"""
dobryy_sokil_view.py: The python file dedicated to the "View" part of the MVC pattern implemented within
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

    The Enum dedicated to the representation of the couple (Widget, External_Event) with a unique Id
    """
    BUTTON_LAUNCH_RESEARCH_CLICKED = 1
    BUTTON_REFRESH_LIST_RESEARCH_RESULTS_CLICKED = 2
    TYPING_ON_INPUT_TEXT_TO_RESEARCH = 3
    ITEM_WITHIN_LIST_RESEARCH_RESULTS_SELECTED = 4


class DobryySokilView:
    def set_dobryy_sokil_hmi(self, dobryy_sokil_hmi: Ui_MainWindow):
        """

        :param dobryy_sokil_hmi: The HMI to be associated to the View Part of the MVC Implementation
        within the PRESENTATION layer of the Dobryy Sokil Project
        :return: None
        """
        self.dobryy_sokil_hmi = dobryy_sokil_hmi

    def get_dobryy_sokil_hmi(self) -> Ui_MainWindow:
        """

        :return: The HMI associated to the View Part of the MVC Implementation
        within the PRESENTATION layer of the Dobryy Sokil Project
        """
        return self.dobryy_sokil_hmi

    def __init__(self, window: Ui_MainWindow):
        """

        :param window: The main window of the application.
        """
        self.set_dobryy_sokil_hmi(window)
        # rule : PRESENTATION_HMI_R001
        self.manage_event(DobryySokilViewWidgetEventId.TYPING_ON_INPUT_TEXT_TO_RESEARCH, self.PRESENTATION_HMI_R001)
        # also, at the start, disabling the Button that launches the Research
        self.PRESENTATION_HMI_R001()
        # linking the external event of selecting an item within the results' list view
        # with the internal action of showing the corresponding image on the dedicated area
        self.manage_event(DobryySokilViewWidgetEventId.ITEM_WITHIN_LIST_RESEARCH_RESULTS_SELECTED
                          , self.load_image_on_the_image_area)

    def manage_event(self, widget_event_id, action):
        """

        :param widget_event_id: The id representing the concerned couple (widget, external event)
        :param action: The internal action to be connected, and then performed, to the Widget after the corresponding
        external event
        """
        if widget_event_id == DobryySokilViewWidgetEventId.BUTTON_LAUNCH_RESEARCH_CLICKED:
            # the Button for the launch of the Research has been clicked
            self.get_dobryy_sokil_hmi().get_button_launch_research().clicked.connect(action)
        elif widget_event_id == DobryySokilViewWidgetEventId.BUTTON_REFRESH_LIST_RESEARCH_RESULTS_CLICKED:
            # the Button for the Refresh process of the Research results list has been clicked
            self.get_dobryy_sokil_hmi().get_button_refresh_list_research_results().clicked.connect(action)
        elif widget_event_id == DobryySokilViewWidgetEventId.TYPING_ON_INPUT_TEXT_TO_RESEARCH:
            # User is typing on the Input Text dedicated for the Research
            # Rule PRESENTATION_HMI_R001 must be respected
            self.get_dobryy_sokil_hmi().get_input_text_to_research().textChanged.connect(self.PRESENTATION_HMI_R001)
        elif widget_event_id == DobryySokilViewWidgetEventId.ITEM_WITHIN_LIST_RESEARCH_RESULTS_SELECTED:
            # an Item is selected within the list view for the results,
            # therefore, loading its corresponding image on the dedicated area
            self.get_dobryy_sokil_hmi().get_list_research_results().clicked.connect(action)
        else:
            # no match found for the couple (widget, event) represented by the Id : widget_event_id
            print('An internal error was occurred!')

    """
    THE SPECIFIC RULES TO APPLY TO THE HMI PART
    """
    def PRESENTATION_HMI_R001(self):
        """

        If the content of the Input Text for the research is empty, the Button for the launch of the Research must be
        disabled.
        """
        if self.get_dobryy_sokil_hmi().get_input_text_to_research().toPlainText() is None \
                or len(self.get_dobryy_sokil_hmi().get_input_text_to_research().toPlainText()) < 1:
            self.get_dobryy_sokil_hmi().get_button_launch_research().setDisabled(True)
        else:
            self.get_dobryy_sokil_hmi().get_button_launch_research().setDisabled(False)

    def get_root_folder_path(self) -> str:
        """

        :return: The path of the Root Folder contained in the Root Folder Browser
        """
        return self.get_dobryy_sokil_hmi().get_root_folder_browser().toPlainText()

    def get_user_input(self) -> str:
        """

        :return: The text inserted by the User inside the Text area dedicated to the label of the Object of Search
        """
        return self.get_dobryy_sokil_hmi().get_input_text_to_research().toPlainText()

    def show_image(self, picture_path: str):
        """
        Showing an image on the "Area Picture found"-dedicated part.

        :param picture_path: The path of the Picture to show
        :return: None
        """
        self.get_dobryy_sokil_hmi().update_area_picture_found(picture_path)

    def load_images_information_results(self, images_information: []):
        """
        Loading all the information on the images found as the results of the Research process in the results
        list view.

        :param images_information: The list of the images' information, structured as  :
            <image>{
                "name": <image_name>,
                "extension": <image_extension>,
                "absolute_path": <image_absolute_path>,
            }
        :return: None
        """
        self.get_dobryy_sokil_hmi().update_list_research_results_content(images_information)

    def load_image_on_the_image_area(self, index):
        """
        Loading an image on the dedicated area, given its corresponding index within the list of results.

        :param index: The index within the list of results corresponding to the image to be loaded
        :return: None
        """
        self.get_dobryy_sokil_hmi().show_selected_image(index)

