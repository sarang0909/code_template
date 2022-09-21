"""A Predictor module to load models and get their predictions.

"""
import pickle
from src.utility.utils import config
from src.utility import constants
from src.utility.loggers import logger


class Predictor:
    """
    This is a class for model load and prediction methods.

    Attributes:
        model : The binary model file
    """

    model = None

    @classmethod
    def get_model(cls):
        """
        The function to load model file in memory.

        Returns:
            model : A model file
        """

        if cls.model is None:
            with open(config.get(constants.MODEL_FILE), "rb") as model_file:
                cls.model = pickle.load(model_file)

        return cls.model

    @classmethod
    def get_model_output(cls, input_data):
        """A method to get model inference

        Args:
            input_data (str): input to model

        Returns:
            str : Output string with model prediction
        """

        # return cls.get_model().predict(input)
        logger.info("Output is generated")
        return "This is dummy model output for input:" + input_data
