
from wordsToNumbers.clean_text import just_words


class Corpus:

    def __init__(self, text):
        """
        :param text: corpus original text as a string
        """
        self.original_text = text
        self.text = just_words(text)
        self.split_text = self.clean_split()
        self.vocabulary = list(set(self.split_text))

    def prop(self):
        prop = "nr. words:{} \nnr. distinct words: {} \n".format(len(self.split_text), len(self.vocabulary))
        prop = prop + "len.text/len.vocab:{}".format(len(self.split_text) / len(self.vocabulary))

        return prop

    def clean_split(self):
        """

        :return:
        """
        split = self.text.split(" ")
        c_split = []
        for w in split:
            if w not in [""]:
                c_split.append(w)
        return c_split



    def frequency(self, words=None):
        """

        :param words: list of words
        :return: frequency dictionary with words as key
        """
        if words is None:
            words = self.vocabulary

        freq = {}

        for word in words:
            w_count = 0
            for w in self.split_text:
                if w == word:
                    w_count = w_count+1
            freq[word] = w_count
        return freq
