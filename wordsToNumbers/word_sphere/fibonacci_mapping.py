import math


def fibonacci_sphere(samples):
    """

    :param samples:  nr o fample points
    :return: a list of points [[x,y,z]] of even spaced point on the surface of a sphere
    """
    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        points.append([x, y, z])

    return points


def fibonacci_vocabulary(vocab):
    """

    :param vocab:
    :return:
    """
    points = fibonacci_sphere(len(vocab))
    fibonacci_translator = {}

    i = 0
    for word in vocab:
        fibonacci_translator[word] = points[i]
        i = i + 1

    return fibonacci_translator
