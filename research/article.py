from nltk import word_tokenize, sent_tokenize, pos_tag, FreqDist


class Article:
    def __init__(self, body, category='Unknown'):
        self.body = body
        self.category = category

        self.words = word_tokenize(self.body)
        self.sentences = sent_tokenize(self.body)

        self.word_tags = pos_tag(self.words)
        self.frequencies = FreqDist([i[1] for i in self.word_tags])
        self.reduced_frequencies = {}

    def get_frequency(self, feature_name):
        try:
            return int(self.frequencies.get(feature_name))
        except TypeError:
            return 0

    def features_reduction(self):
        self.reduced_frequencies['adjectives'] = self.get_frequency('JJ') + self.get_frequency(
            'JJR') + self.get_frequency('JJS')
        self.reduced_frequencies['adverbs'] = self.get_frequency('RB') + self.get_frequency('RBR') + self.get_frequency(
            'RBS')
        self.reduced_frequencies['articles'] = self.get_frequency('DT')
        self.reduced_frequencies['conjunctions'] = self.get_frequency('CC')
        self.reduced_frequencies['interjections'] = self.get_frequency('UH')
        self.reduced_frequencies['nouns'] = self.get_frequency('NN') + self.get_frequency('NNS') + self.get_frequency(
            'NNP') + self.get_frequency('NNPS')
        self.reduced_frequencies['numerals'] = self.get_frequency('CD')
        self.reduced_frequencies['past_part'] = self.get_frequency('VBN')
        self.reduced_frequencies['preposition'] = self.get_frequency('IN')
        self.reduced_frequencies['pronouns'] = self.get_frequency('PRP') + self.get_frequency('PRP$')
        self.reduced_frequencies['punctuation'] = self.get_frequency('``') + self.get_frequency(
            '\'\'') + self.get_frequency('(') + self.get_frequency(')') + self.get_frequency(',') + self.get_frequency(
            '--') + self.get_frequency('.') + self.get_frequency(':')
        self.reduced_frequencies['symbols'] = self.get_frequency('SYM')
