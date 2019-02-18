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

    def adv(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'RB'])

    def articles(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'DT'])

    def conjunctions(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'IN'])

    def interjections(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'UH'])

    def nouns(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'NNS'])

    def numerals(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'CD'])

    def past_participle(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'VBN'])

    # def preposition(self):
    #     return len([i for i in pos_tag(self.words) if i[1] == ''])
    def pronouns(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'PRP'])

    # def punctuation(self):
    #     return len([i for i in pos_tag(self.words) if i[1] == ''])
    def special_symbols(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'SYM'])
