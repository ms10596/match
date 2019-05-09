import os

x = 'Corpus/OneStopEnglishCorpus/Texts-SeparatedByReadingLevel'


class OneStopEnglish:

    def load_raw(self):
        articles = []
        tags = []
        for i in ['Ele-Txt', 'Int-Txt', 'Adv-Txt']:
            files = [i for i in os.listdir(os.path.join(os.path.abspath(os.curdir), x, i)) if not i.startswith('.')]
            # print(len(files))
            for j in files:
                f = open(os.path.join(os.path.abspath(os.curdir), x, i,j))
                print(f)
                articles.append(f.read())
                tags.append(i)
        # print(len(articles))
        # print(len(tags))


OneStopEnglish().load_raw()
