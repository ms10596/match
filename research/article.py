from nltk import word_tokenize, sent_tokenize, pos_tag, FreqDist


class Article:
    def __init__(self, body, category='Unknown'):
        self.body = body
        self.category = category

        self.words = word_tokenize(self.body)
        self.sentences = sent_tokenize(self.body)
        # print(len(self.sentences))

        self.word_tags = pos_tag(self.words)
        self.frequencies = FreqDist([i[1] for i in self.word_tags])
        # print(self.frequencies.get('NNP'))

    def quotation_mark(self):
        return self.frequencies["""''"""] + self.frequencies["""``"""]

    def parenthesis(self):
        return self.frequencies['('] + self.frequencies[')']

    def comma(self):
        return self.frequencies[',']

    def dash(self):
        return self.frequencies['--']

    def sentence_terminator(self):
        return self.frequencies['.']

    def colon(self):
        return self.frequencies[':']

    def conjunction(self):
        return self.frequencies['CC']

    def numerals(self):
        return self.frequencies['CD']

    def determiner(self):
        return self.frequencies['DT']

    def existensial(self):
        return self.frequencies['EX']

    def foreign_word(self):
        return self.frequencies['FW']

    def preposition(self):
        return self.frequencies['IN']

    def adjective(self):
        return self.frequencies['JJ']

    def comparative_adjective(self):
        return self.frequencies['JJR']

    def superlative_adjective(self):
        return self.frequencies['JJS']

    def item_marker(self):
        return self.frequencies['LS']

    def modal(self):
        return self.frequencies['MD']

    def common_nouns(self):
        return self.frequencies['NN'] + self.frequencies['NNS']

    def proper_nouns(self):
        return self.frequencies['NNP'] + self.frequencies['NNPS']

    def predeterminer(self):
        return self.frequencies['PDT']

    def genitive_marker(self):
        return self.frequencies['POS']

    def pronoun(self):
        return self.frequencies['PRP'] + self.frequencies['PRP$']

    def adverb(self):
        return self.frequencies['RB']

    def comparative_adverb(self):
        return self.frequencies['RBR']

    def superlative_adverb(self):
        return self.frequencies['RBS']

    def particle(self):
        return self.frequencies['RP']

    def symbol(self):
        return self.frequencies['SYM']

    def to(self):
        return self.frequencies['SYM']

    def interjection(self):
        return self.frequencies['UH']

    def verb(self):
        return self.frequencies['VB'] + self.frequencies['VBP'] + self.frequencies['VBZ']

    def verb_past(self):
        return self.frequencies['VBD']

    def verb_present_participle(self):
        return self.frequencies['VBG']

    def verb_past_participle(self):
        return self.frequencies['VBN']

    def WH(self):
        return self.frequencies['WDT'] + self.frequencies['WP'] + self.frequencies['WP$'] + self.frequencies['WRB']



x = Article("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
asked her. "No," she said, "now my left arm hurts a lot.""")
print(x.quotation_mark())
