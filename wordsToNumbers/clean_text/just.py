from wordsToNumbers.constants import ALPHABET


def just_words(text, split=False):
    """

    :param text: string texts
    :param split: boolean
    :return: if split=true a list of words else a clean text
    """

    jw = ""
    for char in text:
        if char == " ":
            jw=jw+" "
        if char in ALPHABET:
            jw = jw + char

    if split:
        return jw.lower().split(sep=" ")
    else:
        return jw.lower()
