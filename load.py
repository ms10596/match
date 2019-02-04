import os

from Text import Text


def load():
    texts = []
    for tag in ['A1', 'A2', 'B1', 'B2', 'C1']:
        files = os.listdir('CEFR/' + tag)
        for i in files:
            f = open('CEFR/' + tag + '/' + i)
            texts.append(Text(text=f.read(), tag=tag))
    return texts


print(load()[0].tag)
