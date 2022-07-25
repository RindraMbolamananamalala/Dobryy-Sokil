# -*- coding: utf-8 -*-

"""
conftest.py: The python file dedicated to any configurations related to the Integration Testing of the
"PRESENTATION.CONTROLLER.dobrry_sokil_controller.DobrrySokilController.event_button_launch_research_clicked()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import os

import pytest
from unittest.mock import MagicMock


def dobryy_sokil_view_mock(user_input_provided: str
                           , root_folder_path_provided: str
                           , expected_images_information_to_be_displayed: object):
    """

    :param user_input_provided: The label of the object to search provided by the User
    :param root_folder_path_provided: The Root Folder path for the search provided by the User
    :param expected_images_information_to_be_displayed: The argument expected to be received by the VIEW part in
    function of the two User's input when it comes to loading the information found on the HMI part
    :return: A VIEW Mock established in function of the combination of the User's inputs and the corresponding
    expected outcome at the level of the VIEW part
    """
    get_root_folder_path_mock = MagicMock()
    get_root_folder_path_mock.return_value = root_folder_path_provided
    get_user_input_mock = MagicMock()
    get_user_input_mock.return_value = user_input_provided
    load_images_information_results = MagicMock()
    get_expected_images_information_to_be_displayed = MagicMock()
    get_expected_images_information_to_be_displayed.return_value = expected_images_information_to_be_displayed

    return MagicMock(get_root_folder_path=get_root_folder_path_mock
                     , get_user_input=get_user_input_mock
                     , get_expected_images_information_to_be_displayed=get_expected_images_information_to_be_displayed
                     , load_images_information_results=load_images_information_results)


def dobryy_sokil_view_mocks() -> list:
    """

    :return: A list of already pre-configured Mocks of the Dobryy Sokil VIEW for Integration Tests
    """

    # First, let's get the path leading to the Image Resources especially dedicated to any need of Image
    # classification during Integration Testings
    test_resources_folder_path = os.getcwd().split("Добрый_Сокол")[0] \
                                 + "Добрый_Сокол" \
                                 + "/TESTS/INTEGRATION_TESTS/RESOURCES"
    test_image_resources = test_resources_folder_path.replace("\\", "/") \
                           + "/IMAGE"

    """
    Verifying that a Non-valid information provided by the User will Result to
    the action of Raising the adequate exception, and that no information on any
    Image will be sent to the HMI via the VIEW
    """
    view_mock_1 = dobryy_sokil_view_mock(None, None, TypeError())
    view_mock_2 = dobryy_sokil_view_mock("User_input", None, TypeError())
    view_mock_3 = dobryy_sokil_view_mock(None, "Root_Folder", TypeError())
    view_mock_4 = dobryy_sokil_view_mock("", "", TypeError())
    view_mock_5 = dobryy_sokil_view_mock("User_Input", "", TypeError())
    view_mock_6 = dobryy_sokil_view_mock("", "Root_Folder", TypeError())

    """
    Verifying that if the information provided by the User are all "valid", then a corresponding valid list of
    Information on Images found must be sent to the HMI via the VIEW
    """
    # Meaningless Object's label and|or Meaningless Root Folder path
    view_mock_7 = dobryy_sokil_view_mock("meaningless_label", "meaningless_root_folder_path", [])
    view_mock_8 = dobryy_sokil_view_mock("timber wolf", "meaningless_root_folder_path", [])
    view_mock_9 = dobryy_sokil_view_mock("meaningless_label", test_image_resources, [])

    # Simulating a Real User inserting the label "Timber Wolf" : An actual image file named "Wolf.JPG" containing
    # a "Timber Wolf" exists within the Folder dedicated to the Images to be used during the Testings
    timber_wolf_structured_image_information = {
        "name": "Wolf",
        "extension": "JPG",
        "absolute_path": test_image_resources + "/" + "Wolf.JPG"
    }
    timber_wolf_structured_images_information = [timber_wolf_structured_image_information]
    view_mock_10 = dobryy_sokil_view_mock("Timber_Wolf"
                                          , test_image_resources
                                          , timber_wolf_structured_images_information)
    view_mock_11 = dobryy_sokil_view_mock("timber wolf"
                                          , test_image_resources
                                          , timber_wolf_structured_images_information)
    view_mock_12 = dobryy_sokil_view_mock("timber_wolf"
                                          , test_image_resources
                                          , timber_wolf_structured_images_information)

    # Simulating a Real User inserting the label "Soccer Ball" : Two actual image files respectively named "Ball.JPG"
    # and "Football.JPG", both containing a "Soccer Ball", exist within the Folder dedicated to the Images to be used
    # during the Testings
    soccer_ball_structured_image_information_1 = {
        "name": "Ball",
        "extension": "JPG",
        "absolute_path": test_image_resources + "/" + "Ball.JPG"
    }
    soccer_ball_structured_image_information_2 = {
        "name": "Football",
        "extension": "JPG",
        "absolute_path": test_image_resources + "/" + "Football.JPG"
    }
    soccer_ball_structured_images_information = [soccer_ball_structured_image_information_1
        , soccer_ball_structured_image_information_2]
    view_mock_13 = dobryy_sokil_view_mock("Soccer Ball"
                                          , test_image_resources
                                          , soccer_ball_structured_images_information)

    # Simulating a Real User inserting (successively) the labels "Banana" and "Orange" : One actual image file named
    # "FruitsBowl.JPG" containing a "Banana" and some "Orange"s , exist within the Folder dedicated to the Images to *
    # be used during the Testings
    fruits_bowl_structured_image_information = {
        "name": "FruitsBowl",
        "extension": "jpg",
        "absolute_path": test_image_resources + "/" + "FruitsBowl.jpg"
    }
    fruits_bowl_structured_images_information = [fruits_bowl_structured_image_information]
    view_mock_14 = dobryy_sokil_view_mock("Banana"
                                          , test_image_resources
                                          , fruits_bowl_structured_images_information)
    view_mock_15 = dobryy_sokil_view_mock("Orange"
                                          , test_image_resources
                                          , fruits_bowl_structured_images_information)

    # Simulating a Real User inserting (successively) the labels "Bread" and "Snow" : No image file containing one
    # of those objects exists within the Folder dedicated to the Images to be used during the Testings
    view_mock_16 = dobryy_sokil_view_mock("Bread"
                                          , test_image_resources
                                          , [])
    view_mock_17 = dobryy_sokil_view_mock("Snow"
                                          , test_image_resources
                                          , [])

    view_mocks_to_return = [view_mock_1
        , view_mock_2
        , view_mock_3
        , view_mock_4
        , view_mock_5
        , view_mock_6
        , view_mock_7
        , view_mock_8
        , view_mock_9
        , view_mock_10
        , view_mock_11
        , view_mock_12
        , view_mock_13
        , view_mock_14
        , view_mock_15
        , view_mock_16
        , view_mock_17]

    return view_mocks_to_return


@pytest.fixture(name="dobryy_sokil_view_mocks")
def dobryy_sokil_view_mocks_indirect():
    """

    :return: The fixture version of the "dobryy_sokil_view_mocks"
    """
    return dobryy_sokil_view_mocks()
