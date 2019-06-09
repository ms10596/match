import json

from keras import backend as K
from keras.models import load_model
from keras_preprocessing.text import tokenizer_from_json


def soft_acc(y_true, y_pred):
    return K.mean(K.equal(K.round(y_true), K.round(y_pred)))


class Prediction:
    def __init__(self):
        self.model = load_model('model-182-0.613687-0.736842.h5')
        with open('tokenizer.json') as f:
            data = json.load(f)
            self.tokenizer = tokenizer_from_json(data)
        self.levels = ['Beginner', 'Intermediate', 'Advanced']

    def predict(self, text):
        predicted = self.model.predict(self.transform(text))
        return self.levels.index(int(round(predicted[0]), 0))

    def transform(self, text):
        return self.tokenizer.texts_to_sequences(text)
