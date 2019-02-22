from nltk import word_tokenize, sent_tokenize, pos_tag, FreqDist


class Article:
    def __init__(self, body, category='Unknown'):
        self.body = body
        self.category = category

        self.words = word_tokenize(self.body)
        self.sentences = sent_tokenize(self.body)

        self.word_tags = pos_tag(self.words)
        self.frequencies = FreqDist([i[1] for i in self.word_tags])
