from sqlalchemy import Column, Integer, String

from DATA_ACCESS.data_access_base import Data_Access_Base


class Rindra(Data_Access_Base):
    __tablename__ = 'rindra'

    id = Column(Integer, primary_key=True)
    data = Column(String(60))

    def get_data(self):
        return self.data

    def __init__(self, data):
        self.data = data
