from signs import *
import numpy as np
import cv2 as cv

methods = ["gradient", "hist", "dft", "dct", "scale"]

for method in methods:
    search(method)
