import os
import shutil


def set_num_of_standarts(num_of_standarts):
    try:
        if len(next(os.walk("./ATT_run/1"))[2]) == num_of_standarts:
            return
    except StopIteration:
        pass

    path = os.getcwd()

    files = next(os.walk("./ATT"))[2]

    try:
        shutil.rmtree("./ATT_run")
    except FileNotFoundError:
        pass

    os.makedirs("./ATT_run/test", exist_ok=True)

    for file in files:
        current_person, current_photo_num = file.split("_")

        dirs = next(os.walk("./ATT"))[1]

        testing = True if int(current_photo_num.split(".")[0]) > num_of_standarts else False
        destination_folder = "test" if testing else f"{current_person}"

        if current_person not in dirs:
            os.makedirs("./ATT_run/" + current_person, exist_ok=True)

            shutil.copyfile(f"{path}/ATT/{file}", f"{path}/ATT_run/{destination_folder}/{file}")

        else:
            shutil.copyfile(f"{path}/ATT/{file}", f"{path}/ATT_run/{destination_folder}/{file}")

    dirs = next(os.walk("./ATT_run"))[1]
    for dir in dirs:
        if dir == "test":
            if len(next(os.walk(f"./ATT_run/test"))[2]) != (10 - num_of_standarts) * 40:
                # print(len(next(os.walk(f"./ATT_run/test"))[2]))
                print("Found wrong number of elements in test")
            continue
        train = next(os.walk(f"./ATT_run/{dir}"))[2]
        if len(train) != num_of_standarts:
            print(f"Found wrong number of elements in {dir}")
