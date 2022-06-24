# -*- coding: utf-8 -*-

"""
dobryy_sokil.py: The python file dedicated to the super class of all the Project's Domain Objects (DOs)
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"


class DobryySokilDO:

    def __str__(self) -> str:
        """

        :return:  a structure in which all DO's attributes are presented besides their respective value(s)
        """
        return str(vars(self))
