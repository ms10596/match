from nltk import word_tokenize, sent_tokenize
import re
class lexile:
    def __init__(self, string):
        self.sent = sent_tokenize(string)
        self.words = word_tokenize(string)
        self.wordsFreq = {}
        self.getFrequncies()
        self.removeNonChar()

    def removeNonChar(self):
        for i in self.words:
            if re.search('[^a-zA-Z0-9]', i):
                self.words.remove(i)
    def mean_sentence_Length(self):
        mean = 0
       # print(len(self.sent))
        for i in self.sent:
            mean += i.count(" ") + 1    #counting words in each sentence
        return mean/len(self.sent)

    def mean_word_freq(self):
        mean = 0
        for i in self.words:
            mean+=self.wordsFreq[i]
        return mean/len(self.words)

    def word_count(self):
        pass
    def getFrequncies(self):
        f = open("freq.txt")
        while True:
            line = f.readline().strip()
            if line == '':
                break
            else:
                splited = line.split(" ")
                # print(splited)
                self.wordsFreq.update({splited[0]: (int)(splited[1])})
        # print(self.wordsFreq)
        return self.wordsFreq

    def getScore(self):
        sentnceLen = self.mean_sentence_Length()
        wordFrequncy = self.mean_word_freq()
        return 582 + (1768*sentnceLen - 386*wordFrequncy)
def main():
    l = lexile("regular expression is a sequence of characters that define a search pattern. regular expression is used in search engines, search and replace dialogs of word processors and text editors, and in lexical analysis.")
    # l.mean_sentence_Length()
    # l.mean_word_freq()
    # l.getFrequncies()
    print(l.getScore())

if __name__ =="__main__":
    main()