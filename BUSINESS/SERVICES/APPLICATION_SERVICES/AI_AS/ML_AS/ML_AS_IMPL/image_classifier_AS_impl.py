# -*- coding: utf-8 -*-

"""
image_classifier_AS_impl.py: The python file dedicated to the Implementation Class of the Deep Learning Application
Service part dedicated to the prediction of the probable Labels of Images.
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

from CONFIGURATIONS.logger import LOGGER
from BUSINESS.MODEL.DOMAIN_OBJECTS.image import Image
from BUSINESS.MODEL.DTO.classified_image_DTO import ClassifiedImageDTO
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.ML_AS.ML_AS_INTF.image_classifier_AS_intf import ImageClassifierASIntf

"""
Still considered as one of the most excellent vision model architecture till date, the
VGG16 convolution neural net (CNN) Architecture has been the chosen one here
for the implementation of our Deep Learning model for the classification of 
images.
"""
dl_model = VGG16()


def preprocess_image(pil_image):
    """
    Preprocessing a PIL image, by converting it from pixels matrix to Numpy array.

    :param pil_image: The PIL Image to be preprocessed
    :return: The Numpy array version of the given PIL Image
    """
    if pil_image:
        # a not None PIL Image was provided
        try:
            array_image = img_to_array(pil_image)

            # re-dimensioning process
            array_image = array_image.reshape(1
                                              , array_image.shape[0]
                                              , array_image.shape[1]
                                              , array_image.shape[2])

            # actual pre-processing process
            array_image = preprocess_input(array_image)
        except Exception as exception:
            # At least one error has occurred, therefore the reduction process couldn't happen
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Impossible Preprocessing of the Image: \""
                + str(pil_image) + "\"."
            )
            raise

        return array_image
    else:
        # A None PIL image was provided
        LOGGER.info("No PIL image for the Preprocessing was provided")
        return None


def predict_image_label(pil_image) -> [str]:
    """
    Predicting the set of possible "labels" corresponding to a given Image.

    :param pil_image: The PIL image whose list of possible "labels" is to be predicted by the Model
    :return: The list of possible "labels" predicted by the Model
    """
    if pil_image:
        try:
            # A not None PIL Image was provided
            probable_labels = []

            # First, let's preprocess the given PIL Image
            image_preprocessed = preprocess_image(pil_image)

            # Actual Prediction process, collecting the results obtained on the Y-axis
            y_prediction = dl_model.predict(image_preprocessed)

            # Converting Probabilities into Class Labels
            model_prediction = decode_predictions(y_prediction)

            # Saving the 5 most probable labels for the image
            most_probable_5_labels = model_prediction[0]

            for label in most_probable_5_labels:
                label_value = label[1]
                label_probability = label[2]
                # retaining only the labels corresponding to a significant probability (10 % and more here)
                # , deserving a consideration
                if label_probability >= 0.10:
                    probable_labels.append(label_value)

            return probable_labels
        except Exception as exception:
            # At least one error has occurred, therefore the reduction process couldn't happen
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Impossible Classification of the Image : \""
                + str(pil_image) + "\"."
            )
            raise
    else:
        # A None PIL Image was provided
        LOGGER.info("No PIL image for the Prediction pf labels was provided")
        return None


class ImageClassifierASImpl(ImageClassifierASIntf):

    def predict(self, images: [Image]) -> [ClassifiedImageDTO]:
        """
        Classifying (predicting their probable labels) a list of Images provided in parameters.

        :param images: The list of Images to be classified
        :return: A list of Image DTOs with their "predicted labels" list fed by labels predicted by a
        dedicated DL Model (based on a VGG16 Architecture here) from the list of Images provided within
        the parameters.
        """
        if images:
            try:
                # A non-empty list of Images was provided
                classified_images = []
                for image in images:
                    classified_image = ClassifiedImageDTO()
                    classified_image.set_name(image.get_name())
                    classified_image.set_location_path(image.get_location_path())
                    classified_image.set_extension(image.get_extension())
                    for label in predict_image_label(
                            load_img(classified_image.get_absolute_path()
                                , target_size=(224, 224))
                    ):
                        classified_image.get_predicted_labels().append(label)
                    LOGGER.info(
                        "Image: "
                        + "\"" + str(image) + "\""
                        + " probable labels successfully predicted, results : "
                          "\"" + str(classified_image) + "\""
                    )
                    classified_images.append(classified_image)
                LOGGER.info(
                    "Images : "
                    + "\"" + str(images) + "\""
                    + " probable labels successfully predicted, results : "
                      "\"" + str(classified_images) + "\""
                )
                return classified_images
            except Exception as exception:
                # At least one error has occurred, therefore the reduction process couldn't happen
                LOGGER.error(
                    exception.__class__.__name__ + ": " + str(exception)
                    + ". Impossible Classification of the list of Images : \""
                    + str(images) + "\"."
                )
                raise
        else:
            # An empty list of Images was provided
            LOGGER.info("No Images was provided for the Classification")
            # so, let's return an Empty List
            return []
