import numpy as np
from tensorflow import keras
from research.article import Article
from research.features_factory import FeaturesFactory
tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

class Predict:
    @staticmethod
    def predict_tag(raw):
        x = np.empty(shape=(1, 2))
        ff = FeaturesFactory(Article(raw))
        x[0][0] = ff.avg_sentence_length()
        x[0][1] = ff.avg_word_length()
        model = keras.models.load_model('/home/ms10596/Documents/match/research/model.h5')
        list_of_probabilities = model.predict(x)
        return tags[list_of_probabilities.argmax()]


# train()
# print(Predict.predict_tag("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
# What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
# she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
# fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
# asked her. "No," she said, "now my left arm hurts a lot."""""))
