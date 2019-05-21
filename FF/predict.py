import numpy as np
from tensorflow import keras
from FF.article import Article
from utils.loading import  load_reduced_features_tags
tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


def predict_tag(raw):
    article = Article(raw)
    features = load_reduced_features_tags()
    x = np.empty(shape=(1, len(features)))
    j = 0
    for feature_name in features.keys():
        try:
            x[0][j] = int(article.reduced_frequencies.get(feature_name))
        except TypeError:
            x[0][j] = 0
        j = j + 1

    model = keras.models.load_model('/home/ms10596/Documents/match/FF.h5')
    list_of_probabilities = model.predict(x)
    return tags[list_of_probabilities.argmax()]


# train()
# print(predict_tag("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
# What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
# she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
# fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
# asked her. "No," she said, "now my left arm hurts a lot."""""))
