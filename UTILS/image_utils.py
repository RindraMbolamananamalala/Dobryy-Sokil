# -*- coding: utf-8 -*-

"""
image_utils.py: The python file dedicated to any classical image-related functions
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import os


def get_all_images_within_a_folder(folder_path: str) -> [str]:
    """
    Returns the list of the absolute paths of all the image files contained within a given Folder and its Sub-Folders
    :param folder_path: The path of the Root Folder
    :return: the list of the all the absolute paths found
    """
    possible_image_extensions = ["apng", "avif", "gif", "jpg", "jpeg","jfif", "pjpeg", "pjp", "png", "svg", "webp"]
    images_to_return = []
    for folder_element in os.walk(folder_path):
        location_path = folder_element[0].replace("\\", "/")
        for file_element in folder_element[2]:
            if len(file_element.split(".")) > 1:
                # a file, therefore not another sub-folder
                file_name = file_element.split(".")[0]
                file_extension = file_element.split(".")[1]
                if file_extension.lower() in possible_image_extensions:
                    image_absolute_path = location_path + "/" + file_name + "." + file_extension
                    images_to_return.append(image_absolute_path)
    return images_to_return

