"""

"""

import os


def song_as_corpus(path, limit=1):
    with open(path) as f:
        lines = f.readlines()

    corpus_text = " "
    for index in range(int(len(lines) * limit)):
        corpus_text = corpus_text + "\n " + lines[index]

    return corpus_text

def get_corpus_from_directory(path, limit=1):
    """

    :param path:
    :param limit:
    :return:
    """
    songs_files = os.listdir(path)

    corpus_text = ""
    for f in songs_files:
        if f[0] != ".":
            path_file = path + "/" + f
            corpus_text = corpus_text + song_as_corpus(path_file, limit) + " "

    return corpus_text