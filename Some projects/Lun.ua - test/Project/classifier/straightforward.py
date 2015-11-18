__author__ = 'Oleh'


from deviation import *


PERMISSIBLE_RATIO = 0.5
PERMISSIBLE_DELTA = 30


def proceed_straightforward(img):
    data = list(img.getdata())

    white_pixel = (255, 255, 255)
    white_pixel_count = 0

    for pixel in data:
        white_pixel_count += deviation(pixel, white_pixel, PERMISSIBLE_DELTA)

    return "apartment layout" \
        if float(white_pixel_count) / len(data) > PERMISSIBLE_RATIO \
        else "other"