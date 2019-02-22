from os import listdir

import numpy as np

from research.article import Article


def load():
    return numpify(raw())


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


def numpify(articles):
    # shuffle(articles)
    features = load_pos_tags()
    x = np.empty(shape=(len(articles), len(features)), dtype=np.float64)
    y = np.empty(shape=(len(articles), 1), dtype=np.int)
    for i in range(len(articles)):
        j = 0
        for feature_name in features.keys():
            try:
                x[i][j] = int(articles[i].frequencies.get(feature_name))
            except TypeError:
                x[i][j] = 0
            j = j + 1
        y[i] = articles[i].category
    return x, y


def divide(x, y):
    portion = int(0.8 * len(x))
    x_train = x[:portion]
    y_train = y[:portion]

    x_test = x[portion:]
    y_test = y[portion:]

    return x_train, y_train, x_test, y_test


def load_pos_tags():
    f = open('/home/ms10596/Documents/match/research/nltk_tags')
    dic = {}
    for line in f:
        a, b = line.strip().split(': ')
        dic[a] = b
    return dic
