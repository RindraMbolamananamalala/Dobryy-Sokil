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

from CONFIGURATIONS.logger import LOGGER


def image_file_path_to_image_domain_object(image_file_path: str) -> Image:
    """
    Converts an image's file path into an image DO.

    :param image_file_path: The file path of the image to be converted
    :return: The image DO obtained from the given file path of the image
    """
    if image_file_path is not None and len(image_file_path) > 0:
        try:
            raw_file_name = image_file_path.split("/")[len(image_file_path.split("/")) - 1]
            location_path = image_file_path.replace(("/" + raw_file_name), "")
            file_name = raw_file_name.split(".")[0]
            file_extension = raw_file_name.split(".")[1]
            image_to_return = Image(location_path, file_name, file_extension)
            LOGGER.info(image_file_path + " successfully converted  to " + str(image_to_return))
            return image_to_return
        except Exception as exception:
            # At least one error has occurred, therefore, stop the conversion process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Impossible conversion of the Image File Path : \""
                + image_file_path + "\"."
            )
            raise
    else:
        # A None or Blank file path was provided, therefore, a "None" is returned
        LOGGER.info("A None or Blank file path was provided.")
        return None


def image_file_paths_to_image_domain_objects(image_file_paths: [str]) -> [Image]:
    """
    Converts a list of images' file paths into a list of image DOs.

    :param image_file_paths: The list of file paths of images to be converted
    :return: A list of image DOs obtained from the given list of file paths of each image that it contains
    """
    if image_file_paths is not None and len(image_file_paths) > 0:
        try:
            images_to_return = []
            for image_file_path in image_file_paths:
                images_to_return.append(image_file_path_to_image_domain_object(image_file_path))
            LOGGER.info(str(image_file_paths) + " successfully converted to " + str(images_to_return))
            return images_to_return
        except Exception as exception:
            # At least one error has occurred, therefore, stop the conversion process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Impossible conversion of the list of Image File Paths : \""
                + str(image_file_paths) + "\"."
            )
            raise
    else:
        # A None or Void list of file paths was provided, therefore, a void list is returned
        LOGGER.info("A None or Void file paths list was provided.")
        return []

