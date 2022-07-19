# -*- coding: utf-8 -*-

"""
test_event_button_launch_research_clicked.py: The python file dedicated to the Integration Testing of the
"PRESENTATION.CONTROLLER.dobrry_sokil_controller.DobrrySokilController.event_button_launch_research_clicked()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import warnings
import unittest

from PRESENTATION.CONTROLLER.dobrry_sokil_controller import DobrrySokilController

from BUSINESS.SERVICES.APPLICATION_SERVICES.DOBRYY_SOKIL_AS.DOBRYY_SOKIL_AS_IMPL.dobryy_sokil_AS_impl \
    import DobryySokilASImpl

from TESTS.INTEGRATION_TESTS.PRESENTATION.CONTROLLER.DOBRYY_SOKIL_CONTROLLER.conftest import dobryy_sokil_view_mocks


def ignore_resource_warnings(test_func):
    """
    Not showing as part of the Logs the Warning message related to the "ResourceWarning"
    """

    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)

    return do_test


class TestEventButtonLaunchResearchClicked(unittest.TestCase):
    """
    Do not show the resource warning messages related to the specific reading processes managed by TextBlob
    """

    @ignore_resource_warnings
    def test_event_button_launch_research_clicked(self):
        """
        GIVEN the label of the object of search and the ROOT folder for the same search provided by the User on the
        dedicated HMI and retrieved via the VIEW part,
        WHEN "Launch Research" button is clicked by the latter,
        THEN a valid List of information of Images actually contained within the ROOT folder and related
        to the label of the object of search should be loaded via the same initial VIEW part over the dedicated HMI
        """

        # Preparing the useful mocks (VIEW mocks) and Application Service (Dobryy Sokil AS) for the test,
        dobryy_sokil_view_mocks_to_use = dobryy_sokil_view_mocks()
        dobryy_sokil_as_to_use = DobryySokilASImpl()
        dobryy_sokil_controller = DobrrySokilController()
        # Only one instance of Dobryy Sokil AS (a real one instead of a Mock) will be used throughout the
        # entire Controller to test
        dobryy_sokil_controller.set_dobryy_sokil_as(dobryy_sokil_as_to_use)

        # Actual Testings with all the different VIEW Mocks
        for dobryy_sokil_view_mock_to_use in dobryy_sokil_view_mocks_to_use:
            # Selection pf the VIEW mock to be currently used
            dobryy_sokil_controller.set_dobryy_sokil_view(dobryy_sokil_view_mock_to_use)

            if isinstance(dobryy_sokil_view_mock_to_use.get_expected_images_information_to_be_displayed(),
                          BaseException):
                # Managing the particular case of the fact of expecting the action of raising a specific Exception
                # instead of an action of loading some information on the HMI via the VIEW due to the presence of
                # at least one internal error inside the Controller
                self.assertRaises(type(dobryy_sokil_view_mock_to_use.get_expected_images_information_to_be_displayed())
                                  , dobryy_sokil_controller.event_button_launch_research_clicked)
            else:
                # Assuming that no Controller's internal error has occurred, let's verify the validity of
                # the information to load on the HMI via the VIEW
                dobryy_sokil_controller.event_button_launch_research_clicked()
                dobryy_sokil_view_mock_to_use.load_images_information_results.assert_called()
                dobryy_sokil_view_mock_to_use.load_images_information_results.assert_called_once()
                # Verifying that the expected Arguments are the called ones in function of the situation
                assert dobryy_sokil_view_mock_to_use.load_images_information_results.call_args[0][0] \
                       == dobryy_sokil_view_mock_to_use.get_expected_images_information_to_be_displayed()
