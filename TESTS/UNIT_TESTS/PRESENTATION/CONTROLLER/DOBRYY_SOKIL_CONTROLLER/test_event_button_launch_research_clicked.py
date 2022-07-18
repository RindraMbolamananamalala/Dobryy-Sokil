# -*- coding: utf-8 -*-

"""
test_event_button_launch_research_clicked.py: The python file dedicated to the Unit Testing of the
"PRESENTATION.CONTROLLER.dobrry_sokil_controller.DobrrySokilController.event_button_launch_research_clicked()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import unittest

from PRESENTATION.CONTROLLER.dobrry_sokil_controller import DobrrySokilController

from TESTS.UNIT_TESTS.PRESENTATION.CONTROLLER.DOBRYY_SOKIL_CONTROLLER.conftest import dobryy_sokil_view_mock \
    , dobryy_sokil_as_mock


class TestEventButtonLaunchResearchClicked(unittest.TestCase):

    def test_event_button_launch_research_clicked(self):
        """
        GIVEN the label of the object of search and the ROOT folder for the same search provided by the User on the
        dedicated HMI and retrieved via the VIEW part,
        WHEN "Launch Research" button is clicked by the latter,
        THEN a valid List of information of Images actually contained within the ROOT folder and related
        to the label of the object of search should be loaded via the same initial VIEW part over the dedicated HMI
        """

        # preparing the useful mocks for the test, respectively for the "View" and "AS" parts
        dobryy_sokil_view_mock_to_use = dobryy_sokil_view_mock()
        dobryy_sokil_as_mock_to_use = dobryy_sokil_as_mock()
        dobryy_sokil_controller = DobrrySokilController()
        dobryy_sokil_controller.set_dobryy_sokil_view(dobryy_sokil_view_mock_to_use)
        dobryy_sokil_controller.set_dobryy_sokil_as(dobryy_sokil_as_mock_to_use)

        # launching the actual test
        dobryy_sokil_controller.event_button_launch_research_clicked()

        """
        Verifying that the Label of the object to search and the Root Folder for the search provided by the User 
        is correctly retrieved by the "View" part
        """
        # The label of the object to search
        dobryy_sokil_view_mock_to_use.get_user_input.assert_called()
        dobryy_sokil_view_mock_to_use.get_user_input.assert_called_once()
        # The Root Folder fro the search
        dobryy_sokil_view_mock_to_use.get_root_folder_path.assert_called()
        dobryy_sokil_view_mock_to_use.get_root_folder_path.assert_called_once()

        """
        Verifying that "hunt()" method of the Dobryy Sokil AS is correctly called and used by the current Controller
        """
        dobryy_sokil_as_mock_to_use.hunt.assert_called()
        dobryy_sokil_as_mock_to_use.hunt.assert_called_once()
        # The first argument must be the Label of the Object to search
        assert (dobryy_sokil_as_mock_to_use.hunt.call_args[0][0] is not None) \
               and (dobryy_sokil_as_mock_to_use.hunt.call_args[0][0] == dobryy_sokil_view_mock_to_use.get_user_input())
        # The second argument must be the Root Folder for the search
        assert dobryy_sokil_as_mock_to_use.hunt.call_args[0][1] is not None \
               and (dobryy_sokil_as_mock_to_use.hunt.call_args[0][1]
                    == dobryy_sokil_view_mock_to_use.get_root_folder_path())

        """
        Verifying that after a correct and successful use of "hunt()" method of the Dobryy Sokil AS, 
        the corresponding results are correctly loaded for a specific "Presentation" via the VIEW part
        """
        dobryy_sokil_view_mock_to_use.load_images_information_results.assert_called()
        # The results of the "Hunt" must be correctly formatted before the Loading process handled by the VIEW part
        expected_images_information_results_to_be_load_by_the_view = []
        for i in range(len(dobryy_sokil_as_mock_to_use.hunt())):
            expected_images_information_results_to_be_load_by_the_view.append({
                "name": dobryy_sokil_as_mock_to_use.hunt()[i].get_name(),
                "extension": dobryy_sokil_as_mock_to_use.hunt()[i].get_extension(),
                "absolute_path": dobryy_sokil_as_mock_to_use.hunt()[i].get_absolute_path()
            })
        dobryy_sokil_view_mock_to_use.load_images_information_results.assert_called()
        # The information to be loaded have to be the formatted version of the information returned by the "Hunt"
        assert dobryy_sokil_view_mock_to_use.load_images_information_results.call_args[0][0] is not None \
               and (dobryy_sokil_view_mock_to_use.load_images_information_results.call_args[0][0]
                    == expected_images_information_results_to_be_load_by_the_view)
