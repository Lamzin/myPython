import random


def generate_matrix():
    matrix = [[[random.randint(0, 10) for z in range(10)] for y in range(10)] for x in range(10)]
    return matrix


def get_maximum_x_axis(matrix):
    max_axis_sum = -1
    max_axis_index = -1, -1, -1

    for y in range(10):
        for z in range(10):
            current_axis_sum = 0
            for x in range(10):
                current_axis_sum += matrix[x][y][z]
            if current_axis_sum > max_axis_sum:
                max_axis_sum = current_axis_sum
                max_axis_index = 0, y, z
    return max_axis_index


def get_maximum_y_axis(matrix):
    max_axis_sum = -1
    max_axis_index = -1, -1, -1

    for z in range(10):
        for x in range(10):
            current_axis_sum = 0
            for y in range(10):
                current_axis_sum += matrix[x][y][z]
            if current_axis_sum > max_axis_sum:
                max_axis_sum = current_axis_sum
                max_axis_index = x, 0, z
    return max_axis_index


def get_maximum_z_axis(matrix):
    max_axis_sum = -1
    max_axis_index = -1, -1, -1

    for x in range(10):
        for y in range(10):
            current_axis_sum = 0
            for z in range(10):
                current_axis_sum += matrix[x][y][z]
            if current_axis_sum > max_axis_sum:
                max_axis_sum = current_axis_sum
                max_axis_index = x, y, 0
    return max_axis_index


if __name__ == "__main__":
    matrix = generate_matrix()
    print matrix
    print "x: {}".format(get_maximum_x_axis(matrix))
    print "y: {}".format(get_maximum_y_axis(matrix))
    print "z: {}".format(get_maximum_z_axis(matrix))
