from os import path, listdir, curdir
from statistics import mean

from nltk.corpus.reader.bracket_parse import BracketParseCorpusReader
from sklearn.utils import shuffle

sentences_path = path.join(path.abspath(curdir), 'Corpus/OneStopEnglishCorpus/Sentence-Aligned')
parsed_path = '/home/ms10596/PycharmProjects/match/utils/Corpus/OneStopEnglishCorpus/Processed-AllLevels-AllFiles/Parsed'
file_names = sorted(listdir(parsed_path))[1:]


def load_advanced_elementary():
    f = open(path.join(sentences_path, 'ADV-ELE.txt'))
    all = [i.strip().split('\n') for i in f.read().split("*******")]
    advanced = []
    elementary = []
    for i in all:
        if len(i) == 2:
            advanced.append(i[0].lower())
            elementary.append(i[1].lower())
    return advanced, elementary


def load_advanced_intermediate():
    f = open(path.join(sentences_path, 'ADV-INT.txt'))
    all = [i.strip().split('\n') for i in f.read().split("*******")]
    advanced = [i[0] for i in all if len(i) == 2]
    intermediate = [i[1] for i in all if len(i) == 2]
    return advanced, intermediate


def load_intermediate_elementary():
    f = open(path.join(sentences_path, 'ELE-INT.txt'))
    all = [i.strip().split('\n') for i in f.read().split("*******")]
    elementary = [i[0] for i in all if len(i) == 2]
    intermediate = [i[1] for i in all if len(i) == 2]
    return intermediate, elementary


def load_corpus():
    corpus = BracketParseCorpusReader(root=parsed_path, fileids=file_names[1:])
    return corpus


def corpus_to_words(corpus):
    labels_names = ['ele', 'int', 'adv']
    articles = []
    tags = []
    for i in file_names:
        articles.append(list(corpus.words(i)))
        tags.append(labels_names.index(i[-14:-11]))
    return articles, tags


def corpus_to_pos(corpus):
    labels_names = ['ele', 'int', 'adv']
    articles = []
    tags = []
    for i in file_names:
        articles.append([j[1] for j in corpus.tagged_words(i)])
        tags.append(labels_names.index(i[-14:-11]))
    return articles, tags


def detokenize(l):
    from nltk.tokenize.treebank import TreebankWordDetokenizer
    return TreebankWordDetokenizer().detokenize(l)


def opennmt_preprocessing():
    a, b = load_advanced_elementary()
    a, b = shuffle(a, b)
    src_train = a[:1625]
    tgt_train = b[:1625]

    src_val = a[1625:]
    tgt_val = b[1625:]

    src_train_file = open('src-train.txt', mode='w')
    tgt_train_file = open('tgt-train.txt', mode='w')
    src_val_file = open('src-val.txt', mode='w')
    tgt_val_file = open('tgt-val.txt', mode='w')

    for i in range(len(src_train)):
        src_train_file.write(src_train[i] + '\n')
        tgt_train_file.write(tgt_train[i] + '\n')
    src_train_file.close()
    tgt_train_file.close()
    for i in range(len(src_val)):
        src_val_file.write(src_val[i] + '\n')
        tgt_val_file.write(tgt_val[i] + '\n')
    src_val_file.close()
    tgt_train_file.close()


def average_sentence_length():
    corpus = load_corpus()
    return mean(len(i) for i in corpus.sents())

# if __name__ == '__main__':
# print(average_sentence_length())
