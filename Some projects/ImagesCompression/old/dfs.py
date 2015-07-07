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