from statistics import mean

from nltk import word_tokenize, sent_tokenize, pos_tag

from load import load


class FeaturesFactory:
    def __init__(self, article):
        self.body = article['body']
        self.tag = article['tag']

    def avg_sentence_length(self):
        return mean([len(word_tokenize(i)) for i in sent_tokenize(self.body)])

    def avg_word_length(self):
        return mean([len(i) for i in word_tokenize(self.body)])

    def adj(self):
        return len([i for i in pos_tag(word_tokenize(self.body)) if i[1] == 'JJ'])


if __name__ == '__main__':
    x = FeaturesFactory(load()[0])
    print(x.adj())
