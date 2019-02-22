from os import listdir
from random import shuffle
import numpy as np

from research.article import Article
import re

class Load:

    @staticmethod
    def load():
        return Load.numpify(Load.raw())

    @staticmethod
    def raw():
        tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
        articles = []
        for tag in tags:
            files = listdir('/home/ms10596/Documents/match/research/CEFR/' + tag)
            for i in files:
                f = open('/home/ms10596/Documents/match/research/CEFR/' + tag + '/' + i)
                article = f.read()
                articles.append(Article(article, tags.index(tag)))
        return articles

    @staticmethod
    def numpify(articles):
        shuffle(articles)
        x = np.empty(shape=(len(articles), 46))
        y = np.empty(shape=(len(articles), 1), dtype=object)
        for i in range(len(articles)):
            frequencies = articles[i].frequencies
            j=0
            for tag_name, frequency in frequencies.items():
                # print(frequency)
                x[i][j] = frequency
                j = j+1

            y[i] = articles[i].category
        return x, y

    @staticmethod
    def divide(x, y):
        portion = int(0.8 * len(x))
        x_train = x[:portion]
        y_train = y[:portion]

        x_test = x[portion:]
        y_test = y[portion:]

        return x_train, y_train, x_test, y_test

    @staticmethod
    def load_pos_tags():
        f = open('/home/ms10596/Documents/match/research/nltk_tags')
        dic = {}
        for line in f:
            a, b = line.strip().split(': ')
            dic[a] = b
        return dic
Load.load_pos_tags()
# print(__file__)