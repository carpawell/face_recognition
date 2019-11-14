import os
import shutil


PATH = os.getcwd()


files = next(os.walk("./ATT"))[2]
dirs = ""
testing = False

for file in files:
    current_person, current_photo_num = file.split("_")

    dirs = next(os.walk("./ATT"))[1]

    testing = True if int(current_photo_num.split(".")[0]) > 5 else False
    destination_folder = "test" if testing else "train"

    if current_person not in dirs:
        os.makedirs("./ATT/" + current_person + "/test", exist_ok=True)
        os.makedirs("./ATT/" + current_person + "/train", exist_ok=True)

        shutil.move(PATH + "/ATT/" + file, PATH + "/ATT/" + current_person + "/" + destination_folder)

    else:
        shutil.move(PATH + "/ATT/" + file, PATH + "/ATT/" + current_person + "/" + destination_folder)


dirs = next(os.walk("./ATT"))[1]
for dir in dirs:
    test = next(os.walk("./ATT/" + dir + "/test"))[2]
    train = next(os.walk("./ATT/" + dir + "/train"))[2]
    if len(test) != 5 or len(train) != 5:
        print("Found not 5 elements in " + dir)
