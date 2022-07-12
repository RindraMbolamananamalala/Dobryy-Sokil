# -*- coding: utf-8 -*-


"""
dobryy_sokil_mapper.py: The python file dedicated to the implementation of any need of Objects Mappings
throughout the entire Dobryy Sokil Project
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from mapper.object_mapper import ObjectMapper

from BUSINESS.MODEL.DOMAIN_OBJECTS.image import Image
from BUSINESS.MODEL.DTO.image_DTO import ImageDTO
from BUSINESS.MODEL.DTO.classified_image_DTO import ClassifiedImageDTO

# The Mapper Object to use throughout the whole implementation
mapper = ObjectMapper()

"""
Creating Mappings for:
"""
# Image to ImageDTO
mapper.create_map(Image, ImageDTO)
# Image DTO to Image
mapper.create_map(ImageDTO, Image)
# Classified Image DTO to Image DTO
mapper.create_map(ClassifiedImageDTO, ImageDTO)

def image_to_image_dto(image: Image) -> ImageDTO:
    """

    :param image: The Image Object from which all the values of the concerned properties (every properties here)
    of the Image DTO will be retrieved
    :return: An Image DTO build from the properties of the given Image Object
    """
    image_dto_to_return = mapper.map(image, ImageDTO)
    return image_dto_to_return


def image_dto_to_image(image_dto: ImageDTO) -> Image:
    """

    :param image_dto: The Image DTO from which all the values of the concerned properties of the Image Object
    will be retrieved
    :return: An Image Object build from the properties of the given Image DTO
    """
    image_to_return = mapper.map(image_dto, Image)
    return image_to_return


def classified_image_dto_to_image_dto(classified_image_dto: ClassifiedImageDTO) -> ImageDTO:
    """

    :param classified_image_dto: The Classified Image DTO from which all the values of the concerned properties of the
    classic Image DTO will be retrieved
    :return: An Image DTO build from the properties of the given Classified Image DTO
    """
    image_dto_to_return = mapper.map(classified_image_dto, ImageDTO)
    return image_dto_to_return
