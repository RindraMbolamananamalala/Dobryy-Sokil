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

from BUSINESS.CONSTRAINTS.CONVERTER.image_converter import image_file_paths_to_image_domain_objects

from UTILS.image_utils import get_all_images_within_a_folder


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
        """Will be "seriously" finalized according to the actual needs later """
        # root_folder_path = self.get_dobryy_sokil_view().get_root_folder_path()
        # images_absolutes_path_found = get_all_images_within_a_folder(root_folder_path)
        # images_found = image_file_paths_to_image_domain_objects(images_absolutes_path_found)
        # list_structured_image_information = []
        # for image in images_found:
        #     structured_image_information = {
        #         "name": image.get_name(),
        #         "extension": image.get_extension(),
        #         "absolute_path": image.get_absolute_path()
        #     }
        #     list_structured_image_information.append(structured_image_information)
        # self.get_dobryy_sokil_view().load_images_information_results(list_structured_image_information)
        """butt for the now, just..."""
        pass


