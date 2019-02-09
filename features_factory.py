from statistics import mean

from nltk import word_tokenize, sent_tokenize

from load import load


class FeaturesFactory:
    def __init__(self, article):
        self.body = article['body']
        self.tag = article['tag']

    def avg_sentence_length(self):
        return mean([len(word_tokenize(i)) for i in sent_tokenize(self.body)])


if __name__ == '__main__':
    x = FeaturesFactory(load()[0])
    print(x.avg_sentence_length())
