import os


def load():
    texts = []
    tags = []
    for tag in ['A1', 'A2', 'B1', 'B2', 'C1']:
        files = os.listdir('CEFR/' + tag)
        for i in files:
            f = open('CEFR/'+tag+'/'+i)
            print(f.read())


load()
