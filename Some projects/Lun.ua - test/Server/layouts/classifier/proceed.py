import os
import sys
import urllib
from PIL import Image

from bfs import proceed_bfs
from straightforward import proceed_straightforward

from straightforward_detail import proceed_straightforward_detail
from bfs_detail import proceed_bfs_detail


def proceed_from_url(url):
    res_default, res_bfs = "", ""
    try:
        file_name = url.split("/")[-1]
        urllib.urlretrieve(url, file_name)

        img = Image.open(file_name)

        res_default = proceed_straightforward(img)
        res_bfs = proceed_bfs(img)
    except:
        res_default, res_bfs = "invalid url", "invalid url"
    finally:
        try:
            os.remove(file_name)
        except:
            pass

    return {'default': res_default, 'bfs': res_bfs}


def proceed_file(url):
    res_default, res_bfs = "", ""
    try:
        img = Image.open(url)
        res_default = proceed_straightforward(img)
        res_bfs = proceed_bfs(img)
    except:
        res_default, res_bfs = "invalid url", "invalid url"

    return {'default': res_default, 'bfs': res_bfs}


def proceed_detail(id):
    image_path = "D:\\Lamzin\\Server\\media\\tmp.jpg"
    # image_path = "D:\\Lun.ua\\Server\\media\\tmp.jpg"

    if id != "tmp":
        try:
            os.remove(image_path)
        except:
            print "Error with remove previous image!"
        try:
            url_path = "http://storage.googleapis.com/lun_ua/"
            urllib.urlretrieve("%s%s.jpg" % (url_path, id), image_path)
        except:
            print "Error with download!"

    result = []
    try:
        img = Image.open(image_path)
        for element in proceed_straightforward_detail(img):
            result.append(element)
    except:
        print "error with straight proceed!"

    try:
        img = Image.open(image_path)
        for element in proceed_bfs_detail(img):
            result.append(element)
    except:
        print "error with bfs proceed!"

    print "result = ", result
    return result