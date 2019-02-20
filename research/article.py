from statistics import mean

from nltk import word_tokenize, sent_tokenize, pos_tag


class Article:
    def __init__(self, body, tag='Unknown'):
        self.body = body
        self.tag = tag
        self.words = word_tokenize(self.body)
        self.tags = pos_tag(self.words)

    def avg_sentence_length(self):
        return mean([len(word_tokenize(i)) for i in sent_tokenize(self.body)])

    def avg_word_length(self):
        return mean([len(i) for i in self.words])

    def adj(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'JJ'])

    def adv(self):
        return len([i for i in pos_tag(self.words) if i[1] == 'RB'])

    def article(self):
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


x = Article("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
asked her. "No," she said, "now my left arm hurts a lot.""")
print(x.tags)
f = open('nltk_tags', 'w+')
import nltk
nltk.help.upenn_tagset()
