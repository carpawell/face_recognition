import os
from utils import *
import matplotlib.pyplot as plt

PATH = os.getcwd()
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
            # test.relim()
            # test.autoscale_view()
            # fig.canvas.draw()
            # plt.scatter()
            # plt.draw()
            plt.pause(0.01)
            # plt.show()

    print(f"method: {method}")
    print(f"fail: {fail}")
    print(f"success: {success}")
    print(f"percentage of success: {success / (fail + success) * 100}\n")


def search_optimal(visualize):
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
        plt.show()

    for image in images:
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

        answer = max(result, key=result.get)

        if image.split("_")[0] == answer:
            success += 1
        else:
            fail += 1

        num_of_test.append(success + fail)
        percentage.append(success / (fail + success) * 100)

        if visualize:
            graph.set_data(num_of_test, percentage)
            plt.pause(0.01)

    print("Optimal method")
    print(f"fail: {fail}")
    print(f"success: {success}")
    print(f"percentage of success: {success / (fail + success) * 100}\n")
