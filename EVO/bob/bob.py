#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import logging


from flask import Flask
from flask import request

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

logging.basicConfig(filename='bob.log', level=logging.DEBUG)


app = Flask(__name__, static_url_path="/static")
epithets = []
names = {}


def get_epithets():
    with open("epithets.txt") as f:
        global epithets
        epithets = f.readlines()


@app.route(u'/')
def name():
    return app.send_static_file('form.html')


@app.route(u'/welcome')
def welcome():
    name = request.args.get("name")
    logging.info(name)
    epithet = names.get(name, epithets[random.randint(0, len(epithets))])
    names[name] = epithet
    return 'Рад тебя видеть снова, {} {}!'.format(epithet, name)

if __name__ == '__main__':
    get_epithets()
    app.run(debug=True, port=8080)
