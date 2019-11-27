import os
from utils import *
import matplotlib.pyplot as plt

PATH = os.getcwd()

WAIT_TIME = 1

methods = ["hist", "dft", "dct", "scale", "gradient"]

method_weight = {
    "hist": 0.3,
    "dft": 0.15,
    "dct": 0.15,
    "scale": 0.3,
    "gradient": 0.1
}


def search(method, **kwargs):
    fail = 0
    success = 0
    num_of_test = []
    percentage = []

    images = next(os.walk(f"{PATH}/ATT_run/test"))[2]

    if kwargs.get("visualize"):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        graph, = ax.plot([], [])
        ax.set_xlim([0, len(images)])
        ax.set_ylim([0, 105])
        plt.xlabel('Number of tests')
        plt.ylabel('Percentage of success')
        plt.title(f'Method: {method.upper()}')
        plt.ion()
        plt.show()

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

        num_of_test.append(success + fail)
        percentage.append(success / (fail + success) * 100)

        if kwargs.get("visualize"):
            graph.set_data(num_of_test, percentage)
            plt.pause(WAIT_TIME)

    print(f"method: {method}")
    print(f"fail: {fail}")
    print(f"success: {success}")
    print(f"percentage of success: {success / (fail + success) * 100}\n")


def search_optimal(visualize, show_images):
    fail = 0
    success = 0
    num_of_test = []
    percentage = []

    images = next(os.walk(f"{PATH}/ATT_run/test"))[2]

    if visualize:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        graph, = ax.plot([], [])
        ax.set_xlim([0, len(images)])
        ax.set_ylim([0, 105])
        plt.xlabel('Number of tests')
        plt.ylabel('Percentage of success')
        plt.title('Optimal method')
        plt.ion()
        fig.canvas.manager.window.move(650, 400)
        plt.show()

    if show_images:
        cv.namedWindow("TEST IMAGE", cv.WINDOW_NORMAL)
        cv.moveWindow("TEST IMAGE", 0, 0)
        cv.resizeWindow("TEST IMAGE", 300, 300)

        for idx, method in enumerate(methods):
            cv.namedWindow(f"{method.upper()} ANSWER", cv.WINDOW_NORMAL)
            cv.resizeWindow(f"{method.upper()} ANSWER", 300, 300)
            cv.moveWindow(f"{method.upper()} ANSWER", (idx + 1) * 300 + 150, 0)

    for image in images:
        if show_images:
            test_img = cv.imread(f"{PATH}/ATT_run/test/{image}")
            cv.imshow("TEST IMAGE", test_img)
        result = {}

        for method in methods:
            internal_result = []
            persons = next(os.walk("./ATT_run/"))[1]
            for person in persons:
                if person == "test":
                    continue

                standarts = next(os.walk(f"./ATT_run/{person}"))[2]
                for standart in standarts:
                    internal_result.append(
                        {
                            "score": compare_images(f"{PATH}/ATT_run/test/{image}",
                                                    f"{PATH}/ATT_run/{person}/{standart}",
                                                    method=method),
                            "answer": person,
                        }
                    )

            internal_result.sort(key=lambda a: a["score"], reverse=True)
            internal_answer = internal_result[0]["answer"]

            if internal_answer not in result:
                result[internal_answer] = method_weight[method]
            else:
                result[internal_answer] += method_weight[method]

            if show_images:
                img = cv.imread(f"{PATH}/ATT/{internal_answer}_1.png")
                cv.imshow(f"{method.upper()} ANSWER", img)

        answer = max(result, key=result.get)

        if image.split("_")[0] == answer:
            success += 1
        else:
            fail += 1

        num_of_test.append(success + fail)
        percentage.append(success / (fail + success) * 100)

        if visualize:
            graph.set_data(num_of_test, percentage)
            plt.pause(WAIT_TIME)

    print("Optimal method")
    print(f"fail: {fail}")
    print(f"success: {success}")
    print(f"percentage of success: {success / (fail + success) * 100}\n")
