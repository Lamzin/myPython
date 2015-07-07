import os
import time
from PIL import Image
import threading


global_path = os.getcwd()
suffixes = [u"JPG", u"jpg"]
count = 0
thread_count = 4
images = []
for i in range(thread_count):
    images.append([])


def dfs(current_path):
    global count
    files = os.listdir(u"%s\%s" % (global_path, current_path))
    # print(files)
    for file in files:
        current_file_path = u"%s%s" % (current_path, file)
        # print(current_file_path)
        if os.path.isdir(u"%s\%s" % (global_path, current_file_path)):
            dfs(u"%s\\" % current_file_path)
        elif os.path.isfile(u"%s\%s" % (global_path, current_file_path)) and file.split(".")[-1] in suffixes:
            images[count % thread_count].append(u"%s\%s" % (global_path, current_file_path))
            count += 1


def compress(ind):
    i = 0
    time_begin = time.time()

    for image_path in images[ind]:
        if (i % 1 == 0):
            print("#%i | %i / %i | #Time = %i" % (ind + 1, i, count // thread_count, time.time() - time_begin))
        i += 1

        try:
            image = Image.open(image_path)
            image.save(image_path, "JPEG", quality = 75)
        except:
            print("Error!")


if __name__ == "__main__":
    total_time_begin = time.time()

    dfs(u"")

    t = []
    for ii in range(thread_count):
        t.append(threading.Thread(target=compress, args=(ii,)))
        t[-1].daemon = True
        t[-1].start()

    for ii in range(thread_count):
        t[ii].join()

    print("#TOTAL TIME = %i" % (time.time() - total_time_begin))