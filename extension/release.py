import json

from keras import backend as K
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import tokenizer_from_json
from keras.utils import to_categorical
from nltk import pos_tag, word_tokenize


def soft_acc(y_true, y_pred):
    return K.mean(K.equal(K.round(y_true), K.round(y_pred)))


class Prediction:
    def __init__(self):
        import tensorflow as tf
        self.model = tf.keras.models.load_model('model-182-0.613687-0.736842.h5', custom_objects={'soft_acc': soft_acc})
        with open('tokenizer.json') as f:
            data = json.load(f)
            self.tokenizer = tokenizer_from_json(data)
        self.levels = ['Beginner', 'Intermediate', 'Advanced']

    def predict(self, text):
        import numpy as np
        predicted = self.model.predict(self.__transform(text))
        return self.levels[np.round(predicted.astype(int)[0][0], 0)]

    def __transform(self, text):
        return to_categorical(pad_sequences(self.tokenizer.texts_to_sequences([[i[1] for i in pos_tag(word_tokenize(text))]]),
                            maxlen=1000, padding='post', truncating='post'),num_classes=45)


# x = Prediction()
# print(x.predict("""When you see the word Amazon, whats the first thing you think of  the worlds biggest forest, the longest river or the largest internet shop  and which do you think is most important?
# These are the questions in a debate about the internet. Brazil and Peru have made objections to a bid made by the US online shop for the domain name, .amazon.
# Amazon has asked for its company name to be a top-level domain name (currently .com), but the South American governments say this would stop the use of this internet address for environmental protection, indigenous rights and other public interest uses.
# There are many other disputed claims to names, including .patagonia.
# Until now, the differences between commercial, governmental and other types of identity were easy to see in every internet address by the use of .com, .gov and 20 other categories.
# But soon there are going to be more of these categories  or generic top-level domains (gTLDs) as they are technically known.
# The Internet Corporation for Assigned Names and Numbers (ICANN) has had bids (each worth almost $200,000) for hundreds of new gTLDs to add to the 22 that we use already.
# Amazon has applied for many new domains, including .shop, .song, .book and .kindle. But the one that has caused most discussion is its application for .amazon.
# Brazil and Peru want the .amazon application to be stopped. They say that a private company should not have a name that is also the name of an important geographical area.
# Allowing private companies to register geographical names as gTLDs to profit from the meaning of these names is not, in our view, in the public interest, the Brazilian Ministry of Science and Technology said.
# Brazil said other members of the Amazon Cooperation Treaty support its views (Bolivia, Colombia, Ecuador, Guyana, Suriname and Venezuela).
# There have also been other objections over new top-level domains that use geographical or cultural names.
# Argentina is unhappy that the US outdoor clothing retailer, Patagonia, wants a domain name that has been known far longer as a region of spectacular beauty. Argentina rejects the .patagonia request for a new generic top-level domain. Patagonia is an important region for the countrys economy because it has oil, fishing, mining and agriculture resources. It is also a major tourist destination.
# They will discuss the disputed bids again at a meeting of ICANNs Governmental Advisory Committee in Durban in July. The first new domain names will probably be in use before the end of 2013.
# """))
# print(x.predict("""
# To tourists, Amsterdam still seems very liberal. Recently the citys Mayor told them that the coffee shops that sell marijuana would stay open, although there is a new national law to stop drug tourism. But the Dutch capital has a plan to send antisocial neighbours to scum villages made from shipping containers, and so maybe now people wont think it is a liberal city any more.
# The Mayor, Eberhard van der Laan, says his new plan to solve the problem of antisocial behaviour will cost 810,000. The plan is hopes to protect victims of abuse and homophobia. The camps, where antisocial families will live for three to six months, have been called scum villages because last year Geert Wilders, the far-right politician, said that offenders should go to a village for scum.
# Bartho Boer, a spokesman for the Mayor, says that the plans are not illiberal. We want to defend the liberal values of Amsterdam, he says. We want everyone to be who he and she is  whether they are gay and lesbian or try to stop violence and are then victims of harassment. We want to defend them. According to Boer, the villages are not for a problem neighbour who has the stereo too loud on Saturday night but people who are very violent and in a clear situation where a victim is harassed again and again.
# People found guilty of violent harassment will be evicted from their homes and put in temporary homes, including shipping containers in industrial areas of the city. We call it a living container, says Boer. The containers have showers and kitchens and have been used as student accommodation. They are going to use the containers because they want to show that if people are antisocial they do not get better accommodation.
# One Dutch newspaper wrote that in the 19th century antisocial people were moved to villages in Drenthe and Overijssel, which soon became slums. But Boer says that the government has learned from past mistakes and is not planning to put antisocial families together.
# They are scum houses not scum villages, says Boer, because we dont want to put more than one of these families in the same area. After a maximum of six months in these houses, in different parts of the city, the families will get permanent homes. The city government expects to move about ten families a year, which starts in 2013.
# Police will watch the temporary accommodation, but antisocial families will also be able to see doctors and social workers. We will take care of them so the whole situation is not going to repeat at the new house they are in, says Boer."""))
