import unittest


from unittest.mock import MagicMock, NonCallableMagicMock

from BUSINESS.MODEL.DOMAIN_OBJECTS.rindra import Rindra
from BUSINESS.SERVICES.APPLICATION_SERVICES.rindra_SA import RindraSA


class TestAddNewRindra(unittest.TestCase):

    def test_add_new_rindra(self):
        """
        GIVEN a valid Rindra with valid data,
        WHEN the add_new_rindra method of the RindraSA is called,
        THEN a new Rindra must exist in the database with the same attributes.
        """
        rindra_test = Rindra("LOL 8")
        rindra_sa = RindraSA()

        """"
        Mocking the Rindra DAO used by the SA to be tested
        """
        rindra_dao_mock = MagicMock()
        rindra_sa.set_rindra_dao(rindra_dao_mock)

        """
        Testing adding a New Rindra
        """
        rindra_sa.add_new_rindra(rindra_test)

        """
        the "add_new_rindra()" in the DAO only called once, with the correct
        new Rindra object in argument
        """
        rindra_dao_mock.add_new_rindra.assert_called()
        rindra_dao_mock.add_new_rindra.assert_called_once()
        # verifying the integrity of the data transmitted between the SA and DAO layers
        rindra_dao_mock.add_new_rindra.assert_called_with(rindra_test)

        """
        the method "get_all_rindras()" of the DAO should never be called
        when we add a new Rindra object from the level of the SA
        """
        rindra_dao_mock.get_all_rindras.assert_not_called()




