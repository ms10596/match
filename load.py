import os


def load():
    """
    :return: list of objects {article: , tag: }

    """
    texts = []
    for tag in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        files = os.listdir('CEFR/' + tag)
        for i in files:
            f = open('CEFR/' + tag + '/' + i)
            article = f.read()
            texts.append({'article': article, 'tag': tag})
    return texts


print(load()[0])
