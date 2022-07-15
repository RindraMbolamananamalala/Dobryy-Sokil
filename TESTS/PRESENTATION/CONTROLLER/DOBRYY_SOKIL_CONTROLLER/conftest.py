# -*- coding: utf-8 -*-

"""
conftest.py: The python file dedicated to any configurations related to the Unit Testing of the
"PRESENTATION.CONTROLLER.dobrry_sokil_controller.DobrrySokilController.event_button_launch_research_clicked()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import pytest
from unittest.mock import MagicMock

from BUSINESS.MODEL.DTO.image_DTO import ImageDTO


def dobryy_sokil_view_mock():
    """

    :return: An already pre-configured Mock of a Dobryy Sokil VIEW
    """
    get_root_folder_path_mock = MagicMock()
    get_root_folder_path_mock.return_value = "Test_Root_Folder_Path"
    get_user_input_mock = MagicMock()
    get_user_input_mock.return_value = "Test_User_Input"

    return MagicMock(get_root_folder_path=get_root_folder_path_mock
                     , get_user_input=get_user_input_mock
                     , load_images_information_results=MagicMock())


def dobryy_sokil_as_mock():
    """

    :return: An already pre-configured Mock of a Dobryy Sokile Application Service
    """
    hunt_mock = MagicMock()
    hunt_results_mock = [ImageDTO("location_1", "image_1", "extension_1"),
                         ImageDTO("location_2", "image_2", "extension_2"),
                         ImageDTO("location_3", "image_3", "extension_3")]
    hunt_mock.return_value = hunt_results_mock

    return MagicMock(hunt=hunt_mock)


@pytest.fixture(name="dobryy_sokil_view_mock")
def dobryy_sokil_view_mock_indirect():
    """

    :return: The fixture version of the "dobryy_sokil_view_mock"
    """
    return dobryy_sokil_view_mock()


@pytest.fixture(name="dobryy_sokil_as_mock")
def dobryy_sokil_as_mock_indirect():
    """

    :return: The fixture version of the "dobryy_sokil_as_mock"
    """
    return dobryy_sokil_as_mock()
