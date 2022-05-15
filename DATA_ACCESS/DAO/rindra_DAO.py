from BUSINESS.MODEL.DOMAIN_OBJECTS.rindra import Rindra
from DATA_ACCESS.data_access_base import Data_Access_Base, engine, Session


class RindraDAO:

    def __init__(self):
        # Preparing all the needed setups related to DB access
        self.Data_Access_Base = Data_Access_Base
        self.Data_Access_Base.metadata.create_all(engine)

    def get_all_rindras(self):
        session = Session()
        rindras = session.query(Rindra).all()
        session.expunge_all()
        session.close()
        return rindras

    def get_rindra_by_data(self, data):
        session = Session()
        try:
            rindras = session.query(Rindra).filter(Rindra.data == data).all()
            session.expunge_all()
            session.close()
            return rindras
        except BaseException as error:
            print("error : ", error)

    def add_new_rindra(self, rindra):
        session = Session()
        rindra_to_save = rindra
        session.add(rindra_to_save)
        session.commit()
        session.close()
