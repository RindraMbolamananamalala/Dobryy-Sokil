# -*- coding: utf-8 -*-

"""
dobryy_sokil_DTO.py: The python file dedicated to the super class of all the Project's Data Transfer Objects (DTOs)
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"


class DobryySokilDTO:

    def __str__(self) -> str:
        """

        :return:  a structure in which all DTO's attributes are presented besides their respective value(s)
        """
        return str(vars(self))
