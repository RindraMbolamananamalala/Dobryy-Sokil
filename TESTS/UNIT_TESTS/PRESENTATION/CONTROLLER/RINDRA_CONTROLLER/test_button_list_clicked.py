import unittest

import pytest

from PRESENTATION.CONTROLLER.rindra_controller import RindraController

from TESTS.UNIT_TESTS.PRESENTATION.CONTROLLER.RINDRA_CONTROLLER.conftest import rindra_view_mock, rindra_sa_mock


@pytest.mark.usefixtures("rindra_view_mock")
class TestButtonAddClicked(unittest.TestCase):

    def test_button_list_clicked(self):
        """
        GIVEN the entire information on Rindras contained in the DB
        WHEN "List" button is clicked by the User
        THEN tall of these information should be correctly retrieved and then showed in the Text Area
        """
        # preparing the useful mocks for the test, respectively for the "View" and "SA" parts
        rindra_view_mock_to_use = rindra_view_mock()
        rindra_sa_mock_to_use = rindra_sa_mock()
        rindra_controller = RindraController(rindra_view_mock_to_use)
        rindra_controller.set_rindra_sa(rindra_sa_mock_to_use)

        # launching the actual test
        rindra_controller.event_button_list_clicked()

        """
        The RindraDAO's "get_all_rindras()" method should be called only once with no argument specified, 
        whereas its "add_new_rindra()" method should not be called.
        """
        # verifying if the the method "get_all_rindras()" defined at the RindraSA level was called
        rindra_sa_mock_to_use.get_all_rindras.assert_called()
        # no argument was actually needed for the call
        rindra_sa_mock_to_use.get_all_rindras.assert_called_with()
        # the RindraSA's "add_new_rindra()" method should not be called
        rindra_sa_mock_to_use.add_new_rindra.assert_not_called()

        """
        The data integrity corresponding to the elements retrieved from the SA level
        must be respected when the Controller part calls the "get_all_rindras()" method
        and should be verifiable at the Level of the Text area the show to the User
        """
        rindras_to_retrieve_through_sa = rindra_sa_mock().get_all_rindras()
        rindras_to_retrieve_through_sa_string = "\n" \
            .join([str(line.get_data()) for line in rindras_to_retrieve_through_sa])
        # Verifying that the text correctly sent to the Text area also matches the elements retrieved from the
        # SA level
        rindra_view_mock_to_use.update_text_to_show_to_user.assert_called()
        rindra_view_mock_to_use.update_text_to_show_to_user.assert_called_once()
        rindra_view_mock_to_use.update_text_to_show_to_user.assert_called_with(rindras_to_retrieve_through_sa_string)

