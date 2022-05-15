# -*- coding: utf-8 -*-

"""
dobryy_sokil_controller.py: The dedicated class file for the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from PRESENTATION.VIEW.dobryy_sokil_view import DobryySokilView, DobryySokilViewWidgetEventId


class DobrrySokilController:
    def set_dobryy_sokil_view(self, dobryy_sokil_view: DobryySokilView):
        self.dobryy_sokil_view = dobryy_sokil_view

    def get_dobryy_sokil_view(self):
        return self.dobryy_sokil_view

    def __init__(self, dobryy_sokil_view: DobryySokilView):
        # Preparing the View Part
        self.set_dobryy_sokil_view(dobryy_sokil_view)
        self.get_dobryy_sokil_view().manage_event(
            DobryySokilViewWidgetEventId.BUTTON_LAUNCH_RESEARCH_CLICKED
            , self.event_button_launch_research_clicked
        )

    def event_button_launch_research_clicked(self):
        # Temporary, to be managed later
        pass



