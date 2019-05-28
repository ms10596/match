from collections import defaultdict
from os import listdir
from random import shuffle

import numpy as np

from FF.article import Article


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
    shuffle(articles)
    features = load_reduced_features_tags()
    x = np.empty(shape=(len(articles), len(features)), dtype=np.int)
    y = np.empty(shape=(len(articles), 1), dtype=np.int)
    for i in range(len(articles)):
        j = 0
        for feature_name in features.keys():
            try:
                x[i][j] = int(articles[i].reduced_frequencies.get(feature_name))
            except TypeError:
                x[i][j] = 0
            j = j + 1
        y[i] = articles[i].category
    return x, y


def load_pos_tags():
    f = open('/home/ms10596/Documents/match/research/nltk_tags')
    dic = {}
    for line in f:
        a, b = line.strip().split(': ')
        dic[a] = b
    return dic


def load_reduced_features_tags():
    f = open('/home/ms10596/Documents/match/research/reduced_features')
    dic = {}
    for line in f:
        a, b = line.strip().split(':')
        dic[a] = b
    return dic


def load_glove_embeddings():
    glove = defaultdict(lambda: np.zeros(shape=(50,)))
    with open('/home/ms10596/PycharmProjects/match/utils/glove/glove.6B.50d.txt') as f:
        for line in f:
            if line == '':
                break
            values = line.split()
            glove[values[0]] = np.array(values[1:], dtype='float32')
    return glove