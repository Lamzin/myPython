__author__ = 'Oleh'

from PIL import Image
import os
import time
import classifier


if __name__ == "__main__":
    time_begin = time.clock()

    folder_data = "data"
    file_result = open("result.txt", "w")
    files = os.listdir(folder_data)

    for file in files:
        image_path = folder_data + "\\" + file
        if os.path.isfile(image_path) and file.split(".")[-1] == "jpg":
            img = Image.open(image_path)

            print (file, classifier.proceed_bfs(img))


    print ("Time = %f" % (time.clock() - time_begin))


