import numpy as np
import logging
import typing
import matplotlib.pyplot as plt



log = logging.getLogger(__name__)

"""
PlotsUtils
------------------
Class that contains some static methods to help handle and output plots
"""


class PlotsUtils:

    @staticmethod
    def plot_image_heatmap(image: np.ndarray,title: str, xlabel: str, ylabel: str, save: typing.Union[str, None]=None) -> None:
        plt.figure()
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.colorbar()
        plt.imshow(image, cmap='hot', interpolation='nearest')
        if (save != None):
            plt.savefig(save)

