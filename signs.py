import os
from utils import *
import matplotlib.pyplot as plt

PATH = os.getcwd()


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
