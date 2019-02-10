from random import shuffle

import numpy as np

from research.features_factory import FeaturesFactory


def numpify(data):
    shuffle(data)
    x = np.empty(shape=(len(data), 2))
    y = np.empty(shape=(len(data), 1), dtype=object)
    for i in range(len(data)):
        ff = FeaturesFactory(data[i])
        x[i][0] = ff.avg_sentence_length()
        x[i][1] = ff.avg_word_length()
        # x[i][2] = ff.adj()
        y[i] = ff.tag
    return x, y
