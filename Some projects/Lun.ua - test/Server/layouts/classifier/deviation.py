__author__ = 'Oleh'


def deviation(pixela, pixelb, delta=10):
    for i in range(3):
        if abs(pixela[i] - pixelb[i]) > delta:
            return False
    return True


def deviation_grey(pixel, delta=15, minimum=180):
    return abs(pixel[0] - pixel[1]) < delta \
           and abs(pixel[1] - pixel[2]) < delta \
           and abs(pixel[2] - pixel[0]) < delta \
           and sum(pixel) > 3 * minimum