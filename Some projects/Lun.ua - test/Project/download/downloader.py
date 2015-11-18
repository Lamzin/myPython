import csv
import urllib
import os
import threading


def download(arr):
    for element in arr:
        element_path = "data\\%s.jpg" % element[0]
        if not os.path.exists(element_path):
            try:
                urllib.urlretrieve(element[1], element_path)
                # print "ok %s" % element[0]
            except:
                pass
                # print "fail %s" % element[0]
        else:
            #print "exist %s" % element[0]
            pass


def download_all():
    threads_count = 128
    arr = [[] for x in range(threads_count)]
    threads = []

    with open("images_urls.csv", "r") as urlbase:
        reader = csv.reader(urlbase)
        current_thread = 0
        for row in reader:
            arr[current_thread].append(row)
            current_thread = (current_thread + 1) % threads_count

    for i in range(threads_count):
        try:
            threads.append(threading.Thread(target=download, args=(arr[i])))
            threads[-1].setDaemon(True)
            threads[-1].start()
            print "thread %d is started" % i
        except:
            print "fail thread %d" % i
            #break

    print "Here"
    for thread in threads:
        #print "thread %d is waiting" % -1
        thread.join()


if __name__ == "__main__":

    download_all()