import unittest

from unittest.mock import MagicMock, NonCallableMagicMock

from BUSINESS.MODEL.DOMAIN_OBJECTS.rindra import Rindra
from BUSINESS.SERVICES.APPLICATION_SERVICES.rindra_SA import RindraSA


class TestGetAllRindras(unittest.TestCase):

    def test_get_all_rindras(self):
        """
        GIVEN the entire list of Rindras contained in DB
        WHEN the "get_all_rindras" method of the RindraSA is called,
        THEN the entire content of the list from the DB should be retrieved at the SA level
        """
        rindra_sa = RindraSA()

        """"
        Mocking the Rindra DAO used by the SA to be tested
        """
        rindras_from_db_mock = []
        rindra_from_db_1 = Rindra("Rindra_1")
        rindra_from_db_2 = Rindra("Rindra_2")
        rindra_from_db_3 = Rindra("Rindra_3")
        rindra_from_db_4 = Rindra("Rindra_4")
        rindras_from_db_mock.append(rindra_from_db_1)
        rindras_from_db_mock.append(rindra_from_db_2)
        rindras_from_db_mock.append(rindra_from_db_3)
        rindras_from_db_mock.append(rindra_from_db_4)
        get_all_rindra_mocks = MagicMock()
        get_all_rindra_mocks.return_value = rindras_from_db_mock
        rindra_dao_mock = MagicMock(get_all_rindras=get_all_rindra_mocks)
        rindra_sa.set_rindra_dao(rindra_dao_mock)

        """
        Testing retrieving all the Rindras contained in DB
        """
        rindras_retrieved_through_sa = rindra_sa.get_all_rindras()

        """
        The RindraDAO's "get_all_rindras()" method should be called only once with no argument specified, 
        whereas its "add_new_rindra()" method should not be called.
        """
        # verifying if the the method "get_all_rindras()" defined at the RindraDAO level was called
        rindra_dao_mock.get_all_rindras.assert_called()
        # no argument was actually needed for the call
        rindra_dao_mock.get_all_rindras.assert_called_with()
        # the RindraDAO's "add_new_rindra()" method should not be called
        rindra_dao_mock.add_new_rindra.assert_not_called()

        """
        The data integrity corresponding to the elements retrieved from the DAO level
        must be respected when the SA part calls the "get_all_rindras()" method
        """
        # the list retrieved from the DAO shouldn't be Empty or None
        assert (rindras_retrieved_through_sa is not None) \
               & (len(rindras_retrieved_through_sa) > 0)
        # all the Rindra elements inserted inside the mocked list to be returned by the DAO must
        # all be present and conform at the SA level, without any loss of integrity
        assert len(rindras_retrieved_through_sa) == len(rindras_from_db_mock)
        assert (rindras_retrieved_through_sa[0] == rindras_from_db_mock[0]) \
               & (rindras_retrieved_through_sa[1] == rindras_from_db_mock[1]) \
               & (rindras_retrieved_through_sa[2] == rindras_from_db_mock[2]) \
               & (rindras_retrieved_through_sa[3] == rindras_from_db_mock[3])
