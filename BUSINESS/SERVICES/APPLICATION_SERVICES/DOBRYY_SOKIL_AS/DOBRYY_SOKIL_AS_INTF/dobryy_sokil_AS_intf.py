# -*- coding: utf-8 -*-

"""
dobryy_sokil_AS_intf.py: The python file dedicated to the Abstract Base Class of the Dobryy Sokil Application
Service part dedicated to any implementation of action obtained with the Modeling process of a Real World "smart"
Sokil (The Ukrainian world for Falcon)
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from abc import ABC, abstractmethod


class DobryySokilASIntf(ABC):

    @abstractmethod
    def hunt(self):
        """

        :return:
        """
        return
