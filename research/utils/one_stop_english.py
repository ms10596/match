import os
from random import shuffle

x = 'Corpus/OneStopEnglishCorpus/Texts-SeparatedByReadingLevel'


class OneStopEnglish:
    def __init__(self):
        self.articles = []
        self.tags = []
        self.load_raw()
        self.__shuffle()

    def load_raw(self):
        for i in ['Ele-Txt', 'Int-Txt', 'Adv-Txt']:
            files = [i for i in os.listdir(os.path.join(os.path.abspath(os.curdir), x, i)) if not i.startswith('.')]
            for j in files:
                f = open(os.path.join(os.path.abspath(os.curdir), x, i, j))
                self.articles.append(f.read())
                self.tags.append(['Ele-Txt', 'Int-Txt', 'Adv-Txt'].index(i))

    def __shuffle(self):
        zipped = list(zip(self.articles, self.tags))
        shuffle(zipped)
        self.articles, self.tags = zip(*zipped)
