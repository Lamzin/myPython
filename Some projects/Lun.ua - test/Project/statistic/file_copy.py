import os
import shutil


if __name__ == "__main__":
    # names = ["apartment only bfs.txt", "apartment only straightforward.txt", "apartment.txt", "other.txt"]
    names = ["apartment only bfs.txt", "apartment only straightforward.txt", "apartment.txt",]

    data_folder = "D:\\Lun.ua\\data\\"
    # data_folder = "D:\\Lamzin\\data\\"
    cur_folder = "D:\\Lun.ua\\Project\\statistic\\"
    # cur_folder = "D:\\Lamzin\\Project\\statistic\\"

    for name in names:
        file = open(name, "r")
        files_folder = name.split(".")[0]
        try:
            os.mkdir(files_folder)
        except:
            pass

        for line in file:
            file_name = line.split()[0]
            # try:
            shutil.copy(data_folder + file_name, cur_folder + files_folder + "\\" + file_name)
            # except:
            #     print "Oops!"
