import numpy


def working_window(history_lenghth: object, splited_text):
    """
    :param history_lenghth: (int) It is the number for past words used to predict the new one.
    :param splited_text: [ 'str', 'str',..] the text uses for training
    :return:( x , y ) training data set
    A sliding window is used to form the training data and the targets history_lenghth+1 word
    """
    x = []
    y = []


    for i in range(len(splited_text) - history_lenghth-1):
        x.append([splited_text[i + j] for j in range(history_lenghth)])
        y.append(splited_text[i+history_lenghth])


    return x, y
