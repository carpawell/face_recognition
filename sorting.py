import os
import shutil


PATH = os.getcwd()


files = next(os.walk("./ATT"))[2]
dirs = ""
testing = False

os.makedirs("./ATT/test", exist_ok=True)

for file in files:
    current_person, current_photo_num = file.split("_")

    dirs = next(os.walk("./ATT"))[1]

    testing = True if int(current_photo_num.split(".")[0]) != 5 else False
    destination_folder = "test" if testing else f"{current_person}"

    if current_person not in dirs:
        os.makedirs("./ATT/" + current_person, exist_ok=True)

        shutil.move(f"{PATH}/ATT/{file}", f"{PATH}/ATT/{destination_folder}")

    else:
        shutil.move(f"{PATH}/ATT/{file}", f"{PATH}/ATT/{destination_folder}")


dirs = next(os.walk("./ATT"))[1]
for dir in dirs:
    if dir == "test":
        if len(next(os.walk(f"./ATT/test"))[2]) != 360:
            print(len(next(os.walk(f"./ATT/test"))[2]))
            print("Found wrong number of elements in test")
        continue
    train = next(os.walk(f"./ATT/{dir}"))[2]
    if len(train) != 1:
        print(f"Found wrong number of elements in {dir}")
