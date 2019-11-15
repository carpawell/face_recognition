import cv2 as cv
import numpy as np
import os
from utils import *

PATH = os.getcwd()

HIST_SIZE = 256
HIST_METHOD = "HISTCMP_CORREL"


def hist():
    fail = 0
    success = 0
    images = next(os.walk(f"{PATH}/ATT/test"))[2]
    for image in images:
        result = []

        persons = next(os.walk("./ATT/"))[1]
        for person in persons:
            if person == "test":
                continue

            standarts = next(os.walk(f"./ATT/{person}"))[2]
            for standart in standarts:
                result.append(
                    {
                        "score": compare_image_hist(f"{PATH}/ATT/test/{image}",
                                                    f"{PATH}/ATT/{person}/{standart}",
                                                    HIST_SIZE,
                                                    HIST_METHOD),
                        "answer": person,
                    }
                )

        result.sort(key=lambda a: a["score"], reverse=True)
        answer = result[0]["answer"]

        if image.split("_")[0] == answer:
            success += 1
        else:
            fail += 1

    print(fail)
    print(success)
