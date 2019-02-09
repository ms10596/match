from os import listdir


def load():
    """
    :return: list of objects {article: , tag: }

    """
    articles = []
    for tag in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        files = listdir('CEFR/' + tag)
        for i in files:
            f = open('CEFR/' + tag + '/' + i)
            article = f.read()
            articles.append({'body': article, 'tag': tag})
    return articles


# print(load()[0])
