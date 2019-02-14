from os import listdir

from research.numpifying import numpify
from research.article import Article

def load():
    """
    :return: list of objects {article: , tag: }

    """
    tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    articles = []
    for tag in tags:
        files = listdir('research/CEFR/' + tag)
        for i in files:
            f = open('research/CEFR/' + tag + '/' + i)
            article = f.read()
            articles.append(Article(article, tag))
    return articles


def load_x_y():
    data = load()
    x, y = numpify(data)
    portion = int(0.8 * len(x))
    print(portion)
    x_train = x[:portion]
    y_train = y[:portion]

    x_test = x[portion:]
    y_test = y[portion:]

    return x_train, y_train, x_test, y_test
# load_x_y()