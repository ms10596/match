import os

x = 'Corpus/OneStopEnglishCorpus/Texts-SeparatedByReadingLevel'


class OneStopEnglish:

    def load_raw(self):
        articles = []
        tags = []
        for i in ['Ele-Txt', 'Int-Txt', 'Adv-Txt']:
            files = os.listdir(os.path.join(os.path.abspath(os.curdir), x, i))
            print(files)


OneStopEnglish().load_raw()
