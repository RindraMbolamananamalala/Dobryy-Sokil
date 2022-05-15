from BUSINESS.MODEL.DOMAIN_OBJECTS.rindra import Rindra

from DATA_ACCESS.DAO.rindra_DAO import RindraDAO


class RindraSA:

    def __init__(self):
        self.rindra_DAO = RindraDAO()

    def set_rindra_dao(self, rindra_dao):
        self.rindra_DAO = rindra_dao

    def get_rindra_dao(self):
        return self.rindra_DAO

    def get_all_rindras(self):
        return self.get_rindra_dao().get_all_rindras()

    def add_new_rindra(self, rindra):
        self.get_rindra_dao().add_new_rindra(rindra)
