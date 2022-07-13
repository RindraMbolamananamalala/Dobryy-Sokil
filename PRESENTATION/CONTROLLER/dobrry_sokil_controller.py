# -*- coding: utf-8 -*-

"""
dobryy_sokil_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from CONFIGURATIONS.logger import LOGGER

from MAPPER.dobryy_sokil_mapper import image_dto_to_image

from PRESENTATION.VIEW.dobryy_sokil_view import DobryySokilView, DobryySokilViewWidgetEventId

from BUSINESS.SERVICES.APPLICATION_SERVICES.DOBRYY_SOKIL_AS.DOBRYY_SOKIL_AS_INTF.dobryy_sokil_AS_intf import \
    DobryySokilASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.DOBRYY_SOKIL_AS.DOBRYY_SOKIL_AS_IMPL.dobryy_sokil_AS_impl import \
    DobryySokilASImpl


class DobrrySokilController:
    def set_dobryy_sokil_view(self, dobryy_sokil_view: DobryySokilView):
        """

        :param dobryy_sokil_view: The View part to be associated to the Controller part within the MVC
        Implementation at the level of the Presentation Layer of the Dobryy Sokil Project.
        :return: None
        """
        self.dobryy_sokil_view = dobryy_sokil_view

    def get_dobryy_sokil_view(self) -> DobryySokilView:
        """

        :return: The View part Linked to the Controller part within the MVC Implementation
        at the level of the Presentation Layer of the Dobryy Sokil Project.
        """
        return self.dobryy_sokil_view

    def set_dobryy_sokil_as(self, dobryy_sokil_as: DobryySokilASIntf):
        """

        :param dobryy_sokil_as: The Dobryy Sokil Application Service to be used throughout the entire Controller
        :return: None
        """
        self.dobryy_sokil_as = dobryy_sokil_as

    def get_dobryy_sokil_as(self) -> DobryySokilASIntf:
        """

        :return: The Dobryy Sokil Application Service used throughout the entire Controller
        """
        return self.dobryy_sokil_as

    def __init__(self, dobryy_sokil_view: DobryySokilView):
        """

        :param dobryy_sokil_view: The Dobryy Sokil' View Part to be associated with the current Dobryy Sokil's Controller
        """
        # Preparing the View Part
        self.set_dobryy_sokil_view(dobryy_sokil_view)
        self.get_dobryy_sokil_view().manage_event(
            DobryySokilViewWidgetEventId.BUTTON_LAUNCH_RESEARCH_CLICKED
            , self.event_button_launch_research_clicked
        )

        # Preparing the Dobryy Sokil AS to be used throughout the entire Controller
        self.set_dobryy_sokil_as(DobryySokilASImpl())

    def event_button_launch_research_clicked(self):
        """
        Launching the entire process of Images searching, based on the given label of the Object of search,
        within the selected Root Folder, and then transmitting all the results to the dedicated VIEW part.

        :return: None
        """

        try:
            # First, the Dobryy Sokil listens to the User's orders related to the Image search : the Object of Search
            # and the Root Folder for the search
            object_to_search_label = self.get_dobryy_sokil_view().get_user_input()
            if not object_to_search_label:
                # An invalid Label of Object to search was provided
                LOGGER.error("An invalid Label of Object to search was provided")
                raise TypeError
            LOGGER.info("The label of the object of search: \"" + object_to_search_label + "\"")
            root_folder_path = self.get_dobryy_sokil_view().get_root_folder_path()
            if not root_folder_path:
                # An invalid Root Folder for the search was provided
                LOGGER.error("An invalid Root Folder for the search was provided")
                raise TypeError
            LOGGER.info("The Root Folder for the search: \"" + root_folder_path + "\"")

            # Launching the actual "Search" process
            images_found_dto = self.get_dobryy_sokil_as().hunt(object_to_search_label, root_folder_path)
            if images_found_dto:
                # A successful search
                LOGGER.info(
                    "Raw Images returned from the search process related to \"" + object_to_search_label + "\""
                    + " within \"" + root_folder_path + "\""
                    + ": " + str(images_found_dto)
                )

                # Preparing the results obtained before sending them to the VIEW part
                list_structured_image_information = []
                for image_dto in images_found_dto:
                    image = image_dto_to_image(image_dto)
                    structured_image_information = {
                        "name": image.get_name(),
                        "extension": image.get_extension(),
                        "absolute_path": image.get_absolute_path()
                    }
                    list_structured_image_information.append(structured_image_information)

                # Sending the results obtained and already pre-treated during the previous step to the VIEW part
                self.get_dobryy_sokil_view().load_images_information_results(list_structured_image_information)
            else:
                # An unsuccessful search, sending an empty list of results to the VIEW part
                LOGGER.info(
                    "No Image related to \"" + object_to_search_label
                    + "\" was found within \"" + root_folder_path + "\""
                )
                self.get_dobryy_sokil_view().load_images_information_results([])
        except Exception as exception:
            # At least one Error was encountered during the entire process, therefore, we have to stop the latter
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Search process of Images. "
            )
            raise
