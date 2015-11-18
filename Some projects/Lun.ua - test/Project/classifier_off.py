__author__ = 'Oleh'


from PIL import Image
from sets import Set
import os
from multiprocessing import Process
import classifier
import time


FOLDER_DATA = "D:\\Lun.ua\\data"
# FOLDER_DATA = "D:\\Lun.ua\\Project\\data"
FOLDER_RESULT = "D:\\Lun.ua\\Project\\classifier_offline\\report"
REPORT_NAME = "report.txt"

THREAD_COUNT = 4

def proceed_arr(arr, cnt):
    time_begin = time.clock()
    open("%s\\%d%s" % (FOLDER_RESULT, cnt, REPORT_NAME), "w").close()

    count_proceeded = 0
    count_smth = [[0, 0], [0, 0]]
    for file in arr:
        file_path = "%s\\%s" % (FOLDER_DATA, file)
        try:
            file_report = open("%s\\%d%s" % (FOLDER_RESULT, cnt, REPORT_NAME), "a")
            img = Image.open(file_path)

            result_straight = classifier.proceed_straightforward(img)
            result_bfs = classifier.proceed_bfs(img)

            file_report.write("%s straight_forward=%s bfs=%s\n" % (file, result_straight, result_bfs))
            file_report.close()

            count_smth[0 if result_straight != "other" else 1][0 if result_bfs != "other" else 1] += 1
            print file, count_proceeded, time.clock() - time_begin, count_smth
            count_proceeded+=1
        except:
            print ("Fail with file %s" % file)


def already_proceeded():
    proceeded = Set()
    # proceeded = []
    try:
        with open("%s\\%s" % (FOLDER_RESULT, REPORT_NAME), "r") as file:
            for line in file:
                if line.split()[0] not in proceeded:
                    proceeded.add(line.split()[0])
                    # proceeded.append(line.split()[0])
    except:
        pass
    return proceeded


def compare_result():
    file_report = open("%s\\%s" % (FOLDER_RESULT, REPORT_NAME), "a")

    for file in os.listdir(FOLDER_RESULT):
        file_path = FOLDER_RESULT + "\\" + file
        if os.path.isfile(file_path) and file.split(".")[-1] == "txt" and file != REPORT_NAME:
            with open(file_path, "r") as file_tmp:
                for line in file_tmp:
                    file_report.writelines(line)

    file_report.close()

if __name__ == "__main__":
    time_begin = time.clock()

    compare_result()
    proceeded = already_proceeded()
    print len(proceeded)

    arr = [[] for i in range(THREAD_COUNT)]

    cnt = 0
    added_count = 0

    not_proceeded = Set()
    for file in os.listdir(FOLDER_DATA):
        file_path = FOLDER_DATA + "\\" + file
        if os.path.isfile(file_path) and file.split(".")[-1] == "jpg":
            not_proceeded.add(file)
        # if os.path.isfile(file_path) and file.split(".")[-1] == "jpg" and file not in proceeded:
            # arr[cnt].append(file)
            # cnt = (cnt + 1) % THREAD_COUNT
            # added_count += 1
            # if added_count % 1000 == 0:
            #     print "count = ", added_count

    print len(not_proceeded)
    not_proceeded = not_proceeded.difference(proceeded)
    print len(not_proceeded)
    for elem in not_proceeded:
        arr[cnt].append(elem)
        cnt = (cnt + 1) % THREAD_COUNT


    processes = []
    for i in range(THREAD_COUNT):
        try:
            processes.append(Process(target=proceed_arr, args=(arr[i], i)))
            # processes[-1].setDaemon(True)
            processes[-1].start()
            print "thread %d is started" % i
        except:
            print "fail thread %d" % i

    for process in processes:
        process.join()

    compare_result()

    print time.clock() - time_begin


