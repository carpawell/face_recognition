import cv2 as cv
import numpy as np
import os


def compare_image_hist(path_to_image_1, path_to_image_2, hist_size, method):
    image_1 = cv.imread(path_to_image_1, 0)
    image_2 = cv.imread(path_to_image_2, 0)

    hist_1 = cv.calcHist([image_1], [0], None, [hist_size], (0, 256), accumulate=False)
    hist_2 = cv.calcHist([image_2], [0], None, [hist_size], (0, 256), accumulate=False)

    diff = cv.compareHist(hist_1, hist_2, method=eval("cv." + method))

    return diff
