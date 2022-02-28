import numpy as np


def get_word_from_sphere(sphere_vector, parameterize_vovabulary):
    """

    :param sphere_vector:
    :param parameterize_vovabulary:
    :return:

    """
    dist = 999.0  # max possible distance is <=3
    for w in parameterize_vovabulary:
        w_param = parameterize_vovabulary[w]
        new_d = np.sqrt((w_param[0] - sphere_vector[0]) ** 2 + (w_param[1] - sphere_vector[1]) ** 2 + (
                w_param[2] - sphere_vector[2]) ** 2)
        if new_d < dist:
            next_word = str(w)
            dist = new_d

    return next_word
