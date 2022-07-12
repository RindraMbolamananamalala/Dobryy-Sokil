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
    def hunt(self, object_to_search: str, root_folder_path: str) -> list:
        """
        The Dobryy Sokil's M1 Level model representation of an actual hunt of a target prey in a given perimeter
        in the Real World (M0) Level.

        :param object_to_search: the "label" of the object to find, the current Model (M1) Level equivalent of the Real
        World Level (M0) Sokil's prey
        :param root_folder_path: root_folder_path: the "Root" folder's path for the search, the current Model (M1) Level
        equivalent of the Real World Lever (M0) perimeter of search
        :return: The list of Image Objects within the Root Folder that are related to the Object to Search, the current
        Model (M1) Level equivalent of the Real World Level (M0) potential grabbed prey of the Sokil.
        """
        return
