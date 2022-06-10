# -*- coding: utf-8 -*-

"""
image_converter.py: The python file dedicated to any image-related conversion functions
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from BUSINESS.MODEL.DOMAIN_OBJECTS.image import Image


def image_file_path_to_image_domain_object(image_file_path: str):
    """
    Converts an image's file path into an image DO.

    :param image_file_path: The file path of the image to be converted
    :return: the image DO obtained from the given file path of the image
    """
    raw_file_name = image_file_path.split("/")[len(image_file_path.split("/")) - 1]
    location_path = image_file_path.replace(("/" + raw_file_name), "")
    file_name = raw_file_name.split(".")[0]
    file_extension = raw_file_name.split(".")[1]
    return Image(location_path, file_name, file_extension)


def image_file_paths_to_image_domain_objects(image_file_paths: [str]):
    """
    Converts a list of images' file paths into a list of image DOs.

    :param image_file_paths: The list of file paths of images to be converted
    :return: a list of image DOs obtained from the given list of file paths of each image that it contains
    """
    images_to_return = []
    for image_file_path in image_file_paths:
        images_to_return.append(image_file_path_to_image_domain_object(image_file_path))
    return images_to_return

