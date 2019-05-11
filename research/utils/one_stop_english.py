from os import path, listdir, curdir
from random import shuffle

text_path = path.join(path.abspath(curdir), 'Corpus/OneStopEnglishCorpus/Texts-SeparatedByReadingLevel')
sentences_path = path.join(path.abspath(curdir), 'Corpus/OneStopEnglishCorpus/Sentence-Aligned')


class OneStopEnglish:
    def __init__(self):
        self.articles = []
        self.tags = []
        self.load_raw()
        self.__shuffle()

    def load_raw(self):
        for i in ['Ele-Txt', 'Int-Txt', 'Adv-Txt']:
            files = [i for i in listdir(path.join(text_path, i)) if not i.startswith('.')]
            for j in files:
                f = open(path.join(text_path, i, j))
                self.articles.append(f.read())
                self.tags.append(['Ele-Txt', 'Int-Txt', 'Adv-Txt'].index(i))

    def __shuffle(self):
        zipped = list(zip(self.articles, self.tags))
        shuffle(zipped)
        self.articles, self.tags = zip(*zipped)

    @staticmethod
    def load_advanced_elementary():
        f = open(path.join(sentences_path, 'ADV-ELE.txt'))
        all = [i.strip().split('\n') for i in f.read().split("*******")]
        advanced = [i[0] for i in all if len(i) == 2]
        elementary = [i[1] for i in all if len(i) == 2]
        return advanced, elementary

    @staticmethod
    def load_advanced_intermediate():
        f = open(path.join(sentences_path, 'ADV-INT.txt'))
        all = [i.strip().split('\n') for i in f.read().split("*******")]
        advanced = [i[0] for i in all if len(i) == 2]
        intermediate = [i[1] for i in all if len(i) == 2]
        return advanced, intermediate

    @staticmethod
    def load_intermediate_elementary():
        f = open(path.join(sentences_path, 'ELE-INT.txt'))
        all = [i.strip().split('\n') for i in f.read().split("*******")]
        elementary = [i[0] for i in all if len(i) == 2]
        intermediate = [i[1] for i in all if len(i) == 2]
        return intermediate, elementary


# x = OneStopEnglish()
# a, b = x.load_advanced_elementary()
# print(a[1])
# print(b[1])
# print(len(a), len(b))
# a, b = x.load_advanced_intermediate()
# print(a[1])
# print(b[1])
# print(len(a), len(b))
# a, b = x.load_intermediate_elementary()
# print(a[1])
# print(b[1])
# print(len(a), len(b))
