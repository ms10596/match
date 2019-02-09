from random import shuffle

import numpy as np

from features_factory import FeaturesFactory
from load import load

if __name__ == '__main__':
    data = load()
    shuffle(data)
    x = np.empty(shape=(len(data), 3))
    y = np.empty(shape=(len(data), 1), dtype=object)
    for i in range(len(data)):
        ff = FeaturesFactory(data[i])
        x[i][0] = ff.avg_sentence_length()
        x[i][1] = ff.avg_word_length()
        x[i][2] = ff.adj()
        y[i] = ff.tag
    print(y)


