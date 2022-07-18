import unittest

import pytest

from PRESENTATION.CONTROLLER.rindra_controller import RindraController

from TESTS.UNIT_TESTS.PRESENTATION.CONTROLLER.RINDRA_CONTROLLER.conftest import rindra_view_mock, rindra_sa_mock


@pytest.mark.usefixtures("rindra_view_mock")
class TestButtonAddClicked(unittest.TestCase):

    def test_button_add_clicked(self):
        """
        GIVEN a text provided by the User inside the input Text area
        WHEN "Add" button is clicked by the latter
        THEN the whole content of this input text must be stored by the app in the form
        of a Rindra object
        """
        # preparing the useful mocks for the test, respectively for the "View" and "SA" parts
        rindra_view_mock_to_use = rindra_view_mock()
        rindra_sa_mock_to_use = rindra_sa_mock()
        rindra_controller = RindraController(rindra_view_mock_to_use)
        rindra_controller.set_rindra_sa(rindra_sa_mock_to_use)

        # launching the actual test
        rindra_controller.event_button_add_clicked()

        """
        Verifying that the the text provided by the User is correctly retrieved 
        by the "View" part
        """
        rindra_view_mock_to_use.get_user_input_text.assert_called()
        rindra_view_mock_to_use.get_user_input_text.assert_called_once()
        rindra_view_mock_to_use.get_user_input_text() is not None

        """
        Verifying that the whole text provided by the User has been correctly sent
        to the SA part, before correctly storing it
        """
        rindra_sa_mock_to_use.add_new_rindra.assert_called()
        rindra_sa_mock_to_use.add_new_rindra.assert_called_once()
        assert rindra_sa_mock_to_use.add_new_rindra.call_args[0][0] is not None
        assert rindra_sa_mock_to_use.add_new_rindra.call_args[0][0].get_data() \
               == rindra_view_mock_to_use.get_user_input_text()

        """
        Verifying that the content of the Text Area showed to the user have been correctly 
        and successfully cleared after the series of operations related to the storage of a new Rindra
        """
        rindra_view_mock_to_use.update_text_to_show_to_user.assert_called()
        rindra_view_mock_to_use.update_text_to_show_to_user.assert_called_once()
        rindra_view_mock_to_use.update_text_to_show_to_user.assert_called_with('')
