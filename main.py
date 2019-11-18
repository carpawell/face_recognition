from signs import *
import numpy as np
import cv2 as cv

from sorting import set_num_of_standarts

methods = ["hist", "dft", "dct", "scale", "gradient"]

set_num_of_standarts(4)

for method in methods:
    search(method)
