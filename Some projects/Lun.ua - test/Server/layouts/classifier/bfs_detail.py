__author__ = 'Oleh'


from deviation import *


PERMISSIBLE_RATIO_AREA = 0.03
PERMISSIBLE_RATIO_SUMMARY = 0.4
PERMISSIBLE_DELTA_GREY = 10
PERMISSIBLE_DELTA = 5


def valid_xy(used, x, y, n, m):
    return x >= 0 and x < n \
           and y >= 0 and y < m \
           and used[x * m + y] == 0


def bfs(data, used, x, y, n, m, color_delta=10):
    ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    que = [[x, y],]
    used[x * m + y] = 1

    i = 0
    while i < len(que):
        x_cur, y_cur = que[i]
        for way in ways:
            x_next, y_next = x_cur + way[0], y_cur + way[1]
            if valid_xy(used, x_next, y_next, n, m) \
                    and deviation(data[x * m + y], data[x_next * m + y_next], color_delta):
                que.append([x_next, y_next])
                used[x_next * m + y_next] = 1
        i += 1

    return que

def proceed_bfs_detail(img):
    m, n = img.size
    summary_area = 0

    data = list(img.getdata())
    used = [0 for i in range(n * m)]

    result = []

    for index in xrange(0, n * m, 64):
        if used[index] == 0:
            area = bfs(data, used,
                       index // m, index % m,
                       n, m,
                       PERMISSIBLE_DELTA_GREY if deviation_grey(data[index]) else PERMISSIBLE_DELTA)
            if float(len(area)) / (n * m) > PERMISSIBLE_RATIO_AREA:
                summary_area += len(area)

                for xy in area:
                    img.putpixel(xy[::-1], (255, 0, 0))
                image_name = "media\\%d_%d%d.jpg" % (n * m, index // m, index % m)
                img.save(image_name)
                result.append([image_name.replace("\\", "/"), float(len(area)) / (n * m)])

                if float(summary_area) / len(data) > PERMISSIBLE_RATIO_SUMMARY:
                    break

    return result