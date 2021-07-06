import os
import logging
import numpy as np

from cell_imaging_utils.plot.plot_utils import PlotUtils
from cell_imaging_utils.image.image_utils import ImageUtils

log = logging.getLogger(__name__)
results_save_dir = "{}\\tests\\results".format(os.getcwd())
images_save_dir = "{}\\tests\\images".format(os.getcwd())

organelle_name = "Nuclear_envelop"
image_file_name_1 = "0_prediction_c0."
image_file_name_2 = "0_signal"
result_fig = "heatmap1.png"
# seg_image_file_name = "image_list_test.csv"

if not os.path.exists(results_save_dir):
    os.makedirs(results_save_dir)

def test_plot_utils() -> None:
    image1 = ImageUtils.imread("{}\\{}".format(images_save_dir,image_file_name_1))
    image2 = ImageUtils.imread("{}\\{}".format(images_save_dir,image_file_name_2))
    # print(ImageUtils.get_channel_names(image))
    image1_ndarray = ImageUtils.normalize(ImageUtils.image_to_ndarray(image1),max_value=1.0,dtype=np.double)
    image2_ndarray = ImageUtils.normalize(ImageUtils.image_to_ndarray(image2),max_value=1.0,dtype=np.double)
    diff_image = image1_ndarray - image2_ndarray
    PlotUtils.plot_image_heatmap(diff_image, organelle_name,"x","y")
    return None


test_plot_utils()