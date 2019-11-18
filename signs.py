import os
from utils import *

PATH = os.getcwd()


def search(method):
    fail = 0
    success = 0

    images = next(os.walk(f"{PATH}/ATT_run/test"))[2]

    for image in images:
        result = []

        persons = next(os.walk("./ATT_run/"))[1]
        for person in persons:
            if person == "test":
                continue

            standarts = next(os.walk(f"./ATT_run/{person}"))[2]
            for standart in standarts:
                result.append(
                    {
                        "score": compare_images(f"{PATH}/ATT_run/test/{image}",
                                                f"{PATH}/ATT_run/{person}/{standart}",
                                                method=method),
                        "answer": person,
                    }
                )

        result.sort(key=lambda a: a["score"], reverse=True)
        answer = result[0]["answer"]

        if image.split("_")[0] == answer:
            success += 1
        else:
            fail += 1

    print(f"method: {method}")
    print(f"fail: {fail}")
    print(f"success: {success}")
    print(f"percentage of success: {success / (fail + success) * 100}")
