import os
import sys
import urllib
from PIL import Image

from bfs import proceed_bfs
from straightforward import proceed_straightforward


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