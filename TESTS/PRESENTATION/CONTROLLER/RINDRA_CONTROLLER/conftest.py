import pytest
import unittest

from unittest.mock import MagicMock

from BUSINESS.MODEL.DOMAIN_OBJECTS.rindra import Rindra


def rindra_view_mock():
    # Making a Mock of a text inserted by the User
    get_user_input_text_mock = MagicMock()
    get_user_input_text_mock.return_value = "Test_input_text"

    # Mocking the update of the content of the Text Area showed to the user,
    # an actual "Update" should not take place
    update_text_to_show_to_user_mock = MagicMock()

    rindra_view_mock = MagicMock(get_user_input_text=get_user_input_text_mock
                                 , update_text_to_show_to_user=update_text_to_show_to_user_mock)

    return rindra_view_mock


@pytest.fixture(name="rindra_view_mock")
def rindra_view_mock_indirect():
    return rindra_view_mock()


def rindra_sa_mock():

    # Mocking the list of all rindras to be retrieved from the SA
    rindras_mock = []
    rindra_1 = Rindra("Rindra_1")
    rindra_2 = Rindra("Rindra_2")
    rindra_3 = Rindra("Rindra_3")
    rindra_4 = Rindra("Rindra_4")
    rindras_mock.append(rindra_1)
    rindras_mock.append(rindra_2)
    rindras_mock.append(rindra_3)
    rindras_mock.append(rindra_4)
    get_all_rindra_mocks = MagicMock()
    get_all_rindra_mocks.return_value = rindras_mock

    rindra_sa_mock = MagicMock(get_all_rindras=get_all_rindra_mocks)

    return rindra_sa_mock


@pytest.fixture(name="rindra_sa_mock")
def rindra_sa_mock_indirect():
    return rindra_sa_mock()
