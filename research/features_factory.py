from statistics import mean

from nltk import word_tokenize, sent_tokenize, pos_tag


class FeaturesFactory:
    def __init__(self, article):
        self.body = article.body
        self.tag = article.tag
        self.words = word_tokenize(self.body)

    def avg_sentence_length(self):
        return mean([len(word_tokenize(i)) for i in sent_tokenize(self.body)])

    def avg_word_length(self):
        return mean([len(i) for i in self.words])

    def adj(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'JJ'])
