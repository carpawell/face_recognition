import cv2 as cv
import numpy as np
import os

HIST_SIZE = 256
HIST_METHOD = "HISTCMP_CORREL"

DCT_NORMALIZATION = 256

DFT_NORMALIZATION = 256

NUMBERS_OF_SCALING = 2

GRADIENT_WIDTH = 1
GRADIENT_STEP = 1


def compare_images(path_to_image_1, path_to_image_2, **kwargs):
    image_1 = np.float32(cv.imread(path_to_image_1, 0))
    image_2 = np.float32(cv.imread(path_to_image_2, 0))

    if "method" not in kwargs:
        print("method not found")
        exit()

    if kwargs["method"] == "hist":

        hist_1 = cv.calcHist([image_1], [0], None, [HIST_SIZE], (0, 256), accumulate=False)
        hist_2 = cv.calcHist([image_2], [0], None, [HIST_SIZE], (0, 256), accumulate=False)

        diff = cv.compareHist(hist_1, hist_2, method=eval("cv." + HIST_METHOD))

        return diff

    elif kwargs["method"] == "dct":
        dct_1 = cv.dct(image_1 / DCT_NORMALIZATION)
        dct_2 = cv.dct(image_2 / DCT_NORMALIZATION)

        diff = np.linalg.norm(dct_1 - dct_2)

        return 1 / diff

    elif kwargs["method"] == "dft":
        dft_1 = cv.dft(image_1 / DFT_NORMALIZATION)
        dft_2 = cv.dft(image_2 / DFT_NORMALIZATION)

        diff = np.linalg.norm(dft_1 - dft_2)

        return 1 / diff

    elif kwargs["method"] == "scale":
        for _ in range(NUMBERS_OF_SCALING):
            image_1 = cv.pyrDown(image_1)
            image_2 = cv.pyrDown(image_2)

        diff = np.linalg.norm(image_1 - image_2)

        return 1 / diff

    elif kwargs["method"] == "gradient":
        barcode_1 = get_barcode_from_image(path_to_image_1)
        barcode_2 = get_barcode_from_image(path_to_image_2)

        diff = np.linalg.norm(barcode_1 - barcode_2)

        return 1 / diff


def get_barcode_from_image(path):
    image = np.float32(cv.imread(path, 0))

    rows, _ = map(int, image.shape)
    result = []

    for i in range(0, rows, GRADIENT_STEP):
        if i + 2 * GRADIENT_WIDTH > rows:
            break
        result.append(
            np.linalg.norm(
                image[i : i+GRADIENT_WIDTH] - image[i+GRADIENT_WIDTH : i+(2*GRADIENT_WIDTH)]
            )
        )

    average = sum(result) / len(result)
    result = map(lambda a: 0 if a < average else 1, result)

    return np.fromiter(result, dtype=np.int)


