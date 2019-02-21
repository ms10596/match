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
        # print(len(self.frequencies))
        # print(self.frequencies.get('NNP'))




x = Article("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
asked her. "No," she said, "now my left arm hurts a lot.""")
# print(x.quotation_mark())
