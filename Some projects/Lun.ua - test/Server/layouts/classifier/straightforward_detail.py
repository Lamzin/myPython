__author__ = 'Oleh'


from deviation import *


PERMISSIBLE_RATIO = 0.5
PERMISSIBLE_DELTA = 30


def proceed_straightforward_detail(img):
    data = list(img.getdata())
    m, n = img.size

    white_pixel = (255, 255, 255)
    white_pixel_count = 0

    for i in xrange(len(data)):
        if deviation(data[i], white_pixel, PERMISSIBLE_DELTA):
            img.putpixel([i % m, i // m], (255, 0, 0))
            white_pixel_count += 1

    file_name = "media\\straight.jpg"
    img.save(file_name)
    return [[file_name.replace("\\", "/"), float(white_pixel_count) / len(data)]]