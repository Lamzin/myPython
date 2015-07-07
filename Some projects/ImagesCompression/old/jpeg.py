from PIL import Image
import time

import dfs



# *****
#! usr/bin/env python3.4
import os

suffixes = ["JPG", "jpg"]
global_path, files_count = os.getcwd(), 0
report_file = open("__report__", "w")
images_files = []

def dfs(path):
    global files_count
    files = os.listdir("%s/%s" % (global_path, path))
    for file in files:
        cur_path = "%s%s" % (path, file)
        if os.path.isdir("%s/%s" % (global_path, cur_path)):
            dfs("%s/" % cur_path)
        elif os.path.isfile("%s/%s" % (global_path, cur_path)) and file.split(".")[-1] in suffixes:
            images_files.append(cur_path)
            rep = "#%d: %s" % (files_count, cur_path)
            report_file.write(rep + "\n")
            print(rep)
            files_count += 1

# *****




time_beg = time.time()
def my_print(s):
    dfs.report_file.write(s + "\n")
    print(s)

def im(num, path):
    time_image = time.time()
    try:
        image = Image.open(path)
        image.save(path, "JPEG", quality = 75)
        my_print("#%d : Ok : %s" % (num, path))
        my_print("\ttime = %.6f" % (time.time() - time_image))
        my_print("\tTotal time = %.6f" % (time.time() - time_beg))
    except:
        my_print("\nError in file: %s" % path)
        my_print("\ttime = %.6f" % (time.time() - time_image))
        my_print("\tTotal time = %.6f" % (time.time() - time_beg))

#image.thumbnail((image.size[0] // 2, image.size[1] // 2), Image.ANTIALIAS)

dfs.dfs("")
for i, item in enumerate(dfs.images_files):
    im(i, item)

my_print("*\n**Total time = %.6f***" % (time.time() - time_beg))