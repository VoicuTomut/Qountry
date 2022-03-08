import math


def number_vocabulary(vocab, nr_qubits=None, binar=False):
    """

    """

    if nr_qubits is None:
        nr_qubits = math.ceil(math.log(len(vocab)) / math.log(2))


    points = [i for i in range(int(math.pow(2, nr_qubits)))]

    number_translation = {}
    i = 0
    for word in vocab:
        if binar:
            number_translation[word] = bin(points[i])[2:].zfill(int(nr_qubits))
        else:
            number_translation[word] = points[i]
        i = i + 1

    return number_translation
