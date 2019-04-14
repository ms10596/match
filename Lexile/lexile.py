import math
import re
from collections import defaultdict
from statistics import mean

from nltk import word_tokenize, sent_tokenize


class Lexile:
    def __init__(self, string):
        self.sentences = sent_tokenize(string)
        self.words = word_tokenize(string.lower())
        self.wordsFreq = defaultdict(int)
        self.get_frequencies()
        self.removeNonChar()

    def removeNonChar(self):
        for i in self.words:
            if re.search('[^a-zA-Z0-9]', i):
                self.words.remove(i)

    def mean_sentence_length(self):
        return mean([len(i) for i in self.sentences])

    def mean_word_freq(self):
        return math.log10(mean([self.wordsFreq[i] for i in self.words]))

    def word_count(self):
        return len(self.words)

    def get_frequencies(self):
        f = open("freq.txt", encoding="ISO-8859-1")
        while True:
            line = f.readline().strip()
            # print(line)
            if line == '':
                break
            else:
                splitted = line.split(" ")
                # print(splitted)
                self.wordsFreq[splitted[0]] = int(splitted[1])
        return self.wordsFreq

    def get_score(self):
        sentence_len = self.mean_sentence_length()
        word_frequency = self.mean_word_freq()
        return 582 + (1768 * sentence_len - 386 * word_frequency)


if __name__ == "__main__":
    l = Lexile(
        """The Lexile Analyzer uses an algorithm to evaluate the reading demand — or text complexity — of books, articles and other materials. The Lexile Analyzer measures the complexity of the text by breaking down the entire piece and studying its characteristics, such as sentence length and word frequency, which represent the syntactic and semantic challenges that the text presents to a reader. The outcome is the text complexity, expressed as a Lexile measure, along with information on the word count, mean sentence length and mean log frequency. Generally, longer sentences and words of lower frequency lead to higher Lexile measures; shorter sentences and words of higher frequency lead to lower Lexile measures. Texts such as lists, recipes, poetry and song lyrics are not analyzed because they lack conventional punctuation.""")
    print("Lexile measure: ", l.get_score())
    print("Mean Sentence Length: ", l.mean_sentence_length())
    print("Mean Log Word Frequency: ", l.mean_word_freq())
    print("Word Count: ", l.word_count())
