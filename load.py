import os

from nltk import Text, word_tokenize


def string_to_text(s):
    return Text(word_tokenize(s))


def load():
    """
    :return: list of tuples(nltk.text, tag like A1, A2,...etc)

    """
    texts = []
    for tag in ['A1', 'A2', 'B1', 'B2', 'C1']:
        files = os.listdir('CEFR/' + tag)
        for i in files:
            f = open('CEFR/' + tag + '/' + i)
            # print(f.name)
            texts.append((string_to_text(f.read()), tag))
    return texts


print(load()[0])
